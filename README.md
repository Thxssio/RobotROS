<h1 align="middle">RobotROS</h1>



***ROS Robots***


[![.github/workflows/testcpp.yml](https://github.com/Thxssio/RobotROS/actions/workflows/testcpp.yml/badge.svg)](https://github.com/Thxssio/RobotROS/actions/workflows/testcpp.yml)
[![Python package](https://github.com/Thxssio/RobotROS/actions/workflows/testpython.yml/badge.svg)](https://github.com/Thxssio/RobotROS/actions/workflows/testpython.yml)



*MPU6050:*


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

*or*
```
cd ./python
```
```
pip install -r requeriments.txt
```

*ROS Install:*

```
lsb_release -sc
```
```
locale  

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  
```
```
sudo apt install software-properties-common
sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"
```
```
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
```

```
