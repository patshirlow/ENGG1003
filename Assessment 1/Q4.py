# a)
def word_count(speech):
    num = speech.split()
    return len(num)
print(word_count("this is a sentence"))

# b)
def vowel_words(speech):
    vowels = "aeiouAEIOU"
    count = 0
    for word in speech.split():
        if word[0] in vowels:
            count += 1
    return count
print(vowel_words("this is a sentence with alphanumeric characters exhibiting vowels"))

# c)
def um_count(speech):
    for punctuation in ",.!?;:":
        speech = speech.replace(punctuation, " ")

    words = speech.split()
    return words.count("um")
print(um_count("this um! sentence contains um. a nervous um, student"))

# d)
def num_breaths(speech):
    for breaths in ",.?!":
        speech = speech.replace(breaths, " counter")
    words = speech.split()
    return words.count("counter")
print(num_breaths("this sentence. Is punctual, effective and exhilarating!"))

# e)
def most_common_word(speech):
    punctuation = ".,?!"
    words = speech.split()
    freq = {}
    for w in words:
        if w[-1] in punctuation:
            w = w[:-1]
        w = w.lower()
        if w != "":
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
    max_count = max(freq.values())
    most_common = []
    for word in freq:
        if freq[word] == max_count:
            most_common.append(word)
    if len(most_common) == 1:
        return most_common[0], max_count
    else:
        return "Tie!", -1
print(most_common_word("ENGG1003 teaches python, engg1003 makes Python fun!"))




