#  Generate n random variates from a given distribution.  
#  For a small n, list them.	 Look at them to see that they look as if
#  they came from the appropriate distribution.

n <- 20
x <- runif(n, min=3, max=5)
x


n <- 20
x <- rnorm(n, mean=2, sd=3)
x
#  Generate a large number of random variates from a given distribution.
#  Since it is a large number, don't list them.  
#  Instead, make a histogram of them, 
#  find the mean and standard deviation of the random variates you generated 
#  and think about whether those are what you expected.
#  Find the minimum and the maximum of the random variates you found.


n <- 50000
x <- runif(n)
hist(x)
mean(x)
sd(x)
min(x)
max(x)


n <- 50000
x <- rnorm(n)
hist(x)
mean(x)
sd(x)
min(x)
max(x)


n <- 50000
x <- rcauchy(n)
hist(x)
mean(x)
sd(x)
min(x)
max(x)



#  Explore the sampling distribution of the sample standard deviation
#  when the data come from an chi-squared distribution with df = 2
#  and the samples are of random samples of size 15.
#  Explore it by computing 10,000 values from this sampling distribution,
#  and then showing the histogram, the max, min, mean and standard deviation 
#  of this approximation of the sampling distribution.

#   First, let's just generate one value from this sampling distribution.
#   

y = rchisq(n=15,df=2,ncp=0)
y
value = sd(y)
value

#   Now, let's generate ten values from this sampling distribution
#   and list them, and find various summary statistics for this distribution.
#   Then see if these look like reasonable values for this sampling distn.

n = 15
m = 10

for (j in 1:m){
  
  y = rchisq(n=15,df=2,ncp=0)
  
  value[j] = sd(y)}

value
hist(value)
min(value)
max(value)
mean(value)
sd(value)


#  But, of course, just ten values from a sampling distribution is not
#  giving a good approximation of the distribution.   
#  Generate a larger number of them, like 1000,
#  and, of course, don't list them, by "commenting out" the command that lists.


n = 15
m = 1000

for (j in 1:m){
  
  y = rchisq(n=15,df=2,ncp=0)
  
  value[j] = sd(y)}

#	value
hist(value)
min(value)
max(value)
mean(value)
sd(value)





