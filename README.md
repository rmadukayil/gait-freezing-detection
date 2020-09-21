# Gait-Freezing-Detection
Analysis of raw IMU sensor data to identify freezing in gait cycle for Parkinson's patients. 

## Notes
Sensor used was the MPU 6050 six-axis gyroscope + accelerometer. For this project, the sensor is placed along the user's right shank.

## Overview of Signal Processing
First, we need to downsample the raw data. We were collecting Arduino data too frequently - this downsampled data is in the CSV files in the dataset folder.

Once this happens, we can start doing some feature extraction. Features required to move from heel strike to foot flat are a positive edge through a high threshold in the gyro. Z signal within the last 150ms as well as a negative edge through a high threshold in the gyro. Z signal within the last 30ms. Both criteria must be met!

Freezing is detected by observing the number of median crossings in gyro. Y. If this exceeds a threshold value, we verify that freezing is occurring by checking for sharp positive and/or negative edges in acc. X. Once freezing is detected, the auditory is was initiated. The auditory signal is continued until the user is no longer 'freezing', and only then do we return to the normal gait cycle. 
