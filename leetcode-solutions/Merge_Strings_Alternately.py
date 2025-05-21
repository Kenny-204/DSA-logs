word1 = "ab"
word2 = "pqrs"

def mergeAlternately( word1: str, word2: str) -> str:
    
    string = ""
    for i in range(max(len(word1),len(word2))):
        if i < len(word1 ):
         
            string = string + word1[i]
        if i < len(word2 ):
         
            string = string + word2[i]
    
    print(string)
    
mergeAlternately(word1,word2)