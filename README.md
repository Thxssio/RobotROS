# RobotROS
ROS Robots

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
  
  
