# module supplies classes for data/time manipulation

import datetime 

#take user input 

user_input = input("Enter your goal with a deadline seperate by a colon: \n") 

#split the user input using colon as seperator 

input_list = user_input.split(":") 

#extracts goal and deadline value  from the input list and assign to its own variable. 
goal = input_list[0] 
deadline = input_list[1]  

#Display the values of input list on terminal
print (input_list)

#converting deadline string into date value 

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

#Check the Current Date  
today_date = datetime.datetime.today() 

#calculate how many date from now till deadline#  

print (deadline_date - today_date) 

