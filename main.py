# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


filename = "story.txt";

def read_file_content(filename):
    
    # [assignment] Add your code here 
    
    f = open(filename, "r");
    f_read = f.read();
    if f_read:
        return "Hello World";
print(read_file_content(filename));


def count_words():
    text = read_file_content('story.txt');
    
    # [assignment] Add your code here
    txt2 = open(filename, "r");
    txt2 = txt2.read();
    
    punct = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~';
    txt3 = txt2.strip(punct);
    
    txt3 = txt3.split();
    
    
    dct = dict();
    for i in txt3:
        if i in dct:
            dct[i] += 1;
        else:
            dct[i] = 1;
    return dct;
    
print(count_words());


