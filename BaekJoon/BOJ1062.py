from sys import stdin

N,K = map(int,stdin.readline().split())

alpabet = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']

fix = ['a','c','n','t','i']
def combination(arr,n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:],n-1):
                yield [arr[i]]+next

words = [stdin.readline().rstrip().replace("anta","").replace("tica","") for _ in range(N)]
ans = 0

if K<5:
    print(0)
elif K == 5:
    count = 0
    for word in words:
        flag = False
        for ch in word:
            if ch not in fix:
                flag = True
                break
        if flag:
            count+=1
    print(N-count)
else:
    for candidate in combination(alpabet,K-5):
        count = 0
        candidate = set(fix+candidate)
        for word in words:
            flag = False
            for ch in word:
                if ch not in candidate:
                    flag=True
                    break
            if flag:
                count+=1
        ans = max(ans,N-count)

    print(ans)

