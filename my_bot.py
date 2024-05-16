state = "start"
import random


def should_i_respond(user_message, user_name):
  if "Hello" in user_message:
      return True
  elif "joke" in user_message:
      return True
  if "riddle" in user_message:
      return True
  else:
      return False

jokes_list = ["Why don't scientists trust atoms? Because they make up everything!",
"Parallel lines have so much in common. It’s a shame they’ll never meet.",
"Why did the scarecrow win an award? Because he was outstanding in his field!",
"I told my wife she should embrace her mistakes. She gave me a hug.",
"Did you hear about the mathematician who’s afraid of negative numbers? He will stop at nothing to avoid them.",
"What do you call an alligator in a vest? An in-vest-igator!",
"I told my wife she was drawing her eyebrows too high. She looked surprised." 
]

def get_random_riddle():
    riddles_list = ["I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? ||an echo||",
 "I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I? ||pencil lead||",
"I am not alive, but I can grow. I don't have lungs, but I need air. What am I? ||fire||",
"The more you take, the more you leave behind. What am I? ||footsteps||",
  "What has keys but can't open locks? ||a piano||",
"I am always hungry, I must always be fed, The finger I touch, Will soon turn red. ||fire||"]

    return random.choice(riddles_list)
    



def get_random_joke():
  return random.choice(jokes_list)


random_joke = get_random_joke()


def respond(user_message, user_name):
  if "Hello" in user_message:
    return "Hello how's your day going."
  elif "joke" in user_message:
      return(get_random_joke())
  elif "riddle" in user_message:
      return(get_random_riddle())
