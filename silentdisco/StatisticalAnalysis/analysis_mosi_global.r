library(car)
library(heplots)

# TODO: integrate analysis with python code.

barepath <- "/Volumes/SAMSUNG/MOSI/"
filename <- "csv/globaldata_"
thresholds <- c(150, 200, 250)
extension <- ".csv"

redlabel <- "red_global_cluster"
greenlabel <- "green_global_cluster"
bluelabel <- "blue_global_cluster"

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

for(i in 1:length(thresholds)) {
	inpath <- paste(barepath, filename, toString(thresholds[i]), extension, sep="")
	sumpath <- paste(barepath, "results/global_", toString(thresholds[i]), "summary.r", sep="")
	etapath <- paste(barepath, "results/global_", toString(thresholds[i]), "etasq.r", sep="")
	anopath <- paste(barepath, "results/global_", toString(thresholds[i]), "anova.r", sep="")
	
	csvdata <- read.csv(inpath, header=T, dec=".", sep=",")
	
	# Define groups
	# TODO: check if groups are properly defined.
	n = 3
	k = 13921
	
	group <- gl(n, k, n * k, labels=c(redlabel, greenlabel, bluelabel))
	
	# Define time segments
	# Replace ranges of frame numbers with numbers 1:n
	n_segments = 15
	segments = create_segments(n_segments)
	
	# Then convert to a factor
	threesegments = c(segments, segments, segments)
	time_segment = factor(threesegments)
	
	# Define dependent variable (clustering measures)
	dep_var <- c(as.numeric(unlist(csvdata[redlabel])),
				 as.numeric(unlist(csvdata[greenlabel])),
				 as.numeric(unlist(csvdata[bluelabel])))
	
	# Response is a vector of values for a channel (in a given time segment).
	# Terms is two things:
	myfit <- lm(dep_var ~ group * time_segment, data=csvdata)
	
	sumout <- capture.output(summary(myfit))
	etaout <- capture.output(etasq(myfit, type=2))
	anoout <- capture.output(Anova(myfit))
	
	cat("Myfit summary", sumout, file=sumpath, sep="\n", append=TRUE)
	cat("Myfit Anova", anoout, file=anopath, sep="\n", append=TRUE)
	cat("Myfit etasq", etaout, file=etapath, sep="\n", append=TRUE)
}