# TODO: fix function, somehow last value is 
create_segments <- function(n_segments, n_cols){
    segments = matrix(data = NaN, ncol = n_cols)
    cuts = matrix(data = NaN, ncol = n_segments - 1)
    
    for (i in 1:length(cuts)){
        cuts[i] = (i / n_segments) * length(segments)
    }
    for (i in 1:n_segments){
        if (i == 1){
            segments[1:cuts[i]] = i
        } else if (i == n_segments) {
            segments[cuts[i - 1]:length(segments)+1] = i
        } else {
            cat(cuts[i])
            segments[cuts[i - 1]:cuts[i]] = i
        }
    }
    return(segments)
}


# Define time segments
# Replace ranges of frame numbers with numbers 1:n
n_segments = 3
n_cols = 12
segments = create_segments(n_segments, n_cols)