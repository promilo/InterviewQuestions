''' 8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs. '''

#Brute Force
def countWays(n):
    print "on nth call", n
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays(n - 1)  + countWays(n - 2) + countWays(n - 3)


answer = countWays(5)

print answer
