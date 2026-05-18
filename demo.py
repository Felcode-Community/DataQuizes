import numpy

# my data set 
data = [10, 20, 30, 40, 50, 60]

# print the output on the screen
# lets find of the data set
meanOfData = numpy.mean(data)
print("Mean = ", meanOfData)

# find the median value
medianValue = numpy.median(data)
print("Median number = ", medianValue)

# find the variance of the data set
variance1 = numpy.var(data)
print("The variance is ", variance1)