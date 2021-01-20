
A = [4, 3, 1, 2, 5]
for j in range(2, len(A)):
    k = A[j]
    i = j-1
    while i > 0 and A[i] > k:
        A[i+1] = A[i]
        if (j == 3 and i == 2):
            print(A)
        i = i-1
    A[i+1] = k
