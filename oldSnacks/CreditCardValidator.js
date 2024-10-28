

const userInput = require("prompt-sync");
const prompt = userInput();
				
		
let cardNumbers = prompt("Hello, kindly enter card details to verify: ");

let splittedCardNumbers = cardNumbers.split("");

displayCardDetails(splittedCardNumbers);




function displayCardDetails(numbers){

	if(numbers.length >= 13 && numbers.length <= 16)
			{
		checkPrefix(numbers);
		displayCreditCardNumber(numbers);
		displayCreditCardLength(numbers);
		determineCardValidity(numbers);
		}else{
		console.log("Invalid card numbers");
		console.log("The length must be between 13 and 16");
				
			}
	}



function checkPrefix(numbers){
		
	if (numbers[0] == "4"){
		console.log("Credit Card Type: VisaCard");
			}
	else if(numbers[0] == "5"){
		console.log("Credit Card Type: MasterCard");
			}

	else if(numbers[0] == "3" && numbers[1] == "7"){
		console.log("Credit Card Type: American Express Card");
			}
	else if(numbers[0] == "6"){
		console.log("Credit Card Type: Discover Card");
			}
	else{
		console.log("Credit Card Type: Invalid");
			}

		return numbers;

		}


function displayCreditCardLength(numbers){

	if(numbers.length >= 13 && numbers.length <= 16){
			
		console.log("Credit Card Digit Length: " + numbers.length);
				
			}
		}


function displayCreditCardNumber(numbers){
		
	process.stdout.write("Credit Card Number: ");

	for(let cardNumbers of numbers){
	process.stdout.write(cardNumbers);

		}
	console.log();

	}


function determineCardValidity(numbers){
			
	let cardNumbers = [numbers.length];
	
	for(let count = 0; count < numbers.length; count++){
		cardNumbers[count] = parseInt(numbers[count]);
				}
			
		let sumOfNumbersLessThanOrEqualToFour = 0;
		let sumOfNumbersGreaterThanFour = 0;
			
	for(let index = cardNumbers.length - 1; index >= 0; index--){
		if(index % 2 == 0 && cardNumbers[index] <= 4){
			sumOfNumbersLessThanOrEqualToFour +=cardNumbers[index] * 2;
				}
			}

	for(let index = cardNumbers.length - 1; index >= 0; index--){
		if(index % 2 == 0 && cardNumbers[index] > 4 ){
					
			sumOfNumbersGreaterThanFour +=(cardNumbers[index] * 2) - 9;
				}
			}

		let total = sumOfNumbersLessThanOrEqualToFour + sumOfNumbersGreaterThanFour;


		let sumOfOddPositions = 0;
		for(let index = cardNumbers.length - 1; index >= 0; index--){
			if(index % 2 != 0){
				sumOfOddPositions +=cardNumbers[index];
				}
			}

		let sumTotal = sumOfOddPositions + total;

		
		if(sumTotal % 10 == 0){
			process.stdout.write("Credit Card Validity Status: Valid");
				}
		else{

			process.stdout.write("Credit Card Validity Status: Invalid");
		
			}

			
		}

		

