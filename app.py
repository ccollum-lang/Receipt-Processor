from flask import Flask, request
import uuid
import re
from datetime import datetime
import math


app = Flask(__name__)
app.debug = True
receipt_dict = {}


@app.route("/reciepts/process", methods=["POST"])
def processReceipts():
    data = request.get_json()
    id = str(uuid.uuid4())
    receipt_dict[id] = data
    print(receipt_dict[id])

    return {"id": id}


@app.route("/receipts/<id>/points", methods=["GET"])
def getPoints(id):
    jsonData = receipt_dict[id] 

    # Assign all values from json to variables
    retailer: str = jsonData["retailer"]
    purchaseDate: str = jsonData["purchaseDate"]
    purchaseTime: str = jsonData["purchaseTime"]
    total: str = jsonData["total"]
    

    # ******************************* POINTS SECTION *******************************
    points = 0

    # RULE 1: +1 point for every alphanumeric character in retailer name
    alphanumeric_characters = re.findall(r'\w', retailer)
    points += len(alphanumeric_characters)

    # RULE 2: +50 points if the total is a round dollar with 0 cents
    if float(total) % 1 == 0:
        points += 50

    # RULE 3: 25 points if the total is a multiple of .25
    if float(total) % .25 == 0:
        points += 25

    # RULE 4: 5 points for every two items on the receipt
    for i, item in enumerate(jsonData["items"]):
        if (i + 1) % 2 == 0:
            points += 5

    # RULE 5: if the trimmed length of the item description is a multiple of 3,
    # multiply the 'price' by .2 and round up to the nearest integer. The result
    # is the number of points earned.
    for item in jsonData["items"]:
        shortDescription: str = item["shortDescription"]
        price: str = item["price"]
        if len(shortDescription.strip()) % 3 == 0:
            points += math.ceil(float(price) * 0.2)
            

    # RULE 6: 6 points if the day in the purchase date is odd.
    date_object = datetime.strptime(purchaseDate, '%Y-%m-%d').date()
    if int(date_object.day) % 2 != 0:
        points += 6

    # RULE 7: 10 points if the time of purchase is after 2pm and before 4pm
    start_time = datetime.strptime('14:00', '%H:%M')
    end_time = datetime.strptime('16:00', '%H:%M')
    check_time = datetime.strptime(purchaseTime, "%H:%M")

    if start_time <= check_time < end_time:
        points += 10
    
    #return points as json object
    return {"points": points}