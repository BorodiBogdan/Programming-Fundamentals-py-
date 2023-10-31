from random import randint
def Display(Element_Of_The_Subset : list, NumbersList : list, NumbersListLength : int, LengthOfTheSubset : int):
    for index in range (0, LengthOfTheSubset):
        print(NumbersList[ Element_Of_The_Subset[index] ], end = " ")

    print("")
def Verify_If_Subset_Sum_Is_Div_By_N(Element_Of_The_Subset : list, NumbersList : list, LengthOfTheSubset : int, DivisionConditioner : int) -> bool:
    sumOfNumbers = 0

    for index in range (0, LengthOfTheSubset):
        sumOfNumbers += NumbersList[ Element_Of_The_Subset[index]]

    if(sumOfNumbers % DivisionConditioner == 0):
        return True
    return False
def Generate_Subset_By_A_Given_Mask(Bits_Mask : int, NumbersList : list):
    pos = 0
    GeneratedList = []

    for index in range (0, len(NumbersList) + 1):
        if ( ( (2 ** index) & Bits_Mask) > 0):
            GeneratedList.append(index)

    return GeneratedList
def Generate_All_SubSets_Divisible_By_N(NumbersList : list, NumbersListLength : int, DivisionConditioner : int):

    for Bits_Mask in range (1, 2 ** NumbersListLength):
        GeneratedList = Generate_Subset_By_A_Given_Mask(Bits_Mask, NumbersList)

        if(Verify_If_Subset_Sum_Is_Div_By_N(GeneratedList, NumbersList, len(GeneratedList), DivisionConditioner)):
            Display(GeneratedList, NumbersList, NumbersListLength, len(GeneratedList))


while True:
    print("Press 1 to generate a test and other key to exit")

    Chosen_Option = input(">>")

    if(Chosen_Option == "1"):
        N = randint(1, 10)
        print("n is: " + str(N))
        List = []

        for index in range(0, N):
            List.append(randint(0, 100))

        print("The list is: " + str(List))

        Generate_All_SubSets_Divisible_By_N(List, len(List), N)
    else:
        exit()

