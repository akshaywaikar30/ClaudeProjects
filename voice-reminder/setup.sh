#!/bin/bash

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Setting up Voice Reminder app...${NC}"

# Setup backend
echo -e "\n${GREEN}1. Setting up backend...${NC}"
cd backend

if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found. Please install Python 3."
    exit 1
fi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy .env
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${YELLOW}Created .env file. Please edit it and add your ANTHROPIC_API_KEY${NC}"
fi

cd ..

echo -e "\n${GREEN}Setup complete!${NC}"
echo -e "\n${YELLOW}Next steps:${NC}"
echo "1. Edit backend/.env and add your ANTHROPIC_API_KEY"
echo "2. Get Google OAuth Client ID from https://console.cloud.google.com/"
echo "3. Edit index.html line 141 and replace YOUR_GOOGLE_CLIENT_ID_HERE"
echo ""
echo -e "${GREEN}To run:${NC}"
echo "Terminal 1 (Backend): cd backend && source venv/bin/activate && uvicorn main:app --reload"
echo "Terminal 2 (Frontend): python3 -m http.server 3000"
echo ""
echo "Then open http://localhost:3000 in your browser"
