> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                    Sum Sq    Df F value    Pr(>F)    
group                11.49     1 366.461 < 2.2e-16 ***
time_segment        192.81    29 212.122 < 2.2e-16 ***
group:time_segment   61.76    29  67.948 < 2.2e-16 ***
Residuals          2041.67 65140                      
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                0.005594266
time_segment         0.086287073
group:time_segment   0.029361824
Residuals                     NA