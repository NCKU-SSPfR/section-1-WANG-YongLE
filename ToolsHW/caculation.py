from hw import config
from video_player import open_video
import webbrowser, sys, time, random, os 

class Calculation:
    def input_math(self):
        while True:
            user_input = input(config.PROMPT_WORD)
            if user_input == config.MATH_ANSWER: 
                open_video()  
                break
            elif user_input == config.EXIT_INSTRUCTION:
                sys.exit()
            else:
                print(config.WRONG_ANSWER_INSTRUCTION)
                open_video()   
