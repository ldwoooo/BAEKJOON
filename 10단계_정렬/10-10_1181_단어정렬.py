N = int(input())

i = 0
all_words = []

# N개의 단어 입력 및 리스트에 넣어준다
while i < N:

    word = input()
    all_words.append(word)

    i += 1

# 입력된 모든 단어에서 겹치는 단어를 제거하기 위해 set로 변환
# set는 순서가 없어 sort를 사용할 수 없으므로 list로 다시 변환
not_overlapping_words = list(set(all_words))

# 다중 조건 정렬
# 먼저, len(x)를 기준으로 오름차순 정렬하고
# 그 안에서 x(알파벳 순)으로 오름차순 정렬한다
not_overlapping_words.sort(key = lambda x : (len(x), x))

# 출력값에 맞춰 출력
print('\n'.join(not_overlapping_words))

#---------------------------------------------------------------------------------

N = int(input())

words = sorted(set([input() for i in range(N)]), key = lambda x : (len(x), x))

print('\n'.join(words))