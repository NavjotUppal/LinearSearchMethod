#Task 2.7
# NAVJOT KAUR(P454392)
# Linear Search is performed on the list by defining function linearsearch by passing two parameters'fruitlist' and 'target' to be found
# this program returns the location of the target index starts from 0
def linearsearch(lst,val):
    for i in range(len(lst)):
        if lst[i]==val:
            return i
    return "Not Found"
fruitlist= ['mango', 'watermelon', 'apple', 'orange', 'grape', 'banana']
target=input("Enter the target: ")
print("Found at index: "+str(linearsearch(fruitlist, target)))
