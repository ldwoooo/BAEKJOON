L, C = map(int, input().split())

password = input().split()
password.sort()
print(password)

ans = ''
vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(C):

    for j in range(i + 1, C):

        for k in range(j + 1, C):

            for l in range(k + 1, C):

                if (password[i] not in vowel) and (password[j] not in vowel) and (password[k] not in vowel) and (password[l] not in vowel):
                    continue

                print(password[i] + password[j] + password[k] + password[l])

# while True:
# while 문 또는 재귀함수로 풀면 될 듯



# ['a', 'c', 'i', 's', 't', 'w']
