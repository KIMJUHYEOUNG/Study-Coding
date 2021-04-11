def solution(s):
    answer = []
    array = []
    start = 0
    for i in range(len(s)-1):
        if s[i] == "{":
            start = i+1
        if s[i] == "}":
            ss = s[start:i].replace(","," ")
            array.append(list(map(int,ss.split())))

    
    for i in range(1,len(array)+1):
        for j in range(len(array)):
            if len(array[j]) == i:
                for k in array[j]:
                    if not answer.count(k):
                        answer.append(k)
                        break
    
    return answer
