# Bank API REST Server

## Setup

1. Create and activate virtual environment:

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create a `bank.db` SQLite database and add `banks` and `branches` tables.

4. Run the server:

```
python app/server.py
```

## API Endpoints

- `GET /banks` — Get all banks.
- `GET /branches/<ifsc>` — Get branch details by IFSC code.