a = input("Please Enter 1st String: ")
b = input("Please Enter 2nd String: ")

rows = len(a) + 1
columns = len(b) + 1

Matrix = [[0 for x in range(columns)] for y in range(rows)]


def LevenshteinDistance(a, b):
    #lets iterate throught the matrix
    for i in range(0, rows):
        for j in range(0, columns):
            if (min(i, j) == 0):
                Matrix[i][j] = max(i, j)

            elif (a[i - 1] == b[j - 1]):
                Matrix[i][j] = Matrix[i - 1][j - 1]

            elif (a[i - 1] != b[j - 1]):
                condition1 = (Matrix[i - 1][j]) + 1
                condition2 = (Matrix[i][j - 1]) + 1
                condition3 = (Matrix[i - 1][j - 1]) + 1

                Matrix[i][j] = min(condition1, condition2, condition3)

    LeveshteinDistance = Matrix[rows - 1][columns - 1]

    return LeveshteinDistance


#this function will find the number of deletions, insertions and substitutions
#by backtracking thorugh the matrix


def findDetails(Matrix):
    #iterate from bottom left to top right of the matrix
    #the key is left means deletion up movement means insertion and diagonal movement means substitution

    deletions = 0
    insertions = 0
    substitutions = 0

    i = rows-1
    j = columns-1
    key = Matrix[i][j]

    while (i > 0 or j > 0):

        if (i == 0):  #if we reached the top element so just go left
            insertions = insertions + 1
            j = j - 1
            continue

        if (j == 0):  #if reached the left most element then just go up
            deletions = deletions + 1
            i = i - 1
            continue

        key = min(Matrix[i - 1][j], Matrix[i][j - 1], Matrix[i - 1][j - 1])

        if (a[i - 1] == b[j - 1]):
            i = i - 1
            j = j - 1

        elif (key == Matrix[i - 1][j]):
            deletions = deletions + 1
            i = i - 1

        elif (key == Matrix[i][j - 1]):
            insertions = insertions + 1
            j = j - 1
        
        elif (key == Matrix[i - 1][j - 1]):
            substitutions = substitutions + 1
            i = i - 1
            j = j - 1

    return deletions, insertions, substitutions


Total_distance = LevenshteinDistance(a, b)
deletions, insertions, substitutions = findDetails(Matrix)

#printing the matrix in a human readable format
print("The Matrix is: ")
for i in range(0, rows):
    for j in range(0, columns):
        print(Matrix[i][j], end=" ")
    print()

print("\nTotal number of deletions is: ", deletions)
print("Total number of insertions is: ", insertions)
print("Total number of substitutions is: ", substitutions)

print("\nLevenshtein Distance is: ", Total_distance, "\n")
