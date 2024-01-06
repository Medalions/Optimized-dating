'''
Create randomized list containing 
all numbers from 1 to specified number
representing compatibility
'''
def make_list(count):
    import random
    List = list(range(1, count + 1))
    random.shuffle(List)
    return List

'''
Runs a list based on provided parameters
List = provided list
r = number rejected
'''
def test_list(List, r):
    test = 1
    largest = 1
    for person in List:
        if person > largest:
            if test <= r:
                largest = person
            else:
                return person
        test = test + 1
    return List[-1] # if no one better than rejects found, chooses last person

'''
Main function allowing the ability to 
adjust size of list and amount of 
people automatically rejected, as
well as running it multiple times
'''
def main():
    '''
    Variables to be chosen
    rejections = first set of guarenteed rejections
    size = amount provided in the list i.e. amount of people
    runs = amount of times the test is run to find a more
           statistical result
    '''
    size = 100 # Amount of people in the lineup (100 people)
    rejections = 37 # ~36.8% of size is mathematically best
    runs = 10000 # Number of tables tested - more runs is more accurate
    # Increase runs as much as you'd like, but I did 20000000 and it took 20 minutes
    
    perfects = 0
    sum = 0
    results = []
    for i in range(runs):
        nums = make_list(size)
        final = test_list(nums, rejections)
        print(final)
        results.append(final)
        sum += final
        if final == size:
            perfects += 1
        
    print("Perfect success percent =", str(100 * (perfects/runs)) + '%')
    print("Average result among tests was", sum/runs)
    # Note that this average result also includes the ~37% of runs that give 100
    
if __name__ == "__main__":
    main()