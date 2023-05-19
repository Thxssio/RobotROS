
#include <iostream>
#include <unistd.h>
#include <wiringPi.h>
#include <stdio.h>
#include <cmath>
#include "libSensor.h"

using namespace std;

int main()
{
    if (wiringPiSetup() == -1)
        return -1;

    Sensor gyro;
    perror("Init gyro");

    int x,y,z;

    while(1){
        x=gyro.getAccelX();
        y=gyro.getAccelY();
        z=gyro.getAccelZ();

       
	    printf("\e[H\e[2J");
		
		printf("Acelerometro raw:\n");
	    printf("x=%d    y=%d    z=%d \n", x,y,z );
	  
	   printf("Acelerometro Angulo:\n");
	   printf("x=%f    y=%f    z=%f \n", gyro.getAngleX(),gyro.getAngleY(),gyro.getAngleZ() );
	   
	    printf("Giroscopio:\n");
	   printf("x=%d    y=%d    z=%d \n", gyro.getGyroX(),gyro.getGyroY(),gyro.getGyroZ() );
	   
	   sleep(1);
	   
	   
	   
    }
}
