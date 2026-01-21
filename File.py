# with open(r"C:\Users\hp R5\OneDrive\Desktop\Folder\Amit,20,DElhi.txt","r") as f1:
#     print(len(f1.readlines()))

# with open(r"C:\Users\hp R5\OneDrive\Desktop\Folder\Amit,20,DElhi.txt","w") as f2:
#     f2.write("\nI am ......")

# with open(r"C:\Users\hp R5\OneDrive\Desktop\Folder\Amit,20,DElhi.txt","r") as f1:
#     print(f1.read())



# file open in r+ mode (read + write)
f = open(r"C:\Users\hp R5\OneDrive\Desktop\Folder\Amit,20,DElhi.txt","r+")

# cursor ko end of file par le jana
f.seek(0, 2)   # 2 = SEEK_END

# new student add karna
f.write("\nSneha 20 Hyderabad")

f.close()



    
    