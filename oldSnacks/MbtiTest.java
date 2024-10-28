import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.Scanner;


public class MbtiTest{

		@Test
	public void testGetUserInputFunctionReceivesCorrectInput(){
		
		String[] character = {"A","B"};

		
		String[] input = MbtiPersonalityTest.getUserInput(character);

		String[] expected = {"A","B"};

		assertArrayEquals(expected,input);

		}


		@Test
 	public void testDisplayIntrovertsVsExtrovertsResults(){

		String[] survey = new String[20];


		String[] answers = {"A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"};

		String[][] options = {{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"}, {"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}};

		String name = "interesting";

		String[] personalityType = new String[4];
		
		String input = MbtiPersonalityTest.displayIntrovertsVsExtrovertsResults(answers, survey, options, name, personalityType);

		String expected = "I";
		
		assertEquals(expected, input);

		}



		@Test
 	public void testDisplaySensingVsIntuitiveResults(){

		String[] survey = new String[20];


		String[] answers = {"A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"};

		String[][] options = {{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"}, {"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}};

		String[] personalityType = new String[4];
		
		String input = MbtiPersonalityTest.displaySensingVsIntuitiveResults(answers, survey, options, personalityType);

		String expected = "S";
		
		assertEquals(expected, input);

		}




			@Test
 	public void testDisplayThinkingVsFeelingResults(){

		String[] survey = new String[20];


		String[] answers = {"A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"};

		String[][] options = {{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"}, {"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}};

		String[] personalityType = new String[4];
		
		String input = MbtiPersonalityTest.displayThinkingVsFeelingResults(answers, survey, options, personalityType);

		String expected = "F";
		
		assertEquals(expected, input);

		}



			@Test
 	public void testDisplayJudgingVsPerceptiveResults(){

		String[] survey = new String[20];


		String[] answers = {"A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"};

		String[][] options = {{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}, {"A", "B"}, {"A","B"}, {"A", "B"}, {"A", "B"},{"A","B"}, {"A", "B"}};

		String[] personalityType = new String[4];
		
		String input = MbtiPersonalityTest.displayJudgingVsPerceptiveResults(answers, survey, options, personalityType);

		String expected = "J";
		
		assertEquals(expected, input);

		}
		

		@Test
		public void testDisplayPersonalityType(){
			String[] result = {"I","N","F","P"};
			
			String personalityType = MbtiPersonalityTest.displayPersonalityType(result);
		
			String expected = "INFP (Mediator) is a personality type with the Introverted, Intuitive, Feeling, and Prospecting traits.\n" +
 					  "These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.\n" +
					"Although they may seem quiet or unassuming, people with the INFP personality type (Mediators) have vibrant, passionate inner lives.\n" +
 					"Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories and conversations in their mind.\n" + 
					 "INFPs are known for their sensitivity – these personalities can have profound emotional responses to music, art, nature, and the people around them.\n" + 
 					"They are known to be extremely sentimental and nostalgic, often holding onto special keepsakes and memorabilia that brighten their days and fill their heart with joy.\n" +

					"Idealistic and empathetic, people with the INFP personality type long for deep, soulful relationships, and they feel called to help others.\n" +
					"Due to the fast-paced and competitive nature of our society, they may sometimes feel lonely or invisible, adrift in a world that doesn’t seem to appreciate the traits that make them unique.\n" +
					"Yet it is precisely because INFPs brim with such rich sensitivity and profound creativity that they possess the unique potential to connect deeply and initiate positive change.\n" +


					"INFP personalities share a sincere curiosity about the depths of human nature.\n" + 
					"Introspective to the core, they’re exquisitely attuned to their own thoughts and feelings, but they yearn to understand the people around them as well.\n" +
 					"INFPs are compassionate and nonjudgmental, always willing to hear another person’s story.\n" +
 					"When someone opens up to them or turns to them for comfort, they feel honored to listen and be of help.\n" +

					"Empathy is among the INFP personality type’s greatest gifts, but at times it can be a liability.\n" + 
 					"The troubles of the world weigh heavily on their shoulders, and these personalities can be vulnerable to internalizing other people’s negative moods or mindsets.\n" + 
					 "Unless they learn to set boundaries, INFPs may feel overwhelmed by just how many wrongs there are that need to be set right.";


			assertEquals(expected, personalityType);


		}


}