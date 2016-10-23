library(car)
library(heplots)

# TODO: integrate analysis with python code.

# Read data from csv.
path <- "/Volumes/SAMSUNG/ESCOM/vertexdata_150.csv"
greenlabel <- "green_vertex_average"
redlabel <- "red_vertex_average"

csvdata <- read.csv(path, header = T, dec = ".", sep = ",")

# Define groups
n = 2
k = 36949

group <- gl(n, k, n * k, labels = c(greenlabel, redlabel))

create_segments <- function(n_segments){
    segments = matrix(data = NaN, ncol = lengths(csvdata["full_frameno"]))
    cuts = matrix(data = NaN, ncol = n_segments - 1)
    
    for (i in 1:length(cuts)){
        cuts[i] = (i / n_segments) * length(segments)
        cat(cuts[i])
    }
    for (i in 1:n_segments){
        if (i == 1){
            segments[1:round(cuts[i])] = i
        } else if (i == n_segments) {
            segments[round(cuts[i - 1]):length(segments)] = i
        } else {
            segments[round(cuts[i - 1]):round(cuts[i])] = i
        }
    }
    return(segments)
}


# Define time segments
# Replace ranges of frame numbers with numbers 1:n
n_segments = 60
segments = create_segments(n_segments)

# Then convert to a factor
twosegments = c(segments, segments)
time_segment <- factor(twosegments)

# Define dependent variable (clustering measures)
dep_var <- c(as.numeric(unlist(csvdata[greenlabel])), 
             as.numeric(unlist(csvdata[redlabel])))

# Response is a vector of values for a channel (in a given time segment).
# Terms is two things: 
myfit <- lm(dep_var ~ group * time_segment, data = csvdata)

Anova(myfit)
etasq(myfit, type = 2)