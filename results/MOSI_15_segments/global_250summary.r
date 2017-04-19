Myfit summary

Call:
lm(formula = dep_var ~ group * time_segment, data = csvdata)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.79029 -0.05345 -0.00704  0.05562  0.32196 

Coefficients:
                                          Estimate Std. Error t value Pr(>|t|)    
(Intercept)                               0.755630   0.003940 191.779  < 2e-16 ***
groupgreen_global_cluster                -0.037041   0.005578  -6.640 3.17e-11 ***
groupblue_global_cluster                 -0.004987   0.005574  -0.895 0.370888    
time_segment2                            -0.018010   0.005571  -3.233 0.001226 ** 
time_segment3                            -0.019727   0.005571  -3.541 0.000399 ***
time_segment4                            -0.016213   0.005571  -2.910 0.003611 ** 
time_segment5                             0.043621   0.005571   7.830 4.98e-15 ***
time_segment6                            -0.025618   0.005571  -4.599 4.26e-06 ***
time_segment7                            -0.029649   0.005571  -5.322 1.03e-07 ***
time_segment8                            -0.001746   0.005569  -0.313 0.753907    
time_segment9                             0.007337   0.005571   1.317 0.187795    
time_segment10                           -0.009402   0.005571  -1.688 0.091468 .  
time_segment11                            0.066143   0.005571  11.874  < 2e-16 ***
time_segment12                            0.090641   0.005574  16.262  < 2e-16 ***
time_segment13                            0.061816   0.005580  11.079  < 2e-16 ***
time_segment14                            0.008754   0.005776   1.516 0.129627    
time_segment15                           -0.028295   0.005569  -5.081 3.78e-07 ***
groupgreen_global_cluster:time_segment2   0.020651   0.007907   2.612 0.009015 ** 
groupblue_global_cluster:time_segment2   -0.019992   0.007887  -2.535 0.011253 *  
groupgreen_global_cluster:time_segment3   0.027125   0.007901   3.433 0.000597 ***
groupblue_global_cluster:time_segment3    0.001009   0.007926   0.127 0.898653    
groupgreen_global_cluster:time_segment4   0.034149   0.007901   4.322 1.55e-05 ***
groupblue_global_cluster:time_segment4    0.007901   0.007918   0.998 0.318331    
groupgreen_global_cluster:time_segment5  -0.084167   0.007882 -10.678  < 2e-16 ***
groupblue_global_cluster:time_segment5   -0.041983   0.007890  -5.321 1.04e-07 ***
groupgreen_global_cluster:time_segment6   0.021492   0.007882   2.727 0.006401 ** 
groupblue_global_cluster:time_segment6    0.045248   0.007920   5.713 1.12e-08 ***
groupgreen_global_cluster:time_segment7   0.040573   0.007883   5.147 2.66e-07 ***
groupblue_global_cluster:time_segment7    0.051135   0.007953   6.430 1.29e-10 ***
groupgreen_global_cluster:time_segment8  -0.015559   0.007880  -1.974 0.048341 *  
groupblue_global_cluster:time_segment8    0.015447   0.008040   1.921 0.054693 .  
groupgreen_global_cluster:time_segment9  -0.042113   0.007882  -5.343 9.21e-08 ***
groupblue_global_cluster:time_segment9    0.032313   0.008019   4.030 5.59e-05 ***
groupgreen_global_cluster:time_segment10  0.002630   0.007936   0.331 0.740345    
groupblue_global_cluster:time_segment10  -0.002924   0.008036  -0.364 0.715955    
groupgreen_global_cluster:time_segment11 -0.017377   0.007889  -2.203 0.027615 *  
groupblue_global_cluster:time_segment11  -0.093128   0.007879 -11.820  < 2e-16 ***
groupgreen_global_cluster:time_segment12 -0.049368   0.007911  -6.241 4.40e-10 ***
groupblue_global_cluster:time_segment12  -0.121239   0.007881 -15.383  < 2e-16 ***
groupgreen_global_cluster:time_segment13 -0.014733   0.007892  -1.867 0.061924 .  
groupblue_global_cluster:time_segment13  -0.054387   0.007886  -6.897 5.39e-12 ***
groupgreen_global_cluster:time_segment14  0.011993   0.008576   1.398 0.162004    
groupblue_global_cluster:time_segment14  -0.012119   0.008242  -1.470 0.141487    
groupgreen_global_cluster:time_segment15  0.086564   0.008229  10.520  < 2e-16 ***
groupblue_global_cluster:time_segment15   0.064460   0.008205   7.856 4.06e-15 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.12 on 39873 degrees of freedom
  (1845 observations deleted due to missingness)
Multiple R-squared:  0.07368,	Adjusted R-squared:  0.07266 
F-statistic: 72.08 on 44 and 39873 DF,  p-value: < 2.2e-16

