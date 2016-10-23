> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                    Sum Sq    Df F value    Pr(>F)    
group               249.85     2 4093.11 < 2.2e-16 ***
time_segment         51.94    14  121.55 < 2.2e-16 ***
group:time_segment  162.91    28  190.64 < 2.2e-16 ***
Residuals          1269.65 41600                      
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                 0.16442739
time_segment          0.03929826
group:time_segment    0.11372281
Residuals                     NA