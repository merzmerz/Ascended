import json
import pathlib
from PIL import Image
from filelinkdata import link

def stitch(image_list):
    image1 = Image.open(image_list[0]).convert("RGBA")
    image2 = Image.open(image_list[1])
    layer = Image.alpha_composite(image1, image2)  
    #print(len(image_list)-2)
    for i in range(len(image_list)-2):   
        image = Image.open(image_list[i+2])
        layer = Image.alpha_composite(layer, image)  
    
    return layer



def get_filename(category, trait_type, trait_name):
    return link[category][trait_type][trait_name]


def get_filelocation(category, trait_type, value):
    path = r'C:\Users\Merz\Desktop\nft ascend\pictures\ASCENDED_TRAITS_FINAL'
    path2 = trait_type.upper()
    path3 = get_filename(category, path2, value)
    
    if (path2 == "HAIR/HAT"):
        path2 = "HAIR_HAT"
    if (category == "MASKLESS"):
        path = path + "\\" + "MASKLESS"
    elif (category == "MINOR MASK"):
        path = path + "\\" + "MINOR_MASK"
    elif (category == "BONDED MASK"):
        path = path + "\\" + "BONDED_MASK"
        
    path =  path + "\\" + path2 + "\\" + path3 + ".png"
    return path

def make_imagelist(my_list):
    base = ['Background', 'Energy', 'Body', 'Tattoo', 'Outfit', 'Gear']
    maskless = 9
    minor_mask = 12
    unique_mask = 7
    image_list = []
    
    if (len(my_list['attributes']) == maskless): 
        for trait in my_list['attributes']:
            if (trait.get('trait_type') in base):
                if (trait.get('value') == "No Tattoo" or trait.get('value') == "Naked" or trait.get('value') == "No Gear"):
                    continue
                path = get_filelocation('ALL NFTs', trait.get('trait_type'), trait.get('value'))
                image_list.append(path) 
            else:
                if (trait.get('value') == "Bald"):
                    continue
                path = get_filelocation('MASKLESS', trait.get('trait_type'), trait.get('value'))
                image_list.append(path) 
                
    if (len(my_list['attributes']) == minor_mask): 
        for trait in my_list['attributes']:
            if (trait.get('trait_type') in base):
                if (trait.get('value') == "No Tattoo" or trait.get('value') == "Naked" or trait.get('value') == "No Gear"):
                    continue
                path = get_filelocation('ALL NFTs', trait.get('trait_type'), trait.get('value'))
                image_list.append(path) 
                
                #print("skip base")
            else:
                '''
                path = get_filelocation('MINOR MASK', trait.get('trait_type'), trait.get('value'))
                image_list.append(path) 
                '''
                print("skip minor")
                
    if (len(my_list['attributes']) == unique_mask): 
        for trait in my_list['attributes']:
            if (trait.get('trait_type') in base):
                if (trait.get('value') == "No Tattoo" or trait.get('value') == "Naked" or trait.get('value') == "No Gear"):
                    continue
                path = get_filelocation('ALL NFTs', trait.get('trait_type'), trait.get('value'))
                image_list.append(path) 
            else:
                path = get_filelocation('UNIQUE MASK', trait.get('trait_type'), trait.get('value'))
                image_list.append(path)
    return image_list

def make_imagelist_bonded(my_list):
    base = ['Background', 'Energy', 'Body', 'Tattoo', 'Outfit', 'Gear']
    minor_mask = 12
    
    image_list = []
    
    
    if (len(my_list['attributes']) == minor_mask): 
        for trait in my_list['attributes']:
            if (trait.get('trait_type') in base):
                if (trait.get('value') == "No Tattoo" or trait.get('value') == "Naked" or trait.get('value') == "No Gear"):
                    continue
                path = get_filelocation('ALL NFTs', trait.get('trait_type'), trait.get('value'))
                image_list.append(path) 

            else:
                
                path = get_filelocation('BONDED MASK', trait.get('trait_type'), trait.get('value'))
                image_list.append(path) 
     
    return image_list

    

if __name__ == "__main__":
    
    with open('jsondata.json', 'r') as openfile:
        data = json.load(openfile)

        bondmask_list = []
        for i in range(512,8888):
            if (len(data[i]['attributes']) >= 8):
                if (data[i]['attributes'][6].get('value') == 'Bonded Mask'):
                    image_list = make_imagelist_bonded(data[i])
                    image = stitch(image_list) 
                    image_re = image.resize((1000, 1000),Image.ANTIALIAS)
                    image_path = r'C:\Users\Merz\Desktop\nft ascend\bonded mask'
                    image_re.save(f"{image_path}/%d.png" % i, optimize = True)
        
        
    
    '''
    with open('jsondataupdate.json', 'r') as openfile:
        data = json.load(openfile)
        
        minor_masks = []
        count = 0
        for i in range(8888):
            for traits in data[i]['attributes']:
                if (traits.get("value") == "Minor Mask"):
                    minor_masks.append(i)
      
    '''
    #for i in minor_masks:
    #    image_list = make_imagelist(data[i])
    #    image = stitch(image_list) 
    #    image_re = image.resize((1000, 1000),Image.ANTIALIAS)
    #    image_path = r'C:\Users\Merz\Desktop\nft ascend\sample gen'
    #    image_re.save(f"{image_path}/%d.png" % i, optimize = True)
    