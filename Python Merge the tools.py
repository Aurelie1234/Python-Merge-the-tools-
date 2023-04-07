def merge_the_tools(string, k):
    # your code goes here
    
    split = [(string[i:i + k]) for i in range(0, len(string), k)]
    
    new_str = []
    for i in split:
     new_str.append("".join(set(i)))


    for i in range (len(new_str)):
        
         print(new_str[i])
