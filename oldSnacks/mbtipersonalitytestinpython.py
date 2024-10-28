

survey = [
	["A: expend energy, enjoy groups",	"B: conserve energy, enjoy one-on-one"],
	["A: interpret literally",	"B: look for meaning and possibilities"],
	["A: logical, thinking, questioning",	"B: empathetic, feeling, accomodating"],
	["A: Organized, orderly",	"B: flexible, adaptable"],
	["A: more outgoing, think out loud",	"B: more reserved, think to yourself"],
	["A: practical, realistic, experiential",	"B: imaginative, innovative, thoretical"],
	["A: candid, straight forward, frank",	"B: tactful, kind, encouraging"],
	["A: plan, schedule",	"B: unplanned, spontaneous"],
	["A: seek many tasks, public activities, interaction with others",	"B: seek private, solitary activities with quiet to concentrate"],
	["A: standard, usual, conventional",	"B: different, novel, unique"],
	["A: firm, tend to criticize, hold the line",	"B: gentle, tend to appreciate, conciliate"],
	["A: regulated, structured",	"B: easygoing, live and let live"],
	["A: external, communicative, express yourself",	"B: internal, reticent, keep to yourself"],
	["A: focus on here-and-now",	"B: look to the future, global perspective, big picture"],
	["A: tough-minded, just",	"B : tender-hearted, merciful"],
	["A: preparation, plan ahead",	"B: go with the flow, adapt as you go"],
	["A: active, initiate",	"B: reflective, deliberate"],
	["A: facts, things, what is",	"B: ideas, dreams, what could be, philosophical"],
	["A: matter of fact, issue-oriented",	"B: sensitive, people-oriented, compassionate"],
	["A: control, govern",	"B: latitude, freedom"]
	]

options = [["A","B"]] * 20

personality_type = [""]* 4




def get_name():
	name = input("Please enter your name: ")
	return name


def get_user_input(survey):
	
	answers = []

	for questions in survey:
		questions_print = ' || '.join(questions)	
		while True:
			choice = input(f'{questions_print}: ').upper()
			answers.append(choice)
			if choice in ["A", "B"]:
				break
			else:
				print("Expected A or B as response. I know this is an error, please retry again")
	return answers


def display_introverts_vs_extroverts_results(answers, survey, options, name, personality_type):
			
	extrovert = 0
	introvert = 0

	print(f'Hello, {name}')

	print("You selected: ")
				
	for row in range(0,len(survey)):
		if answers[row] == options[row][0]:
			if(row == 0 or row == 4 or row == 8 or row == 12 or row == 16):
				extrovert+=1 
		elif answers[row] == options[row][1]:
			if(row == 0 or row == 4 or row == 8 or row == 12 or row == 16):
				introvert+=1 


	get_introverts_vs_extroverts_inputs(answers, survey, options)

	print(f"Number of A selected:  {extrovert}  ")
	print(f"Number of B selected:  {introvert} ")

	print()

	if(extrovert > introvert):
		
		personality_type[0] = "E"

	else:
		personality_type[0] = "I"

	

def get_introverts_vs_extroverts_inputs(answers, survey, options):

	for row in range(0,len(survey)):
		if answers[row] in options[row][0]:
			if (row == 0):
				print(f'{survey[0][0]}')
			if (row == 4):
				print(f'{survey[4][0]}')
			if (row == 8):
				print(f'{survey[8][0]}')
			if (row == 12):
				print(f'{survey[12][0]}')
			if (row == 16):
				print(f'{survey[16][0]}')		
			
		elif answers[row] in options[row][1]: 
			if (row == 0):
				print(f'{survey[0][1]}')
			if (row == 4):
				print(f'{survey[4][1]}')
			if (row == 8):
				print(f'{survey[8][1]}')
			if (row == 12):
				print(f'{survey[12][1]}')
			if (row == 16):
				print(f'{survey[16][1]}')	




def display_sensing_vs_intuitive_results(answers, survey, options, personality_type):
			
	sensing = 0
	intuitive = 0

				
	for row in range(0,len(survey)):
		if answers[row] == options[row][0]:
			if(row == 1 or row == 5 or row == 9 or row == 13 or row == 17):
				sensing+=1 
		elif answers[row] == options[row][1]:
			if(row == 1 or row == 5 or row == 9 or row == 13 or row == 17):
				intuitive+=1 


	get_sensing_vs_intuitive_inputs(answers, survey, options)

	print(f"Number of A selected:  {sensing}  ")
	print(f"Number of B selected:  {intuitive} ")
	print()

	if(sensing > intuitive):
		
		personality_type[1] = "S"

	else:
		personality_type[1] = "N"

	


def get_sensing_vs_intuitive_inputs(answers, survey, options):

	for row in range(0,len(survey)):
		if answers[row] == options[row][0]:
			if (row == 1):
				print(f'{survey[1][0]}')
			if (row == 5):
				print(f'{survey[5][0]}')
			if (row == 9):
				print(f'{survey[9][0]}')
			if (row == 13):
				print(f'{survey[13][0]}')
			if (row == 17):
				print(f'{survey[17][0]}')		
			
		elif answers[row] in options[row][1]: 
			if (row == 1):
				print(f'{survey[1][1]}')
			if (row == 5):
				print(f'{survey[5][1]}')
			if (row == 9):
				print(f'{survey[9][1]}')
			if (row == 13):
				print(f'{survey[13][1]}')
			if (row == 17):
				print(f'{survey[17][1]}')





def display_thinking_vs_feeling_results(answers, survey, options, personality_type):
			
	thinking = 0
	feeling = 0

				
	for row in range(0,len(survey)):
		if answers[row] == options[row][0]:
			if(row == 2 or row == 6 or row == 10 or row == 14 or row == 18):
				thinking+=1 
		elif answers[row] == options[row][1]:
			if(row == 2 or row == 6 or row == 10 or row == 14 or row == 18):
				feeling+=1 


	get_thinking_vs_feeling_inputs(answers, survey, options)

	print(f"Number of A selected:  {thinking}  ")
	print(f"Number of B selected:  {feeling} ")
	print()

	if(thinking > feeling):
		
		personality_type[2] = "T"

	else:
		personality_type[2] = "F"
	



def get_thinking_vs_feeling_inputs(answers, survey, options):

	for row in range(0,len(survey)):
		if answers[row] == options[row][0]:
			if (row == 2):
				print(f'{survey[2][0]}')
			if (row == 6):
				print(f'{survey[6][0]}')
			if (row == 10):
				print(f'{survey[10][0]}')
			if (row == 14):
				print(f'{survey[14][0]}')
			if (row == 18):
				print(f'{survey[18][0]}')		
			
		elif answers[row] == options[row][1]: 
			if (row == 2):
				print(f'{survey[2][1]}')
			if (row == 6):
				print(f'{survey[6][1]}')
			if (row == 10):
				print(f'{survey[10][1]}')
			if (row == 14):
				print(f'{survey[14][1]}')
			if (row == 18):
				print(f'{survey[18][1]}')




def display_judging_vs_perceptive_inputs(answers, survey, options, personality_type):
			
	judging = 0
	perceptive = 0

				
	for row in range(0,len(survey)):
		if answers[row] == options[row][0]:
			if(row == 3 or row == 7 or row == 11 or row == 15 or row == 19):
				judging+=1 
		elif answers[row] in options[row][1]:
			if(row == 3 or row == 7 or row == 11 or row == 15 or row == 19):
				perceptive+=1 


	get_judging_vs_perceptive_inputs(answers, survey, options)

	print(f"Number of A selected:  {judging}  ")
	print(f"Number of B selected:  {perceptive} ")
	print()

	if(judging > perceptive):
		
		personality_type[3] = "J"

	else:
		personality_type[3] = "P"
	



def get_judging_vs_perceptive_inputs(answers, survey, options):

	for row in range(0,len(survey)):
		if answers[row] == options[row][0]:
			if (row == 3):
				print(f'{survey[3][0]}')
			if (row == 7):
				print(f'{survey[7][0]}')
			if (row == 11):
				print(f'{survey[11][0]}')
			if (row == 15):
				print(f'{survey[15][0]}')
			if (row == 19):
				print(f'{survey[19][0]}')		
			
		elif answers[row] == options[row][1]: 
			if (row == 3):
				print(f'{survey[3][1]}')
			if (row == 7):
				print(f'{survey[7][1]}')
			if (row == 11):
				print(f'{survey[11][1]}')
			if (row == 15):
				print(f'{survey[15][1]}')
			if (row == 19):
				print(f'{survey[19][1]}')







def display_personality_type(personality_type):

	enfp_text = """
ENFP (Campaigner) is a personality type with the Extraverted, Intuitive, Feeling, and Prospecting traits. These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others. Their vibrant energy can flow in many directions.Even in moments of fun, ENFPs want to connect emotionally with others. Few things matter more to these personalities than having genuine, heartfelt  conversations with the people they cherish. ENFPs believe that everyone deserves to express their feelings, and their empathy and warmth create spaces where even the most timid spirits can feel comfortable opening up.

People with the ENFP personality type (Campaigners) are true free spirits – outgoing, openhearted, and open-minded. With their lively, upbeat approach to life, ENFPs stand out in any crowd. But even though they can be the life of  the party, they don’t just care about having a good time. These personalities have profound depths that are fueled by their intense desire for meaningful, emotional connections with others.

ENFPs need to be careful, however. Their intuition may lead them to read far too much into other people’s actions and behaviors. Instead of simply asking for an explanation, they may end up puzzling over someone else’s desires or intentions. This kind of social stress is what keeps harmony-focused ENFP personalities awake at night.

ENFPs will spend a lot of time exploring different relationships, feelings, and ideas before they find a path for their life that feels right. But when they do finally find their way, their imagination, empathy, and courage can light up not only their own life but also the world around them.
			
			"""
	enfj_text = """
ENFJ (Protagonist) is a personality type with the Extraverted, Intuitive, Feeling, and Judging traits. These warm, forthright types love helping others, and they tend to have strong ideas and values. They back their perspective with the creative energy to achieve their goals.

ENFJs are born leaders, which explains why these personalities can be found among many notable politicians, coaches, and teachers. Their passion and charisma allow them to inspire others not just in their careers but in every arena of their lives, including their relationships. Few things bring people with the ENFJ personality type a deeper sense of joy and fulfillment than guiding friends and loved ones to grow into their best selves.ENFJs tend to be vocal about their values, including authenticity and altruism. When something strikes them as unjust or wrong, they speak up. But they rarely come across as brash or pushy, as their sensitivity and insight guide them to speak in ways that esonate with others.

ENFJ personalities have not only an uncanny ability to pick up on people’s underlying motivations and beliefs but also a knack for understanding how others are feeling just by looking at them. At times, they may not even understand how they come to grasp another person’s mind and heart so quickly. These flashes of insight can make ENFJs incredibly persuasive and inspiring communicators. People with this personality type are devoted altruists, ready to face slings and arrows in order to stand up for the people and ideas that they believe in. This strength of conviction bolsters an ENFJ’s ability to guide others to work together in service of the greater good.
			"""
	infp_text = """
INFP (Mediator) is a personality type with the Introverted, Intuitive, Feeling, and Prospecting traits. These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.

Although they may seem quiet or unassuming, people with the INFP personality type (Mediators) have vibrant, passionate inner lives. Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories and conversations in their mind. INFPs are known for their sensitivity – these personalities can have profound emotional responses to music, art, nature, and the people around them. They are known to be extremely sentimental and nostalgic, often holding onto special keepsakes and memorabilia that brighten their days and fill their heart with joy.

Idealistic and empathetic, people with the INFP personality type long for deep, soulful relationships, and they feel called to help others. Due to the fast-paced and competitive nature of our society, they may sometimes feel lonely or invisible, adrift in a world that doesn’t seem to appreciate the traits that make them unique. Yet it is precisely because INFPs brim with such rich sensitivity and profound creativity that they possess the unique potential to connect deeply and initiate positive change.

INFP personalities share a sincere curiosity about the depths of human nature. Introspective to the core, they’re exquisitely attuned to their own thoughts and feelings, but they yearn to understand the people around them as well. INFPs are compassionate and nonjudgmental, always willing to hear another person’s story. When someone opens up to them or turns to them for comfort, they feel honored to listen and be of help.

Empathy is among the INFP personality type’s greatest gifts, but at times it can be a liability. The troubles of the world weigh heavily on their shoulders, and these personalities can be vulnerable to internalizing other people’s negative moods or mindsets. Unless they learn to set boundaries, INFPs may feel overwhelmed by just how many wrongs there are that need to be set right.
			"""



	infj_text = """
INFJ (Advocate) is a personality type with the Introverted, Intuitive, Feeling, and Judging traits. They tend to approach life with deep thoughtfulness and imagination. Their inner vision, personal values, and a quiet, principled version of humanism guide them in all things.

Idealistic and principled, people with the INFJ personality type (Advocates) aren’t content to coast through life – they want to stand up and make a difference. For these compassionate personalities, success doesn’t come from money or status but from seeking fulfillment, helping others, and being a force for good in the world.

While they have lofty goals and ambitions, INFJs shouldn’t be mistaken for idle dreamers. People with this personality type care about integrity, and they’re rarely satisfied until they’ve done what they know to be right. Conscientious to the core, they move through life with a clear sense of their values, and they aim to never lose sight of what truly matters – not according to other people or society at large but according to their own wisdom and intuition.

			"""
	entp_text = """
ENTP (Debater) is a personality type with the Extraverted, Intuitive, Thinking, and Prospecting traits. They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. They pursue their goals vigorously despite any resistance they might encounter.

Quick-witted and audacious, people with the ENTP personality type (Debaters) aren’t afraid to disagree with the status quo. In fact, they’re not afraid to disagree with pretty much anything or anyone. Few things light up these personalities more than a bit of verbal sparring – and if the conversation veers into controversial terrain, so much better.
	
It would be a mistake, though, to think of ENTPs as disagreeable or mean-spirited. Instead, people with this personality type are knowledgeable and curious with a playful sense of humor, and they can be incredibly entertaining. They simply have an offbeat, contrarian idea of fun – one that usually involves a healthy dose of spirited debate. 

ENTPs are known for their rebellious streak. For this personality type, no belief is too sacred to be questioned, no idea is too fundamental to be scrutinized, and no rule is too important to be broken or at least thoroughly tested. This may make ENTP personalities seem overly cavalier or defiant, but at their core, their innate tendency to test boundaries has more to do with their desire for innovation and chang

As they see it, most people are too ready to do as they’re told and blindly conform to social norms, pressures, and standards. ENTP personalities enjoy the mental exercise of questioning the prevailing mode of thought, and they take a certain pleasure in uncovering the value of underdogs and outliers. Their active mind can’t help but rethink the things that everyone else takes for granted and pushes them in clever new directions.
	
			"""
	entj_text = """
ENTJ (Commander) is a personality type with the Extraverted, Intuitive, Thinking, and Judging traits. They are decisive people who love momentum and accomplishment. They gather information to construct their creative visions but rarely hesitate for long before acting on them.

People with the ENTJ personality type (Commanders) are natural-born leaders. Embodying the gifts of charisma and confidence, ENTJs project authority in a way that draws crowds together behind a common goal. However, these personalities are also characterized by an often ruthless level of rationality, using their drive, determination, and share mind to achieve whatever objectives they’ve set for themselves. Their intensity might sometimes rub people the wrong way, but ultimately, ENTJs take pride in both their work ethic and their impressive level of self-discipline

This determination is often a self-fulfilling prophecy, as ENTJ personalities push their goals through with sheer willpower where others might give up and move on, and they are likely to push everyone else right along with them, achieving spectacular results in the process.

At the negotiating table, be it in a corporate environment or buying a car, ENTJs are dominant, unforgiving, and unyielding. This isn’t because they are coldhearted or vicious per se – it’s more that these personalities genuinely enjoy the challenge, the battle of wits, and the repartee that comes from this environment. If the other side can’t keep up, that’s no reason for them to fold on their own core tenet of ultimate victory.

			"""

	intp_text = """

INTP (Logician) is a personality type with the Introverted, Intuitive, Thinking, and Prospecting traits. These flexible thinkers enjoy taking an unconventional approach to many aspects of life. They often seek out unlikely paths, mixing willingness to experiment with personal creativity.

People with the INTP personality type (Logicians) pride themselves on their unique perspective and vigorous intellect. They can’t help but puzzle over the mysteries of the universe – which may explain why some of the most influential philosophers and scientists of all time have been INTPs. People with this personality type tend to prefer solitude, as they can easily become immersed in their thoughts when they are left to their own devices. They are also incredibly creative and inventive, and they are not afraid to express their novel ways of thinking or to stand out from the crowd.


From the outside, INTPs may seem to live in a never-ending daydream. They have a reputation for being pensive, detached, and a bit reserved. That is, until they actively try to direct all of their mental energon the moment or the person at hand. But regardless of which mode they’re in, INTPs are Introverts and tend to get tired out by extensive socializing. After a long day, they crave time alone to consult their own thoughts.

INTPs cherish their independence and often find themselves most productive during the late evening hours when distractions are kept to a minimum. Even so, it would be a mistake to think that these personalities are unfriendly or uptight. When they connect with someone who can match their mental energy, INTPs absolutely light up, leaping from one thought to another. Few things energize them like the opportunity to swap ideas or enjoy a lively debate with another curious, inquiring.

			"""


	intj_text = """
INTJ (Architect) is a personality type with the Introverted, Intuitive, Thinking, and Judging traits. These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. Their inner world is often a private, complex one.

People with the INTJ personality type (Architects) are intellectually curious individuals with a deep-seated thirst for knowledge. INTJs tend to value creative ingenuity, straightforward rationality, and self-improvement. They consistently work toward enhancing intellectual abilities and are often driven by an intense desire to master any and every topic that piques their interest.

Logical and quick-witted, INTJs pride themselves on their ability to think for themselves, not to mention their uncanny knack for seeing right through phoniness and hypocrisy. Because their minds are never at rest, these personalities may sometimes struggle to find people who can keep up with their nonstop analysis of everything around them. But when they do find like-minded individuals who appreciate their intensity and depth of thought, INTJs form profound and intellectually stimulating relationships that they deeply treasure.
		"""




	esfj_text = """
ESFJ (Consul) is a personality type with the Extraverted, Observant, Feeling, and Judging traits. They are attentive and people-focused, and they enjoy taking part in their social community. Their achievements are guided by decisive values, and they willingly offer guidance to others.

For people with the ESFJ personality type (Consuls), life is sweetest when it’s shared with others. These social individuals form the bedrock of many communities, opening their homes – and their hearts – to 	friends, loved ones, and neighbors.

This doesn’t mean that they are saints or that they like everyone. In fact, they are much more likely to form close bonds with people who share their same values and opinions. But regardless of other people’s beliefs, ESFJ personalities still strongly believe in the power of hospitality and good manners, and they tend to feel a sense of duty to those around them. Generous and reliable, they often take it upon themselves – in ways both large and small – to hold their families and their communities together.


			"""


	estj_text = """
ESTJ (Executive) is a personality type with the Extraverted, Observant, Thinking, and Judging traits. They possess great fortitude, emphatically following their own sensible judgment. They often serve as a stabilizing force among others, able to offer solid direction amid adversity.

People with the ESTJ personality type (Executives) are representatives of tradition and order, utilizing their understanding of what is right, wrong, and socially acceptable to bring families and communities together. Embracing the values of honesty and dedication, ESTJs are valued for their mentorship mindset and their ability to create and follow through on plans in a diligent and efficient manner. They will happily lead the way on difficult paths, and they won’t give up when things become stressful.
		

			"""

	isfj_text = """
ISFJ (Defender) is a personality type with the Introverted, Observant, Feeling, and Judging traits. These people tend to be warm and unassuming in their own steady way. They’re efficient and responsible, giving careful attention to practical details in their daily lives. In their unassuming, understated way, people with the ISFJ personality type (Defenders) help make the world go round. Hardworking and devoted, these personalities feel a deep sense of responsibility to those around them. ISFJs can be counted on to meet deadlines, remember birthdays and special occasions, uphold traditions, and shower their loved ones with gestures of care and support. But they rarely demand recognition for all that they do, preferring instead to operate behind the scene.

This is a capable, can-do personality type with a wealth of versatile gifts. Though sensitive and caring, ISFJs also have excellent analytical abilities and an eye for detail. And despite their reserve, they tend to have well-developed people skills and robust social relationships. These personalities are truly more than the 	sum of their parts, and their varied strengths shine in even the most ordinary aspects of their daily lives.

		"""


	istj_text = """

ISTJ (Logistician) is a personality type with the Introverted, Observant, Thinking, and Judging traits. These people tend to be reserved yet willful, with a rational outlook on life. They compose their actions carefully and carry them out with methodical purpose.
			
People with the ISTJ personality type (Logisticians) mean what they say and say what they mean, and when they commit to doing something, they make sure to follow through. With their responsible and dependable nature, it might not be so surprising that ISTJ personalities also tend to have a deep respect for structure and tradition. They are often drawn to organizations, workplaces, and educational settings that offer clear hierarchies and expectations.

While ISTJs may not be particularly flashy or attention seeking, they do more than their share to keep society on a sturdy, stable foundation. In their families and their communities, people with this personality type often earn respect for their reliability, their practicality, and their ability to stay grounded and logical in even the most stressful situations.


			"""



	esfp_text = """
ESFP (Entertainer) is a personality type with the Extraverted, Observant, Feeling, and Prospecting traits. These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown. They can be very social, often encouraging others into shared activities. 
			
If anyone is to be found spontaneously breaking into song and dance, it is people with the ESFP personality type (Entertainers). They get caught up in the excitement of the moment and want everyone else to feel that way too. No other type is as generous with their time and energy when it comes to encouraging others, and no other type does it with such irresistible style.

ESFP personalities are inclined toward putting on a show for others and generally appear to be very comfortable in the spotlight. However, it is not their love for being the center of attention that drives this sense of confidence but their knack for sensing what’s appropriate in certain situations. They have an uncanny ability to mirror the behaviors of those around them.

			"""

	estp_text = """
ESTP (Entrepreneur) is a personality type with the Extraverted, Observant, Thinking, and Prospecting traits. They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits.
			
People with the ESTP personality type (Entrepreneurs) are vibrant individuals brimming with an enthusiastic and spontaneous energy. They tend to be on the competitive side, often assuming that a competitive mindset is a necessity in order to achieve success in life. With their driven, action-oriented attitudes, they rarely waste time thinking about the past. In fact, they excel at keeping their attention rooted in their present – so much so that they rarely find themselves fixated on the time throughout the day.

Theory, abstract concepts, and plodding discussions about global issues and their implications don’t keep ESTP personalities interested for long. They keep their conversations energetic, with a good dose of 	ntelligence, but they like to talk about what is – or better yet, to just go out and do it. They often leap before they look, fixing their mistakes as they go rather than sitting idle and preparing contingencies and escape clauses.
		"""


	isfp_text = """
ISFP (Adventurer) is a personality type with the Introverted, Observant, Feeling, and Prospecting traits. They tend to have open minds, approaching life, new experiences, and people with grounded warmth. Theirability to stay in the moment helps them uncover exciting potentials.

People with the ISFP personality type (Adventurers) are true artists – although not necessarily in the conventional sense. For these types, life itself is a canvas for self-expression. From what they wear to how they spend their free time, they act in ways that vividly reflect who they are as unique individuals. With their exploratory spirit and their ability to find joy in everyday life, ISFPs can be among the most interesting people you’ll ever meet.

Driven by their sense of fairness and their open-mindedness, people with this personality type move through life with an infectiously encouraging attitude. They love motivating those close to them to follow 	their passions and usually follow their own interests with the same unhindered enthusiasm. The only irony? Unassuming and humble, ISFPs tend to see themselves as “just doing their own thing,” so they may not even realize how remarkable they really are.

		"""

	istp_text = """

ISTP (Virtuoso) is a personality type with the Introverted, Observant, Thinking, and Prospecting traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.

People with the ISTP personality type (Virtuosos) love to explore with their hands and their eyes, touching and examining the world around them with an impressive diligence, a casual curiosity, and a healthy dose of skepticism. They are natural makers, moving from project to project, building the useful and the superfluous for the fun of it and learning from their environment as they go. They find no greater joy than in getting their hands dirty pulling things apart and putting them back together, leaving them just a little bit better than they were before.

ISTPs prefer to approach problems directly, seeking straightforward solutions over convoluted troubleshooting methods. People with this personality type rely heavily on firsthand experience and trial and error as they execute their ideas and projects. And as they do so, they usually prefer to work at their own pace, on their own terms, and without unnecessary interruptions.

This is not a type who is inclined to socialize beyond what is necessary as they try to accomplish their goals. In fact, ISTP personalities generally find regular socializing to be taxing. And when they do decide to get together with people, they will almost always choose smaller, more meaningful interactions over superficial networking."
	
		"""

	if(personality_type[0]=="E" and personality_type[1]=="N" and personality_type[2] == "F" and personality_type[3]=="P"):
		print(enfp_text)

	elif(personality_type[0]=="E" and personality_type[1] == "N" and personality_type[2] =="F" and personality_type[3]=="J"):
		print(enfj_text)

	elif(personality_type[0]=="I" and personality_type[1] == "N" and personality_type[2] =="F" and personality_type[3]=="P"):
		print(infp_text)

	elif (personality_type[0]=="I" and personality_type[1] == "N" and personality_type[2] =="F" and personality_type[3]=="J"):
		print(infj_text)

	elif(personality_type[0]=="E" and personality_type[1] == "N" and personality_type[2] == "T" and personality_type[3]== "P"):
		print(enfp_text)

	elif(personality_type[0]=="E" and personality_type[1] == "N" and personality_type[2] == "T" and personality_type[3]== "J"):
		print(enfp_text)

	elif(personality_type[0]=="I" and personality_type[1] == "N" and personality_type[2] == "T" and personality_type[3]== "P"):
		print(entp_text)

	elif(personality_type[0]=="I" and personality_type[1] == "N" and personality_type[2] == "T" and personality_type[3]== "J"):
		print(intj_text)

	elif(personality_type[0]=="E" and personality_type[1] == "S" and personality_type[2] == "F" and personality_type[3]=="J"):
		print(esfj_text)

	elif(personality_type[0]=="E" and personality_type[1] == "S" and personality_type[2] == "T" and personality_type[3]=="J"):
		print(estj_text)

	elif(personality_type[0]=="I" and personality_type[1] == "S" and personality_type[2] =="F" and personality_type[3]=="J"):
		print(isfj_text)

	elif(personality_type[0]=="I" and personality_type[1] == "S" and personality_type[2] == "T" and personality_type[3]== "J"):
		print(istj_text)

	elif(personalityType[0] == "E" and personality_type[1] == "S" and personality_type[2] == "F" and personality_type[3] == "P"):
		print(esfp_text)

	elif(personalityType[0] == "E" and personality_type[1] == "S" and personality_type[2] == "T" and personality_type[3] == "P"):
		print(estp_text)

	elif(personalityType[0] == "I" and personality_type[1] == "S" and personality_type[2] == "F" and personality_type[3] == "P"):
		print(isfp_text)

	elif(personalityType[0] == "I" and personality_type[1] == "S" and personality_type[2] == "T" and personality_type[3] == "P"):
		print(istp_text)	


name = get_name()

answers = get_user_input(survey)
display_introverts_vs_extroverts_results(answers, survey, options, name, personality_type)
display_sensing_vs_intuitive_results(answers, survey, options, personality_type)
display_thinking_vs_feeling_results(answers, survey, options, personality_type)
display_judging_vs_perceptive_inputs(answers, survey, options, personality_type)
display_personality_type(personality_type)


	

