from flask import Flask
import json

import requests
import csv



url = "https://rickandmortyapi.com/api/character/?species=human&status=alive" #link for species = human & status = alive
response = requests.get(url)
characters = response.json()
characters = characters["results"]


included = []
included2 = []


app = Flask(__name__)


@app.route("/stage1")
def stage1():

    for character in characters:
        origin = character["origin"]
        if "Earth" in origin["name"]:
            included.append(character)


    json_included = json.dumps(included)
    return json_included


@app.route("/stage2")
def stage2():

    for character in included:
        name = character["name"]
        location = character["location"]["name"].split("(")[0]
        image = character["image"]

        character_dict = {"name": name, "location": location, "image": image}
        included2.append(character_dict)


    json_included2 = json.dumps(included2)
    return json_included2


@app.route("/stage3")
def stage3():
    with open('results.csv', 'w', newline='') as file:
        titles = ['name', 'location', 'image']
        fileWriter = csv.DictWriter(file, fieldnames=titles)

        fileWriter.writeheader()
        fileWriter.writerows(included2)

    return "Written to to the csv file!"


@app.route("/healthcheck")
def healthcheck():
    with open('results.csv') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if rows == included2:
        return "I checked and your file is perfect!"
    else:
        return "I checked and your file is not as needed..."



if __name__ == "__main__":
    app.run()










