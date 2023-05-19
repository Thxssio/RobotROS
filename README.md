<h1 align="center">RobotROS</h1>



***ROS Robots***

*MPU6050:*

[![.github/workflows/c-cpp.yml](https://github.com/Thxssio/RobotROS/actions/workflows/c-cpp.yml/badge.svg)](https://github.com/Thxssio/RobotROS/actions/workflows/c-cpp.yml)

 - i2c detect
 ```
 sudo i2cdetect -y 1
 ```
 - Config 
  ```
  sudo nano /boot/config.txt
  ```
  - edit line and add 
  ```
dtparam=i2c_arm=on, i2c_arm_baudrate=1000000
  ```
  - test IMU cpp
  ```
  g++ main.cpp -o test -lwiringPi libSensor.cpp
  ```
  
  #
