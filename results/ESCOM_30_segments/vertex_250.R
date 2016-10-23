> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                   Sum Sq    Df  F value    Pr(>F)    
group               56429     1 30926.36 < 2.2e-16 ***
time_segment       189803    29  3586.98 < 2.2e-16 ***
group:time_segment  50192    29   948.56 < 2.2e-16 ***
Residuals          134393 73655                       
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                  0.2957158
time_segment           0.5854569
group:time_segment     0.2719193
Residuals                     NA