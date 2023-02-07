"""
the program returns the maximum value that can be put in a knapsack of capacity C
"""

def highest_value(C, wi, value, N):
    if N == 0 or C ==0:
        return 0

        """if the weight of the nth item is > knapsack of capacity C,
         then its not included in optimal solution."""

    if (wi[N-1]>C):
        return highest_value(C, wi, value, N-1)
    
    else:
        return max(value[N-1]+ highest_value(C-wi[N-1],wi,value, N-1), highest_value(C, wi, value, N-1))


value = [60,100,120, 200]
wi = [10, 20, 30, 40]
C=50
N = len(value)

print(highest_value(C, wi, value, N))