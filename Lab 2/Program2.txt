"""
(10 points) Program 2: Counting Duplicate words
Write a script that uses a dictionary to determine and print the number of 
duplicate words in a sentence. Treat uppercase and lowercase letters the same 
and assume there is no punctuation in the sentence. Words with count larger 
than 1 have duplicates.
Example: The Brown cow jumped over the brown jug which contained BROWN milk 
Output should be:
brown 3
the 2
"""

def count_duplicate_words(sentence):
    # normalize the sentence by using lower() function
    normalized_sentence = sentence.lower()
    
    # split sentence into words
    words = normalized_sentence.split()
    
    # use a dictionary to count occurrences of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1 # equals itself plus 1
        else:
            word_counts[word] = 1
    
    # print words that have duplicates
    for word, count in word_counts.items():
        if count > 1:
            print(f"{word} {count}")

if __name__ == "__main__":
    sentence = input("Please enter a sentence to analyze for duplicate " +
    				 "words: ")
    count_duplicate_words(sentence)