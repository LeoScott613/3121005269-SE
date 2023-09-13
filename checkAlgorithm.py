import nltk
# nltk.download('punkt') should run it once
# try to tokenize a sentence
word_data="The great mathematician David Hilbert noticed that a number of important mathematical arguments were structurally similar."
nlp_token=nltk.word_tokenize(word_data)
unordered=list(set(nlp_token))

print(unordered)