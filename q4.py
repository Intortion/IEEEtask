# input
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
n4 = int(input("Enter 4th number: "))
n5 = int(input("Enter 5th number: "))

# vars
l = [n1,n2,n3,n4,n5]
set_l = []

def find_divs(n):
    # find divisors
    divs = {1}
    for i in range(2,n+1):
        if n % i == 0:
            divs.add(i)
    divs.union()
    return divs

for num in l:
    set_l.append(find_divs(num))
    
all_div_set = set_l[0].intersection(*set_l[1:])
print("GCD is:",max(all_div_set))