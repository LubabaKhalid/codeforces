def solve_case(a):
    n=len(a)
    sums=set()
    prefix_sum=[0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i]=prefix_sum[i - 1] + a[i - 1]
    
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            sums.add(prefix_sum[j] - prefix_sum[i])
    
    sums.add(0)
    result_sums=sorted(sums)
    return len(result_sums), result_sums

t = int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    
    count,distinct_sums=solve_case(a)
    print(count)
    print(" ".join(map(str, distinct_sums)))
