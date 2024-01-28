import numpy as np
import pandas as pd


def has_fever(temperatures, limit):
    return temperatures >= limit


def temperature_group(temperatures):
    """
    Split temperatures in groups like:
        T < 38
        38 <= T < 38.5
        38.5 <= T < 39
        T >= 39

    Reference:
        Performance of influenza case definitions for influenza community
        surveillance: based on the French influenza surveillance network
        GROG, 2009-2014. Casalegno et al., 2016
        https://www.eurosurveillance.org/content/10.2807/1560-7917.ES.2017.22.14.30504#t1
    """
    params = dict(right=False, include_lowest=True)
    custom_bins = [0, 38, 38.5, 39, np.inf]
    grouped_data = pd.cut(temperatures, bins=custom_bins, **params)
    return grouped_data, custom_bins
