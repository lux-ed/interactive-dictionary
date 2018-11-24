import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:   #if returns true
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y is yes, or N if no: "%get_close_matches(w, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return "the word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query. Please double check it."
    else:        
        return " \n The word doesn't exist. Please double check it. "

word = input("Enter word: ")   
#global variable, we define it here

output = translate(word)   
#global variable, and then we pass the variable here. Whatever is passed in translate(whatever is passed), goes back to the function argument.
if type(output) == list:
    for item in output:
        print("\n", item)
else:
    print(output)
