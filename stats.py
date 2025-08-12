def word_count(text):
    return len(text.split())

def character_counts(text):
    characters = {}
    new_text = text.lower()
    for character in new_text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def character_sort(num_character):
    sorted_characters = []
    for char in num_character:
        num = num_character[char]
        sorted_characters.append({"char": char, "num": num})
    sorted_characters.sort(reverse=True, key=lambda item: item["num"])
    return sorted_characters

