#!/bin/bash 

RED='\033[0;31m'
GREEN='\033[0;32m'
BROWN='\033[0;33m'
YELLOW='\033[1;33m'
NC='\033[0;0m' # No Color

# Helpers
function set_source {
	WINDOWS_SCRIPT1_DIR="venv/Scripts/activate"
	WINDOWS_SCRIPT2_DIR="venv/scripts/activate"
	UNIX_SCRIPT_DIR="venv/bin/activate"

	if [[ -f "$WINDOWS_SCRIPT1_DIR" ]] 
	then
		ACTIVATE_SCRIPT_DIR="$WINDOWS_SCRIPT1_DIR"
	elif [[ -f "$WINDOWS_SCRIPT2_DIR" ]] 
	then
		ACTIVATE_SCRIPT_DIR="$WINDOWS_SCRIPT2_DIR"
	else 
		ACTIVATE_SCRIPT_DIR="$UNIX_SCRIPT_DIR"
	fi

	source "$ACTIVATE_SCRIPT_DIR"
}

# Script start
echo -e "${GREEN}==================================="
echo -e "Creating Python virtual environment"
echo -e "===================================${NC}"
python -m venv venv
set_source
echo -e "Done"

echo -e "${GREEN}========================="
echo -e "Installing Python modules"
echo -e "=========================${NC}"
pip install -r requirements.txt
echo "Done"

echo -e "${GREEN}===================="
echo -e "Creating config file"
echo -e "====================${NC}"
cp ./config.example.py ./config.py
echo -e "Done"
echo -e "${BROWN}WARNING: Make sure to review and update the config.py${NC}"
echo -e "Setup complete"
