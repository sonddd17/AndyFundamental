def letter_count(agrs):
    counts = {}
    
    for i in agrs:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts



word1 = input("Emter a word1: ")
word2 = input("Enter a word2: ")

def is_anagram(x,y):
    countx = letter_count(x.lower().replace(" ",""))
    county = letter_count(y.lower().replace(" ",""))
    
    return countx == county
print(is_anagram(word1,word2))