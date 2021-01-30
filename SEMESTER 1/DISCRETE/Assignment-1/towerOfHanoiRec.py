'''
2. Write a program to implement tower of Hanoi (Recursive).
'''
'''
Step 1 − Move n-1 disks from source to aux
Step 2 − Move nth disk from source to dest
Step 3 − Move n-1 disks from aux to dest
'''
def hanoi(disk,source,des,aux):
    if(disk==1):
        print("Move {} from {} to {}".format(disk,source,des))
    else:
        hanoi(disk-1,source,aux,des)
        print("Move {} from {} to {}".format(disk,source,des))
        hanoi(disk-1,aux,des,source)
def main():
    disk=int(input("Enter number of disks: "))
    hanoi(disk,'A','C','B')

if __name__ == "__main__":
    main()