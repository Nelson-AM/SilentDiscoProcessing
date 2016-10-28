library(car)
library(heplots)

# TODO: integrate analysis with python code.

barepath <- "/Volumes/SAMSUNG/ESCOM/"
framename <- "framedata_"
filename <- "vertexdata_"
thresholds <- c(150, 200, 250)
extension <- ".csv"

greenlabel <- "green_vertex_average"
redlabel <- "red_vertex_average"
greenvertices <- "green_vertices"
redvertices <- "red_vertices"
# Read data from csv.

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

for(i in 1:length(testval)) {
	inpath <- paste(barepath, filename, toString(thresholds[i]), extension, sep="")
	framepath <- paste(barepath, framename, toString(thresholds[i]), extension, sep="")
	sumpath <- paste(barepath, "results/vertex_norm_", toString(thresholds[i]), "_summary.r", sep="")
	etapath <- paste(barepath, "results/vertex_norm_", toString(thresholds[i]), "_etasq.r", sep="")
	anopath <- paste(barepath, "results/vertex_norm_", toString(thresholds[i]), "_anova.r", sep="")
	
	csvdata <- read.csv(inpath, header=T, dec=".", sep=",")
	framedata <- read.csv(framepath, header=T, dec=".", sep=",")

	# Define groups
	n = 2
	k = 36949

	group <- gl(n, k, n * k, labels = c(greenlabel, redlabel))


	# Define time segments
	# Replace ranges of frame numbers with numbers 1:n
	n_segments = 60
	segments = create_segments(n_segments)

	# Then convert to a factor
	twosegments = c(segments, segments)
	time_segment <- factor(twosegments)
	
	# Normalise dependent variables.
	

	# Define dependent variable (clustering measures)
	dep_var <- c(as.numeric(unlist(csvdata[greenlabel])) / 
				 as.numeric(unlist(framedata[greenvertices])), 
				 as.numeric(unlist(csvdata[redlabel])) / 
				 as.numeric(unlist(framedata[redvertices])))

	# Response is a vector of values for a channel (in a given time segment).
	# Terms is two things: 
	myfit <- lm(dep_var ~ group * time_segment, data = csvdata)

	Anova(myfit)
	etasq(myfit, type = 2)
	
	sumout <- capture.output(summary(myfit))
	etaout <- capture.output(etasq(myfit))
	anoout <- capture.output(Anova(myfit))
	
	cat("Myfit summary", sumout, file=sumpath, sep="\n", append=TRUE)
	cat("Myfit Anova", anoout, file=anopath, sep="\n", append=TRUE)
	cat("Myfit etasq", etaout, file=etapath, sep="\n", append=TRUE)
}