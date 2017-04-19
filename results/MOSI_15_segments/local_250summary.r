Myfit summary

Call:
lm(formula = dep_var ~ group * time_segment, data = csvdata)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.73615 -0.05618  0.01871  0.08679  0.64635 

Coefficients:
                                          Estimate Std. Error t value Pr(>|t|)    
(Intercept)                              0.7028855  0.0054682 128.541  < 2e-16 ***
groupgreen_local_cluster                -0.0583836  0.0077332  -7.550 4.45e-14 ***
groupblue_local_cluster                 -0.0941962  0.0077332 -12.181  < 2e-16 ***
time_segment2                           -0.0312311  0.0077311  -4.040 5.36e-05 ***
time_segment3                           -0.0238365  0.0077311  -3.083 0.002049 ** 
time_segment4                           -0.0047374  0.0077311  -0.613 0.540026    
time_segment5                           -0.0205311  0.0077311  -2.656 0.007919 ** 
time_segment6                           -0.0054983  0.0077311  -0.711 0.476967    
time_segment7                            0.0064088  0.0077311   0.829 0.407133    
time_segment8                           -0.0074102  0.0077290  -0.959 0.337689    
time_segment9                           -0.0384640  0.0077311  -4.975 6.54e-07 ***
time_segment10                           0.0356321  0.0077311   4.609 4.06e-06 ***
time_segment11                           0.0304194  0.0077311   3.935 8.34e-05 ***
time_segment12                           0.0332621  0.0077311   4.302 1.69e-05 ***
time_segment13                          -0.0003331  0.0077311  -0.043 0.965635    
time_segment14                          -0.0520689  0.0078335  -6.647 3.03e-11 ***
time_segment15                           0.0374788  0.0077290   4.849 1.24e-06 ***
groupgreen_local_cluster:time_segment2  -0.0154061  0.0109334  -1.409 0.158817    
groupblue_local_cluster:time_segment2   -0.0330115  0.0109334  -3.019 0.002535 ** 
groupgreen_local_cluster:time_segment3  -0.0066619  0.0109334  -0.609 0.542318    
groupblue_local_cluster:time_segment3   -0.1045440  0.0109334  -9.562  < 2e-16 ***
groupgreen_local_cluster:time_segment4  -0.0920607  0.0109334  -8.420  < 2e-16 ***
groupblue_local_cluster:time_segment4   -0.0706870  0.0109334  -6.465 1.02e-10 ***
groupgreen_local_cluster:time_segment5   0.0221705  0.0109334   2.028 0.042589 *  
groupblue_local_cluster:time_segment5   -0.0170466  0.0109334  -1.559 0.118972    
groupgreen_local_cluster:time_segment6   0.0204580  0.0109334   1.871 0.061332 .  
groupblue_local_cluster:time_segment6   -0.0588565  0.0109334  -5.383 7.36e-08 ***
groupgreen_local_cluster:time_segment7   0.0416379  0.0109334   3.808 0.000140 ***
groupblue_local_cluster:time_segment7   -0.0929752  0.0109349  -8.503  < 2e-16 ***
groupgreen_local_cluster:time_segment8   0.0386819  0.0109305   3.539 0.000402 ***
groupblue_local_cluster:time_segment8   -0.1623670  0.0109305 -14.855  < 2e-16 ***
groupgreen_local_cluster:time_segment9   0.0580883  0.0109334   5.313 1.08e-07 ***
groupblue_local_cluster:time_segment9   -0.0977738  0.0109334  -8.943  < 2e-16 ***
groupgreen_local_cluster:time_segment10 -0.0525762  0.0109364  -4.807 1.53e-06 ***
groupblue_local_cluster:time_segment10  -0.1267095  0.0109334 -11.589  < 2e-16 ***
groupgreen_local_cluster:time_segment11  0.0047767  0.0109334   0.437 0.662193    
groupblue_local_cluster:time_segment11   0.0284120  0.0109334   2.599 0.009363 ** 
groupgreen_local_cluster:time_segment12 -0.1098521  0.0109334 -10.047  < 2e-16 ***
groupblue_local_cluster:time_segment12   0.0394587  0.0109334   3.609 0.000308 ***
groupgreen_local_cluster:time_segment13 -0.0048353  0.0109334  -0.442 0.658312    
groupblue_local_cluster:time_segment13   0.0705345  0.0109334   6.451 1.12e-10 ***
groupgreen_local_cluster:time_segment14 -0.2387856  0.0110497 -21.610  < 2e-16 ***
groupblue_local_cluster:time_segment14  -0.0291862  0.0110283  -2.646 0.008137 ** 
groupgreen_local_cluster:time_segment15 -0.2346887  0.0109468 -21.439  < 2e-16 ***
groupblue_local_cluster:time_segment15  -0.1706218  0.0109498 -15.582  < 2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.1665 on 41600 degrees of freedom
  (118 observations deleted due to missingness)
Multiple R-squared:  0.2366,	Adjusted R-squared:  0.2358 
F-statistic: 293.1 on 44 and 41600 DF,  p-value: < 2.2e-16

