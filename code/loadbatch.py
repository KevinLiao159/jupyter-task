import os
import glob
from collections import defaultdict

import pandas as pd
import numpy as np


def load_batch(batch_directory):
    df_batches = defaultdict(list)
    for key in {
        'metrics',
        'orders',
        'portfolio',
        'simulation',
        'target_portfolio',
        'transactions',
    }:
        dfs = []
        for pickle_filepath in glob.glob(os.path.join(batch_directory, '**', key + '.pkl')):
            dfs.append(pd.read_pickle(pickle_filepath))
        df_batches[key] = pd.concat(dfs)
    return df_batches