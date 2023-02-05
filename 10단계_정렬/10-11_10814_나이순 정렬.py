N = int(input())

people = []

for i in range(N):
    age, name = input().split()
    age = int(age)

    people.append((age, name))

people.sort(key = lambda x : x[0])

for i in people:
    print(i[0], i[1])
