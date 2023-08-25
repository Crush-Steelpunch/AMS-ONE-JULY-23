# Conditionals

var1 = int(input("NUMBER IN!:"))

if var1 != 5:
    #indented stuff here
    # this is indented
    print("the test returned True")



# Not indented
print("This line was run after the if stament had all finished")

# Boolean conditionals

var2 = 3
if var1 > 5 or (var1 == var2 and var1%2 != 0):
    print('Both tests returned true')


# elif

if var1 == 11:
    print('The test was equal to 11')
elif var1 == 12:
    print('the test was equal to 12')
elif var1 == 13:
    print('the test was equal to 13')
else:
    print('the test was false')



# nested if

if var1 < 5:
    if var1%2 !=0:
        print('It is odd')
    else:
        print('It is even')
else:
    print('It is a biggish number')


# IN

strvar1 = input("STRING!: ")

if "b" in strvar1:
    print("b is in " + strvar1)


testindict = input("What is in the dict: ")

dictionary_variable = {'name': 'Leon', 'cool': True, 'Watch': 'Charged', 'Awesomeness': 9001}

if testindict in dictionary_variable.keys():
    print(dictionary_variable[testindict])
else:
    print(testindict+ " is not a key in the dict")

mark = int(input("NUMBER IN!:"))


if float(mark) > 85:
    print("distinction")
if float(mark) > 65 and float(mark) <= 85:
    print("pass")
if float(mark) <= 65:
    print("fail")


if mark > 65:
    if mark < 85:
        print("pass")
    else:
        print("distinction")
else:
    print("fail")



if mark > 85:
    print("Distinction")
    if 65<= mark <=85:
        print("pass")
else:
    print("fail") 




temp = "21C"
templist = temp.split('C')
numtemp = int(templist[0])

