# DOC analysis
A Python library for calculating Dissimilarity Overlap Curve and alpha/beta diversity for microbiome samples
### Installation
```
pip install DO_analysis
```

### Get started
How to plot DOC curve with this lib:

``` Python
from DOC_analysis.DOC import DOC_with_plots

#upload ASV or abundance table as data, with columns as samples and rows as taxa
#upload metadata table with information about samples
#let metadata table have column of interest 'Group'
#Then simply run:

DOC_with_plots(data, metadata, 'Group')
```

### Available functions

**DOC.DOC_with_plots(data, metadata, feature, num_bins=50, sample_col='Sample')** - plots DOC curve for each group and all groups combined

**DOC.run_DOC_time(data, metadata, times, feature, time_col='Time', sample_col='Sample')** - if you have longitudinal data, it will generate DOC plots across all time points and for each group

**diversity.plot_diversity(data, metadata, feature, pairs=None, id_column='Sample', beta_metric="braycurtis", alfa_metric='shannon', plot_alpha=True, plot_beta=True)** - to compute and plot alpha and beta diversity metrics
