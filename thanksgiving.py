#tukery cooking program
cooking = input("would you like to calculate your turkey cook time")
cook = True
while cook == True:
    if cooking == "yes" or cooking == "Yes":
        turkey = input("is the turkey stuffed or unstuffed?:")
        if turkey == "stuffed" or turkey == "Stuffed":
            weight = int(input("How much does the turkey weight(lbs)?:"))
            total_cook = weight*13
            print(str(total_cook)  + str("minutes at 350 farenheight"))
        elif turkey == "unstuffed" or turkey == "Unstuffed":
            weight = int(input("How much does the turkey weight(lbs)?:"))
            total_cook = weight*15
            print(str(total_cook)  + str("minutes at 350 farenheight"))
    else:
        cook == False
