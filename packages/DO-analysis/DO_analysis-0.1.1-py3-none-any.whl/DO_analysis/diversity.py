import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
from statannotations.Annotator import Annotator

from skbio.diversity import alpha_diversity
from skbio.diversity import beta_diversity
from skbio.stats.ordination import pcoa
from skbio.stats.distance import anosim, permanova


def select_data_metadata(data, metadata, meta_col='Sample'):
    metadata_time = metadata.loc[metadata[meta_col].isin(data.columns)]
    df_time = data[metadata_time[meta_col]].T
    df_time = df_time.reindex(index=metadata_time[meta_col])
    IDs = list(df_time.index.to_numpy())
    print(metadata_time.shape, df_time.shape, len(IDs))
    return df_time, metadata_time, IDs


def plot_pcoa_beta_diversity(beta_div, metadata_time, hue_feature, ax, results_permanova):
    bd_pc = pcoa(beta_div).samples[['PC1', 'PC2']].rename_axis('name').reset_index()
    bd_pc[hue_feature] = metadata_time[hue_feature].to_numpy()
    g = sns.scatterplot(data=bd_pc, x="PC1", y='PC2', hue=hue_feature, palette="deep",  ax=ax)
    g.set(title='Beta diversity, grouping by ' + hue_feature + ', p-value = ' +str(results_permanova['p-value']))
    g.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), ncol=1)


def plot_hist_bray_curtis(beta_div, IDs, ax, metadata, feature, id_col='Sample'):
    list_values = list(metadata[feature].dropna().unique())
    beta_div_m = pd.DataFrame(beta_div[:], columns=IDs, index=IDs)

    for i, value in enumerate(list_values):
        metadata_v = metadata.loc[metadata[feature] == value]
        samples_v = metadata_v[id_col].dropna()
        beta_div_v = beta_div_m.filter(samples_v, axis=0).filter(samples_v, axis=1)
        beta_div_v = beta_div_v.to_numpy()[np.triu_indices(len(beta_div_v), k=1)]
        ax[i].hist(beta_div_v, bins=100, density=True)
        ax[i].set_title(value + ' median value  %.2f' % np.median(beta_div_v))
        # ax[i].set_ylim([0, 500])

    for val_1, val_2 in list(itertools.combinations(list_values, 2)):
        i += 1
        sampl_1 = metadata.loc[metadata[feature] == val_1][id_col].dropna()
        sampl_2 = metadata.loc[metadata[feature] == val_2][id_col].dropna()
        beta_div_v = beta_div_m.filter(sampl_1, axis=0).filter(sampl_2, axis=1).to_numpy().ravel()
        ax[i].hist(beta_div_v, bins=100, density=True)
        ax[i].set_title(val_1 + ', ' + val_2 + ' median value  %.2f' % np.median(beta_div_v))


def plot_alpha_stat(data, metadata, IDs, feature, ax, pairs=False, alfa_metric='shannon', meta_col='Sample'):
    alpha_div = alpha_diversity(alfa_metric, data, IDs)
    alpha_div = alpha_div.rename_axis(meta_col).reset_index().rename(columns={0: alfa_metric})
    alpha_div = alpha_div.merge(metadata[[feature, meta_col]].astype(str), on=meta_col)
    sns.boxplot(data=alpha_div, x=feature, y=alfa_metric, ax=ax).set(title=alfa_metric + feature)
    sns.scatterplot(data=alpha_div, x=feature, y=alfa_metric, ax=ax)

    if pairs:
        annotator = Annotator(ax, pairs, data=alpha_div, x=feature, y=alfa_metric)  # order=order
        annotator.configure(test='Mann-Whitney', text_format='star', loc='inside')
        annotator.apply_and_annotate()


def plot_diversity(data, metadata, feature, pairs=None, id_column='Sample', beta_metric="braycurtis", alfa_metric='shannon', plot_alpha=True, plot_beta=True):

    fig, ax = plt.subplots(plot_alpha + plot_beta) #figsize=(35, 17)
    df_time, metadata_time, IDs = select_data_metadata(data, metadata)
    if plot_alpha:
        plot_alpha_stat(df_time, metadata_time, IDs, feature, ax[0], pairs, meta_col=id_column, alfa_metric=alfa_metric)

    if plot_beta:
        beta_div = beta_diversity(beta_metric, df_time, IDs)
        results = permanova(beta_div, metadata_time[feature].to_numpy(), permutations=999)
        print('Permanova comparison on ' + feature, results['p-value'] < 0.05, results['p-value'])
        plot_pcoa_beta_diversity(beta_div, metadata_time, 'Breastfeeding_type', ax[plot_alpha + plot_beta - 1], results)

    plt.autoscale(enable=True, axis="x", tight=True)
    plt.show()

