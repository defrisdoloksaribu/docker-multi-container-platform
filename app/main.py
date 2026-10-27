
import os
from contextlib import asynccontextmanager

import psycopg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


DATABASE_URL = os.environ["DATABASE_URL"]


def get_connection():
    return psycopg.connect(DATABASE_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    for attempt in range(10):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS inventory (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            quantity INTEGER NOT NULL CHECK (quantity >= 0)
                        )
                    """)
            break
        except psycopg.OperationalError:
            if attempt == 9:
                raise
            import time
            time.sleep(2)
    yield


app = FastAPI(
    title="Docker Multi-Container Inventory API",
    version="1.0.0",
    lifespan=lifespan,
)


class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    quantity: int = Field(ge=0)


@app.get("/health")
def health():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except psycopg.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")


@app.get("/items")
def list_items():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, quantity FROM inventory ORDER BY id"
            )
            rows = cur.fetchall()
    return [
        {"id": row[0], "name": row[1], "quantity": row[2]}
        for row in rows
    ]


@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO inventory (name, quantity) VALUES (%s, %s) "
                "RETURNING id, name, quantity",
                (item.name, item.quantity),
            )
            row = cur.fetchone()
    return {"id": row[0], "name": row[1], "quantity": row[2]}
