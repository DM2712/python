s = "programming"

freq = {}
order = []

for ch in s:
    if ch not in freq:
        freq[ch] = 1
        order.append(ch)
    else:
        freq[ch] += 1

result = []
for ch in order:
    result.append((ch, freq[ch]))

print(tuple(result))
