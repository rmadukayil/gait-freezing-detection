#import data
import matplotlib.pyplot as plt
import numpy as np
import statistics
graph_walking=np.genfromtxt(r'C:\Users\Linda\PycharmProjects\BME262Project\nov26walk_freeze_ankle2.txt', delimiter=',')

# assign value to specific column for walking

gy=[row[4] for row in graph_walking]
time=[row[6] for row in graph_walking]
time=np.divide(time,1000) #ARRAY THAT WILL STORE THE NUMBER OF CROSSINGS EVERY 10 POINTS
def ten_points_calculation(i):
    test_points=[]
    num_crossings=0
            #i rep the point it is at
            #test_points is a temporary array that appends the next 10 points in an array
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
    test_points.append(gy[i - 11])
    test_points.append(gy[i - 12])
    test_points.append(gy[i - 13])
    test_points.append(gy[i - 14])
    test_points.append(gy[i - 15])
    test_points.append(gy[i - 16])
    test_points.append(gy[i - 17])
    test_points.append(gy[i - 18])
    test_points.append(gy[i - 19])
    test_points.append(gy[i - 20])
    median = statistics.median(test_points)
    for j in range(len(test_points)):
        if ((test_points[j - 1] > median and test_points[j] < median) or (test_points[j - 1] < median and test_points[j] > median)):
            num_crossings = num_crossings + 1
    return num_crossings

def num_of_crossings(gy):
    i=40
    crossings_plot = []
    while i<len(gy):
        ten_points=ten_points_calculation(i)
        crossings_plot.append(ten_points) # what would be this argument?
        i=i+1
    return crossings_plot

num_crossings=[]
num_crossings=num_of_crossings(gy)
print(num_crossings)
ew=np.linspace(0,len(num_crossings)-1,len(num_crossings))
plt.bar(ew,num_crossings)
plt.show()

