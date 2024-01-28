import random

class RandomNumberSelector:
    def __init__(self):
        self.selected_number = None
        self.count = 0

    def select_random_number(self, current_number):
        self.count += 1

        if self.count == 1:
            self.selected_number = current_number
        elif random.randint(1, self.count) == 1:
            self.selected_number = current_number

        return self.selected_number

# Example usage
stream = [1, 2, 3, 4, 5]
random_selector = RandomNumberSelector()

for current_number in stream:
    selected_number = random_selector.select_random_number(current_number)
    print(f"Selected Number: {selected_number}")




import random

# A function to randomly select an item 
# from stream[0], stream[1], .. stream[i-1] 
def random_number(x, y=0, count=1):
    # x is the new value
    # y is the old value, default 0
    
    # If this is the first element 
    # from stream, return it 
    if (count == 1): 
        res = x; 
    else: 
        
        # Generate a random number 
        # from 0 to count - 1 
        rnd = random.randrange(count); 

        # Replace the prev random number 
        # with new number with 1/count 
        # probability 
        if (rnd == count - 1): 
            res = x
        else: 
            res = y
    return res