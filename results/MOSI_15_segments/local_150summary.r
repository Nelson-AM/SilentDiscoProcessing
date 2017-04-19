Myfit summary

Call:
lm(formula = dep_var ~ group * time_segment, data = csvdata)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.55515 -0.10150  0.01641  0.11224  0.80818 

Coefficients:
                                          Estimate Std. Error t value Pr(>|t|)    
(Intercept)                              0.5257396  0.0057379  91.625  < 2e-16 ***
groupgreen_local_cluster                -0.0624247  0.0081146  -7.693 1.47e-14 ***
groupblue_local_cluster                 -0.1524433  0.0081146 -18.786  < 2e-16 ***
time_segment2                           -0.0085456  0.0081125  -1.053 0.292170    
time_segment3                            0.0007507  0.0081125   0.093 0.926273    
time_segment4                           -0.0371274  0.0081125  -4.577 4.74e-06 ***
time_segment5                           -0.0441900  0.0081125  -5.447 5.15e-08 ***
time_segment6                           -0.0263883  0.0081125  -3.253 0.001144 ** 
time_segment7                            0.0234212  0.0081125   2.887 0.003891 ** 
time_segment8                           -0.0467162  0.0081103  -5.760 8.46e-09 ***
time_segment9                           -0.0649480  0.0081125  -8.006 1.22e-15 ***
time_segment10                           0.0235576  0.0081125   2.904 0.003688 ** 
time_segment11                           0.0168647  0.0081125   2.079 0.037636 *  
time_segment12                           0.0294109  0.0081125   3.625 0.000289 ***
time_segment13                          -0.0178319  0.0081125  -2.198 0.027948 *  
time_segment14                          -0.0018583  0.0082199  -0.226 0.821147    
time_segment15                           0.1310285  0.0081103  16.156  < 2e-16 ***
groupgreen_local_cluster:time_segment2  -0.0455035  0.0114728  -3.966 7.31e-05 ***
groupblue_local_cluster:time_segment2   -0.0455188  0.0114728  -3.968 7.27e-05 ***
groupgreen_local_cluster:time_segment3  -0.0629676  0.0114728  -5.488 4.08e-08 ***
groupblue_local_cluster:time_segment3   -0.1004286  0.0114728  -8.754  < 2e-16 ***
groupgreen_local_cluster:time_segment4  -0.0795227  0.0114728  -6.931 4.23e-12 ***
groupblue_local_cluster:time_segment4   -0.0434346  0.0114728  -3.786 0.000153 ***
groupgreen_local_cluster:time_segment5   0.0811053  0.0114728   7.069 1.58e-12 ***
groupblue_local_cluster:time_segment5   -0.0012579  0.0114728  -0.110 0.912696    
groupgreen_local_cluster:time_segment6   0.0406428  0.0114728   3.543 0.000397 ***
groupblue_local_cluster:time_segment6   -0.0537444  0.0114728  -4.685 2.81e-06 ***
groupgreen_local_cluster:time_segment7   0.0185067  0.0114728   1.613 0.106729    
groupblue_local_cluster:time_segment7   -0.1350549  0.0114743 -11.770  < 2e-16 ***
groupgreen_local_cluster:time_segment8   0.0871075  0.0114697   7.595 3.15e-14 ***
groupblue_local_cluster:time_segment8   -0.0953339  0.0114697  -8.312  < 2e-16 ***
groupgreen_local_cluster:time_segment9   0.1074153  0.0114728   9.363  < 2e-16 ***
groupblue_local_cluster:time_segment9   -0.0665631  0.0114728  -5.802 6.61e-09 ***
groupgreen_local_cluster:time_segment10 -0.0311297  0.0114758  -2.713 0.006678 ** 
groupblue_local_cluster:time_segment10  -0.0776380  0.0114728  -6.767 1.33e-11 ***
groupgreen_local_cluster:time_segment11  0.0030410  0.0114728   0.265 0.790960    
groupblue_local_cluster:time_segment11   0.0543189  0.0114728   4.735 2.20e-06 ***
groupgreen_local_cluster:time_segment12 -0.1438987  0.0114728 -12.543  < 2e-16 ***
groupblue_local_cluster:time_segment12   0.1003253  0.0114728   8.745  < 2e-16 ***
groupgreen_local_cluster:time_segment13 -0.0243864  0.0114728  -2.126 0.033543 *  
groupblue_local_cluster:time_segment13   0.1043312  0.0114728   9.094  < 2e-16 ***
groupgreen_local_cluster:time_segment14 -0.2696415  0.0115948 -23.255  < 2e-16 ***
groupblue_local_cluster:time_segment14  -0.0377777  0.0115723  -3.264 0.001098 ** 
groupgreen_local_cluster:time_segment15 -0.2819752  0.0114868 -24.548  < 2e-16 ***
groupblue_local_cluster:time_segment15  -0.1613420  0.0114900 -14.042  < 2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.1747 on 41600 degrees of freedom
  (118 observations deleted due to missingness)
Multiple R-squared:  0.2682,	Adjusted R-squared:  0.2674 
F-statistic: 346.4 on 44 and 41600 DF,  p-value: < 2.2e-16

