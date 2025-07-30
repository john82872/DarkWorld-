#!/bin/bash

echo "🔥 Installing or updating all DarkWorld tools..."

mkdir -p ~/DarkWorld
cd ~/DarkWorld

clone_or_update() {
    if [ -d "$1" ]; then
        echo "Updating $1..."
        cd $1
        git pull || echo "Failed to update $1, skipping..."
        cd ..
    else
        echo "Cloning $1..."
        git clone $2 || echo "Failed to clone $1, skipping..."
    fi
}

clone_or_update zphisher https://github.com/htr-tech/zphisher
clone_or_update hulk https://github.com/grafov/hulk
clone_or_update infect https://github.com/noob-hackers/infect
clone_or_update IP-Tracer https://github.com/rajkumardusad/IP-Tracer
clone_or_update RED_HAWK https://github.com/Tuhinshubhra/RED_HAWK
clone_or_update weeman https://github.com/evait-security/weeman

echo "🔄 Updating packages..."
pkg update -y
pkg upgrade -y
pkg install git python python2 php curl openssh nmap sqlmap termux-api -y

echo "📦 Installing Metasploit..."
pkg install unstable-repo -y
pkg install metasploit -y

echo "⚙️ Setting permissions..."
chmod +x ~/DarkWorld/zphisher/zphisher.sh
chmod +x ~/DarkWorld/infect/infect.sh
chmod +x ~/DarkWorld/IP-Tracer/IP-Tracer.sh
chmod +x ~/DarkWorld/RED_HAWK/rhawk.php

echo "✅ All tools installed or updated successfully inside ~/DarkWorld"
