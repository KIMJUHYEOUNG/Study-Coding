def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
def main():
    t = int(input())
    for _ in range(t):
        n,m = list(map(int,input().split()))
        if n == 0 or m == 0:
            print(0)
            continue
        result = factorial(m) // (factorial(n) * factorial(m-n))
        print(int(result))
        
        
       
if __name__=="__main__":
    main()
