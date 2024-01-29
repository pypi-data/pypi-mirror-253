def WritePrime(FileName = "Data", Start_Number = 0, Range_Numbers = None):

    """
    Assign FileName to change the name of Data File\n
    Assign Start_Number to change the number from which Prime Numbers are checked\n
    Assign Range_Numbers to change the number at which checking Prime Numbers are ended\n
    """

    Prime_File = open(FileName + ".txt", "w+")

    while Start_Number <= Range_Numbers:
        WritePrime_Raw(Start_Number, Prime_File)
        Start_Number += 1
    
    Prime_File.close()

    print(open(FileName + ".txt").read())
    
def WritePrime_Raw(Max_Range, Prime_File):

    """
    Function to support other Function [NOT TO USE ALONE]
    """

    init_var = 2

    if (Max_Range == init_var):
        Prime_File.write(str(Max_Range) + "\n")

    else:
        while (init_var < Max_Range):
            if (Max_Range % init_var == 0):
                break
            elif (init_var + 1 == Max_Range):
                Prime_File.write(str(Max_Range)+ "\n")
                break
            if (Max_Range / init_var <= init_var):
                Prime_File.write(str(Max_Range) + "\n")
                break
            init_var += 1


def IsPrime(Number):
    """
    Assign value to Number to check if it is a Prime Number
    Returns True if Prime
    """

    init_var = 2
    
    if (Number == init_var):
        print(str(Number) + " is a Prime Number!")
        return True
    elif (Number == 1 or Number == 0):
        print(str(Number) + " is not a Prime Number!")
        return False
    elif (Number < 0):
        print ("Negative Numbers are not Prime!")
        return False
    else:
        while (init_var < Number):
            if (Number % init_var == 0):
                print(str(Number) + " is not a Prime Number!")
                return False
            elif (init_var + 1 == Number):
                print(str(Number) + " is a Prime Number!")
                return True
            if (Number / init_var <= init_var):
                print(str(Number) + " is a Prime Number!")
                return True
            init_var += 1

def Factors(Number):
    """
    Returns the factors of a number
    """
    all_factors = []
    for init in range(1, (Number + 1)):
        if (Number % init == 0):
            print(init)
            all_factors.append(init)
    return all_factors

def Permutation(HeadNumber, BaseNumber):

    """
    Returns the Permutation of the inputs
    """

    Product = 1
    Products = 0
    init = HeadNumber

    if (BaseNumber == 0):
        return Product

    while init >= 1:
        Product *= init
        Products += 1

        if (Products == BaseNumber):
            break

        init -= 1

    return Product