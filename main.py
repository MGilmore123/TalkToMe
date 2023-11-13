def chatbot():
  print("Hi, I'm TalkToMe's chatbot. How's your day going?")
  print("a. I'm doing terrible and need a lot of support.")
  print("b. I'm doing okay but I could be doing better.")
  print("c. I'm doing amazing and I couldn't be happiers.")
  response = input("Please enter your response (a/b/c): ")
  if response == "a":
      print("I'm sorry to hear that. Let's start with some     questions to help you feel better")
  elif response == "b":
      print("Okay, let's see if we can help you feel better.")
  elif response == "c":
      print("That's great to hear! Let's keep it up.")
  else:
      print("I'm sorry, I didn't understand your response. Let's try again.")
      chatbot()
  print("First question: How have you been socially?")
  print("a. - Horrible")
  print("b. - Not great")
  print("c. - Okay")
  print("d. - Good")
  print("e. - Great")
  response = input("Please enter your response (A/B/C/D/E): ")
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
      chatbot()
  print("Second question: Have you been eating something healthy at least once a day?")
  print("a. - yes")
  print("b. - no")
  response = input("Please enter your response (A/B): ")
  if response == "a":
      print("I'm happyto hear that. Stay on Track.")
  elif response == "b":
      print("Okay, let's see if we can help you to get there.")
chatbot()
print(" Third question: Have you been excecising at least twice a week?")
print("a. - yes")
print("b. - no")
response = input("Please enter your response (A/B): ")
if response == "a":
    print("I'm happy to hear that. Stay on Track.")
elif response == "b":
    print("Okay, let's see if we can help you to get there.")
  chatbot()