#take three marks from user as an input
mark1 = float(input("Enter the first mark: "))
mark2 = float(input("Enter the second mark: "))
mark3 = float(input("Enter the third mark: ")) 

#=============PART 1=================
#====================================
# 1. Calculate total marks of three subjects
# 2. Calculate average marks of three subjects

#Calculating using functions
#Calculate Total marks
'''def calcTotal(mark1, mark2, mark3):
    totalMarks = mark1 + mark2 + mark3
    return totalMarks'''

#Calculate Average
'''def calcAverage(mark1, mark2, mark3):
    totalMarks = calcTotal(mark1, mark2, mark3)
    averageMarks = totalMarks / 3
    return averageMarks'''

#calculate total marks without using function
total = mark1 + mark2 + mark3

#Prints the total marks
#total = calcTotal(mark1, mark2, mark3)
print("Total Marks: ", total)

#calculate average marks without using function
average = total / 3

#prints the average marks
#average = calcAverage(mark1, mark2, mark3)
strAverage = str(average)
print("Average Marks: ", strAverage[:4])


#=============PART 2=================
#====================================
# 1. Check pass/fail status
# 2. Check scholarship eligibility
# 3. Check Distinction eligibility

#Check pass/fail status
boolPassResult = (mark1 >= 40) and (mark2 >=40) and (mark3 >=40)
exameResult = "You have passed the exam." if boolPassResult else"You have failed the exam."
print(exameResult)

#Check scholarship eligibility
boolScholarshipResult = "You are eligible for a scholarship." if (average >= 70) and boolPassResult else "You are not eligible for a scholarship."
print(boolScholarshipResult)

#Check distinction eligibility
boolDistinctionResult = "You are eligible for a distinction." if (average >= 80) and boolPassResult else "You are not eligible for a distinction."
print(boolDistinctionResult)