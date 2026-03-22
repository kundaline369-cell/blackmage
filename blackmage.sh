#!/data/data/com.termux/files/usr/bin/bash

clear
echo "⚡ BLACKMAGE CORE INICIANDO ⚡"

# Atualizar sistema
pkg update -y && pkg upgrade -y

# Limpeza
pkg autoclean
pkg clean

# Status CPU
echo "=== CPU STATUS ==="
top -n 1 | head -15

# Memória
echo "=== MEMORY ==="
free -h

# Rede
echo "=== NETWORK ==="
ping -c 2 8.8.8.8

echo "⚡ BLACKMAGE ATIVO ⚡"
