import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Main function is extract_keywords. It takes in a string and returns a list of keywords, verbs and nouns #
# Returns a list of items. [keywords, verbs, nouns]

def extract_keywords(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Tag the words with their part of speech
    tagged_words = pos_tag(words)
    # Extract the key words and verbs
    keywords = []
    verbs = []
    nouns = []
    for word, tag in tagged_words:
        if tag.startswith('N') or tag.startswith('V'):
            keywords.append(word)
            if tag.startswith('V'):
                verbs.append(word)
            if tag.startswith('N'):
                nouns.append(word)
    return keywords, verbs, nouns

# # Example usage
# sentence = "find folder named money in directory tree HOME"
# keywords, verbs, nouns = extract_keywords(sentence)
# print("Keywords:", keywords)
# print("-")
# print("Verbs:", verbs)
# print("-")
# print("Nouns:", nouns)

