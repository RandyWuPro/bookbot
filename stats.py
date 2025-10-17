# Get the number of words
def get_num_words(retrieved_content):
    # Split method is used to split a string into a list of substrings
    words = retrieved_content.split()
    word_count = len(words)
    return word_count

# Get the number of characters in a dictionary
def get_num_char(retrieved_content):
    string_dict = {}
    words = retrieved_content
    # Convert any character to lowercase
    words = words.lower()
    # For loop to check every letter
    for char in words:
        if char in string_dict:
            string_dict[char] += 1
        else:
            string_dict[char] = 1   
    return string_dict

# Helper function to return the count from each dictionary
def sort_on(item):
    return item["num"]

# Sorts the character counts from most to least
def sort_char_counts(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(key=sort_on, reverse=True)
    return char_list