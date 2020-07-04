#import data
import matplotlib.pyplot as plt
import numpy as np
import statistics
data=np.genfromtxt(r'C:\Users\Linda\PycharmProjects\BME262Project\nov26walk_freeze_ankle1.txt', delimiter=',')

# assign value to specific column for walking
gy=[row[4] for row in data]
time=[row[6] for row in data]
time=np.divide(time,1000)
def mean_ten_points_calculation(i):
    test_points=[]

    test_points.append(gy[i])
    test_points.append(gy[i - 1])
    test_points.append(gy[i - 2])
    test_points.append(gy[i - 3])
    test_points.append(gy[i - 4])
    test_points.append(gy[i - 5])
    test_points.append(gy[i - 6])
    test_points.append(gy[i - 7])
    test_points.append(gy[i - 8])
    test_points.append(gy[i - 9])
    test_points.append(gy[i - 10])
    mean= statistics.mean(test_points)
    return mean

def num_of_points(gy): #creates smooth array
    i=40
    smoothened_plot=[]
    while i<len(gy):
        mean_ten_points=mean_ten_points_calculation(i)
        smoothened_plot.append(mean_ten_points)
        i=i+1
    return smoothened_plot

smooth_plot=num_of_points(gy)
plt.plot(smooth_plot)
plt.show()


