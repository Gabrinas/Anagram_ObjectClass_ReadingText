#-*-coding:utf8;-*-
#qpy:console

# print "This is console module"

txt = "Racecar";
"""
def anagram_words(txt, anagram):
    txt2 = txt.replace("", " ");
    txt2 = txt2.split();
    print(txt2);
    txc = anagram.replace("", " ");
    txc = txc.split();
    print(txc);
    for i in txc:
        if i in txt2:
            return True;
        else:
            return False         

print(anagram_words("Racecar", "abr"));
"""


def anagram_words(txt, anagram):
    """
    asm = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
    Abg = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    for i in range(len(asm)):
        asm[i] = Abg[i];
    """ 
    txt2 = txt.lower();
    txc = anagram.lower();
     
    
    txt2 = sorted(txt2);
   # print(txt2);
    txc = sorted(txc);
    #print(txc);
    
    if txt2 == txc:
        return True;
    else:
        return False;

print(anagram_words("Elbow", "Below"));









