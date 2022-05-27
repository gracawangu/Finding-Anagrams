# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


word = input("word: ")
anagram = input("anagram: ")

def find_anagram(word, anagram):
    
    if len(word) != len(anagram):
        print("False")
  
    elif (sorted(word) == sorted(anagram)):
        print("True")
    else:
        print("False")

find_anagram(word, anagram)




