> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                    Sum Sq    Df  F value    Pr(>F)    
group               361.58     1 10010.19 < 2.2e-16 ***
time_segment        944.70    29   901.86 < 2.2e-16 ***
group:time_segment  117.91    29   112.56 < 2.2e-16 ***
Residuals          2660.47 73655                       
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                 0.11964584
time_segment          0.26204017
group:time_segment    0.04243691
Residuals                     NA