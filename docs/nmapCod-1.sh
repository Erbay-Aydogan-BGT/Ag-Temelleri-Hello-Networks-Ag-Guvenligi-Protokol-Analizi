#!/bin/bash

echo "Hedef (scanme.nmap.org) üzerinde HIZLI port taraması başlatılıyor..."

# -F parametresi (Fast) en popüler 100 portu tarar.
nmap -F scanme.nmap.org

echo "Tarama bitti!"

# Amaç: Sadece en bilinen 100 portu tarayarak hızlıca bilgi toplamak. 
nmap -F scanme.nmap.org
