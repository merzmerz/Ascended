import json
from pickle import FALSE
from data import clear, save_data, load_data
import random
from AscendData import traits
import glob
import shutil
import os

frequency = {}
black_spike = False
white_spike = False

def avatar_create(ascended_count):
    data = load_data()
    global black_spike
    global white_spike
    created = False
    my_list = []
    category = ["MASKLESS", "MINOR MASK", "UNIQUE MASK"]
    prob = [70, 25, 5]
    # create avatar
    background = generate("ALL NFTs", "BACKGROUND")
    energy = generate("ALL NFTs", "ENERGY")
    body = generate("ALL NFTs", "BODY")
    tattoo = generate("ALL NFTs", "TATTOO")
    outfit = generate("ALL NFTs", "OUTFIT")
    gear = generate("ALL NFTs", "GEAR")
    # if green outfit, avatar have no gear
    if (green_outfit(outfit[0])):
        gear[0] = "No Gear"
        
    # choose category
    add_on = random.choices(category, prob, k=1)
    
    
    # base avatar
    avatar = {"description": "Ascended is a collection of 8,888 unique randomly generated explorers who seek the enigmatic power of the Masks. Join them as they venture into the surreal and supernatural world of Inmanis!",
              "external_url": "https://ascendednft.com/",
              "name": "Ascended #" + str(ascended_count),
              "attributes": [{"trait_type": "Background", "value": background[0]}, {"trait_type": "Energy", "value": energy[0]}, 
            {"trait_type": "Body", "value": body[0]}, {"trait_type": "Tattoo", "value": tattoo[0]}, {"trait_type": "Outfit", "value": outfit[0]},
            {"trait_type": "Gear", "value": gear[0]}],
              "image": "to be replaced"
            }
    
    # include maskless add on to base avatar
    if (add_on[0] == "MASKLESS"):
        hh = generate("MASKLESS", "HAIR/HAT")
        eyes = generate("MASKLESS", "EYES")
        mouth = generate("MASKLESS", "MOUTH")
        
        # blue highlight
        if (black_spike == False):
            black_spike = True
            hh[0] = "Black Spikes"
            eyes[0] = "Black Spikes"
            mouth[0] = "Black Spikes"
        
        elif (white_spike == False and black_spike == True):
            white_spike = True
            hh[0] = "White Spikes"
            eyes[0] = "White Spikes"
            mouth[0] = "White Spikes"
            
        if (hh[0] == "White Spikes" or eyes[0] == "White Spikes" or mouth[0] == "White Spikes"):
            if (hh[0] == "Black Spikes"):
                hh[0] = "White Spikes"
            if (eyes[0] == "Black Spikes"):
                eyes[0] = "White Spikes"
            if (mouth[0] == "Black Spikes"):
                mouth[0] = "White Spikes"
                
        if (hh[0] == "Black Spikes" or eyes[0] == "Black Spikes" or mouth[0] == "Black Spikes"):
            if (hh[0] == "White Spikes"):
                hh[0] = "Black Spikes"
            if (eyes[0] == "White Spikes"):
                eyes[0] = "Black Spikes"
            if (mouth[0] == "White Spikes"):
                mouth[0] = "Black Spikes"
                   
        # yellow highlight
        if (eyes[0] == "Black Strips"):
            mouth[0] = "Black Strips"
            eyes[0] = "Black Strips"
            
        if (eyes[0] == "White Strips"):
            mouth[0] = "White Strips"
            eyes[0] = "White Strips"
        
        if (mouth[0] == "Black Strips" and eyes[0] != "Black Strips"):
            while (True):
                mouth = generate("MASKLESS", "MOUTH")
                if (mouth[0] != "White Strips" and mouth[0] != "Black Strips"):
                    break

        if (mouth[0] == "White Strips" and eyes[0] != "White Strips"):
            while (True):
                mouth = generate("MASKLESS", "MOUTH")
                if (mouth[0] != "White Strips" and mouth[0] != "Black Strips"):
                    break
            
        my_list.extend([hh[0], eyes[0], mouth[0]])     
        avatar["attributes"].extend([{"trait_type": "Hair/hat", "value": hh[0]}, {"trait_type": "Mouth", "value": mouth[0]}, {"trait_type": "Eyes", "value": eyes[0]}])
    
    # include minor mask add on to base avatar
    elif (add_on[0] == "MINOR MASK"):
        base = generate("MINOR MASK", "BASE")
        strap = generate("MINOR MASK", "STRAPS")
        ears = generate("MINOR MASK", "EARS")
        mouth = generate("MINOR MASK", "MOUTH")
        eyes = generate("MINOR MASK", "EYES")
        top = generate("MINOR MASK", "TOP")
        
        my_list.extend([base[0], strap[0], ears[0], mouth[0], eyes[0], top[0]]) 
        avatar["attributes"].extend([{"trait_type": "Base", "value": base[0]}, {"trait_type": "Straps", "value": strap[0]}, {"trait_type": "Ears", "value": ears[0]},
                                     {"trait_type": "Mouth", "value": mouth[0]}, {"trait_type": "Eyes", "value": eyes[0]}, {"trait_type": "Top", "value": top[0]}])
    
    # include unique mask add on to base avatar
    elif (add_on[0] == "UNIQUE MASK"):
        mask = generate("UNIQUE MASK", "MASK")
        
        # if not pink outfit, get pink outfit
        if (not_pink_outfit(outfit[0])):
            while (not_pink_outfit(outfit[0])):
                outfit = generate("ALL NFTs", "OUTFIT")
        
        if (rare_unique_mask(mask[0]) and green_outfit(outfit[0])):
            gear[0] = "No Gear"
        
        elif ((rare_unique_mask(mask[0])) and (green_outfit(outfit[0]) == False)):
            while (gear[0] == "No Gear"):
                gear = generate("ALL NFTs", "GEAR")
        
        elif (rare_outfit(outfit[0])):
            i = 0
            while (rare_unique_mask(mask[0]) == False):
                mask = generate("UNIQUE MASK", "MASK")
                i+=1
                if (i == 10):
                    break
         
        avatar = {"description": "Ascended is a collection of 8,888 unique randomly generated explorers who seek the enigmatic power of the Masks. Join them as they venture into the surreal and supernatural world of Inmanis!",
              "external_url": "https://ascendednft.com/",
              "name": "Ascended #" + str(ascended_count),
              "attributes": [{"trait_type": "Background", "value": background[0]}, {"trait_type": "Energy", "value": energy[0]}, 
             {"trait_type": "Body", "value": body[0]}, {"trait_type": "Tattoo", "value": tattoo[0]}, {"trait_type": "Outfit", "value": outfit[0]},
             {"trait_type": "Gear", "value": gear[0]}],
              "image": "to be replaced"
            }
        
        my_list.extend([background[0], energy[0], body[0], tattoo[0], outfit[0], gear[0]])
        avatar["attributes"].append({"trait_type": "Mask", "value": mask[0]})

    check_dupe = duplicate_check(avatar)
    
    if (check_dupe == False):
        created = True
        CountFrequency(my_list)   
        data.append(avatar)
        save_data(data)
        
    return created

def toJson():
    data = load_data()
    with open('jsondata.json', 'w') as file:
        json.dump(data, file)

    return {
    }

def individual_Json():
    with open('jsondata.json', 'r') as openfile:
        data = json.load(openfile)
    i = 0
    for avatar in data:
        file = open('jsondata%s.json' % i, 'w')
        json.dump(avatar, file)
        file.close()
        i+=1

'''
////////////////////////////////////////////////////
Generate attributes base on given category and type
///////////////////////////////////////////////////
'''

def generate(category, type):
    type_list = getList(traits[category][type])
    rarity = []
    for acc in type_list:
        rarity.append(traits[category][type][acc])
    get_acc = random.choices(type_list, rarity, k=1)
    return get_acc

def bonded_mask():
    base = generate("BONDED MASK", "BASE")
    straps = generate("BONDED MASK", "STRAPS")
    ears = generate("BONDED MASK", "EARS")
    mouth = generate("BONDED MASK", "MOUTH")
    eyes = generate("BONDED MASK", "EYES")
    top = generate("BONDED MASK", "TOP")

    bonded_list = [base[0], straps[0], ears[0], mouth[0], eyes[0], top[0]]

    return bonded_list

'''
//////////////////
Helper function
/////////////////
'''
def green_outfit(outfit):
    nomad = "Nomad Gown"
    rebozo = "Rebozo"
    if (nomad in outfit or rebozo in outfit):
        return True
    return False

def not_pink_outfit(outfit):
    non_pink_outfit = ["White Pioneer Hoodie", "Red Sturdy Hoodie", "Grey Worn Tshirt", "Red Worn Tshirt", "Black Worn Tshirt", "White Nomad Gown", 
                       "White Navigator Jacket", "Black Navigator Jacket", "Blue Navigator Jacket", "Blue Shortsleeve Tshirt", "White Shortsleeve Tshirt", "Red Ritual Sweater",
                       "Blue Ritual Sweater", "Dark Ritual Sweater", "Grey Climber Sweater", "White Climber Sweater", "White Rebozo", "Red Rebozo", "Red Scout Jacket", "Dark Scout Jacket", 
                       "Black Puffer Jacket", "White Ceremonial Garment", "Red Regular Tshirt", "Blue Astral Sweatshirt", "White Traveller Jacket", "Red Astral Sweatshirt"
                       "Dark Traveller Jacket", "Grey Traveller Jacket", "Naked"]
    
    if (outfit in non_pink_outfit):
        return True
    return False

def rare_unique_mask(mask):
    rare_mask = ["Red Mask Of The Waking Devil", "Black Mask Of The Sixth Gate", "Blue Mask Of The Usurper", "Black Mask Of False Chaos", "Red Mask Of The Falling Star",
                 "Grey Mask Of The Endless Time", "Red Mask Of Doubt", "Red Mask Of The Ancestor", "Red Mask Of The Nines", "Blue Mask Of The Fifth Vision", "Red Mask Of The Fifth Vision",
                 "Red Mask Of The True Blind", "White Mask Of The True Blind", "Black Mask Of The Marauder", "Black Mask Of The Reaper", "Red Mask Of The Maze", "Red Mask Of The Void",
                 "Blue Mask Of The Bewitcher", "Red Mask Of The Bewitcher", "Grey Mask Of Rorschach", "Red Mask Of Wisdom", "Red Mask Of The Shadows", "White Mask Of The Shadows",
                 "Red Mask Of The Merciful", "Grey Mask Of The Speaking Wind", "Red Mask Of The Speaking Wind", "Dark Mask Of The Infinite Dusk", "Red Mask Of The Moon", "Blue Mask Of The Deep Valley",
                 "Blue Mask Of The Rising Sun", "Black Mask Of The Rufa", "Red Mask Of The Rufa", "Yellow Mask Of The Dreamer", "Red Mask Of The Dreamer", "White Mask Of Death",
                 "Grey Mask Of Death", "Blue Mask Of The Trinity", "Red Mask Of The Trinity", "Blue Mask Of The Hunter" , "Red Mask Of The Hunter", "Black Mask Of The Underworld", "Grey Mask Of The Underworld"            
                 ]  
    
    if (mask in rare_mask):
        return True
    return False

def rare_outfit(outfit) :
    rare_oft = ["Grey Serious Shirt With Pattern", "Blue Tactical Jacket", "Black Pioneer Hoodie With Pattern", "Red Shortsleeve Tshirt", "Black Climber Sweater", "Red Puffer Jacket",
                "Black Ceremonial Garment", "Red Astral Sweatshirt"
                ]
    if (outfit in rare_oft):
        return True
    return False
        
def getList(dict):
    return list(dict.keys())

def convert():
    d = dict()
    file = open("ascendcsv.csv")
    for row in file:
        row = row.strip('\n')
        row = row.strip('%')
        [key, val] = row.split(",")
        d[key] = val
    print(d)
    
def CountFrequency(my_list):

    # Creating an empty dictionary
    for item in my_list:
        if (item in frequency):
            frequency[item] += 1
        else:
            frequency[item] = 1

    return {}

def duplicate_check(avatar):
    data = load_data()
    for elements in data:
        # check size of attributes
        if (len(elements['attributes']) == len(avatar['attributes'])):   
            # check each trait for dupes
            i = 0
            dup_counter = 0
            for trait in elements['attributes']:       
                if (trait == avatar['attributes'][i]):
                    dup_counter += 1
                if (dup_counter >= len(elements['attributes'])):
                    return True
                i += 1
    return False

if __name__ == "__main__":
    count = 0
    run = 0
    #frequency = {}
    #clear()
    #convert()
    '''
    for i in range(8888):
        print(i)
        create = avatar_create(i)
        if (create == False):
            print(create)
            break
        
    with open('frequency.txt', 'w') as file:
        file.write(json.dumps(frequency))
    
    toJson()
    '''
    '''
    with open('jsondata.json', 'r') as openfile:
        data = json.load(openfile)
        
        for i in range(8888):
            my_list = []
            for traits in data[i]['attributes']:
                my_list.append(traits.get("value"))
                
            CountFrequency(my_list)
    
    with open('frequency.txt', 'w') as file:
        file.write(json.dumps(frequency))
    '''
    
    data = load_data()
    '''
    maskless_list = []
    for i in range(8888):
        if (len(data[i]['attributes']) == 6):
            maskless_list.append(i)

    print(len(maskless_list))

    for i in maskless_list:
        base = generate("BONDED MASK", "BASE")
        straps = generate("BONDED MASK", "STRAPS")
        ears = generate("BONDED MASK", "EARS")
        mouth = generate("BONDED MASK", "MOUTH")
        eyes = generate("BONDED MASK", "EYES")
        top = generate("BONDED MASK", "TOP")
        
        data[i]["attributes"].extend([{"trait_type": "Base", "value": base[0]}, {"trait_type": "Straps", "value": straps[0]}, {"trait_type": "Ears", "value": ears[0]},
                                     {"trait_type": "Mouth", "value": mouth[0]}, {"trait_type": "Eyes", "value": eyes[0]}, {"trait_type": "Top", "value": top[0]}])
        save_data(data)                        
    '''
    print(data[0]['attributes'])
    
    #save_data(data)
                
    
    #for i in minor_masks:
        #src_dir = r'C:\Users\Merz\Desktop\nft ascend\Ascend Final'
        #dst_dir = r'C:\Users\Merz\Desktop\nft ascend\6666-8888mm'
        #for pngfile in glob.iglob(os.path.join(src_dir, "%d.png" %i)):
            #shutil.copy(pngfile, dst_dir)  
     
    #individual_Json()
    #clear_Json()
    
    #print(load_data())

