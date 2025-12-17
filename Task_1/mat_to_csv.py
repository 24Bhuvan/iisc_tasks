#found from google

import scipy.io
import pandas as pd

# load mat file (make sure values.mat is in same folder)
mat = scipy.io.loadmat("values.mat")

# extract only required variable
values = mat["values"].squeeze()  # removes extra brackets

# convert to DataFrame
df = pd.DataFrame(values, columns=["values"])

# save to csv
df.to_csv("filename.csv", index=False)
