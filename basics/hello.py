## 1.Hello World
print("Hello World")

## 2.Printing
a = input()
b = input()
separator = input()[0]
# Print with space
print(a+" "+b)
# Print without newline at the end
print(a+" "+b,end="")
# Print with separator
print(a+separator+b)
# Print without space
print(a+b)

## 3. Int str -  Write your code below that prints a a times and b b times, seperated by c

a = int( input())
b = int(input())
c = input()
print(str(a)*a+c+str(b)*b)


