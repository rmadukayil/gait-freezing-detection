#import data
import matplotlib.pyplot as plt
import numpy as np
import statistics
graph_walking=np.genfromtxt(r'C:\Users\Linda\PycharmProjects\BME262Project\nov26walk_freeze_ankle1.txt', delimiter=',')

# assign value to specific column for walking
crossings_plot = []
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
    mean= statistics.mean(test_points)
    return mean
#/10
def num_of_crossings(gy): #creates smooth array
    crossings_plot=[]
    for i in range(len(gy)):
        ten_points=ten_points_calculation(i)
        crossings_plot.append(ten_points)
    return crossings_plot

num_crossings=num_of_crossings(gy)
print (len(num_crossings))
check_peaks=[]
i=1
while i<len(num_crossings)-1:
    if(num_crossings[i-1]<num_crossings[i] and num_crossings[i+1]<num_crossings[i] and num_crossings[i]>1000):
        check_peaks.append(i)
    i=i+1
detector=[np.nan]*len(num_crossings)
for j in range(len(num_crossings)):
    for i in range(len(check_peaks)):
        if j==check_peaks[i]:
            detector[j]=num_crossings[j]

distance_between_peaks=[np.nan]*len(num_crossings)
#somehow keep the value the same until next indices

k=1
while k<len(check_peaks):
    for i in range(len(distance_between_peaks)):
        if (i<=check_peaks[k] and i>=check_peaks[k-1]):
            distance_between_peaks[i]=check_peaks[k]-check_peaks[k-1]
    k=k+1
#/2
# print (len(distance_between_peaks))
ew=np.linspace(0,len(distance_between_peaks)-1,len(distance_between_peaks))
# plt.bar(ew,distance_between_peaks)
# plt.show()



plt.plot(ew,gy)
plt.show()


from Feature_detect_max_min import amplitudes
ampl=[]
amplf1=[]
amplf2=[]
ampl1=[]
ampl2=[]
ampl=amplitudes(gy)
amplf1=ampl[1:944]
amplf2=ampl[1778:2584]
ampl1=ampl[945:1777]
ampl2=ampl[2585:3400]
distance_between_peaks2=distance_between_peaks[2585:3400]
distance_between_peaks1=distance_between_peaks[945:1777]
distance_between_peaksf2=distance_between_peaks[1778:2584]
distance_between_peaksf1=distance_between_peaks[1:944]


plt.scatter(ampl1,distance_between_peaks1,color='cyan')
plt.scatter(ampl2,distance_between_peaks2,color='cyan')
plt.scatter(amplf1,distance_between_peaksf1,color='blue')
plt.scatter(amplf2,distance_between_peaksf2,color='blue')
plt.show()
plt.axis=('Max','Distance Between Peaks')
#t=np.linspace(0,3615,3616)
# plt.plot(t,num_crossings)
# plt.plot(t,detector,'--x',color='blue')
# #median_signal=num_of_crossingz(num_crossings)
# #print(median_signal)
# plt.show()

