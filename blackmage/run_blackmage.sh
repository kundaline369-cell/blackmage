#!/data/data/com.termux/files/usr/bin/bash

cd ~/blackmage
source blackmage_env/bin/activate

echo "🩸 Iniciando API..."

pkill -f blackmage_api.py 2>/dev/null

python blackmage_api.py &
sleep 3

echo "🩸 Iniciando Lysarah..."
python lysarah.py
