from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number (excluding 0 and negatives)."""
    if n <= 0:
        return False  
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    return sum(int(digit) ** len(str(abs(n))) for digit in str(abs(n))) == n

@app.get("/")
def read_root():
    """Root endpoint with instructions."""
    return {"message": "Welcome to the Number Classification API! Use /api/classify-number?number=<your_number>"}

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="Number to classify")):
    """Classify a number and return its properties in the required format."""
    
    # Validate input: must be a valid integer
    if not number.lstrip('-').isdigit():
        return JSONResponse(status_code=400, content={"number": number, "error": True})

    number = int(number)
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")

    # Fetch fun fact from Numbers API
    fun_fact = "No fact found."
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math?json=True", timeout=5)
        if response.status_code == 200:
            fun_fact = response.json().get("text", "No fact found.")
    except requests.exceptions.RequestException:
        fun_fact = "Could not retrieve fun fact."

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(number))),
        "fun_fact": fun_fact
    }




import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
