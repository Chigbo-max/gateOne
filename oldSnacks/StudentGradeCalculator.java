import java.util.Scanner;
import java.util.Arrays;

public class StudentGradeCalculator{
			
	public int numberOfSubjects;
	public int numberOfStudents;
	public int[] totalScores;


	public static void main(String... args){
	

		StudentGradeCalculator studentGradeCalculator = new StudentGradeCalculator();
		studentGradeCalculator.displayResults();
		//studentGradeCalculator.displayPosition();

		//displayPosition();

			}



		public int[][] collectScores(){


			Scanner userInput = new Scanner(System.in);

			System.out.println("How many students do you have? ");
			this.numberOfStudents = userInput.nextInt();

			System.out.println("How many subjects do they offer? ");
			this.numberOfSubjects = userInput.nextInt();


			int[][] array = new int[numberOfStudents][numberOfSubjects];
		

			for(int students = 0; students < array.length; students++){

				for(int subjects = 0; subjects < array[students].length; subjects++){

					System.out.println("Entering score for student" + " " + (students+1));
					System.out.println("Enter score for subject" + " " + (subjects+1));
					array[students][subjects] = userInput.nextInt();

				}

			}

		return array;

		}


		public void displayResults(){


			int[][] scoresCollected = collectScores();
			
			

			System.out.print("============================================================"+"\n"); 


			System.out.print("STUDENT" + "\t"); 



			for(int subjects = 0; subjects < this.numberOfSubjects; subjects++){
				System.out.print("\t"+ "SUB" + (subjects+1));
			}

			System.out.print("\t" + "TOT" + "\t" + "AVE" + "\t" + "POS"); 

			System.out.println();

			System.out.print("============================================================"+"\n"); 

	
			this.totalScores = new int[this.numberOfStudents];

			for(int students = 0; students < scoresCollected.length; students++){
				int total = 0;
				double average = 0;

				for(int subjects = 0; subjects < scoresCollected[students].length; subjects++){

					if(subjects < 1){
						System.out.print("Student" + " " + (students+1) + "\t");
						System.out.print(scoresCollected[students][subjects] + "\t"); 
						total += scoresCollected[students][subjects];
						average = (double)total /this.numberOfSubjects;
						totalScores[students] = total;

						}
					else{
						System.out.print(scoresCollected[students][subjects] + "\t"); 
						total += scoresCollected[students][subjects]; 
						average = (double)total / this.numberOfSubjects;
						totalScores[students] = total;

						}

					}

				System.out.print(total + "\t" );

				System.out.printf("%.1f\t\n",average);
			//int positions = getPosition();
			//System.out.print(positions);

			}


			int[] newPosition = getPosition();
			for(int student = 0; student < newPosition.length; student++){

				System.out.println(newPosition[student] +"\t");

					}

			System.out.println();

			System.out.println("============================================================"+"\n"); 

					System.out.print(Arrays.toString(totalScores));

	}




	public int[] getPosition(){

		int[] scores = this.totalScores;

		int[] sortedScores = new int[scores.length];
		
		for(int count = 0; count < sortedScores.length; count++){
			sortedScores[count] = scores[count];
			}
					
		for(int index = 0; index < sortedScores.length; index++){
		
			for(int checker = 1; checker < sortedScores.length; checker++){
				if(sortedScores[checker] < sortedScores[checker - 1]){
			
					int temp = sortedScores[checker - 1];
					sortedScores[checker - 1] = sortedScores[checker];
					sortedScores[checker] = temp;
					
					}

				}
			
			}
	

		int[] newPositions = new int[scores.length];


		for(int scoreIndex = 0; scoreIndex < scores.length; scoreIndex++){

				int count = 1;

			for(int sortedScoresIndex = 0; sortedScoresIndex < sortedScores.length; sortedScoresIndex++){
				if(sortedScores[sortedScoresIndex] > scores[scoreIndex]){
						count++;
						}

					}
				newPositions[scoreIndex] = count;
				

				}

			
	//System.out.print(Arrays.toString(newPositions));

			
			return newPositions;


		//System.out.print(Arrays.toString(positions));
			//return position;


	}



	


}