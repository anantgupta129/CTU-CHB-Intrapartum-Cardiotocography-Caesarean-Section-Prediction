import os

import numpy as np
import pandas as pd


ann_df = pd.read_csv('database/ann_db.csv')
ann_df.sort_values('ID', inplace=True)

for phase in ['', '-interpolated']:
    print(phase)
    path = r'database/signals{}'.format(phase)
    files = os.listdir(path)

    mean_f =[]
    median_f = []
    sd_f = []
    peak_f = []
    rms_f = []
    peakto_rms_f = []

    mean_u =[]
    median_u = []
    sd_u = []
    peak_u = []
    rms_u = []
    peakto_rms_u = []

    target = []
    ids = []
    for f in files:
        file_path = os.path.join(path, f)
        df = pd.read_csv(file_path)
        # FHR
        mean_f.append(np.mean(df.FHR_denoised))
        median_f.append(np.median(df.FHR_denoised))
        sd_f.append(np.std(df.FHR_denoised))
        rms_f.append(np.sqrt(np.mean(df.FHR_denoised**2)))
        peak_f.append(np.max(df.FHR_denoised))
        peakto_rms_f.append(np.max(df.FHR_denoised) - np.sqrt(np.mean(df.FHR_denoised**2)))
        # UC
        mean_u.append(np.mean(df.UC))
        median_u.append(np.median(df.UC))
        sd_u.append(np.std(df.UC))
        rms_u.append(np.sqrt(np.mean(df.UC**2)))
        peak_u.append(np.max(df.UC))
        peakto_rms_u.append(np.max(df.UC) - np.sqrt(np.mean(df.UC**2)))
        
        if f[0]=='1':
            target.append(1)
        else:
            target.append(0)
        
        ids.append(int(f.split(".")[0]))

    main_df = pd.DataFrame({
        'Patient_ID':ids,
        'Mean_FHR': mean_f,
        'Mean_UC': mean_u,
        'Median_FHR': median_f,
        'Median_UC': median_u,
        'Std_FHR': sd_f,
        'Std_UC': sd_u,
        'RMS_FHR': rms_f,
        'RMS_UC': rms_u,
        'Peak_to_RMS_FHR': peakto_rms_f,
        'Peak_to_RMS_UC': peakto_rms_u,
        'Peak_FHR': peak_f,
        'Peak_UC': peak_u,
        'target': target,
    })

    main_df.sort_values('Patient_ID', inplace=True)
    final_df = pd.concat([ann_df, main_df], axis=1)

    final_df.drop(['Patient_ID'], axis=1,inplace=True)
    print(final_df.head())
    final_df.to_csv("database/ctu_df{}.csv".format(phase), index=False)


