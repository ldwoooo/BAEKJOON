while True:
    txt = list(input())                             # sys 모듈을 사용하면 '스페이스 바'도 지워줌

    if len(txt) == 1 and '.' in txt:                # 리스트 길이가 1이고 동시에 .일때 break
        break
    # ''' 이렇게도 쓸 수 있음
    # txt = list(sys.stdin.readline())

    # if txt == ['.', '\n']:
    #     break
    # '''
    else:
        stack = []
        for i in txt:
            if i == '(':
                stack.append(i)
            elif i == '[':
                stack.append(i)
            elif i == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    print('no')
                    break
            elif i == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    print('no')
                    break
            elif i == '.':
                if len(stack) == 0:
                    print('yes')
                else:
                    print('no')
