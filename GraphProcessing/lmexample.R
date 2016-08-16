require(graphics)

## Annette Dobson (1990): "An Introduction to Generalized Linear Models".
## Page 9: Plant Weight Data.

# Define two groups, vectors.
ctl <- c(4.17, 5.58, 5.18, 6.11, 4.50, 4.61, 5.17, 4.53, 5.33, 5.14)
trt <- c(4.81, 4.17, 4.41, 3.59, 5.87, 3.83, 6.03, 4.89, 4.32, 4.69)

# group: generate factors by specifying the pattern of their levels.
# 	n = 2 levels: ctl, trt
#	k = 10 replications for each level.
#	length = n * k
group <- gl(2, 10, 20, labels = c("Ctl", "Trt"))

# weight: 
weight <- c(ctl, trt)
print("weights:")
print(weight)
lm.D9 <- lm(weight ~ group)

# Omitting intercept.
lm.D90 <- lm(weight ~ group - 1)

anova(lm.D9)
summary(lm.D90)

opar <- par(mfrow = c(2, 2), oma = c(0, 0, 1.1, 0))
plot(lm.D9, las = 1)
par(opar)