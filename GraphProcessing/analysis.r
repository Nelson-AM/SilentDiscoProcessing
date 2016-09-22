library(car)
library(heplots)

# Read data from csv.
localpath <- "localdata_150.csv"

localdata <- read.csv(localpath, header = T, dec = ".", sep = ",")
# loalcadata <- as.matrix(localdata)

# Define groups
n = 2
k = 36949
group <- gl(n, k, n * k, labels = c("green_local_cluster", "red_local_cluster"))

# Define time segments
# Replace ranges of frame numbers with numbers 1:n
# Define cutpoints:
cut_1 = (1/4)*lengths(localdata["full_frameno"])
cut_2 = (2/4)*lengths(localdata["full_frameno"])
cut_3 = (3/4)*lengths(localdata["full_frameno"])

(segments <- rep(NA, lengths(localdata["full_frameno"])))
segments[1:cut_1] = 1
segments[cut_1:cut_2] = 2
segments[cut_2:cut_3] = 3
segments[cut_3:length(segments)] = 4

# Then convert to a factor
twosegments = c(segments, segments)
time_segment <- factor(twosegments)

# Define dependent variable (clustering measures)
dep_var <- c(as.numeric(unlist(localdata["green_local_cluster"])), 
             as.numeric(unlist(localdata["red_local_cluster"])))



# Response is a vector of values for a channel (in a given time segment).
# Terms is two things: 

# myfit <- lm(dep_var ~ group, data = localdata)
myfit <- lm(dep_var ~ group * time_segment, data = localdata)


# myfit <- lm(dep_var ~ channel * time_segment, data = mydata)
Anova(myfit)
etasq(myfit, type = 2)