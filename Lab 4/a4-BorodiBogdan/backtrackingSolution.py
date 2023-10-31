from  random import  randint
def Display(Element_Of_The_Subset : list, NumbersList : list, NumbersListLength : int, LengthOfTheSubset : int):
    for index in range (0, LengthOfTheSubset + 1):
        print(NumbersList[ Element_Of_The_Subset[index] ], end = " ")

    print("")

def Verify_If_Subset_Sum_Is_Div_By_N(Element_Of_The_Subset : list, NumbersList : list, LengthOfTheSubset : int, DivisionConditioner : int) -> bool:
    sumOfNumbers = 0

    for index in range (0, LengthOfTheSubset + 1):
        sumOfNumbers += NumbersList[ Element_Of_The_Subset[index] ]

    if(sumOfNumbers % DivisionConditioner == 0):
        return True
    return False

def Generate_All_SubSets_Divisible_By_N(GeneratedSubset : list, NumbersList : list, NumbersListLength : int, LengthOfTheSubset : int, DivisionConditioner : int):
    for Element_Index in range (GeneratedSubset[LengthOfTheSubset - 1] + 1, NumbersListLength):
        GeneratedSubset[LengthOfTheSubset] = Element_Index

        if(Verify_If_Subset_Sum_Is_Div_By_N(GeneratedSubset, NumbersList, LengthOfTheSubset, DivisionConditioner)):
            Display(GeneratedSubset, NumbersList, NumbersListLength, LengthOfTheSubset)

        if(LengthOfTheSubset + 1 < NumbersListLength):
            Generate_All_SubSets_Divisible_By_N(GeneratedSubset, NumbersList, NumbersListLength, LengthOfTheSubset + 1, DivisionConditioner)

        GeneratedSubset[LengthOfTheSubset] = 0


while True:
    print("Press 1 to generate a test and other key to exit")

    Chosen_Option = input(">>")

    if(Chosen_Option == "1"):
        N = randint(1, 7)

        BacktrackingArray = [0] * (N + 2)
        BacktrackingArray[-1] = -1

        print("n is: " + str(N))
        List = []

        for index in range(0, N):
            List.append(randint(0, 100))

        print("The list is: " + str(List))

        Generate_All_SubSets_Divisible_By_N(BacktrackingArray, List, len(List), 0, N)
    else:
        exit()