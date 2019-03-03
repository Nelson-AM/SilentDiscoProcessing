import pandas as pd

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6



# TODO: check if scipy, numpy, pandas and matplotlib have the same functionality as these R packages.
# They probably do.
# library(car)
# library(heplots)

# TODO: read csv 
data = pd.read_csv("/Volumes/SAMSUNG/ESCOM/localdata_150.csv", index_col="full_frameno")
# print data.head()
# print "\n Data types:"
# print data.dtypes

print(data.index)

# TODO: transform dataframes to timeseries
# gts = greendf["localcluster"]
# rts = reddf["localcluster"]

# TODO: define segment (can also be done in the model creation based on the index)
# TODO: Save dataframes for testing.


# TODO: create linear model in scipy function.
# A typical model (first variable of lm) has the following form:
# 	response ~ terms
# where response is the (numeric) response vector and terms is a series of terms which specifies a linear predictor for response.  A terms specification of the form first * second

# Response is a vector of values for a channel (in a given time segment).
# Terms is two things: 
# myfit <- lm(dependent_variable ~ channel * time_segment, data = mydata)

# TODO: anova and py-equivalent of etasq for the fitted model.
# Anova(my_fit)
# etasq(my_fit, type = 2)