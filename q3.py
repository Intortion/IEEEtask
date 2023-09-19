
class Power:

    def __init__(self):
        self.l = []
        self.new_l = []
    
    def input(self):

        print("Enter a number to add to list or press q to quit: ")
        while True:
            n = input()
            if n == 'q':
                break
            else:
                self.l.append(int(n)) 
        
    def powerset(self,l):

        # if last element
        if len(l) < 1:
            return [[]]

        power_l = []
        for rem_powerset_l in self.powerset(l[1:]):  # recursing in rest list
            power_l.append(rem_powerset_l + [l[0]])
            power_l.append(rem_powerset_l)
        
        return power_l

    def output(self):
        # sorting the output
        for j in self.new_l:
            j = j.sort()
        self.new_l.sort()

        return self.new_l
    
power = Power()

power.input()

power.new_l = power.powerset(power.l)

print(power.output())
