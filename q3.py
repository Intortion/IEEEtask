# input
l = []
print("Enter a number to add to list or press q to quit: ")
while True:
    n = input()
    if n == 'q':
        break
    else:
        l.append(int(n))

def powerset(l):
    new_l = []

    # if last element
    if len(l) < 1:
        return [[]]

    for rem_powerset_l in powerset(l[1:]):  # recursing in rest list
        new_l.append(rem_powerset_l + [l[0]])
        new_l.append(rem_powerset_l)
    
    return new_l

p_l = powerset(l)
# sorting the output
for j in p_l:
    j = j.sort()
p_l.sort()
print(p_l)