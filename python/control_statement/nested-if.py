# nested if
mark=int(input("Enter the mark:"))
if(mark>=45):
	if(mark>=65):
		if(mark>=80):
			print("Grade A")
		else:
			print("Grade B")
	else:
		print("Grade C")
else:
	print("Failed")
print("Outside nested if")

