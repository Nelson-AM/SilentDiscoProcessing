> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                    Sum Sq    Df F value    Pr(>F)    
group                21.83     1 479.481 < 2.2e-16 ***
time_segment        246.22    29 186.525 < 2.2e-16 ***
group:time_segment   47.96    29  36.334 < 2.2e-16 ***
Residuals          2809.16 61715                      
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                0.007709378
time_segment         0.080585415
group:time_segment   0.016787018
Residuals                     NA