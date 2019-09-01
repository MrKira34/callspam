#! /bin/sh
cd
apt install python
apt install python3
apt install python3-pip
pip3 install requests
pip3 install colorama
echo clear>>.bashrc
echo alias callspam-update="'clear && cd && rm -rf callspam && git clone https://github.com/FSystem88/callspam && clear && sh callspam/install.sh'">>.bashrc
echo alias callspam="'clear && cd && python3 callspam/spammer.py'">>.bashrc
clear
cd
python3 callspam/spammer.py
