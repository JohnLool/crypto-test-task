# Crypto Log Service

## Quick start
 
   ```bash
   git clone github.com/JohnLool/crypto-test-task && cd crypto-test-task
   ```
   ```bash
   cp .env.example .env
   ```
   ```bash
   docker-compose up --build
   ```
####  Launching tests
   ```bash
    docker-compose run --rm fastapi pytest
   ```
## Without Docker

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   ```bash
   pip install -r requirements.txt
   ```
#### Make sure that your PostgreSQL is launched 

   ```bash
   uvicorn app.main:app --reload
   ```
####  Launching tests
   ```bash
   pytest
   ```