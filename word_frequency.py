sentence = input("Enter the sentence : ")

words = sentence.split()
word_freq = {}

for word in words:
    word.strip('.,?')
    word = word.lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

sorted_items = sorted(word_freq.items())

for word,freq in sorted_items:
    print(f"{word}:{freq}")
