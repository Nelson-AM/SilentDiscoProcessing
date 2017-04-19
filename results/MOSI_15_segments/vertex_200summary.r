Myfit summary

Call:
lm(formula = dep_var ~ group * time_segment, data = csvdata)

Residuals:
    Min      1Q  Median      3Q     Max 
-11.412  -1.066  -0.152   0.822 139.087 

Coefficients:
                                         Estimate Std. Error t value Pr(>|t|)    
(Intercept)                               4.12995    0.13762  30.010  < 2e-16 ***
groupgreen_vertex_average                -0.22298    0.19462  -1.146 0.251910    
groupblue_vertex_average                 -1.50594    0.19462  -7.738 1.03e-14 ***
time_segment2                             0.61322    0.19457   3.152 0.001624 ** 
time_segment3                             0.52473    0.19457   2.697 0.007002 ** 
time_segment4                             0.03788    0.19457   0.195 0.845639    
time_segment5                            -0.99039    0.19457  -5.090 3.59e-07 ***
time_segment6                             0.11814    0.19457   0.607 0.543714    
time_segment7                             0.63080    0.19457   3.242 0.001188 ** 
time_segment8                            -0.54572    0.19452  -2.806 0.005026 ** 
time_segment9                            -0.52223    0.19457  -2.684 0.007276 ** 
time_segment10                            0.62029    0.19457   3.188 0.001433 ** 
time_segment11                            0.55160    0.19457   2.835 0.004585 ** 
time_segment12                            0.51877    0.19457   2.666 0.007672 ** 
time_segment13                           -0.30776    0.19457  -1.582 0.113707    
time_segment14                            1.76888    0.19714   8.973  < 2e-16 ***
time_segment15                            7.85932    0.19452  40.405  < 2e-16 ***
groupgreen_vertex_average:time_segment2  -1.01701    0.27516  -3.696 0.000219 ***
groupblue_vertex_average:time_segment2   -0.99968    0.27516  -3.633 0.000280 ***
groupgreen_vertex_average:time_segment3  -1.55545    0.27516  -5.653 1.59e-08 ***
groupblue_vertex_average:time_segment3   -1.33225    0.27516  -4.842 1.29e-06 ***
groupgreen_vertex_average:time_segment4  -1.54739    0.27516  -5.624 1.88e-08 ***
groupblue_vertex_average:time_segment4   -0.66071    0.27516  -2.401 0.016347 *  
groupgreen_vertex_average:time_segment5   1.24268    0.27516   4.516 6.31e-06 ***
groupblue_vertex_average:time_segment5    0.75976    0.27516   2.761 0.005763 ** 
groupgreen_vertex_average:time_segment6  -0.30289    0.27516  -1.101 0.271002    
groupblue_vertex_average:time_segment6   -0.62179    0.27516  -2.260 0.023844 *  
groupgreen_vertex_average:time_segment7  -0.57472    0.27516  -2.089 0.036742 *  
groupblue_vertex_average:time_segment7   -1.35523    0.27520  -4.925 8.49e-07 ***
groupgreen_vertex_average:time_segment8   0.68442    0.27509   2.488 0.012850 *  
groupblue_vertex_average:time_segment8   -0.15042    0.27509  -0.547 0.584524    
groupgreen_vertex_average:time_segment9   0.97910    0.27516   3.558 0.000374 ***
groupblue_vertex_average:time_segment9   -0.39851    0.27516  -1.448 0.147550    
groupgreen_vertex_average:time_segment10 -0.91932    0.27523  -3.340 0.000838 ***
groupblue_vertex_average:time_segment10  -0.56639    0.27516  -2.058 0.039559 *  
groupgreen_vertex_average:time_segment11 -1.23885    0.27516  -4.502 6.74e-06 ***
groupblue_vertex_average:time_segment11   0.38466    0.27516   1.398 0.162133    
groupgreen_vertex_average:time_segment12 -2.06524    0.27516  -7.506 6.24e-14 ***
groupblue_vertex_average:time_segment12   0.93638    0.27516   3.403 0.000667 ***
groupgreen_vertex_average:time_segment13 -0.53366    0.27516  -1.939 0.052453 .  
groupblue_vertex_average:time_segment13   1.33808    0.27516   4.863 1.16e-06 ***
groupgreen_vertex_average:time_segment14 -4.10012    0.27809 -14.744  < 2e-16 ***
groupblue_vertex_average:time_segment14  -1.74134    0.27755  -6.274 3.55e-10 ***
groupgreen_vertex_average:time_segment15 -0.35459    0.27550  -1.287 0.198070    
groupblue_vertex_average:time_segment15  -5.69663    0.27557 -20.672  < 2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 4.19 on 41600 degrees of freedom
  (118 observations deleted due to missingness)
Multiple R-squared:  0.1834,	Adjusted R-squared:  0.1825 
F-statistic: 212.3 on 44 and 41600 DF,  p-value: < 2.2e-16

