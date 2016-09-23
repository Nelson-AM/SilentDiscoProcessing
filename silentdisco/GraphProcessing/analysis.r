library(car)
library(heplots)

# Read data from csv.
localpath <- "/Volumes/SAMSUNG/ESCOM/localdata_150.csv"

localdata <- read.csv(localpath, header = T, dec = ".", sep = ",")
# loalcadata <- as.matrix(localdata)

# Define groups
n = 2
k = 36949
group <- gl(n, k, n * k, labels = c("green_local_cluster", "red_local_cluster"))


create_segments <- function(n_segments){
    segments = matrix(data = NaN, ncol = lengths(localdata["full_frameno"]))
    cuts = matrix(data = NaN, ncol = n_segments - 1)
    
    for (i in 1:length(cuts)){
        cuts[i] = (i / n_segments) * length(segments)
        cat(cuts[i])
    }
    for (i in 1:n_segments){
        if (i == 1){
            segments[1:cuts[i]] = i
        } else if (i == n_segments) {
            segments[cuts[i - 1]:length(segments)] = i
        } else {
            segments[cuts[i - 1]:cuts[i]] = i
        }
    }
    return(segments)
}


# Define time segments
# Replace ranges of frame numbers with numbers 1:n
n_segments = 30
segments = create_segments(n_segments)

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

Anova(myfit)
etasq(myfit, type = 2)