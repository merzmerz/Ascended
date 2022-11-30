import pickle

data = []

def save_data(data):
    with open('database.p', 'wb') as FILE:
        pickle.dump(data, FILE)
    return data

def load_data():
    global data
    try:
        data = pickle.load(open("database.p", "rb"))    
    except Exception:
        pass
    return data

def clear():
    data = load_data()   
    data.clear()
    save_data(data)
    return {}
