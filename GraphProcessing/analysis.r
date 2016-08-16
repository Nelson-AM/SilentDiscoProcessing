library(car)
library(heplots)

# Read data from csv.
redpath <- "/Volumes/SAMSUNG/csv/reddata_t150.csv"
greenpath <- "/Volumes/SAMSUNG/csv/greendata_t150.csv"

reddata <- read.csv(redpath, header = T, dec = ".", sep = ",")
greendata <- read.csv(greenpath, header = T, dec = ".", sep = ",")

print(reddata)
# Define time_segments

# A typical model (first variable of lm) has the following form:
# 	response ~ terms
# where response is the (numeric) response vector and terms is a series of terms which specifies a linear predictor for response.  A terms specification of the form first * second

# Response is a vector of values for a channel (in a given time segment).
# Terms is two things: 

myfit <- lm(dependent_variable ~ channel * time_segment, data = mydata)


# myfit <- lm(dep_var ~ channel * time_segment, data = mydata)
# Anova(my_fit)
# etasq(my_fit, type = 2)