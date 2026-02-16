s = "aabbab"
max_len = 0

for i in range(len(s)):
    a = b = 0
    for j in range(i, len(s)):
        if s[j] == 'a':
            a += 1
        else:
            b += 1

        if a == b:
            max_len = max(max_len, j - i + 1)

print(max_len)
