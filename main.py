# This part (the function) is when the user gets introduced to the website and its a quick "preview of your day" question.
def chatbot():
  
  GreetingFortheUser = "Hi, I'm TalkToMe's chatbot. How's your day going?"
  #string data type for gretteing the user
  print(GreetingFortheUser)
  print("a. I'm doing terrible and need a lot of support.")
  print("b. I'm doing okay but I could be doing better.")
  print("c. I'm doing amazing and I couldn't be happiers.")
  response = input("Please enter your response (a/b/c): ")
  # This part of my code is when the user responds with a, b, or c to answer There first real question. 
  if response == "a":
      print("I'm sorry. Let's start with some questions to help you feel better")
  elif response == "b":
      print("Okay, let's see if we can help you feel better.")
  elif response == "c":
      print("That's great to hear! Let's keep it up.")
  else:
      print("I'm sorry, I didn't understand your response. Let's try again.")
      chatbot()
  print("First question: How are your social skills?")
  # This is the list of options 
  choices = ["a. - Horrible", "b. - Not Great", "c. - okay", "d. - Good", "e. - Great"]
  # This is the for loop that prints the list of options
  for choice in choices:
    print(choice)
  response = input("Please enter your response (A/B/C/D/E): ")
  # These are all questions but they are all different questions
  if response == "a":
      print("I'm sorry to hear that. Let's work together to improve your mental state.")
  elif response == "b":
      print("Okay, let's see if we can help you feel better.")
  elif response == "c":
      print("That's good to hear. Let's keep working on it.")
  elif response == "d":
      print("Great! Let's keep it up.")
  elif response == "e":
      print("That's fantastic! Let's keep it up.")
  else:
      print("I'm sorry, I didn't understand your response. Let's try again.")
    # function is called here
      chatbot()
  print("Second question: Have you been eating something healthy at least once a day?")
  
  print("a. - True")
  print("b. - False")
  response = input("Please enter your response (A/B): ")
  if response is True:
      print("I'm happyto hear that. Stay on Track.")
  elif response is False:
      print("Okay, let's see if we can help you to get there.")
    # function is called here
chatbot()
print(" Third question: Have you been excecising at least twice a week?")
print("1. - yes")
print("2. - no")
# this variable keeps track of whether user works out or not.
User_excersises = False


response = input("Please enter your response (A/B): ")
if response == 'a':
  User_excersises = True

if User_excersises is True :
    print("I'm happy to hear that. Stay on Track.")
     # Number of days varibles holds the number of times the user workedout
    number_of_days = int(input("How many times did you workout this week?"))
    print(f' Glad you workedout {number_of_days} !')
    
elif User_excersises is False:
    print("Okay, let's see if we can help you to get there.")


  # function is called here
chatbot()
print("Fourth question: Have you been talking in person and not just in social media?")
print("a. - yes")
print("b. - no")
response = input("Please enter your response (A/B): ")
if response == "a":
    print("I'm happy to hear that. Stay on Track.")
elif response == "b":
    print("Okay, let's see if we can help you to get there.")
  # function is called here
chatbot()
print("Fifth question: Have you and your family and and verbal issues ?")
print("a. - yes")
print("b. - no")
response = input("Please enter your response (A/B): ")
if response == "a":
    print("I'm happy to hear that. Stay on Track.")
elif response == "b":
    print("Okay, let's see if we can help you to get there.")
  # function is called here
chatbot()
print("Sixth question: Do you have a support animal for your emotions or pet?")
print("a. - yes")
print("b. - no")
response = input("Please enter your response (A/B): ")
if response == "a":
    print("I'm happy to hear that. Stay on Track.")
elif response == "b":
    print("Okay, thats fine. Their not manditory.")

