#!/bin/sh
killall wpa_supplicant
killall dhclient
		# ??
ifconfig wlan0 down
ifconfig wlan0 up
/etc/rc.d/wicd stop &>/dev/null
wpa_supplicant
