#!/usr/bin/env python

    # Moving averages over full data.
    localav = pd.ewma(fulldf.localcluster, span = span)
    localavsd = pd.ewma(fulldf.localsd, span = span)
    
    globalav = pd.ewma(fulldf.globalcluster, span = span)
    globalavsd = pd.ewma(fulldf.globalsd, span = span)
    
    vertexav = pd.ewma(fulldf.vertexaverage, span = span)
    vertexavsd = pd.ewma(fulldf.vertexsd, span = span)
    
    # Append smoothed values to dataframe
    smoothdf = smoothdf.append({"frameno": int(i[1]),
                                "localcluster": localav,
                                "localsd": localavsd,
                                "globalcluster": globalav,
                                "globalsd": globalavsd,
                                "vertexaverage": vertexav,
                                "vertexsd": vertexavsd},
                                ignore_index = True)
    
    # TODO: save dataframe.
    smoothcsvname = savedir + "smoothdata_t" + str(threshold) + "_s50.csv"
    smoothdf.to_csv(smoothcsvname, sep = ",")
    
    
    globalplotname = (savedir + "global_" + str(threshold) + "_" +
                     str(frame_start) + "_" + str(frame_stop) + ".png")
    globalewmaplotname = (savedir + "global" + str(threshold) + "_" +
                    str(frame_start) + "_" + str(frame_stop) + "ewma_" + str(span) + ".png")
    localplotname = (savedir + "local_" + str(threshold) + "_" +
                    str(frame_start) + "_" + str(frame_stop) + ".png")
    localewmaplotname = (savedir + "local" + str(threshold) + "_" +
                    str(frame_start) + "_" + str(frame_stop) + "ewma_" + str(span) + ".png")
    vertavplotname = (savedir + "vertav_" + str(threshold) + "_" + 
                     str(frame_start) + "_" + str(frame_stop) + ".png")
    vertavewmaplotname = (savedir + "vertav" + str(threshold) + "_" + 
                     str(frame_start) + "_" + str(frame_stop) + "ewma_" + str(span) + ".png")
    
    # Plot local clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, fulldf.localcluster, color = "black")
    plt.fill_between(fulldf.frameno,
                     fulldf.localcluster - fulldf.localsd,
                     fulldf.localcluster + fulldf.localsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 1.2])
    axes.set_xlim([frame_start, frame_total])
    
    plt.savefig(localplotname)
    plt.clf()
    
    # Plot local clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, localav, color = "black")
    plt.fill_between(fulldf.frameno,
                     localav - localsd,
                     localav + localsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 1.2])
    axes.set_xlim([frame_start, frame_total])
    
    plt.savefig(localewmaplotname)
    plt.clf()
    
    
    # Plot global clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, fulldf.globalcluster, color = "black")
    plt.fill_between(fulldf.frameno, 
                     fulldf.globalcluster - fulldf.globalsd, 
                     fulldf.globalcluster + fulldf.globalsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 1.2])
    axes.set_xlim([frame_start, frame_total])
    
    
    
    plt.savefig(globalplotname)
    plt.clf()
    
    
    
    globalav = pd.ewma(fulldf.globalcluster, span = span)
    globalsd = pd.ewma(fulldf.globalsd, span = span)
    
    # EWMA GLOBAL
    # Plot global clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, globalav, color = "black")
    plt.fill_between(fulldf.frameno, 
                     globalav - globalsd, 
                     globalav + globalsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 1.2])
    axes.set_xlim([frame_start, frame_total])
    
    plt.savefig(globalewmaplotname)
    plt.clf()
    
    
    
    # Plot vertex average + shaded standard deviation.
    plt.plot(fulldf.frameno, fulldf.vertexaverage, color = "black")
    plt.fill_between(fulldf.frameno,
                     fulldf.vertexaverage - fulldf.vertexsd,
                     fulldf.vertexaverage + fulldf.vertexsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 5])
    axes.set_xlim([frame_start, frame_total])
    plt.savefig(vertavplotname)
    
    plt.clf()
    
    # EWMA VERTEX AVERAGE
    # Plot vertex average + shaded standard deviation.
    plt.plot(fulldf.frameno, vertexav, color = "black")
    plt.fill_between(fulldf.frameno,
                     vertexav - vertexsd,
                     vertexav + vertexsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 5])
    axes.set_xlim([frame_start, frame_total])
    plt.savefig(vertavewmaplotname)
    
    plt.clf()