from math import sqrt

import numpy as np
import pandas as pd
from scipy.stats import spearmanr, zscore


def replicate_correlation_coefficient(df_replicates: pd.DataFrame):
    """
    Computes replicate correlation coefficient as described on https://clue.io/connectopedia/signature_quality_metrics
    Replicate correlation is a measure that assesses how consistent these replicates are in a given experiment.
    It is computed as the 75th quantile of all pairwise Spearman correlations between replicate level 4 profiles.
    Higher CC indicates that the given treatment induced a consistent response.

    Args:
        df_replicates (pd.DataFrame): a pd.DataFrame with the columns being z-score normalized features
            and the index column being the replicate samples

    Raises:
        ValueError: if the shapes are invalid

    Returns:
        float: correlation coefficient
        dict: a dictionary with values being pairwise correlation coefficients and keys being the replicates' indices.
    """

    if df_replicates.shape[0] <= 1:
        raise ValueError(
            f"One sample or less provided. df_replicates shape is {df_replicates.shape}"
        )
    if df_replicates.shape[1] <= 1:
        raise ValueError(
            f"One feature or less provided. df_replicates shape is {df_replicates.shape}"
        )

    spearman_coeffs = {}
    replicate_weights = {}

    # Compute pairwise Spearman correlations for all features
    for i in range(df_replicates.shape[0]):
        for j in range(i + 1, df_replicates.shape[0]):
            correlation, _ = spearmanr(
                df_replicates.iloc[i, :], df_replicates.iloc[j, :], axis=0
            )
            spearman_coeffs[f"{i}{j}"] = correlation

    # Flatten the correlation matrix and calculate the 75th percentile
    rep_corr_coeff = np.percentile(list(spearman_coeffs.values()), 75)

    return rep_corr_coeff, spearman_coeffs


def collapse_and_adjust_signature(
    df_replicates: pd.DataFrame, rep_corr_coeff: float, spearman_coeffs: dict
):
    """
    Collapses and adjusts signature as described on https://clue.io/connectopedia/replicate_collapse
    Weighting is determined via Spearman correlation between each pair of replicate profiles from each perturbagen experiment in the level 4 data.
    Since Spearman correlation operates on ranked lists, the raw z-scores are first converted to ranks from 1 to n within a replicate, where n is the number of genes in the replicates.
    The weighting of each replicate is then calculated as the normalized sum of associations between each replicate with the others.
    These normalized values act as multipliers for each respective replicate vector.

    Args:
        df_replicates (pd.DataFrame): a pd.DataFrame with the columns being z-score normalized features
            and the index column being the replicate samples
        rep_corr_coeff (float): replicate correlation coefficient - first return value of replicate_correlation_coefficient()
        spearman_coeffs (dict): replicate correlation coefficients dictd - second return value of replicate_correlation_coefficient()

    Returns:
        pd.Series: adjusted signature of shape (df_replicates.shape[1],)
    """
    collapsed_signature = np.zeros(shape=(df_replicates.shape[1]))

    for i in range(df_replicates.shape[0]):
        spearmans = [v for k, v in spearman_coeffs.items() if str(i) in k]
        weight = (sum(spearmans) / len(spearmans)) / sum(spearman_coeffs.values())
        collapsed_signature += df_replicates.iloc[i, :] * weight

    # Now we multiply the collapsed signature by the number of replicates and return the adjusted signature
    adjusted_signature = collapsed_signature * sqrt(df_replicates.shape[0])
    return adjusted_signature


def signature_strength(
    adjusted_signature: pd.Series,
    population_means: pd.Series,
    population_stds: pd.Series,
    num_stds: float = 1.96,
):
    """
    Computes signature strength (total number of features deviated more than 2 STDs from the mean - threshold may vary).
    See https://clue.io/connectopedia/signature_quality_metrics for more information.

    Args:
        adjusted_signature (pd.Series): returning value of collapse_and_adjust_signature() of shape (num_features,)
        population_means (pd.Series): mean values of all features for the entire plate population
            The number of features must match exactly the number of features in adjusted_signature.
        population_stds (pd.Series): std values of all features for the entire plate population
            The number of features must match exactly the number of features in adjusted_signature.
        num_stds (float): number of standard deviation in each way required to be considered a hit (defaults to 1.96)

    Returns:
        int: total number of features deviated more than 2 STDs from the mean
    """
    ss = 0

    for col, val in adjusted_signature.items():
        curr_mean = population_means[col]
        curr_std = population_stds[col]

        if adjusted_signature[col] > (
            curr_mean + num_stds * curr_std
        ) or adjusted_signature[col] < (curr_mean - num_stds * curr_std):
            ss += 1

    return ss


def activity_score(ss: int, rep_corr_coeff: float, num_features: int):
    """
    Returns activity score (originally termed transcriptional activity score (PAS)) based on the number of
    feature hits, replicate correlation coefficient and the amount of features.
    See https://clue.io/connectopedia/signature_quality_metrics for more information

    Args:
        ss (int): signature strength
        rep_corr_coeff (float): replicate correlation coefficient
        num_features (int): number of features in each signature

    Returns:
        float: activity score
    """
    return sqrt(ss * max(rep_corr_coeff, 0) / num_features)


if __name__ == "__main__":
    pass
