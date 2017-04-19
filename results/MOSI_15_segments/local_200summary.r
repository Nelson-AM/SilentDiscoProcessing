Myfit summary

Call:
lm(formula = dep_var ~ group * time_segment, data = csvdata)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.67368 -0.07568  0.01876  0.10149  0.71840 

Coefficients:
                                         Estimate Std. Error t value Pr(>|t|)    
(Intercept)                              0.639570   0.005689 112.418  < 2e-16 ***
groupgreen_local_cluster                -0.062825   0.008046  -7.808 5.92e-15 ***
groupblue_local_cluster                 -0.128023   0.008046 -15.912  < 2e-16 ***
time_segment2                           -0.027473   0.008044  -3.415 0.000637 ***
time_segment3                           -0.011279   0.008044  -1.402 0.160834    
time_segment4                           -0.020374   0.008044  -2.533 0.011315 *  
time_segment5                           -0.037494   0.008044  -4.661 3.15e-06 ***
time_segment6                           -0.008609   0.008044  -1.070 0.284477    
time_segment7                            0.023997   0.008044   2.983 0.002853 ** 
time_segment8                           -0.018937   0.008041  -2.355 0.018531 *  
time_segment9                           -0.048239   0.008044  -5.997 2.02e-09 ***
time_segment10                           0.032351   0.008044   4.022 5.78e-05 ***
time_segment11                           0.021144   0.008044   2.629 0.008575 ** 
time_segment12                           0.034110   0.008044   4.241 2.23e-05 ***
time_segment13                          -0.018840   0.008044  -2.342 0.019176 *  
time_segment14                          -0.039591   0.008150  -4.858 1.19e-06 ***
time_segment15                           0.063883   0.008041   7.944 2.00e-15 ***
groupgreen_local_cluster:time_segment2  -0.027459   0.011375  -2.414 0.015786 *  
groupblue_local_cluster:time_segment2   -0.048791   0.011375  -4.289 1.80e-05 ***
groupgreen_local_cluster:time_segment3  -0.035946   0.011375  -3.160 0.001579 ** 
groupblue_local_cluster:time_segment3   -0.121562   0.011375 -10.686  < 2e-16 ***
groupgreen_local_cluster:time_segment4  -0.093550   0.011375  -8.224  < 2e-16 ***
groupblue_local_cluster:time_segment4   -0.074470   0.011375  -6.547 5.95e-11 ***
groupgreen_local_cluster:time_segment5   0.055058   0.011375   4.840 1.30e-06 ***
groupblue_local_cluster:time_segment5   -0.014420   0.011375  -1.268 0.204939    
groupgreen_local_cluster:time_segment6   0.028484   0.011375   2.504 0.012283 *  
groupblue_local_cluster:time_segment6   -0.062226   0.011375  -5.470 4.52e-08 ***
groupgreen_local_cluster:time_segment7   0.030098   0.011375   2.646 0.008151 ** 
groupblue_local_cluster:time_segment7   -0.126608   0.011377 -11.129  < 2e-16 ***
groupgreen_local_cluster:time_segment8   0.066682   0.011372   5.864 4.57e-09 ***
groupblue_local_cluster:time_segment8   -0.157141   0.011372 -13.818  < 2e-16 ***
groupgreen_local_cluster:time_segment9   0.081333   0.011375   7.150 8.83e-13 ***
groupblue_local_cluster:time_segment9   -0.103894   0.011375  -9.133  < 2e-16 ***
groupgreen_local_cluster:time_segment10 -0.046325   0.011378  -4.071 4.68e-05 ***
groupblue_local_cluster:time_segment10  -0.102744   0.011375  -9.032  < 2e-16 ***
groupgreen_local_cluster:time_segment11  0.016989   0.011375   1.494 0.135312    
groupblue_local_cluster:time_segment11   0.052311   0.011375   4.599 4.27e-06 ***
groupgreen_local_cluster:time_segment12 -0.138126   0.011375 -12.143  < 2e-16 ***
groupblue_local_cluster:time_segment12   0.077555   0.011375   6.818 9.37e-12 ***
groupgreen_local_cluster:time_segment13 -0.018190   0.011375  -1.599 0.109818    
groupblue_local_cluster:time_segment13   0.097848   0.011375   8.602  < 2e-16 ***
groupgreen_local_cluster:time_segment14 -0.255551   0.011496 -22.229  < 2e-16 ***
groupblue_local_cluster:time_segment14  -0.029326   0.011474  -2.556 0.010597 *  
groupgreen_local_cluster:time_segment15 -0.258814   0.011389 -22.724  < 2e-16 ***
groupblue_local_cluster:time_segment15  -0.163304   0.011392 -14.334  < 2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.1732 on 41600 degrees of freedom
  (118 observations deleted due to missingness)
Multiple R-squared:  0.2686,	Adjusted R-squared:  0.2679 
F-statistic: 347.3 on 44 and 41600 DF,  p-value: < 2.2e-16

