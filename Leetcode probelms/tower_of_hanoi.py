def hanoi(disks, source, helper, destination):
    if disks==1:
        print(f'Disk {disks} moves from tower {source} to tower{destination}')
        return

    hanoi(disks-1, source, destination, helper)
    print(f'Disk {disks} moves from tower {source} to tower{destination}')
    hanoi(disks-1, helper, source, destination)

disks=int(input("How many disks, do you want to add: "))    
#source='A'
#helper='B'
#destination='C'
hanoi(disks, 'A', 'B', 'C')

# Explanation
# If you can imagine the disks in question as displayed in the image, you can understand how the code successfully displaces the three disks from tower A to C, following the expected rules. 

# Note how the variable disk initially takes the number of disks as the input and later is read or understood as the disk number in question inside the code.

# In the block of code, the first section is the base condition that that you apply when using disk 1. Once executed, it returns to the rest of the execution flow out of the if condition.

# The remaining disks are moved by passing the values from source to helper with destination as helper. The remaining disk is moved from source to destination. The remaining n-1 disks on the helper are moved from helper to destination with source as the helper.

# In the last section, the driver code takes the input for the number of disks I want to move. In accordance, I pass the values of A, B and C as the tower names and give the function call.

# You will notice that it took 2^3 - 1 = 7 steps to complete the transfer, which meets my expectations.

# The Tower of Hanoi and recursion, in general, can be confusing, even for an avid Python programmer. As such, the best way to understand recursion is by inserting the values and running a dry code using a pen and paper to see how the values change and which function gets called in the code at what point.

