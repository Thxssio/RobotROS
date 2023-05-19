from mpu6050_i2c import *
import smbus,time,datetime
import numpy as np
import matplotlib.pyplot as plt



plt.style.use('ggplot') 
time.sleep(1) 
ii = 1000 
t1 = time.time() 




mpu6050_str = ['accel-x','accel-y','accel-z','gyro-x','gyro-y','gyro-z']
mpu6050_vec, t_vec = [],[]


print('recording data')


for ii in range(0,ii):
    
    try:
        ax,ay,az,wx,wy,wz = mpu6050_conv() 
    except:
        continue
        
    t_vec.append(time.time()) 
    mpu6050_vec.append([ax,ay,az,wx,wy,wz])
    
    
print('sample rate accel: {} Hz'.format(ii/(time.time()-t1))) 
t_vec = np.subtract(t_vec,t_vec[0])

fig,axs = plt.subplots(2,1,figsize=(12,7),sharex=True)

cmap = plt.cm.Set1

ax = axs[0]
for zz in range(0,np.shape(mpu6050_vec)[1]-3):
    data_vec = [ii[zz] for ii in mpu6050_vec]
    ax.plot(t_vec,data_vec,label=mpu6050_str[zz],color=cmap(zz))

    
ax.legend(bbox_to_anchor=(1.12,0.9))
ax.set_ylabel('Acceleration [g]',fontsize=12)


ax2 = axs[1] 
for zz in range(2,np.shape(mpu6050_vec)[1]):
    data_vec = [ii[zz] for ii in mpu6050_vec]
    ax2.plot(t_vec,data_vec,label=mpu6050_str[zz],color=cmap(zz))
ax2.legend(bbox_to_anchor=(1.12,0.9))
ax2.set_ylabel('Angular Vel. [dps]',fontsize=12)
ax2.set_xlabel('Time [s]',fontsize=14)
       
fig.align_ylabels(axs)
plt.show()
