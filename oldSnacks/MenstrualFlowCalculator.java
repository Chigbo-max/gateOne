import java.util.Scanner;
import java.time.LocalDate;

public class MenstrualFlowCalculator{
	
	public static void main(String...args){
		Scanner userInput =  new Scanner(System.in);

			while (true){
			System.out.print("Please enter your age: ");
				int age = userInput.nextInt();
				
				if(age >= 8 && age <= 55){
				
					displayMainMenu();
					break;
				}else{
					System.out.println("Oops, age must be from 8 to 55, please try again");
				}
			}

		}



	

		public static void displayMainMenu(){
		
			String menu = """
		
			Select your choice	
			====================================
			[1] I don't know my average cycle yet
			[2] I already have my average cycle
			=====================================

			""";
			System.out.print(menu);
			Scanner userInput =  new Scanner(System.in);
			System.out.print("Enter your choice number here: ");
			int choice = userInput.nextInt();

			switch(choice){

			case 1: System.out.println("Your Average Cycle is " + calculateAverageCycle() + ", press 0 to go back to main menu to calculate your menstrual flow cycle"); 

				int number = userInput.nextInt();
				if(number == 0){
					displayMainMenu();
					}
				break;

			case 2: displayResults();break;
			default: System.out.println("Oops, you entered a wrong number, please enter either 1 or 2");break;


				}
		

		
			}




		public static void displayResults(){

			LocalDate firstFlowDate =  getFirstFlowDate();

			int averageCycle = getAverageCycle();
		
			int average = getAverage(averageCycle);

			getNextFlowDate(firstFlowDate, averageCycle);

			getOvulationDate(firstFlowDate, average);

			getHealingPeriod(firstFlowDate);

			getSafePeriod(firstFlowDate, averageCycle);

			}



		public static LocalDate getFirstFlowDate(){
		
			Scanner userInput =  new Scanner(System.in);


				System.out.print("Enter year of your last period e.g 2024: ");
				int year = userInput.nextInt();

				System.out.print("Enter month of your last period e.g 1,2,3: ");
				int month = userInput.nextInt();

				System.out.print("Enter day of your last period e.g 1,2,3: ");
				int day = userInput.nextInt();
		
				LocalDate lastFlowDate = LocalDate.of(year, month, day);

				LocalDate firstFlowDate = lastFlowDate.plusDays(1);

				System.out.println("Your first flow date was: " + firstFlowDate);
				
				System.out.println();


			return firstFlowDate;		
		
		}



		public static int calculateAverageCycle(){

			Scanner userInput =  new Scanner(System.in);

				int count = 0;

				int total = 0;

				while(count < 3){

				System.out.print("Enter the length of your menstrual cycle in the past three months e.g; 26, 28: ");
				int day = userInput.nextInt();
				count++;

				total+=day;
		
				}
		
				int calculatedAverageCycle = total/3;

			return calculatedAverageCycle;


		}


		public static int getAverageCycle(){

			Scanner userInput =  new Scanner(System.in);

				System.out.print("Enter your average cycle e.g; 26, 28, 30: ");
					int averageCycle = userInput.nextInt();
		
				return averageCycle;
		
		}


		public static int getAverage(int averageCycle){

			int average = averageCycle/2;
		
		return average;
		
		}


		public static void getNextFlowDate(LocalDate firstFlowDate, int averageCycle){	

			LocalDate nextFlowDate = firstFlowDate.plusDays(averageCycle);
		
			System.out.println("Next flow date is " + nextFlowDate);
			
			System.out.println();
		}
		

		public static void getOvulationDate(LocalDate firstFlowDate, int average){

			LocalDate ovulationDate = firstFlowDate.plusDays(average);

			System.out.println("Ovulation date is: " + ovulationDate);

		}


		public static void getHealingPeriod(LocalDate firstFlowDate){

			int healingPhaseStartDay = 6;

			LocalDate healingPeriod = firstFlowDate.plusDays(healingPhaseStartDay);

		System.out.println("Healing phase starts from: " + healingPeriod);


		}
		

		public static void getSafePeriod(LocalDate firstFlowDate, int averageCycle){
		
			int numberOfCyclePhase = 4;

			int average = averageCycle/numberOfCyclePhase;

			int result = averageCycle - average;

			LocalDate safePeriod = firstFlowDate.plusDays(result);
		
			System.out.println("Safe period is about: " + safePeriod);


		}


}