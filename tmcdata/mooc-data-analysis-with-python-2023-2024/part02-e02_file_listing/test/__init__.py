f= open("basics.ipynb","r") as f:


    for i in range(5):
        line = f.readline()
        print(f"Line {i}: {line}", end="\n")
   