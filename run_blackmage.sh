echo "🩸 Iniciando API Flask..."

pkill -f blackmage_api.py 2>/dev/null

python ~/blackmage/blackmage_api.py &
sleep 2
