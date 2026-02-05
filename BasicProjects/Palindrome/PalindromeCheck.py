    #Palindrome check using slicing

def is_palindrome():
    userInput = input("Enter your value:").lower()
    lengthOfUserInput = len(userInput)

    for i in range(lengthOfUserInput // 2):
        if(userInput[i] != userInput[lengthOfUserInput -i -1]):
            print("FirstChar:",userInput[i])
            print("LastChar:",userInput[lengthOfUserInput -i -1])
            print("Not a palindrome")
            return
    print("It's a plaindrome")

is_palindrome()