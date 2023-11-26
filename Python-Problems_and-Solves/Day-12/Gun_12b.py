words = ["cat", "car", "code", "home", "learn", "fun", "job", "love", "friend", "zoo", "enjoy", "happiness", "family", "goal", "desire"]

def filter_words(letter):
    letter = letter.lower()  # Convert input letter to lowercase for case-insensitive comparison
    filtered_words = [word for word in words if letter in word]
    return filtered_words

if __name__ == '__main__':
    letter_input = input("Enter a letter: ")
    result = filter_words(letter_input)
    for word in result:
        print(word)
