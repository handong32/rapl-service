#!/bin/bash

#sudo dnf -y install msr-tools

currdir=$(pwd)

# update paths with currdir
sed -i "s#tmpdir#$currdir#" rapl_log.service
sed -i "s#tmpdir#$currdir#" rapl_log.py

# lets run without sudo
sudo setcap cap_sys_rawio=ep /usr/sbin/rdmsr 
sudo setcap cap_sys_rawio=ep /usr/sbin/wrmsr

# create new service
cd uarch-configure/rapl-read/ && make raplog && sudo setcap cap_sys_rawio=ep raplog && cd $currdir
sudo cp rapl_log.service /etc/systemd/system/
sudo systemctl daemon-reload

# creates msr group and lets user rdmsr, wrmsr without sudo
sudo groupadd msr
sudo chgrp msr /dev/cpu/*/msr
sudo ls -l /dev/cpu/*/msr
sudo chmod g+rw /dev/cpu/*/msr
sudo usermod -aG msr $(whoami)
echo "⚠️ ⚠️ ⚠️  NOTE: Please exit completely and re-login to this node for msr group changes to take effect ⚠️ ⚠️ ⚠️"

sudo newgrp - msr

