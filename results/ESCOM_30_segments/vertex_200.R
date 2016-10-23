> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                   Sum Sq    Df  F value    Pr(>F)    
group               29572     1 29744.35 < 2.2e-16 ***
time_segment        87938    29  3050.05 < 2.2e-16 ***
group:time_segment  24105    29   836.07 < 2.2e-16 ***
Residuals           73227 73655                       
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                  0.2876648
time_segment           0.5456384
group:time_segment     0.2476596
Residuals                     NA