from fastapi import FastAPI
import datetime

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')               # The decorator defines the route used in an API request
def root():
    response = {
        'greeting': 'Hello batch 2376!',    # This is a typical Bavarian greeting ;)
        'timestamp': datetime.now()
    }

    return response

@app.get('/predict')
def predict(day_of_week: int, hour:int):
    prediction = day_of_week * hour
    return {'wait': prediction}
