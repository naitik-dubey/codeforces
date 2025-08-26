'''
In this problem we have N participant and kth position and each participant has a score
a1,a2,a3,...an. and the score is already sorted in the decreasing order.

A participant can only go advance if their score is >= score of the kth place finisher
and the participant can not go further if their score is zero.

'''


n, k = map(int,input().split())
participant = list(map(int, input().split()))
place = participant[k-1]
count = 0
for i in participant:
    if i ==0:
        break
    elif i >= place:
        count += 1
    else:
        break
print(count)
