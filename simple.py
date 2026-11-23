from fastapi import FastAPI

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')               # The decorator defines the route used in an API request
def index():              # The Python function with your code
    return {'ok': False}   # The return will be serialized into JSON

@app.get('/predict')
def predict(day_of_week, hour):
    prediction = day_of_week * hour
    return {'wait': prediction}
