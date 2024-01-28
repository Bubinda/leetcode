# input:
# roots = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"

# output:
# "the cat was rat by the bat"


# solution with list comprehension and root set

def stemming(roots: list, sentence: str):
	single_words = sentence.split(" ")
	root_set = set(roots)

	stemmed_words = [root if word.startswith(root) else word for word in single_words for root in root_set]

	stemmed_sentence = ''.join(stemmed_words)
	return stemmed_sentence
			

# solution with double loop

def stem_sentence(roots, sentence):
    words = sentence.split()
    stemmed_words = []

    for word in words:
        for root in roots:
            if word.stratswith(root):
                stemmed_words.append(root)
                break
        else:
            stemmed_words.append(word)

    stemmed_sentence = " ".join(stemmed_words)
    return stemmed_sentence




# double loop solution with less memory usage


def replace_words(roots, sentence):
    words = sentence.split(" ")
    for index, word in enumerate(words):
        for root in roots:
            if word.startswith(root):
                words[index] = root
                break
    return " ".join(words)


#replace_words(roots, sentence)