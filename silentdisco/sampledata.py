#!/usr/bin/env python
# testquantiles

import pandas as pd
import numpy as np

series = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sampledata = pd.DataFrame({"frameno": series,
                           "segment": np.full(len(series), np.nan)})

# print sampledata

for col in sampledata:
    print(col)
