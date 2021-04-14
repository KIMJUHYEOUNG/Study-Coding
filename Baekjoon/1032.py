def main():
    n = int(input())

    array = list(input())
    
    for i in range(n-1):
        temp = list(input())
        for j in range(len(array)):
            if array[j] != temp[j]:
                array[j] = "?"
    print(''.join(array))
    
if __name__=="__main__":
    main()
