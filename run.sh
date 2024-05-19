#!/bin/bash
python3 -mvenv env
source env/bin/activate
pip install -r requirements.txt
python3 main.py
