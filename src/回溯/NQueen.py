'''
n皇后问题
'''

def isOk(cur):
    for j in range(cur):
        if A[j] == A[cur] or cur-j == abs(A[cur]-A[j]):
            return False
    return True

def find(cur):
    if cur == n:
        print(A)
        return
    for i in range(n):
        A[cur] = i
        if isOk(cur) : find(cur+1)  

if __name__ == '__main__':
    n = 8
    A = [0]*n
    find(0)
