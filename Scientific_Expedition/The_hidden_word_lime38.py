def checkio(text, word):
    # 0. Set text ( #1 erase space & \n points #2 replace lower case)
    # 1. Fill whitespaces in the list elements.
    # 2. Transform text row/column direction using zip method
    # 3. Find the 'word' - row direction
    # 4. Is empty > find column direction
    
    
        # 0. Set text ( #1 erase space & \n points #2 replace lower case)
    res = []
    res_list = []
    text = text.replace(' ','').lower()
    text_list = text.split('\n')
    max_len = max(len(i) for i in text_list) 
    
        # 1. Fill whitespaces in the list elements using ljust method.
    for i in range(len(text_list)):
        text_list[i] = text_list[i].ljust(max_len)
        
        # 2. Transform text row/column direction using zip method
        #   (*) In the list, 'Star-Operator' means all elements
    text_tr = [''.join(t) for t in zip(*text_list)]   
    
    print(text_list)
    print(text_tr)
        
        # 3. Find the 'word' - row direction
    for i in range(len(text_list)):
        #print(text_list[i])
        if text_list[i].find(word) >= 0:
            res = [i+1, text_list[i].find(word)+1, i+1, text_list[i].find(word)+len(word)]
            print(res)
    
        # 4. Is empty > find column direction
    if res == []:
        for i in range(len(text_tr)):
            #print(text_tr[i], word)
            #print(text_tr[i].find(word))
            if text_tr[i].find(word) >= 0:
                res = [text_tr[i].find(word)+1, i+1, text_tr[i].find(word)+len(word), i+1]
                print(res)

    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
