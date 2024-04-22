import matplotlib.pyplot as plt 
import numpy as np 
import math 
import time

#Description: This program receives a list of reduced words U in the alphabet
#              {1,2} and test if U is a Nielsen reduced set


U= [[-2], [2, -1, -2], [-1, -1], [1, 2, 1]]


############## FUNCTIONS ##########################################
####### Function for reducing a word

def func1(list):
	i=0;
	for j in range(0,len(list)):
		#print(type(list))
		if (j+1<len(list)) and (list[j]+list[j+1]==0):
			del list[j]
			del list[j]
			i=1;#some change was made in the list
		if i==1:
			return True,list #the return statement ends function execution
	if i==0:#no change was made (the word is already reduced)
		return False,list

def reducing_a_word(list):
	#list=list0.copy()
	flag=True;
	while flag == True:#Reducing the word
		flag, list =func1(list);
	return list


###### Function for inverting a word
def inverting_a_word(list):
	#list=list0.copy()
	list.reverse()
	for i in range(0,len(list)):
		if list[i]==1:
			list[i]=-1;
			continue
		if list[i]==-1:
			list[i]=1;
			continue
		if list[i]==2:
			list[i]=-2;
			continue
		if list[i]==-2:
			list[i]=2;
			continue
	return list	
###############################################################	

#### TESTING IF THE SET U IS NIELSEN REDUCED #########

flag=1
print('Testing Nielsen reducibility for U=', U)

#Condition 1
empty_list=[]
if empty_list in U:
	flag=0
	print('There is an empty word in U ==> U is not Nielsen reduced.')

if flag==0:
	exit()

#Condition 2
#Appending the inverses to U 
for i in range(0,len(U)):
	v_=U[i].copy()
	u=inverting_a_word(v_);
	if u in U:
		flag=0
		print('Error in the condition 1:')
		print('There are inverse words in U ==> U is not Nielsen reduced.')
		print('U[',i,']^-1=',u,' is in the set U together with U[',i,'].')
		
	else:	
		U.append(u)

print('U augmented via the inverses, U=', U)

if flag==0:
	exit()

#verifying condition 2
for i in range(0,len(U)):
	for j in range(0,len(U)):
		v=U[i]+U[j]
		v=reducing_a_word(v)
		if len(v)==0:#if U[j] is an inverse of U[i] go to the next j
			continue
		else:
			if len(v)<len(U[i]):
				flag=0
				print('Error in the condition 2:')
				print('Length of U[',i,'] + U[',j,'] =', v, '< Length of U[',i,']=',U[i])
				print('Thus, U is not Nielsen reduced.')
			if len(v)<len(U[j]):
				flag=0
				print('Error in the condition 2:')
				print('Length of U[',i,'] + U[',j,'] =', v, '< Length of U[',j,']=',U[j])
				print('Thus, U is not Nielsen reduced.')


if flag==0:
	exit()

#Condition 3
for i in range(0,len(U)):
	for j in range(0,len(U)):
		for k in range(0,len(U)):
			vij=U[i]+U[j]
			vij=reducing_a_word(vij)

			vjk=U[j]+U[k]
			vjk=reducing_a_word(vjk)

			vijk=U[i]+U[j]+U[k]
			vijk=reducing_a_word(vijk)

			if len(vij)==0 or len(vjk)==0:#if U[j] is an inverse of U[i] go to the next j
				continue
			else:
				if (len(vijk)<=(len(U[i])-len(U[j])+len(U[k]))):
					print('Error in the condition 3:')
					print('Length of U[',i,'] + U[',j,'] + U[',k,']=', vijk, '<= Length of U[',i,']-U[',j,'] + U[',k,'] = ',len(U[i])-len(U[j])+len(U[k]))

