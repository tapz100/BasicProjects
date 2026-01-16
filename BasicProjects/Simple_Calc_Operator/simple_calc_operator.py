
#Calculate Total marks
def calcTotal(mark1, mark2, mark3):
    totalMarks = mark1 + mark2 + mark3
    return totalMarks

#Calculate Average
def calcAverage(mark1, mark2, mark3):
    totalMarks = calcTotal(mark1, mark2, mark3)
    averageMarks = totalMarks / 3
    return averageMarks

#take three marks from user as an input
mark1 = float(input("Enter the first mark: "))
mark2 = float(input("Enter the second mark: "))
mark3 = float(input("Enter the third mark: "))  

#Prints the total marks
total = calcTotal(mark1, mark2, mark3)
print("Total Marks: ", total)

#prints the average marks
average = calcAverage(mark1, mark2, mark3)
strAverage = str(average)
print("Average Marks: ", strAverage[:4])


