#!/bin/bash

export DISPLAY=:1
X -ac :1 2>/dev/null 1>&2 &
vncviewer 192.168.0.100:0

