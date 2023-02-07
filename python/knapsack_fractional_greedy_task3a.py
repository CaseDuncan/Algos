import sys
class KnapsackItems:
    def __init__(self, value, weight): # weight = weight of items
        self.value = value
        self.weight = weight

def fractional_knapsack(C, given_values): # C = the given weight of Knapsack

    #sort given values based on ratio

    given_values.sort(key=lambda i: (i.value/i.weight), reverse=True)

    #value in knapsack
    value_in_knapsack = 0.0

    for item in given_values:
        # if adding a particular item won't cause an overflow then its added completely
        if item.weight <= C:
            C -= item.weight
            #update value in knapsack
            value_in_knapsack += item.value

        #add a fraction of the item if not completely
        else:
            value_in_knapsack += item.value * C / item.weight
            break
     
    # return the value in knapsack
    return value_in_knapsack

if __name__ == "__main__":
     
    C = 100
    given_values = [KnapsackItems(100, 10), KnapsackItems(150, 20), KnapsackItems(200, 30),KnapsackItems(300, 50)]
 
    max_value = fractional_knapsack(C, given_values)
    print(max_value)

    print(sys.maxsize)