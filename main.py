import tiktoken
encoder = tiktoken.encoding_for_model("gpt-4o")
print("Token",encoder.n_vocab)

text = "the cat sat on the mat"

token = encoder.encode(text)
print("Tokens of text:",token)

print("Decoded : ", encoder.decode([3086, 9059, 10139, 402, 290, 2450]))