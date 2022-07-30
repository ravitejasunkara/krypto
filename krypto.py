from fastapi import FastAPI
import requests
import json

app = FastAPI()


#Function to load all data from JSON file
def load_data():
    with open('sample.json') as f:
        return json.load(f)

json_data=load_data()

#Function to save data into the JSON file
def save_data(json_data):
    with open('sample.json', 'w') as f:
        json.dump(json_data, f, indent=4)

#Function to return status and price of an alert
def get_alert_status_and_price(alert_name):
    resultList=[json_data[alert_name][0],json_data[alert_name][1]]
    return resultList

#Function to get all alerts from JSON
def get_all_alerts_data():
    return(json_data)

#Function to insert/update data in JSON file
def add_data_to_json(alert_name,alert_data):
    Dict={alert_name:alert_data}
    json_data[alert_name]=alert_data
    save_data(json_data)


Dict = {}


@app.get("/getAllAlerts")
def get_All_Alerts():
    return get_all_alerts_data()

@app.get("/alerts/create")
def alert_create(target_price, alert_name):
    alert_data=[target_price,"Created"]
    add_data_to_json(alert_name,alert_data)
    return Dict




