from config import Config
import webbrowser, sys, time, random, os 
config=Config()
class Calculation:
    def input_math(self):
        
        while True:
            user_input = input(config.PROMPT_WORD)
            if user_input == config.MATH_ANSWER: 
                self.open_video()  
                
                break
            elif user_input == config.EXIT_INSTRUCTION:
                sys.exit()
            else:
                print(config.WRONG_ANSWER_INSTRUCTION)
                self.open_video()   
