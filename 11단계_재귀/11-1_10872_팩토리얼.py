def factorial(x):
    if x > 0:
        x -= 1
    
    if x == 0:
        return 1

    return factorial(x) * (x + 1)

print(factorial(int(input())))

# # -----------------------------------------------------------------
# # 혜진님 코드
# def factorial(N):
#     if N == 0:
#         return 1        # 0 이면 리턴 1
#     return N * factorial(N - 1)

# N = int(input())
# print(factorial(N))