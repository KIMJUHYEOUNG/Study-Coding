def main():

    n = int(input())
    
    graph = [[0 for _ in range(n) ] for _ in range(n) ]

    for i in range(n):
        k = input()
        for j in range(n):
            graph[i][j] = 1 if k[j] == "Y" else 0

    result = 0
    for l in range(n):
        v = [0 for _ in range(n) ]
        v[l] = 1
        for i in range(n):
            for j in range(n):
                if graph[l][i] or (graph[l][j] and graph[i][j]):
                    v[i] = 1

        if result < sum(v)-1:
            result = sum(v)-1

    print(result)
    
if __name__=="__main__":
    main()
