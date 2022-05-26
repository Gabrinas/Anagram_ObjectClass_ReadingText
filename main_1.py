# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

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

