text = "X-DSPAM-Confidence:    0.8475"

pos = text.find(':')
# print(pos)
# piece = text[pos+5:]
piece = text[pos+1:]
print(piece)
value = float(piece)
print(value)
