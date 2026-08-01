subscribers = ["an@email.com", "binh@email.com", "chi@email.com"]
customers = ["binh@email.com", "chi@email.com", "duy@email.com"]

# print(prices_a.keys() & prices_b.keys())   # {'sql'} — keys in both
# print(prices_a.keys() | prices_b.keys())   # all keys combined
# print(prices_a.keys() - prices_b.keys())   # keys only in prices_a


### Find Common ###

def find_common(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a & set_b

# print(find_common(subscribers,customers))


### Dict Comprehension ###


words = ["cat", "elephant", "dog", "python"]
word_lengths = { word : len(word) for word in words } 
print(word_lengths)