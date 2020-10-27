#!/bin/bash

echo "---------------------------------"
iw dev | awk '$1=="Interface"{print $2}'
echo "---------------------------------"

echo "Select interface to start Airodump :"
read selected_interface

sudo airmon-ng start $selected_interface
sudo airmon-ng check kill
echo ""

