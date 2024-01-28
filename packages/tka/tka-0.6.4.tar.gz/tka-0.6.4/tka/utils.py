import importlib.resources
import os
import webbrowser
from typing import Dict, List

import numpy as np
import pandas as pd
import scipy.linalg
from rdkit import Chem


def transform_l1000_ids(
    from_id,
    to_id,
    gene_ids,
    dataset_path="l1000_mapped.csv",
    ignore_missing=False,
) -> Dict:
    """
    Transforms L1000 gene IDs from one format to another.

    Args:
        from_id (str): The source probe type ("affyID", "entrezID", "ensemblID").
        to_id (str): The target probe type ("affyID", "entrezID", "ensemblID").
        gene_ids (list): List of L1000 gene IDs to transform.
        dataset_path (str): Path to the DataFrame containing L1000 gene IDs for each probe type.
        ignore_missing (bool): If set to True, it will not raise an error on missing or invalid probe IDs.

    Raises:
        ValueError: If either from_id or to_id is not one of the allowed values.
        ValueError: If any of the gene IDs in the dataset is not within the scope of L1000.

    Returns:
        dict: Original and transformed L1000 gene IDs as keys and values respectively.
    """
    # Initialize dataset pd.DataFrame
    with importlib.resources.path("tka.data", dataset_path) as file_path:
        l1000 = pd.read_csv(file_path)

    # Define the allowed probe types
    allowed_probes = ["affyID", "entrezID", "ensemblID"]

    # Check if the probe types are valid
    if from_id not in allowed_probes or to_id not in allowed_probes:
        raise ValueError(
            "Invalid probe type. Allowed values: 'affyID', 'entrezID', 'ensemblID'."
        )

    # Initialize the output dict
    transformed_ids = {}

    # Perform the transformation
    for gene_id in gene_ids:
        # Safety check for missing IDs
        if gene_id not in l1000[from_id].values:
            if ignore_missing:
                continue
            raise ValueError(
                f"Gene ID '{gene_id}' is not within the scope of L1000 {from_id} values."
            )

        # Find the mapping from L1000 and save it to transformed_ids
        transformed_ids[gene_id] = l1000[l1000[from_id] == gene_id][to_id].values[0]

    return transformed_ids


def _find_valid_moshkov_assays(model_id, auc_threshold):
    with importlib.resources.path(
        "tka.data", f"auc_modalities_({model_id}).csv"
    ) as file_path:
        assays = pd.read_csv(file_path)

    modality = "_".join(model_id.split("-")[2:])

    assays = assays[
        (assays["descriptor"] == modality)
        & (assays["auc"] >= auc_threshold)
    ]

    return assays["assay_id"].values


def transform_moshkov_outputs(
    identifier_col_vals: List[str],
    output: List[List],
    model_id: str,
    auc_threshold: float = 0.0,
    use_full_assay_names: bool = False,
) -> pd.DataFrame:
    """
    Transform Moshkov outputs into a Pandas DataFrame.

    Args:
        identifier_col_vals (List[str]): List of id strings corresponding to input data points (or any other identifiers).
        output (List[List[]]): List of lists containing output data (shape: X, 270).
        auc_threshold (float, optional): If supplied, assays whose prediction accuracies are lower than auc_threshold, will be dropped.
            Allowed auc_threshold values are any floating point values between 0.5 and 1.0.
        model_id (str): One of ["2023-02-mobc-es-op", "2023-01-mobc-es-op", "2021-02-mobc-es-op", "2024-01-mobc-es-op"].
        use_full_assay_names (bool, optional): Whether to use full assay names from the CSV. Defaults to False.

    Returns:
        pd.DataFrame: df with identifier_col_vals as the first column and assay data columns.
    """

    # Load the PUMA_ASSAY_ID values from the CSV file
    with importlib.resources.path("tka.data", "assay_metadata.csv") as file_path:
        assay_metadata = pd.read_csv(file_path)

    puma_assay_ids = assay_metadata["PUMA_ASSAY_ID"].tolist()

    # Create a dictionary to store the data for DataFrame creation
    data_dict = {"id": identifier_col_vals}

    # Loop through each PUMA_ASSAY_ID and add its values to the dictionary
    for idx, puma_assay_id in enumerate(puma_assay_ids):
        if use_full_assay_names:
            puma_assay_id = (
                assay_metadata[assay_metadata["PUMA_ASSAY_ID"] == puma_assay_id][
                    "ASSAY_NAME"
                ].values[0]
                + "/"
                + puma_assay_id
            )
        column_values = [row[idx] for row in output]
        data_dict[puma_assay_id] = column_values

    # Create a Pandas DataFrame from the data dictionary
    df = pd.DataFrame(data_dict)
    df.set_index("id", inplace=True)


    filtered_assays = _find_valid_moshkov_assays(
        model_id=model_id,
        auc_threshold=auc_threshold
    )

    filtered_cols = [x for x in df.columns if x.split("/")[1] in filtered_assays]
    filtered_df = df[filtered_cols]
    return filtered_df

    return df


class SpheringNormalizer(object):
    def __init__(self, controls):
        REG_PARAM = 10 ** np.log(1 / controls.shape[0])
        # Sphering transform on population level data
        self.mu = controls.mean()
        self.sphering_transform(controls - self.mu, REG_PARAM, rotate=True)
        # print(self.mu.shape, self.W.shape)

    def sphering_transform(self, X, lambda_, rotate=True):
        C = (1 / X.shape[0]) * np.dot(X.T, X)
        s, V = scipy.linalg.eigh(C)
        D = np.diag(1.0 / np.sqrt(s + lambda_))
        W = np.dot(V, D)
        if rotate:
            W = np.dot(W, V.T)
        self.W = W

    def normalize(self, X):
        return np.dot(X - self.mu, self.W)


def is_valid_smiles(smiles: str):
    """Returns True if SMILES representations is valid and False otherwise."""
    try:
        molecule = Chem.MolFromSmiles(smiles)
        return molecule is not None
    except:
        return False


def load_mobc_ordered_feature_columns(model_id: str = "2023-02-mobc-es-op"):
    """
    Loads cell morphology ordered features in a list format. 
    Currently all models use CellProfiler features.

    Args:
        model_id (str): One of ["2023-02-mobc-es-op", "2023-01-mobc-es-op", "2021-02-mobc-es-op", "2024-01-mobc-es-op"].

    """
    with importlib.resources.path(
        "tka.data", f"mobc_feature_columns_({model_id}).txt"
    ) as file_path:
        with file_path.open() as file:
            return [x.split("\n")[0] for x in file.readlines()]


def load_l1000_ordered_feature_columns(gene_id):
    """
    Loads L1000 ordered features in a list format based on the specified gene_id

    Args:
        gene_id (str): one of "affyID", "ensemblID" or "entrezID"

    Raises:
        ValueError: If either gene_id is not of the allowed probes.

    Returns:
        list: L1000 ordered features in a list format based on the specified gene_id
    """
    allowed_probes = ["affyID", "entrezID", "ensemblID"]

    # Check if the probe types are valid
    if gene_id not in allowed_probes:
        raise ValueError(
            "Invalid probe type. Allowed values: 'affyID', 'entrezID', 'ensemblID'."
        )

    with importlib.resources.path("tka.data", "l1000_mapped.csv") as file_path:
        return list(pd.read_csv(file_path)[gene_id].values)


def docs():
    """Upon calling the function, the website with the documentation will pop up on screen."""
    # Get the path to the package's directory
    package_dir = os.path.dirname(__file__)

    # Construct the path to the index.html file using importlib.resources
    with importlib.resources.path("tka.docs._build.html", "index.html") as html_path:
        html_path_str = str(html_path)  # Convert the Path object to a string

        # Open the index.html file using the webbrowser module
        webbrowser.open_new_tab(html_path_str)


if __name__ == "__main__":
    docs()
