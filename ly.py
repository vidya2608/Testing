import json
from difflib import get_close_matches 

data = json.load(open(r"C:\Users\HP\Desktop\data.json"))

def translate(w):
    if w in data:     
        return data[w]
    else:
        print("Have you enterd the wrong word ? Did you mean this ")
        print(get_close_matches(w,list(data))) 
        choose = input("Here you can type the correct word and continue:")
        return data[choose.lower()]
    
word = input("Enter word:")
print(translate(word.lower()))