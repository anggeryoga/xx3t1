#!/bin/bash
echo "🚀 Menginstal dependency..."
pkg update -y && pkg upgrade -y
pkg install python -y
pip install -r requirements.txt

echo "✅ Instalasi selesai! Jalankan dengan: python start.py"
