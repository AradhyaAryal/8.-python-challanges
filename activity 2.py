print("Enter a Number (Numerator)")
numn = int(input())
print("ENter a Number (Denomenator)")
numd = int(input())
if numn%numd == 0:
    print("\n" + str(numn)+ "is divisible by" + str(numd))
else:
    print("\n" + str(numn)+ "is not divisible bye" + str(numd))