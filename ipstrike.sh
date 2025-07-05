#!/bin/bash

ACCESS_KEY_FILE="config/lock.cfg"
MODULE_FILE="modules/tracker.py"

clear
cat banner.txt
echo ""

read -p "🔑 Enter Access Key: " input_key
real_key=$(grep 'Access_Key' $ACCESS_KEY_FILE | cut -d '=' -f2)

if [ "$input_key" != "$real_key" ]; then
    echo "❌ Invalid Access Key!"
    exit 1
fi

echo ""
echo "🎯 Menu:"
echo "1. Track IP"
echo "0. Exit"
read -p "➤ Enter your choice: " choice

case $choice in
    1) python3 $MODULE_FILE ;;
    0) echo "👋 Exiting..."; exit 0 ;;
    *) echo "❗ Invalid Option" ;;
esac
