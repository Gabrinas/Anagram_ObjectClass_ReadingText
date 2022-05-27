# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

# PLEASE KINDLY NOTE THAT THIS IS PALIDRONE THAT I DID HERE, 
# I REALIZED THIS AFTER SUBMISSION, THANK YOU.

#txt = "home";
txt = "racecar";

def find_anagrams(word):
    
    # [assignment] Add your code here
    txt2 = txt[::-1];
    if txt == txt2:
        return True;
    else:
        return False;
        
print(find_anagrams(txt));

