#!/bin/bash

# Installing APP requirements
apt-get update
apt-get install -y python3
apt-get install -y curl
curl -o ./get-pip.py https://bootstrap.pypa.io/get-pip.py
apt-get install -y python3-distutils
python3 ./get-pip.py
pip3 install -r ./requirements.txt

# Installing OS requirements
sudo apt-get install -y traceroute
sudo apt-get install -y net-tools

# Finalizing installation by creating shortcut in usr/bin
here=$(pwd)
sudo ln -s $here/mazinet.py /usr/bin/mazinet