import numpy as np
from scipy.stats import ks_2samp, mannwhitneyu, ttest_ind, f_oneway, shapiro
import logging

log = logging.getLogger(__name__)


def detect_drift(data_old: np.array = None, data_new: np.array = None, alpha: np.float16 = 0.05):
    # data_old: Numpy array of the feature data from the old model
    # data_new: Numpy array of the feature data from the new model
    # alpha: Significance level for the statistical tests
    drift = False
    # Test for normality
    stat, pvalue = shapiro(data_old)
    if pvalue < alpha:
        log.info("Data is not normally distributed!")

        # Perform the KS test on the two sets of data
        stat, pvalue = ks_2samp(data_old, data_new)
        if pvalue < alpha:
            log.warning("KS test: Drift detected!")
            drift = True
        else:
            log.info("KS test: No drift detected.")

        # Perform the Mann-Whitney U test on the two sets of data
        stat, pvalue = mannwhitneyu(data_old, data_new)
        if pvalue < alpha:
            log.warning("Mann-Whitney U test: Drift detected!")
            drift = True
        else:
            log.info("Mann-Whitney U test: No drift detected.")

    else:
        log.info("Data is normally distributed.")

        # Perform Student's t-test on the two sets of data
        stat, pvalue = ttest_ind(data_old, data_new)
        if pvalue < alpha:
            log.warning("Student's t-test: Drift detected!")
            drift = True
        else:
            log.info("Student's t-test: No drift detected.")

        # Perform ANOVA on the two sets of data
        stat, pvalue = f_oneway(data_old, data_new)
        if pvalue < alpha:
            log.warning("ANOVA: Drift detected!")
            drift = True
        else:
            log.info("ANOVA: No drift detected.")

    return drift
