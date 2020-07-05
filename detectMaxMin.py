#import data
import matplotlib.pyplot as plt
import numpy as np
import statistics
graph_walking=np.genfromtxt(r'C:\Users\Linda\PycharmProjects\BME262Project\nov26walk_freeze_ankle1.txt', delimiter=',')

# assign value to specific column for walking

gy=[row[2] for row in graph_walking]
time=[row[6] for row in graph_walking]
time=np.divide(time,1000) #ARRAY THAT WILL STORE THE NUMBER OF CROSSINGS EVERY 10 POINTS
def twenty_points_calculation(i):
    test_points=[]
    amplitude_value=0
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
    max=np.max(test_points)
    min=np.min(test_points)
    amplitude_value=max-min

    return amplitude_value

def amplitudes(gy):
    crossings_plot = []
    for i in range(len(gy)):
        ten_points=twenty_points_calculation(i)
        crossings_plot.append(ten_points) # what would be this argument?
    return crossings_plot

ampl=[]
ampl=amplitudes(gy)
ew=np.linspace(20,len(ampl)-1,len(ampl))
plt.bar(ew,ampl)
#plt.hist(ampl,40)
print(len(ampl))
plt.show()


