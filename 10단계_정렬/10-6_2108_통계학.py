# 산술평균 함수
def mean(x):
    return round(sum(x) / N)

# 중앙값 함수
def median(x):
    x.sort()
    return x[N // 2]

# 최빈값 함수
def mode(x):

    # 입력 받은 리스트가 하나이면 그대로 출력
    if len(x) == 1:
        return x[0]

    else:

        x.sort()
        dict = {}

        # 리스트의 숫자를 key, 갯수를 value로 하는 딕셔너리
        for i in x:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        # items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
        # + list로 형 변환
        a = list(dict.items())      # [(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)]

        # 나오는 갯수(최빈값)을 기준으로 내림차순 정렬
        a.sort(key = lambda x : x[1], reverse = True)

        # 초기 리스트 x를 오름차순으로 정렬해놨기 때문에
        # 최반값이 같은 값들 중 제일 작은 값과 두번 째로 작은 값만 고려하면 된다.
        if a[0][1] > a[1][1]:
            return a[0][0]

        else:
            return a[1][0]
        
# 범위 함수
def length(x):
    return max(x) - min(x)

# sys 모듈로 시간초과 해결
import sys
N = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(N)]

print(mean(arr))
print(median(arr))
print(mode(arr))
print(length(arr))