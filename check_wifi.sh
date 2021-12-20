#!/bin/bash

# keep LAN alive
echo "................................................"
date "+%Y.%m.%d %H:%M:%S"
echo " "
#ping dns server to check wifi status
ping -c2 -i3 8.8.8.8;
if [ $? != 0 ]
then
  echo " "
  echo "No network connection, restarting wlan0"
# put your router reboot code here
#sudo ifdown wlan0;
#sudo ifup wlan0;
sudo ip link set wlan0 down;
sudo ip link set wlan0 up;
fi
echo "................................................"
echo " "

