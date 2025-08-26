'''
In this problem we need to identify that the given username(string) is female or male.
If the length of the username is even then it is girl and print "CHAT WITH HER" else
print "IGNORE HIM".
NOTE :->we need to count only the unique character
'''

name = input()
count = len(set(name))
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")