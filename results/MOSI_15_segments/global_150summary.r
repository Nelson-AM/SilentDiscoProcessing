Myfit summary

Call:
lm(formula = dep_var ~ group * time_segment, data = csvdata)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.82248 -0.06960  0.00298  0.08898  0.32722 

Coefficients:
                                          Estimate Std. Error t value Pr(>|t|)    
(Intercept)                               0.724223   0.005697 127.121  < 2e-16 ***
groupgreen_global_cluster                -0.051446   0.008086  -6.363 2.00e-10 ***
groupblue_global_cluster                  0.025349   0.008097   3.131  0.00174 ** 
time_segment2                             0.018123   0.008070   2.246  0.02473 *  
time_segment3                            -0.010665   0.008055  -1.324  0.18548    
time_segment4                             0.007638   0.008055   0.948  0.34303    
time_segment5                             0.071028   0.008059   8.813  < 2e-16 ***
time_segment6                            -0.008810   0.008055  -1.094  0.27407    
time_segment7                            -0.025293   0.008055  -3.140  0.00169 ** 
time_segment8                             0.019965   0.008053   2.479  0.01317 *  
time_segment9                             0.015655   0.008057   1.943  0.05201 .  
time_segment10                            0.006399   0.008055   0.794  0.42696    
time_segment11                            0.067742   0.008061   8.403  < 2e-16 ***
time_segment12                            0.098255   0.008068  12.179  < 2e-16 ***
time_segment13                            0.055204   0.008070   6.841 8.00e-12 ***
time_segment14                            0.001216   0.008419   0.144  0.88517    
time_segment15                           -0.014181   0.008053  -1.761  0.07824 .  
groupgreen_global_cluster:time_segment2   0.019492   0.011536   1.690  0.09109 .  
groupblue_global_cluster:time_segment2   -0.046864   0.011533  -4.063 4.84e-05 ***
groupgreen_global_cluster:time_segment3   0.103330   0.011492   8.991  < 2e-16 ***
groupblue_global_cluster:time_segment3   -0.004081   0.011611  -0.351  0.72522    
groupgreen_global_cluster:time_segment4   0.090371   0.011509   7.852 4.20e-15 ***
groupblue_global_cluster:time_segment4   -0.025027   0.011547  -2.167  0.03021 *  
groupgreen_global_cluster:time_segment5  -0.048943   0.011418  -4.287 1.82e-05 ***
groupblue_global_cluster:time_segment5   -0.100808   0.011559  -8.721  < 2e-16 ***
groupgreen_global_cluster:time_segment6   0.063818   0.011416   5.590 2.28e-08 ***
groupblue_global_cluster:time_segment6   -0.036289   0.011595  -3.130  0.00175 ** 
groupgreen_global_cluster:time_segment7   0.075739   0.011416   6.635 3.30e-11 ***
groupblue_global_cluster:time_segment7   -0.037554   0.011758  -3.194  0.00141 ** 
groupgreen_global_cluster:time_segment8   0.009702   0.011408   0.850  0.39511    
groupblue_global_cluster:time_segment8    0.002964   0.012034   0.246  0.80547    
groupgreen_global_cluster:time_segment9  -0.010367   0.011413  -0.908  0.36367    
groupblue_global_cluster:time_segment9   -0.015528   0.011927  -1.302  0.19296    
groupgreen_global_cluster:time_segment10  0.018330   0.011518   1.591  0.11151    
groupblue_global_cluster:time_segment10  -0.062415   0.011835  -5.274 1.34e-07 ***
groupgreen_global_cluster:time_segment11 -0.001447   0.011449  -0.126  0.89942    
groupblue_global_cluster:time_segment11  -0.142883   0.011439 -12.490  < 2e-16 ***
groupgreen_global_cluster:time_segment12  0.015347   0.011630   1.320  0.18695    
groupblue_global_cluster:time_segment12  -0.167368   0.011430 -14.643  < 2e-16 ***
groupgreen_global_cluster:time_segment13  0.007359   0.011449   0.643  0.52039    
groupblue_global_cluster:time_segment13  -0.112045   0.011430  -9.803  < 2e-16 ***
groupgreen_global_cluster:time_segment14  0.021363   0.013064   1.635  0.10201    
groupblue_global_cluster:time_segment14  -0.036597   0.012128  -3.018  0.00255 ** 
groupgreen_global_cluster:time_segment15  0.053798   0.012244   4.394 1.12e-05 ***
groupblue_global_cluster:time_segment15   0.024718   0.012142   2.036  0.04179 *  
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.1735 on 38349 degrees of freedom
  (3369 observations deleted due to missingness)
Multiple R-squared:  0.03852,	Adjusted R-squared:  0.03741 
F-statistic: 34.92 on 44 and 38349 DF,  p-value: < 2.2e-16

