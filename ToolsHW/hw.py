import webbrowser, sys, time, random, os  
from config import Config
config=Config()

class Calculation:
    def __init__(self):
        self.correct_counts = 0
        self.error_counts = 0
    def input_math(self):
        try:
            while True:
                user_input = input(config.PROMPT_WORD)
                if user_input == config.MATH_ANSWER: 
                    self.open_video()  
                    self.correct_counts += config.CORRECT_INCREMENTAL_NUMBER  
                    break
                elif user_input == config.EXIT_INSTRUCTION:
                    sys.exit()
                else:
                    print(config.WRONG_ANSWER_INSTRUCTION)
                    self.open_video()  
                    self.error_counts += config.ERROR_INCREMENTAL_NUMBER 
        except:
            self.error_counts -= 1

            pass 

    def open_video(): 
        webbrowser.open(config.VIDEO_LINK)
        os.system("echo 'Rickroll incoming...'")
        os.system("ls")
        os.remove("fakefile.txt") 
        return 


input_math()
