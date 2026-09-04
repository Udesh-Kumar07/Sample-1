N1 = int(input("Enter a positive integer number :"))
N2 = 0
N3 = 0
for a in range(1,N1+1):
  if a%2 == 0:
    N2 = N2+a
    N3 = N3+1
    # print(a)
print("Sum of even numbers: " , N2)
print("Number of even numbers: " ,N3)
  
