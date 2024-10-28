from datetime import datetime, timedelta




def get_first_flow_date():

		
	year = int(input("Enter year of your last period e.g 2024: "))

	month = int(input("Enter month of your last period e.g 1,2,3: "))

	day = int(input("Enter day of your last period e.g 1,2,3: "))
		
	last_flow_date = datetime(year, month, day)

	first_flow_date = last_flow_date + timedelta(1)
	
	print("Your first flow date was: " + first_flow_date.strftime('%d-%m-%y'))
				
	print()


	return first_flow_date	



def calculate_average_cycle():

	count = 0
	total = 0

	while(count < 3):

		day = int(input("Enter the length of your menstrual cycle in the past three months e.g; 26, 28: "))
		count+=1

		total+=day
		
		
	calculated_average_cycle = total/3

	return calculated_average_cycle



def get_average_cycle():

	average_cycle = int(input("Enter your average cycle e.g; 26, 28, 30: "))

	return average_cycle
		


def get_average(average_cycle):

	average = average_cycle/2
		
	return average


def get_next_flow_date(first_flow_date, average_cycle):	

	next_flow_date = first_flow_date + timedelta(average_cycle)
		
	print("Next flow date is: " + next_flow_date.strftime('%d-%m-%y'))
	
	print()
		

def get_ovulation_date(first_flow_date, average):

	ovulation_date = first_flow_date + timedelta(average)
	
	print("Ovulation date is: " + ovulation_date.strftime('%d-%m-%y'))


def get_healing_period(first_flow_date):

	healing_phase_start_day = 6

	healing_period = first_flow_date + timedelta(healing_phase_start_day)

	print("Healing period starts from: " + healing_period.strftime('%d-%m-%y'))

		

def get_safe_period(first_flow_date, average_cycle):
		
	number_of_cycle_phase = 4

	average = average_cycle/number_of_cycle_phase

	result = average_cycle - average

	safe_period = first_flow_date + timedelta(result)

	print("Safe period is about: " + safe_period.strftime('%d-%m-%y'))




def display_results():

	first_flow_date =  get_first_flow_date()

	average_cycle = get_average_cycle()
		
	average = get_average(average_cycle)

	get_next_flow_date(first_flow_date, average_cycle)

	get_ovulation_date(first_flow_date, average)

	get_healing_period(first_flow_date)

	get_safe_period(first_flow_date, average_cycle)



def display_main_menu():

	while True:
		
		menu = """
		
			Select your choice	
			====================================
			[1] I don't know my average cycle yet
			[2] I already have my average cycle
			[3] Exit
			=====================================

			"""

		print(menu)

		choice = int(input("Enter your choice number here: "))
	
		if choice == 1:
			print("Your Average Cycle is ",round(calculate_average_cycle(), 0))
			user_input = int(input("press 0 to go back to main menu to calculate your menstrual flow cycle"))
				
		elif choice == 2:
			display_results()
			print()
			user_input = int(input("press 0 to go back to main menu"))

		elif choice == 3:
			print("Thanks for using this application, bye")
			break
		else:
			print("Oops, you entered a wrong number, please enter either 1 or 2")
	
		

while True:
	age = int(input("Please enter your age: "))
	
	if(age >= 8 and age <= 55):
		display_main_menu()
		break

	else:
		print("Oops, age must be from 8 to 55, please try again")



