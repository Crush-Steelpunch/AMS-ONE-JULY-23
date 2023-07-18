# for loop

#for loopvar in <list>:
    # code stuff

# unindented code is not in the loop

listvar = ["peas","carrots","sweetcorn","potatoes"]
dictvar = {"col1":"Red", "col2":"Orange","col3":"Yellow", "col4":"Green","col5":"Blue"}

for loopvar in dictvar:
    print(loopvar)


for i in range(10,50,10):
    print(i)

var1=6

while var1 < 0:
    print("The test is true")
    var1 = var1 - 1  # var1 -= 1

# break
print('')

numberlist = [12,5,6,94,15,13,6,1324,55,54,563]
for check in numberlist:
    print('precheck')
    if check == 13:
       continue 
    print(check)
    print('postcheck')


# nesting

for iterate in numberlist:
    if iterate%2 != 0:
        while iterate > 0:
            print(iterate)
            iterate = iterate - 1


