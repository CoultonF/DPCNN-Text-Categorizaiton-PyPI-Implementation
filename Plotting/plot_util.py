import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


# smoothing param moving average
sp=20

# file locations
input_file = 'DBPedia/dbpedia-acc-train.csv'
output_file = 'DBPedia/acc_train.png'
title = 'DBpedia Training Accuracy'
y_label = 'Accuracy'

# context can be: talk, paper, notebook, poster
sns.set_theme(style="whitegrid")
sns.set_context("talk",  rc={"lines.linewidth": 2})

data = pd.read_csv(input_file)
sns_plot = sns.lineplot(y=smooth(data["Value"], sp)[:-sp],x=data["Step"][:-sp]).set_title(title)
plt.ylabel(y_label)
fig = sns_plot.get_figure()
plt.tight_layout()
fig.savefig(output_file)
