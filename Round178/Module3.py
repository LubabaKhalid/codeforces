import sys
import threading

def main():
    sys.setrecursionlimit(1<<25)
    n,q=map(int, sys.stdin.readline().split())
    g=list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    parent=[i for i in range(n)]
    size=[1]*n
    cycle=[False]*n

    def find(u):
        while parent[u]!=u:
            parent[u]=parent[parent[u]]
            u=parent[u]
        return u

    def union(u, v):
        u_root=find(u)
        v_root=find(v)
        if u_root==v_root:
            cycle[u_root]=True
            return
        if size[u_root]<size[v_root]:
            u_root, v_root=v_root, u_root
        parent[v_root]=u_root
        size[u_root]+=size[v_root]
        cycle[u_root] |= cycle[v_root]

    for i in range(n):
        union(i, g[i])

    def mod_pow(a,b,mod):
        result=1
        a%=mod
        while b>0:
            if b%2==1:
                result=(result*a)%mod
            a=(a*a)%mod
            b//=2
        return result

    for _ in range(q):
        x_str, y_str, k_str = sys.stdin.readline().split()
        x=int(x_str) - 1
        y=int(y_str) - 1
        k=int(k_str)
        old_target=g[x]
        g[x] = y
        parent = [i for i in range(n)]
        size = [1] * n
        cycle = [False] * n
        for i in range(n):
            union(i, g[i])
        num_cycles = sum(1 for i in range(n) if parent[i] == i and cycle[i])
        print(mod_pow(k, num_cycles, 3))


main()
