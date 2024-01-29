import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.ndimage import uniform_filter1d

import seaborn as sns
import matplotlib.pyplot as plt


#Define Kullback-Leibler Divergence
def KLD(x,y):
    return(sum(x*np.log(x/y)))


#Define Jason-Shanon Divergence
def rJSD(x,y):
    value = (np.sqrt(0.5 * KLD(x, (x+y)/2) + 0.5 * KLD(y, (x+y)/2)))
    if (0.5 * KLD(x, (x+y)/2) + 0.5 * KLD(y, (x+y)/2)) < 0:
        print('Negative value !!!', np.log(x /((x+y)/2)), x /((x+y)/2), np.log(y /((x+y)/2)), y /((x+y)/2))
        value = 0
    return value


def calc_Overlap_rJSD(df, NumSamples):
    Overlap = pd.DataFrame(index=range(NumSamples), columns=range(NumSamples))
    RootJSD = pd.DataFrame(index=range(NumSamples), columns=range(NumSamples))
    counter = 0
    num_shared_sp = list()

    df_table = df.T.to_numpy()

    for i in range(0, NumSamples - 1):
        for j in range(i + 1, NumSamples):
            SharedSpecies = list(np.where((df_table[i] > 0) & (df_table[j] > 0))[0])
            num_shared_sp.append(len(SharedSpecies))
            counter += 1
            if len(SharedSpecies) == 0:
                Overlap[i][j] = 0
                RootJSD[i][j] = 0
            else:
                Overlap[i][j] = 0.5 * (sum(df_table[i, SharedSpecies]) + sum(df_table[j, SharedSpecies]))

                # Renormalize the shared species
                RenormalizedA = df_table[i, SharedSpecies] / sum(df_table[i, SharedSpecies])
                RenormalizedB = df_table[j, SharedSpecies] / sum(df_table[j, SharedSpecies])

                # Calculate the rJSD dissimilarity
                RootJSD[i][j] = rJSD(RenormalizedA, RenormalizedB)

    print('max shared sp = ', max(num_shared_sp), '; min shared sp = ', min(num_shared_sp), '; mean shared sp = ',
          sum(num_shared_sp) / len(num_shared_sp))

    return Overlap, RootJSD, num_shared_sp

def flattten_Overlap_rJSD(Overlap, RootJSD, Subj1, Subj2):
    Overlap = Overlap.to_numpy().ravel().astype('float')
    RootJSD = RootJSD.to_numpy().ravel().astype('float')
    Subj1 = Subj1.ravel()
    Subj2 = Subj2.ravel()

    RootJSD = RootJSD[~np.isnan(RootJSD)]
    Subj1 = Subj1[~np.isnan(Overlap)]
    Subj2 = Subj2[~np.isnan(Overlap)]
    Overlap = Overlap[~np.isnan(Overlap)]

    RootJSD = RootJSD[Overlap > 0]
    Subj1 = Subj1[Overlap > 0]
    Subj2 = Subj2[Overlap > 0]
    Overlap = Overlap[Overlap > 0]
    print('final len Overlap, RootJSD', len(Overlap), len(RootJSD))
    return Overlap, RootJSD, Subj1, Subj2



def lowess_with_confidence_bounds(x, y, Subj1, Subj2, N=10, frac=0.2, conf_interval=0.95):
    """
    Perform Lowess regression and determine a confidence interval by bootstrap resampling
    """
    # Lowess smoothing
    NumPointsInGrid = 100
    change_point = np.median(x)

    xs = np.linspace(min(x), max(x), num=NumPointsInGrid)
    smoothed = sm.nonparametric.lowess(exog=x, endog=y, xvals=xs, frac=frac)

    # Perform bootstrap resamplings of the data
    # and  evaluate the smoothing at a fixed set of points
    smoothed_values = np.empty((N, NumPointsInGrid))
    num_points = len(x)
    p_lme = np.empty(N)  # (N,1)

    for i in range(N):
        sample = np.random.choice(num_points, num_points, replace=True)
        sampled_x = x[sample]
        sampled_y = y[sample]
        Subj1_sampled = Subj1[sample]
        Subj2_sampled = Subj2[sample]
        smoothed_values[i] = sm.nonparametric.lowess(exog=sampled_x, endog=sampled_y, xvals=xs, frac=frac)

        # fit lme for each bootstrap realization
        ind_LowOverlap = x > change_point
        Overlap = sampled_x[ind_LowOverlap]
        RootJSD = sampled_y[ind_LowOverlap]
        Subj1_sampled = Subj1_sampled[ind_LowOverlap]
        Subj2_sampled = Subj2_sampled[ind_LowOverlap]

        data = pd.DataFrame({'Subj1': Subj1_sampled, 'Subj2': Subj2_sampled, 'Overlap': Overlap, 'RootJSD': RootJSD})
        md = smf.mixedlm("RootJSD ~ 1 + Overlap", data, groups=data["Subj1"])
        mdf = md.fit(method=["powell", "lbfgs"])

        p_lme[i] = mdf.params['Overlap']

    sorted_values = np.sort(smoothed_values, axis=0)
    bound = int(N * (1 - conf_interval) / 2)
    bottom = sorted_values[bound - 1]
    top = sorted_values[-bound]

    return smoothed, bottom, top, xs, p_lme

def detect_negative_slope(xx,yy):
    Smoothed_yy = uniform_filter1d(yy, size=3)
    LocalSlope = np.diff(Smoothed_yy)/np.diff(xx)
    indices = np.argwhere(LocalSlope>0)
    if len(indices) ==0:
        xc = xx[0]
    else:
        xc = xx[indices[-1]]
    return xc, LocalSlope


def DOC_with_plots(data, metadata, feature, num_bins=50, sample_col='Sample'):
    num_class = len(metadata[feature].dropna().unique())
    print(num_class)
    fig, ax = plt.subplots(3, num_class + 1, figsize=(25, 18))

    for k, value in enumerate(metadata[feature].dropna().unique()):
        df_time_with_zeros = data[(metadata.loc[metadata[feature] == value][sample_col].to_list())]
        df_time = df_time_with_zeros.loc[(df_time_with_zeros != 0).any(axis=1)]
        NumSpecies, NumSamples = df_time.shape
        print('NumSpecies, NumSamples = ', NumSpecies, NumSamples, 'for class', value)
        print('Mean number of OTU = %.2f' % (df_time > 0).sum(axis=0).mean())

        if NumSamples < 2:
            print("Not enough samples !!!")
        else:
            Overlap, RootJSD, num_shared_sp = calc_Overlap_rJSD(df_time, NumSamples)
            # print counts stat
            num_shared_sp_unique = list(set(num_shared_sp))
            counts = [num_shared_sp.count(value) for value in num_shared_sp_unique]
            sns.barplot(x=num_shared_sp_unique, y=counts, ax=ax[0, k]).set_title(
                value + ', NumSpecies, NumSamples = ' + str(NumSpecies) + ', ' + str(NumSamples))
            # plot DOC curve
            Subj1 = np.tile(np.arange(1, NumSamples + 1, 1), (NumSamples, 1))
            Subj2 = np.tile(np.arange(1, NumSamples + 1, 1)[:, None], (1, NumSamples))
            Overlap, RootJSD, Subj1, Subj2 = flattten_Overlap_rJSD(Overlap, RootJSD, Subj1, Subj2)
            if len(Overlap) > 10:
                smoothed, bottom, top, xs, slope_lme = lowess_with_confidence_bounds(Overlap, RootJSD, Subj1, Subj2, 10,
                                                                                     0.3, 0.95)
                # Fraction of data with negative slope
                xc, LocalSlope = detect_negative_slope(xs, smoothed)
                Fns = sum(Overlap > xc) / len(Overlap)
                P_real = sum(slope_lme >= 0) / len(slope_lme)
                print('Fraction of data with negative slope', Fns)
                print('Fraction of times p_lme is non-negative, P_real =', P_real,
                      'mean slope_lme = %.2f ' % slope_lme.mean())
                print()

                ax[1, k].hist(Overlap, bins=num_bins)
                ax[1, k].set_title('Overlap distribution')
                ax[2, k].scatter(Overlap, RootJSD)
                ax[2, k].plot(xs, smoothed, c='r')  # smoothed[:, 0], smoothed[:, 1], c= 'r')
                ax[2, k].set_ylim([0, 1])
                ax[2, k].set_xlim([0, 1])
                ax[2, k].fill_between(xs, bottom, top, alpha=0.5, color="b")
                ax[2, k].set_title('mean slope_lme = %.2f ' % slope_lme.mean())
            else:
                print('N pairs of samples with Ovarlap > 0 is <=10')

    df_time_with_zeros = data[(metadata[sample_col].to_list())]
    df_time_all = df_time_with_zeros.loc[(df_time_with_zeros != 0).any(axis=1)]
    NumSpecies, NumSamples = df_time_all.shape
    print('NumSpecies, NumSamples = ', NumSpecies, NumSamples, 'for all samples')
    print('Mean number of OTU = %.2f' % (df_time_all > 0).sum(axis=0).mean())
    Overlap, RootJSD, num_shared_sp = calc_Overlap_rJSD(df_time_all, NumSamples)

    # print counts stat
    num_shared_sp_unique = list(set(num_shared_sp))
    counts = [num_shared_sp.count(value) for value in num_shared_sp_unique]
    sns.barplot(x=num_shared_sp_unique, y=counts, ax=ax[0, -1]).set_title(
        'all , NumSpecies, NumSamples = ' + str(NumSpecies) + ', ' + str(NumSamples))

    Subj1 = np.tile(np.arange(1, NumSamples + 1, 1), (NumSamples, 1))
    Subj2 = np.tile(np.arange(1, NumSamples + 1, 1)[:, None], (1, NumSamples))
    Overlap, RootJSD, Subj1, Subj2 = flattten_Overlap_rJSD(Overlap, RootJSD, Subj1, Subj2)
    smoothed, bottom, top, xs, slope_lme = lowess_with_confidence_bounds(Overlap, RootJSD, Subj1, Subj2, 10, 0.3, 0.95)

    # Fraction of data with negative slope
    xc, LocalSlope = detect_negative_slope(xs, smoothed)
    Fns = sum(Overlap > xc) / len(Overlap)
    P_real = sum(slope_lme >= 0) / len(slope_lme)
    print('Fraction of data with negative slope', Fns)
    print('Fraction of times p_lme is non-negative, P_real =', P_real, 'mean slope_lme = %.2f ' % slope_lme.mean())
    print()
    ax[1, -1].hist(Overlap, bins=num_bins)
    ax[1, -1].set_title('Overlap distribution')
    ax[2, -1].scatter(Overlap, RootJSD)
    ax[2, -1].plot(xs, smoothed, c='r')
    ax[2, -1].set_ylim([0, 1])
    ax[2, -1].set_xlim([0, 1])
    ax[2, -1].fill_between(xs, bottom, top, alpha=0.5, color="b")
    ax[2, -1].set_title('mean slope_lme = %.2f ' % slope_lme.mean())

    plt.autoscale(enable=True, axis="x", tight=True)
    plt.show()


def run_DOC_time(data, metadata, times, feature, time_col='Time', sample_col='Sample'):

    for reg in times:
        print('Analyzing for time =', reg)
        metadata_time = metadata.loc[(metadata[time_col] == reg) & (metadata[sample_col].isin(data.columns))]
        print(metadata_time[feature].unique(), metadata_time.shape)
        DOC_with_plots(data, metadata_time, feature)
