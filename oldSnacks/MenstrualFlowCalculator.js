const userInput = require("prompt-sync");
const prompt = userInput();


while (true){
	let age = Number(prompt("Please enter your age: "));
	
	if(age >= 8 && age <= 55){
		displayMainMenu();
		break;

		}else{
		
		console.log("Oops, age must be from 8 to 55, please try again");
			}

		};


function displayMainMenu(){
		
	const menu = 
		
		"Select your choice\n"+	
		"====================================\n"+
		"[1] I don't know my average cycle yet\n"+
		"[2] I already have my average cycle\n"+
		"=====================================\n";

		console.log(menu);

		let choice = Number(prompt("Enter your choice number here: "));

		switch(choice){

		case 1: console.log("Your Average Cycle is " + calculateAverageCycle() + ", press 0 to go back to main menu to calculate your menstrual flow cycle"); 

			let number = Number(prompt());
			if(number === 0){
				displayMainMenu();
				}
			break;

		case 2: displayResults();break;
		
		default: console.log("Oops, you entered a wrong number, please enter either 1 or 2");break;


			}
		
	};




function displayResults(){

	let firstFlowDate =  getFirstFlowDate();

	let averageCycle = getAverageCycle();
		
	let average = getAverage(averageCycle);

	getNextFlowDate(firstFlowDate, averageCycle);

	getOvulationDate(firstFlowDate, average);

	getHealingPeriod(firstFlowDate);

	getSafePeriod(firstFlowDate, averageCycle);

	};


function getFirstFlowDate(){
		
	let year = Number(prompt("Enter year of your last period e.g 2024: "));

	let month = Number(prompt("Enter month of your last period e.g 1,2,3: "));

	let day = Number(prompt("Enter day of your last period e.g 1,2,3: "));
		
	let lastFlowDate = new Date(year, month - 1, day + 1);

	let firstFlowDay = lastFlowDate.getDate() + 1;

	let firstFlowDate = new Date(year, month - 1, firstFlowDay);

	let convertedFirstFlowDate = firstFlowDate.toISOString().split('T')[0];
	
	console.log("Your first flow date was: " + convertedFirstFlowDate);
				
	console.log();


	return firstFlowDate;		
		
	};



function calculateAverageCycle(){

	let count = 0;
	let total = 0;

	while(count < 3){
		let day = Number(prompt("Enter the length of your menstrual cycle in the past three months e.g; 26, 28: "));
		count++;

		total+=day;
		
		}
		
	let calculatedAverageCycle = (total/3).toFixed(0);

	return calculatedAverageCycle;

};


function getAverageCycle(){

let averageCycle = Number(prompt("Enter your average cycle e.g; 26, 28, 30: "));

return averageCycle;
		
	};


function getAverage(averageCycle){

	let average = averageCycle/2;
		
	return average;
		
	};


function getNextFlowDate(firstFlowDate, averageCycle){	

	let flowDate = new Date(firstFlowDate);

	flowDate.setDate(flowDate.getDate() + averageCycle);

	let newYear = flowDate.getFullYear();
	let newMonth = flowDate.getMonth() + 1;
	let newDay = flowDate.getDate() - 1;
		
	console.log("Next flow date is: " + newYear +"-"+ newMonth +"-"+ newDay);
			
	console.log();
		
};
		

function getOvulationDate(firstFlowDate, average){

	let flowDate = new Date(firstFlowDate);

	flowDate.setDate(flowDate.getDate() + average);
	
	let newYear = flowDate.getFullYear();
	let newMonth = flowDate.getMonth() + 1;
	let newDay = flowDate.getDate() - 1;

	console.log("Ovulation date is: " + newYear +"-"+ newMonth +"-"+ newDay);

};


function getHealingPeriod(firstFlowDate){

	let flowDate = new Date(firstFlowDate);

	let healingPhaseStartDay = 6;

	flowDate.setDate(flowDate.getDate() + healingPhaseStartDay);

	let newYear = flowDate.getFullYear();
	let newMonth = flowDate.getMonth() + 1;
	let newDay = flowDate.getDate() - 1;

	console.log("Healing phase starts from: "  + newYear +"-"+ newMonth +"-"+ newDay);

};
		

function getSafePeriod(firstFlowDate, averageCycle){
		
	let numberOfCyclePhase = 4;

	let average = averageCycle/numberOfCyclePhase;

	let result = averageCycle - average;

	let flowDate = new Date(firstFlowDate);

	flowDate.setDate(flowDate.getDate() + result);

	let newYear = flowDate.getFullYear();
	let newMonth = flowDate.getMonth() + 1;
	let newDay = flowDate.getDate() - 1;

	console.log("Safe period is about: " + newYear +"-"+ newMonth +"-"+ newDay);


	};



