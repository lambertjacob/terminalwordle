from english_words import english_words_lower_set

# get 6 letter words
X = 6

f = open("words.txt", "w")

for word in english_words_lower_set:
    if(len(word) == X):
        s = word + "\n"
        f.write(s)

f.close()

