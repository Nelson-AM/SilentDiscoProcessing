Myfit summary

Call:
lm(formula = dep_var ~ group * time_segment, data = csvdata)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.80861 -0.05924 -0.00365  0.06549  0.33362 

Coefficients:
                                           Estimate Std. Error t value Pr(>|t|)    
(Intercept)                               0.7435257  0.0045851 162.160  < 2e-16 ***
groupgreen_global_cluster                -0.0434039  0.0064984  -6.679 2.44e-11 ***
groupblue_global_cluster                  0.0008133  0.0064931   0.125 0.900320    
time_segment2                            -0.0023782  0.0064826  -0.367 0.713721    
time_segment3                            -0.0126671  0.0064826  -1.954 0.050707 .  
time_segment4                            -0.0225873  0.0064826  -3.484 0.000494 ***
time_segment5                             0.0491342  0.0064826   7.579 3.55e-14 ***
time_segment6                            -0.0216058  0.0064826  -3.333 0.000860 ***
time_segment7                            -0.0246309  0.0064826  -3.800 0.000145 ***
time_segment8                             0.0055476  0.0064809   0.856 0.392007    
time_segment9                             0.0041587  0.0064826   0.642 0.521192    
time_segment10                           -0.0215057  0.0064826  -3.317 0.000909 ***
time_segment11                            0.0650843  0.0064826  10.040  < 2e-16 ***
time_segment12                            0.1020055  0.0064861  15.727  < 2e-16 ***
time_segment13                            0.0435882  0.0064949   6.711 1.96e-11 ***
time_segment14                           -0.0033255  0.0067436  -0.493 0.621919    
time_segment15                           -0.0344657  0.0064809  -5.318 1.05e-07 ***
groupgreen_global_cluster:time_segment2   0.0203102  0.0092172   2.204 0.027565 *  
groupblue_global_cluster:time_segment2   -0.0334093  0.0091966  -3.633 0.000281 ***
groupgreen_global_cluster:time_segment3   0.0564359  0.0092146   6.125 9.18e-10 ***
groupblue_global_cluster:time_segment3    0.0071804  0.0092584   0.776 0.438017    
groupgreen_global_cluster:time_segment4   0.0641787  0.0092081   6.970 3.22e-12 ***
groupblue_global_cluster:time_segment4    0.0108371  0.0092389   1.173 0.240811    
groupgreen_global_cluster:time_segment5  -0.0701109  0.0091790  -7.638 2.25e-14 ***
groupblue_global_cluster:time_segment5   -0.0451836  0.0092095  -4.906 9.32e-07 ***
groupgreen_global_cluster:time_segment6   0.0409591  0.0091790   4.462 8.13e-06 ***
groupblue_global_cluster:time_segment6    0.0301183  0.0092458   3.257 0.001125 ** 
groupgreen_global_cluster:time_segment7   0.0497583  0.0091802   5.420 5.99e-08 ***
groupblue_global_cluster:time_segment7    0.0316653  0.0093282   3.395 0.000688 ***
groupgreen_global_cluster:time_segment8  -0.0152119  0.0091753  -1.658 0.097341 .  
groupblue_global_cluster:time_segment8    0.0059598  0.0094724   0.629 0.529239    
groupgreen_global_cluster:time_segment9  -0.0378984  0.0091778  -4.129 3.65e-05 ***
groupblue_global_cluster:time_segment9   -0.0027955  0.0094236  -0.297 0.766740    
groupgreen_global_cluster:time_segment10  0.0282801  0.0092482   3.058 0.002230 ** 
groupblue_global_cluster:time_segment10  -0.0183981  0.0093972  -1.958 0.050258 .  
groupgreen_global_cluster:time_segment11 -0.0071696  0.0091902  -0.780 0.435316    
groupblue_global_cluster:time_segment11  -0.1143013  0.0091740 -12.459  < 2e-16 ***
groupgreen_global_cluster:time_segment12 -0.0443517  0.0092562  -4.792 1.66e-06 ***
groupblue_global_cluster:time_segment12  -0.1442732  0.0091765 -15.722  < 2e-16 ***
groupgreen_global_cluster:time_segment13 -0.0075300  0.0091976  -0.819 0.412967    
groupblue_global_cluster:time_segment13  -0.0524975  0.0091827  -5.717 1.09e-08 ***
groupgreen_global_cluster:time_segment14 -0.0011973  0.0101510  -0.118 0.906112    
groupblue_global_cluster:time_segment14  -0.0246702  0.0096503  -2.556 0.010580 *  
groupgreen_global_cluster:time_segment15  0.0893946  0.0096901   9.225  < 2e-16 ***
groupblue_global_cluster:time_segment15   0.0559827  0.0096310   5.813 6.19e-09 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.1396 on 39353 degrees of freedom
  (2365 observations deleted due to missingness)
Multiple R-squared:  0.05341,	Adjusted R-squared:  0.05235 
F-statistic: 50.46 on 44 and 39353 DF,  p-value: < 2.2e-16

