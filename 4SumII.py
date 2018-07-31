import collections


def fourSumCount( A, B, C, D):
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)

if __name__ == '__main__':
    print(fourSumCount([1,2,3],[-2,-1,3],[-1, 2,0],[ 0, 2,2]))