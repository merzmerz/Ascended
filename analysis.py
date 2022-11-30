from data import save_data, load_data
import json
def occurence():
    with open('jsondata.json', 'r') as openfile:
        data = json.load(openfile)
        
    eyes = []
    mouths = []
    ears = []
    faces = []
   
    for avatar in data:
        if (avatar['attributes'][0]['trait_type'] == 'eyes'):
            eyes.append(avatar['attributes'][0]['value'])
        if (avatar['attributes'][1]['trait_type'] == 'mouth'):
            mouths.append(avatar['attributes'][1]['value'])
        if (avatar['attributes'][2]['trait_type'] == 'ears'):
            ears.append(avatar['attributes'][2]['value'])
        if (avatar['attributes'][3]['trait_type'] == 'face'):
            faces.append(avatar['attributes'][3]['value'])
    CountFrequency(eyes, "eyes")
    CountFrequency(mouths, "mouths")
    CountFrequency(ears, "ears")
    CountFrequency(faces, "faces")
    #{"<trait category>": {"<trait type>": <number of occurances>}}
    
    return {
    }

def CountFrequency(my_list, category):
 
    # Creating an empty dictionary
    dict = {category:{}}
    for item in my_list:
        if (item in dict[category]):
            dict[category][item] += 1
        else:
            dict[category][item] = 1

    print(dict)

    return {
    }


