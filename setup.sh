#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Setup complete. Use 'source venv/bin/activate' and then 'python3 main.py' to run the tool."
