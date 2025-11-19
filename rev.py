def reverse_words(text):
    w = text.split()
    out = " ".join(w[::-1])
    return out

s = "hello world python"
result = reverse_words(s)
print(result)