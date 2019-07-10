#! /bin/sh
cd
apt install python3
apt install python3-pip
pip3 install requests
echo alias callspam="'cd && python3 Call-Spammer/spammer.py'">>.bashrc
echo "\033[37;1;42m G O O D ! \033[0m"
cd
python3 Call-Spammer/spammer.py -h
