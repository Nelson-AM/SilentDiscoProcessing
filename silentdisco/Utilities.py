import sys

def printProgress(iteration, 
                  total, 
                  prefix = "", 
                  suffix = "", 
                  decimals = 1,
                  barLength = 100):
    """ Call in a loop to create terminal progress bar.
    
    Params:
        iteration
        total
        prefix
        suffix
        decimals
        barLength
    """
    
    formatStr = "{0:." + str(decimals) + "f}"
    percents = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = "X" * filledLength + "=" * (barLength - filledLength)
    sys.stdout.write("\r%s |%s| %s%s %s" % (prefix, 
                                            bar, 
                                            percents,
                                            "%", 
                                            suffix))
    sys.stdout.flush()
    
    if iteration == total:
        sys.stdout.write("\n")
        sys.stdout.flush()