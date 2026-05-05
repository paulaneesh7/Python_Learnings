import tiktoken



encoder = tiktoken.encoding_for_model("gpt-4o")

# Token:  [25216, 3274, 0, 3673, 7317, 382, 146942, 8382]
text = "Hey There! My Name is Aneesh"

tokens = encoder.encode(text)

print("Token: ", tokens)


# De-Tokenize
de_tokenize = encoder.decode([25216, 3274, 0, 3673, 7317, 382, 146942, 8382])

print("Decoded: ", de_tokenize)