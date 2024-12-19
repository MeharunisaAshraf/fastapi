from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

# Sample data
quotes = [
    {"id": 1, "quote": "The only way to do great work is to love what you do."},
    {"id": 2, "quote": "Life is what happens when you're busy making other plans."},
    {"id": 3, "quote": "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment."},
]

# Route to get all quotes
@app.get("/quotes")
def get_quotes():
    return quotes

# Route to get a random quote
@app.get("/quotes/random")
def get_random_quote():
    if not quotes:
        raise HTTPException(status_code=404, detail="No quotes found.")
    return random.choice(quotes)

# Route to add a new quote
@app.post("/quotes")
def add_quote(quote: str):
    new_id = len(quotes) + 1
    new_quote = {"id": new_id, "quote": quote}
    quotes.append(new_quote)
    return {"message": "Quote added successfully!", "quote": new_quote}
