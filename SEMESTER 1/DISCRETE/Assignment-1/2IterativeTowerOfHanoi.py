'''
2. Write a program to implement tower of Hanoi (Iterative).
'''
rod={0:'A',1:'B',2:'C'}

def hanoi(n):
	for i in range(2**n-1):
		start = (i & i+1) % 3
		end = ((i | i+1)+1) % 3
		move_disk(start, end)


def move_disk(start, end):
	print("Move topmost disk from rod {} to rod {}".format(rod[start], rod[end]))

def main():
    n=int(input("Enter number of disks: "))
    hanoi(n)

if __name__ == "__main__":
	main()
		