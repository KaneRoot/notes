#!/bin/bash

Xephyr -ac -br -screen 800x600 :1
#X -ac :1 2>/dev/null 1>&2 &
export DISPLAY=:1
vncviewer 192.168.0.100:0
