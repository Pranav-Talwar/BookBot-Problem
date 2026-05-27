def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    words = text.lower()
    chars_dict = {}
    for char in words:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(key=lambda d: d["char"])
    return sorted_list
