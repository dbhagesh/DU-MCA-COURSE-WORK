b=[]
for i in range(5):
    try:
        a=(int(input("Enter")))
        if(a>10):
            raise Exception("SORRY") 
        b.append(a)
    except Exception as e:
        print(e)

print(b)
