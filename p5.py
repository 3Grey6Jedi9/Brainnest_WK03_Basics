#target blank rows and remove them modifying the original file

# create a string with non-ASCII characters
text = "こんにちは世界"

# encode the string to UTF-8
utf8_bytes = text.encode('utf-8')

# decode the bytes back to a string
decoded_text = utf8_bytes.decode('utf-8')

# print the original string and the decoded string
print("Original string: ", text)
print("Decoded string: ", decoded_text)
