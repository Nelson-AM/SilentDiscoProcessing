> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                    Sum Sq    Df F value    Pr(>F)    
group                 4.54     1 212.662 < 2.2e-16 ***
time_segment        269.69    29 435.406 < 2.2e-16 ***
group:time_segment   57.44    29  92.739 < 2.2e-16 ***
Residuals          1432.67 67078                      
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                0.003160352
time_segment         0.158419428
group:time_segment   0.038548596
Residuals                     NA