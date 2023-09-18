s1 = input("Enter first String: ")
s2 = input("Enter second String: ")

balanced = True
for ch in set(s1):
    if ch not in s2:
        balanced = False

if balanced:
    print("Strings are balanced")
else:
    print ("Strings are not balanced")