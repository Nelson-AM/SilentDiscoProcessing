> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                   Sum Sq    Df  F value    Pr(>F)    
group               12862     1 28479.93 < 2.2e-16 ***
time_segment        29358    29  2241.63 < 2.2e-16 ***
group:time_segment   7980    29   609.31 < 2.2e-16 ***
Residuals           33263 73655                       
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                  0.2788461
time_segment           0.4688173
group:time_segment     0.1934846
Residuals                     NA