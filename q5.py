# input
n = int(input("Enter number of elements: "))
l = input("Enter numbers: ").split()

# int conversion
l = [int(x) for x in l]

# if number of elements match
if len(l) == n:
    # absolute value
    for element in range(len(l)):
        if l[element] < 0:
            l[element] *= -1

    def alt_sum(l):
        sum = 0
        for i in range(0,len(l),2):
            sum += l[i]
        for j in range(1,len(l),2):
            sum -= l[j]
        
        return sum

    def interchange(l):
        # finding min from +ve places and max from -ve places
        # multipy and addition for index relative to original l
        minv = l[::2].index(min(l[::2])) * 2
        maxv = l[1::2].index(max(l[1::2])) * 2 + 1

        l[minv],l[maxv] = l[maxv],l[minv]

        # print(l)      # interchanged list
        return(l)

    print(alt_sum(interchange(l)))
else:
    print("Enter correct number of elements")