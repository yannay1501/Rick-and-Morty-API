
import requests
import csv



url = "https://rickandmortyapi.com/api/character/?species=human&status=alive" #link for species = human & status = alive
response = requests.get(url)
characters = response.json()
characters = characters["results"]

included = []


for character in characters:
    origin = character["origin"]
    if "Earth" in origin["name"]:

        name = character["name"]
        location = character["location"]["name"].split("(")[0]
        image = character["image"]

        character_dict = {"name" : name, "location" : location, "image" : image}
        included.append(character_dict)



print ()


with open('results.csv', 'w', newline='') as file:
    titles = ['name', 'location', 'image']
    fileWriter = csv.DictWriter(file, fieldnames = titles)

    fileWriter.writeheader()
    fileWriter.writerows(included)














