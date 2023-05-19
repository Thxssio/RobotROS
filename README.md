<h1 align="center">RobotROS</h1>



***ROS Robots***

*MPU6050:*

[![.github/workflows/testcpp.yml](https://github.com/Thxssio/RobotROS/actions/workflows/testcpp.yml/badge.svg)](https://github.com/Thxssio/RobotROS/actions/workflows/testcpp.yml)

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

`pip install collection`
`pip install pyqtgraph`
`pip install board`
`pip install adafruit-circuitpython-fxos8700`
`pip install imufusion`
`pip install adafruit-circuitpython-fxas21002c`
