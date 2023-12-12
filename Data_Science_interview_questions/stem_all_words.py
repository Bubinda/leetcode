#  Given a dictionary consisting of many roots and a sentence, write a function to stem all the words in the sentence with the root forming it.

# In data science, there exists the concept of stemming, which is the heuristic of chopping off the end of a word to clean and bucket it into an easier feature set. That’s being tested in this Facebook question.

# One tip: If a word has many roots that can form it, replace it with the root with the shortest length.

# Example:

# Input:


# roots = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"

# Output:

#  "the cat was rat by the bat"

roots = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

def stemming(roots, sentence):

    def find_sortest_stem(word, roots):
        shortest = word
        for i in roots:
            if word.startswith(i) and len(i) < len(shortest):
                shortest = i
        return shortest
    

    stemmed_words = []
    for i in sentence.split(' '):
        shortest_stem = find_sortest_stem(i,roots)
        stemmed_words.append(shortest_stem)

    return ' '.join(stemmed_words)


stemmed_sentence = stemming(roots,sentence)
print(stemmed_sentence)
