A = int(input("Enter the A value: "))
B = int(input("Enter the B value: "))
C = int(input("Enter the C value: "))

#Find the largest value among A, B, and C

print("A is the largest value ") if A > B and A > C else print("B is the largest value") if B > C else print ("C is the largest values")

# Check if all values are equal

print("All values are equal") if A == B == C else print("A is the largest value ") if A > B and A > C else print("B is the largest value") if B > C else print ("C is the largest values")

# Find whether a number is even or odd

number = int(input("Enter the number:"))
print ("even number") if number%2 == 0 else print("odd number")

'''
Output1:
Enter the A value: 220
Enter the B value: 220
Enter the C value: 220
All values are equal
Enter the number:120
even number

Output2:
Enter the A value: 30
Enter the B value: 40
Enter the C value: 20
B is the largest value
Enter the number:221
odd number

Output3:
Enter the A value: 40
Enter the B value: 30
Enter the C value: 100
C is the largest values
Enter the number:20
even number

Output4:
Enter the A value: 300
Enter the B value: 200
Enter the C value: 220
A is the largest value 
Enter the number:331
odd number
'''