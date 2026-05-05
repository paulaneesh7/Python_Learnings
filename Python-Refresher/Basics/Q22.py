

def capitalize_str(text):
    words = text.split(" ")
    new_str = ""

    for i in range(len(words)):
        s = words[i]
        first_char = s[0].upper()
        rest_chars = s[1:]
        new_str += first_char + rest_chars + " "
    return new_str


print(capitalize_str("pynative.com is for python lovers"))