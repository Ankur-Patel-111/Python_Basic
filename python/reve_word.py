# WAP to reverse the word if it is alphabitd is alphabits else dont reverse
st=input()
for i in st.split():
	if i.alpha():
		print(i[::-1,end=' ')
	else:
	 print(i,end=' ')
