def word_frequency(text):
    words = text.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


text = input("Enter a text: ")

result = word_frequency(text)

print(result)