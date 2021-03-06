> Anova(myfit)
Anova Table (Type II tests)

Response: dep_var
                   Sum Sq    Df F value    Pr(>F)    
group               13344     2 837.925 < 2.2e-16 ***
time_segment        46242    14 414.800 < 2.2e-16 ***
group:time_segment  13313    28  59.709 < 2.2e-16 ***
Residuals          331252 41600                      
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

> etasq(myfit, type = 2)
                   Partial eta^2
group                 0.03872484
time_segment          0.12249621
group:time_segment    0.03863614
Residuals                     NA