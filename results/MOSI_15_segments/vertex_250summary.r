Myfit summary

Call:
lm(formula = dep_var ~ group * time_segment, data = csvdata)

Residuals:
    Min      1Q  Median      3Q     Max 
-14.788  -1.463  -0.208   1.145 180.297 

Coefficients:
                                         Estimate Std. Error t value Pr(>|t|)    
(Intercept)                               5.67711    0.18010  31.523  < 2e-16 ***
groupgreen_vertex_average                -0.22831    0.25470  -0.896 0.370052    
groupblue_vertex_average                 -2.13257    0.25470  -8.373  < 2e-16 ***
time_segment2                             0.89897    0.25463   3.531 0.000415 ***
time_segment3                             0.67469    0.25463   2.650 0.008059 ** 
time_segment4                             0.11462    0.25463   0.450 0.652618    
time_segment5                            -1.63681    0.25463  -6.428 1.30e-10 ***
time_segment6                             0.31750    0.25463   1.247 0.212437    
time_segment7                             0.96304    0.25463   3.782 0.000156 ***
time_segment8                            -0.78049    0.25456  -3.066 0.002170 ** 
time_segment9                            -0.73339    0.25463  -2.880 0.003976 ** 
time_segment10                            0.92056    0.25463   3.615 0.000300 ***
time_segment11                            0.31616    0.25463   1.242 0.214369    
time_segment12                           -0.03762    0.25463  -0.148 0.882551    
time_segment13                           -0.68722    0.25463  -2.699 0.006959 ** 
time_segment14                            2.46941    0.25800   9.571  < 2e-16 ***
time_segment15                           10.71467    0.25456  42.091  < 2e-16 ***
groupgreen_vertex_average:time_segment2  -1.41313    0.36010  -3.924 8.71e-05 ***
groupblue_vertex_average:time_segment2   -1.38087    0.36010  -3.835 0.000126 ***
groupgreen_vertex_average:time_segment3  -2.13486    0.36010  -5.929 3.08e-09 ***
groupblue_vertex_average:time_segment3   -1.72579    0.36010  -4.793 1.65e-06 ***
groupgreen_vertex_average:time_segment4  -2.30917    0.36010  -6.413 1.45e-10 ***
groupblue_vertex_average:time_segment4   -0.86997    0.36010  -2.416 0.015699 *  
groupgreen_vertex_average:time_segment5   2.27502    0.36010   6.318 2.68e-10 ***
groupblue_vertex_average:time_segment5    1.25088    0.36010   3.474 0.000514 ***
groupgreen_vertex_average:time_segment6  -0.60168    0.36010  -1.671 0.094752 .  
groupblue_vertex_average:time_segment6   -1.06339    0.36010  -2.953 0.003148 ** 
groupgreen_vertex_average:time_segment7  -1.02639    0.36010  -2.850 0.004370 ** 
groupblue_vertex_average:time_segment7   -1.97452    0.36014  -5.483 4.22e-08 ***
groupgreen_vertex_average:time_segment8   1.10225    0.36000   3.062 0.002201 ** 
groupblue_vertex_average:time_segment8   -0.19089    0.36000  -0.530 0.595938    
groupgreen_vertex_average:time_segment9   1.50619    0.36010   4.183 2.89e-05 ***
groupblue_vertex_average:time_segment9   -0.55464    0.36010  -1.540 0.123505    
groupgreen_vertex_average:time_segment10 -1.24601    0.36019  -3.459 0.000542 ***
groupblue_vertex_average:time_segment10  -0.81567    0.36010  -2.265 0.023509 *  
groupgreen_vertex_average:time_segment11 -1.44443    0.36010  -4.011 6.05e-05 ***
groupblue_vertex_average:time_segment11   1.00300    0.36010   2.785 0.005349 ** 
groupgreen_vertex_average:time_segment12 -2.23850    0.36010  -6.216 5.13e-10 ***
groupblue_vertex_average:time_segment12   2.15477    0.36010   5.984 2.20e-09 ***
groupgreen_vertex_average:time_segment13 -0.47073    0.36010  -1.307 0.191136    
groupblue_vertex_average:time_segment13   2.06929    0.36010   5.747 9.17e-09 ***
groupgreen_vertex_average:time_segment14 -5.78198    0.36393 -15.888  < 2e-16 ***
groupblue_vertex_average:time_segment14  -2.39515    0.36322  -6.594 4.33e-11 ***
groupgreen_vertex_average:time_segment15 -1.37512    0.36054  -3.814 0.000137 ***
groupblue_vertex_average:time_segment15  -8.39397    0.36064 -23.275  < 2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 5.483 on 41600 degrees of freedom
  (118 observations deleted due to missingness)
Multiple R-squared:  0.1902,	Adjusted R-squared:  0.1893 
F-statistic:   222 on 44 and 41600 DF,  p-value: < 2.2e-16

