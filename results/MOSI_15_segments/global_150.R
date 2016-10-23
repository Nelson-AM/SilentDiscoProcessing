> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                    Sum Sq    Df F value    Pr(>F)    
group                 6.04     2 100.391 < 2.2e-16 ***
time_segment          8.77    14  20.819 < 2.2e-16 ***
group:time_segment   31.65    28  37.574 < 2.2e-16 ***
Residuals          1153.83 38349                      
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                0.005208357
time_segment         0.007542937
group:time_segment   0.026701910
Residuals                     NA