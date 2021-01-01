def main():
    x=int(input("Enter x of list:"))
    y=int(input("Enter y of list:"))
    x,y=swap(x,y)
    print(x)
    print(y)
def swap(x,y):
    return y,x
main()