

# M = int(input())

# A = []
# B = []

# while True:
#     num = list(map(int, input().split()))

#     A.append(num)
    
#     if len(A) == M:
#         break

# while True:
#     num = list(map(int, input().split()))

#     B.append(num)
    
#     if len(B) == M:
#         break

# print(A)
# print(B)
# print(A + B)
# -------------------------------------------------------------------

N, M = map(int(input()).split)

A = []
B = []

while True:
    num = map(int, input().split())

    A.append(num)
    if len(A) == N * M:
        break

while True:
    num = map(int, input().split())

    B.append(num)
    if len(B) == N * M:
        break

print(A)
print(B)