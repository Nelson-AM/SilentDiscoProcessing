> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                    Sum Sq    Df F value    Pr(>F)    
group               149.85     1 3747.04 < 2.2e-16 ***
time_segment       1005.97    29  867.41 < 2.2e-16 ***
group:time_segment  188.23    29  162.31 < 2.2e-16 ***
Residuals          2945.52 73655                      
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                 0.04841014
time_segment          0.25457927
group:time_segment    0.06006552
Residuals                     NA