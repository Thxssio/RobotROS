<h1 align="middle">RobotROS</h1>



***ROS Robots***


[![.github/workflows/testcpp.yml](https://github.com/Thxssio/RobotROS/actions/workflows/testcpp.yml/badge.svg)](https://github.com/Thxssio/RobotROS/actions/workflows/testcpp.yml)
[![Python package](https://github.com/Thxssio/RobotROS/actions/workflows/testpython.yml/badge.svg)](https://github.com/Thxssio/RobotROS/actions/workflows/testpython.yml)



*MPU6050:*

`Error MPU6050:`


No caso do MPU6050, o cálculo do ângulo de yaw (guinada) requer informações adicionais, como o campo magnético terrestre, para determinar com precisão o ângulo de rotação em torno do eixo vertical. O MPU6050 é um sensor de giroscópio e acelerômetro, mas não possui um magnetômetro integrado para medir o campo magnético necessário para o cálculo do yaw.

Para obter medições precisas de yaw, você precisaria combinar o MPU6050 com um magnetômetro, como o MPU9250, que possui giroscópio, acelerômetro e magnetômetro integrados.

Se o seu objetivo é obter apenas o ângulo de roll e pitch usando o MPU6050, o código fornecido anteriormente deve funcionar corretamente para essas duas medições. No entanto, para incluir o ângulo de yaw, seria necessário utilizar um sensor adicional que possua um magnetômetro integrado para medições mais precisas nessa dimensão.



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
<!--
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
-->

Cpu temperature:
```
vcgencmd measure_temp
```
Python name default:

```
sudo ln -sf /usr/bin/python3 /usr/bin/python
```
Install Gpio:

```
sudo apt install python3-lgpio
```

Install smbus:

```
sudo apt install python3-smbus
```

ROS2:

```
source /opt/ros/humble/setup.bash
```

Source setup.bash in your workspace:

```
. install/setup.bash
```
<p align="middle">
<strong>
 RUN IMU - CPP
</strong>
</p>


- [ ] Update IMU - MPU6050 >>> MPU9250
    
    
    `MPU6050`
     -  [x] Pitch
     -  [x] Roll
     -  [ ] Yaw   (Magnetometer required)

    `MPU9250`
     -  [x] Pitch
     -  [x] Roll
     -  [x] Yaw   (Magnetometer required)




<div align="center">
 <img src="https://i.pinimg.com/originals/09/9d/7c/099d7c665bb501d39facd33de0f4c22c.png" width="auto" height="300">
 <img src="https://i.ebayimg.com/images/g/eVIAAOSwYh5hwq9h/s-l500.jpg" width="auto" height="300">
</div>

```
pip install setuptools==58.2.0
```
- [x] Pub:
```
ros2 launch imu imu_launch.py
```

Check Cam:

Install:

```
sudo apt install v4l-utils -y
```
* `v4l2-ctl --list-devices`
    - [x] CSI CAM: `/dev/video0`
