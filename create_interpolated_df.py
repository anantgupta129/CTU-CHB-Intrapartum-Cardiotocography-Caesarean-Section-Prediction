import os

import pandas as pd

from utils.signal_analysis import interpolate_df


root = 'database/signals/'
files = os.listdir(root)

for count, f_name in enumerate(files):
    try:
        path = root + f_name
        df = pd.read_csv(path)
        df = interpolate_df(df, 'FHR')
        patiend_id = f_name.split('.')[0]
        df.to_csv(f'database/signals-interpolated/{patiend_id}.csv', index=False)

        print(f'Saved {f_name}, done {count+1}', end='\r')
    except Exception as e:
        print(e)
        print(f_name)

