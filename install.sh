#/bin/bash/
mkdir tools
cd tools
git clone https://github.com/krypton-byte/SpamWa
git clone https://github.com/LimerBoy/Impulse
sudo apt install python3 python3-pip git -y
cd Impulse/
pip3 install -r requirements.txt
cd ../
#Instalacion de Firefox
echo "Estas Usando Arch linux / Derivadas del mismo si asi marque la opcion "
sleep 3
echo "[1] Si"
echo "[2] No"
read -p ">>>> :" opt
    if [ $opt = 1 ]; then
        sudo pacman -Sy firefox
    elif [ $opt = 2 ]; then
        sudo apt install firefox
rm -rf install.sh
fi