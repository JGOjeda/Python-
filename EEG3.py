# License: BSD-3-Clause
# Copyright the MNE-Python contributors.
import time
import numpy as np

import mne



## 2 bloque descargamos datos 
sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif"
)

sample_data_raw_file2 = (
    sample_data_folder / "MEG" / "sample" / "Jesus_19_Marzo_2024_001.cnt"
)

raw = mne.io.read_raw_fif(sample_data_raw_file)
raw2 = mne.io.read_raw_cnt(sample_data_raw_file2)

print(sample_data_raw_file)
print(sample_data_raw_file2) 

#raw = mne.io.read_raw_fif(sample_data_raw_file)
#raw = mne.io._get_cnt_info(sample_data_raw_file, preload= True)


