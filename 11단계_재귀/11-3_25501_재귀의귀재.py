def recursion(s, l, r, c):
    # 함수에 들어오면 c++
    c += 1

    if l >= r:  
        return 1, c

    elif s[l] != s[r]:
        return 0, c

    else: 
        return recursion(s, l+1, r-1, c)

def isPalindrome(s):
    # 재귀함수 호출 횟수를 나타내는 변수 c 선언, 재귀함수의 위치 인자 추가
    c = 0
    return recursion(s, 0, len(s)-1, c )

N = int(input())

words = [input() for i in range(N)]
# 아래와 같은 의미
# words = []
# for i in range(N):
#     word = input()
#     words.append(word)

for j in words:
    print(*isPalindrome(j))