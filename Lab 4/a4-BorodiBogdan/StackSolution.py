from random import randint
def Display(Element_Of_The_Subset : list, NumbersList : list, LengthOfTheSubset : int):
    for index in range (0, LengthOfTheSubset):
        print(NumbersList[ Element_Of_The_Subset[index] - 1 ], end = " ")

    print("")
def Verify_If_Subset_Sum_Is_Div_By_N(Element_Of_The_Subset : list, NumbersList : list, LengthOfTheSubset : int, DivisionConditioner : int) -> bool:
    sumOfNumbers = 0

    for index in range (0, LengthOfTheSubset):
        sumOfNumbers += NumbersList[ Element_Of_The_Subset[index] - 1 ]

    if(sumOfNumbers % DivisionConditioner == 0):
        return True
    return False
def GenerateSubsetsWithStack( LengthOfTheSequence : int, NumbersList : list, DivisionConditioner : int):
    Stack = []
    Stack.append((0 , []))
    while(len(Stack) > 0):
        nextElementToBeAdded = Stack[-1][0] + 1
        SubsetOfTheSequence = Stack[-1][1]
        Stack.pop()


        if(nextElementToBeAdded <= LengthOfTheSequence):
            if(nextElementToBeAdded + 1 <= LengthOfTheSequence):
                Stack.append((nextElementToBeAdded, SubsetOfTheSequence[:]))

            SubsetOfTheSequence.append(nextElementToBeAdded)

            if(Verify_If_Subset_Sum_Is_Div_By_N(SubsetOfTheSequence, NumbersList, len(SubsetOfTheSequence),DivisionConditioner) == True and len(SubsetOfTheSequence) > 0):
                Display(SubsetOfTheSequence, NumbersList, len(SubsetOfTheSequence))

            Stack.append((nextElementToBeAdded, SubsetOfTheSequence[:]))

while True:
    print("Press 1 to generate a test and other key to exit")

    Chosen_Option = input(">>")

    if(Chosen_Option == "1"):
        N = randint(1, 7)
        print("n is: " + str(N))
        List = []

        for index in range(0, N):
            List.append(randint(1, 100))

        print("The list is: " + str(List))

        GenerateSubsetsWithStack(N, List, N)
    else:
        exit()