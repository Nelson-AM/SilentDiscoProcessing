Myfit summary

Call:
lm(formula = dep_var ~ group * time_segment, data = csvdata)

Residuals:
   Min     1Q Median     3Q    Max 
-7.821 -0.692 -0.116  0.523 92.147 

Coefficients:
                                          Estimate Std. Error t value Pr(>|t|)    
(Intercept)                               2.701625   0.092681  29.150  < 2e-16 ***
groupgreen_vertex_average                -0.230511   0.131071  -1.759 0.078641 .  
groupblue_vertex_average                 -0.901720   0.131071  -6.880 6.09e-12 ***
time_segment2                             0.404586   0.131036   3.088 0.002019 ** 
time_segment3                             0.342204   0.131036   2.612 0.009017 ** 
time_segment4                            -0.075190   0.131036  -0.574 0.566099    
time_segment5                            -0.446639   0.131036  -3.409 0.000654 ***
time_segment6                            -0.011813   0.131036  -0.090 0.928171    
time_segment7                             0.359930   0.131036   2.747 0.006021 ** 
time_segment8                            -0.309374   0.131001  -2.362 0.018200 *  
time_segment9                            -0.335237   0.131036  -2.558 0.010520 *  
time_segment10                            0.310759   0.131036   2.372 0.017718 *  
time_segment11                            0.538636   0.131036   4.111 3.95e-05 ***
time_segment12                            0.710851   0.131036   5.425 5.83e-08 ***
time_segment13                           -0.070426   0.131036  -0.537 0.590955    
time_segment14                            1.043121   0.132771   7.857 4.04e-15 ***
time_segment15                            5.238788   0.131001  39.990  < 2e-16 ***
groupgreen_vertex_average:time_segment2  -0.641541   0.185313  -3.462 0.000537 ***
groupblue_vertex_average:time_segment2   -0.638807   0.185313  -3.447 0.000567 ***
groupgreen_vertex_average:time_segment3  -0.938612   0.185313  -5.065 4.10e-07 ***
groupblue_vertex_average:time_segment3   -0.830927   0.185313  -4.484 7.35e-06 ***
groupgreen_vertex_average:time_segment4  -0.785483   0.185313  -4.239 2.25e-05 ***
groupblue_vertex_average:time_segment4   -0.336280   0.185313  -1.815 0.069583 .  
groupgreen_vertex_average:time_segment5   0.617722   0.185313   3.333 0.000859 ***
groupblue_vertex_average:time_segment5    0.309856   0.185313   1.672 0.094518 .  
groupgreen_vertex_average:time_segment6  -0.006854   0.185313  -0.037 0.970495    
groupblue_vertex_average:time_segment6   -0.317669   0.185313  -1.714 0.086494 .  
groupgreen_vertex_average:time_segment7  -0.273870   0.185313  -1.478 0.139448    
groupblue_vertex_average:time_segment7   -0.824421   0.185338  -4.448 8.68e-06 ***
groupgreen_vertex_average:time_segment8   0.365383   0.185263   1.972 0.048589 *  
groupblue_vertex_average:time_segment8   -0.089790   0.185263  -0.485 0.627918    
groupgreen_vertex_average:time_segment9   0.508088   0.185313   2.742 0.006113 ** 
groupblue_vertex_average:time_segment9   -0.247853   0.185313  -1.337 0.181072    
groupgreen_vertex_average:time_segment10 -0.405869   0.185363  -2.190 0.028560 *  
groupblue_vertex_average:time_segment10  -0.377430   0.185313  -2.037 0.041685 *  
groupgreen_vertex_average:time_segment11 -0.845678   0.185313  -4.564 5.04e-06 ***
groupblue_vertex_average:time_segment11  -0.074021   0.185313  -0.399 0.689575    
groupgreen_vertex_average:time_segment12 -1.606030   0.185313  -8.667  < 2e-16 ***
groupblue_vertex_average:time_segment12   0.090784   0.185313   0.490 0.624211    
groupgreen_vertex_average:time_segment13 -0.413807   0.185313  -2.233 0.025553 *  
groupblue_vertex_average:time_segment13   0.628371   0.185313   3.391 0.000697 ***
groupgreen_vertex_average:time_segment14 -2.459002   0.187284 -13.130  < 2e-16 ***
groupblue_vertex_average:time_segment14  -1.085173   0.186922  -5.805 6.46e-09 ***
groupgreen_vertex_average:time_segment15  0.110832   0.185540   0.597 0.550277    
groupblue_vertex_average:time_segment15  -3.544953   0.185591 -19.101  < 2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 2.822 on 41600 degrees of freedom
  (118 observations deleted due to missingness)
Multiple R-squared:  0.1805,	Adjusted R-squared:  0.1797 
F-statistic: 208.3 on 44 and 41600 DF,  p-value: < 2.2e-16

