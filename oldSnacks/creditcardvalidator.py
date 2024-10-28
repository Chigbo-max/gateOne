

		
card_numbers = input("Hello, kindly enter card details to verify:  ")

splitted_card_numbers = list(card_numbers);



def check_card_length(splitted_card_numbers):

	if len(splitted_card_numbers) < 13 or len(splitted_card_numbers) > 16:
		print("Invalid number")
		print("Number must be between 13 and 16")

check_card_length(splitted_card_numbers)


def check_prefix(splitted_card_numbers):
		
	if (splitted_card_numbers[0] == "4"):
		print("Credit Card Type: VisaCard")
	elif(splitted_card_numbers[0] == "5"):
		print("Credit Card Type: MasterCard")
	elif(splitted_card_numbers[0] == "3" and numbers[1] == "7"):
		print("Credit Card Type: American Express Card")
	elif(splitted_card_numbers[0] == "6"):
		print("Credit Card Type: Discover Card")
	else:
		print("Credit Card Type: Invalid")
			
	return splitted_card_numbers


def display_credit_card_length(splitted_card_numbers):

	if(len(splitted_card_numbers) >= 13 and len(splitted_card_numbers) <= 16):
			
		print("Credit Card Digit Length: ", len(splitted_card_numbers))

	return splitted_card_numbers			


def display_credit_card_number(splitted_card_numbers):
		
	print("Credit Card Number: ",  end=" ")

	for card_numbers in splitted_card_numbers:
		print(card_numbers, end =" ")
	print()

	return splitted_card_numbers			



def determine_card_validity(splitted_card_numbers):
			
	card_numbers = [ ]

	for number in splitted_card_numbers:
		card_numbers.append(int(number))
		
	sum_of_numbers_less_than_or_equal_to_four = 0
	sum_of_numbers_greater_than_four = 0

	for index in range(len(card_numbers)-1, 0, -1):
		if(index % 2 == 0 and card_numbers[index] <= 4):
			sum_of_numbers_less_than_or_equal_to_four += card_numbers[index] * 2
			
	for index in range(len(card_numbers)-1, 0, -1):
		if(index % 2 == 0 and card_numbers[index] > 4 ):
			sum_of_numbers_greater_than_four += (card_numbers[index] * 2) - 9

	total = sum_of_numbers_less_than_or_equal_to_four + sum_of_numbers_greater_than_four

	
	sum_of_odd_positions = 0

	for index in range(len(card_numbers) -1, 0, -1):
		if(index % 2 != 0):
			sum_of_odd_positions += card_numbers[index]

	sum_total = sum_of_odd_positions + total

	if(sum_total % 10 == 0):
		print("Credit Card Validity Status: Valid")		
	else:

		print("Credit Card Validity Status: Invalid")

	return card_numbers			

check_prefix(splitted_card_numbers)
display_credit_card_number(splitted_card_numbers)
display_credit_card_length(splitted_card_numbers)
determine_card_validity(splitted_card_numbers)	

