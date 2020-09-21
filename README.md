# Gait-Freezing-Detection
Analysis of raw IMU sensor data to identify freezing in gait cycle for Parkinson's patients. 

## Notes
Sensor used was the MPU 6050 six-axis gyroscope + accelerometer. You could make do with just an accelerometer but you will have to make the appropriate changes in the INO file. For this project, the sensor is placed along the shank of the user's right foot. 

## Overview of Signal Processing
First, raw data from sensor was downsampled. We were collecting data from the Arduino too frequently. 

Once this happened, we started doing some feature extraction. Features required to move from heel strike to foot flat are a positive edge through a high threshold in the gyro. Z signal within the last 150ms as well as a negative edge through a high threshold in the gyro. Z signal within the last 30ms. Both criteria must be met!

Freezing was detected by observing the number of median crossings in gyro. Y. If this exceeded a threshold value, we verified that freezing was occurring by checking for sharp edges in acc. X. Once freezing was detected, the auditory cue was initiated. The auditory signal continues until the user is no longer 'freezing', and we return to the normal gait cycle. 
