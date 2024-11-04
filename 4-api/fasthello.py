from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI instance

@app.get("/")    # Define a route
def root():      # Define a function that will be called when the route is requested
    return {"message": "Hello World"} # Serializes to JSON automatically


@app.get("/hi/{name}")
def say_hi(name:str):
    return {"message": f"Hi {name}"}

@app.get("/roll/{number}d{sides}")
def roll_dice(number:int, sides:int):
    import random
    rolls = [random.randint(1, sides) for _ in range(number)]
    return {
        "number_of_rolls": number,
        "number_of_sides": sides,
        "rolls": rolls
    }