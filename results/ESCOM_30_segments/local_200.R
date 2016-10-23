> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                    Sum Sq    Df F value    Pr(>F)    
group               263.76     1 6667.95 < 2.2e-16 ***
time_segment       1103.24    29  961.73 < 2.2e-16 ***
group:time_segment  155.24    29  135.32 < 2.2e-16 ***
Residuals          2913.54 73655                      
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                 0.08301426
time_segment          0.27465717
group:time_segment    0.05058544
Residuals                     NA