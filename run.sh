#!/bin/bash
if [ ! -f 'database.db' ]; then
touch database.db
fi
python3 main.py
