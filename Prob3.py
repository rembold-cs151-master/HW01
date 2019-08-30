#---------------- Problem 3 ------------------
#
# Name: Ethan Levitt
#
# Who did you work with (if anyone)?:
#
# --------------------------------------------


def big_odd_finder(): # Pls don't change this line, for my own purposes
    # Your code goes below here and WILL NEED TO BE INDENTED like
    # these comments are (sorry, it has to do with my own purpose above)

    # Prompt for variable inputs
    listOfOddNumbers = []

    x= int(input("Input value of X:"))
    y= int(input("Input value of Y:"))
    z= int(input("Input value of Z:"))

    # Logic to check for being largest odd:

    if x % 2 == 1:
        listOfOddNumbers.append(x)

    if y % 2 == 1:
        listOfOddNumbers.append(y)

    if z % 2 == 1:
        listOfOddNumbers.append(z)

    listOfOddNumbers.sort(reverse=True)

    # Print out largest odd value
    # or "No odd numbers found." if no odds exist
    
    if len(listOfOddNumbers) > 0:
        print (listOfOddNumbers[0])
    else:
        print ("No odd numbers found")

# Don't modify code below here please!
if __name__ == '__main__':
    big_odd_finder()
