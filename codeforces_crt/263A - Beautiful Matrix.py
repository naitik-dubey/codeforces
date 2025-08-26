'''
In this program we need to modified a matrix so that the matrix looks beautiful
we have given a 5x5 matrix which contain 24 zeros and 1 ones and  .
we need to put the 1 in the middle and find the least step in which this work can be done.
'''
matrix = []
for i in range(5):
    row = list(map(int,input().split()))
    for j in range(5):
        if row[j] == 1:
            x, y = i+1, j+1
print(abs(x - 3)+abs(y - 3))

