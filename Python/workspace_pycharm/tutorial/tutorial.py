#Notes:
#
#
import time;

num1 = 0.1
num2 = 100
str1 = "hello"
list = [785, 'name', 70.2]
print (list)
print(list[0])
print(list[0:]*2)

if num2 == 100:
    if num1==1:
        print (num2)
    else:
        print(str1)
else:
    print("Num2 is one hundred")


for num2 in range (100, 105):
    print(num2)
    ++num2

while(num2 < 110):
    print(num2)
    num2 = num2 + 1

ticks = time.time()
print(ticks)



#functions
def test_func(number):
    if number < 120:
        print(number)

test_func(num2)