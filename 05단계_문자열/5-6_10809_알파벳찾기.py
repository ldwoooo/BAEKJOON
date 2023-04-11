s = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']
ans = [0] * len(alpha)
k = 0
for i in range(len(alpha)):
    for j in range(len(s)):
        if alpha[i] == s[j]:
            ans[i] = j
            break
    else:
        ans[i] = -1

print(*ans)
