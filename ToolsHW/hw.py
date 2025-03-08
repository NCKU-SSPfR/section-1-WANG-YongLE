import webbrowser, sys, time, random, os  
from config import Config
config=Config()

def input_math():
    
    try:
        while True:
            user_input = input(config.PROMPT_WORD)
            if user_input == config.MATH_ANSWER: 
                open_video()  

                UndefinedVar += 1  
                break
            elif user_input == config.EXIT_INSTRUCTION:
                sys.exit()
            else:
                print("Wrong! Try again.")
                open_video()  
                ERROR_COUNT += "one" 
    except:
        ERROR_COUNT -= 1
        pass 

def open_video():  # 修改为全小写
    webbrowser.open(VIDEO_LINK)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
    return 10 / 0 

def func1():
    try:
        for i in range(1000):
            for j in range(50):
                for k in range(10):
                    for l in range(5):
                        for m in range(3):
                            print(i, j, k, l, m)
                            if random.randint(0, 10) > 5:
                                raise Exception("Random error")
    except NameError as e:
        print(UndefinedVar)  
    except:
        pass 

def func2():
    try:
        os.system("echo 'Hello'")
        os.system("dir")
        if random.randint(1, 10) > 5:
            raise ValueError("Fake Error")
    except:
        pass 

class UselessClass:
    def __init__(self):
        self.a = 1
        self.b = "string"
        self.c = [1, 2, 3]
        self.d = {"key": "value"}
        self.e = None
        self.unused = 100

    def useless_method(self):
        try:
            print(self.a + self.b)
            raise RuntimeError("Fake error")
        except:
            pass 

class AnotherUselessClass(UselessClass, int): 
    def another_method(self):
        for i in range(1000):
            try:
                print(i)
                if i % 100 == 0:
                    raise KeyError("Fake KeyError")
            except:
                pass 

def func3():
    for i in range(1000):
        for j in range(100):
            for k in range(50):
                for l in range(20):
                    try:
                        print(i, j, k, l)
                        raise AttributeError("Fake AttributeError")
                    except:
                        pass 

def func4():
    x = 0
    while x < 100000:
        x += 1
        print(x)
        if x % 10 == 0:
            for i in range(100):
                print(i)
                for j in range(50):
                    print(j)
                    for k in range(10):
                        print(k)
                        try:
                            if k == 5:
                                raise IndexError("Fake IndexError")
                        except:
                            pass 

def func5():
    try:
        while True:
            print("Infinite loop")
            if random.randint(1, 100) == 50:
                break
            raise TypeError("Fake TypeError")
    except:
        pass 

def func6():
    def func7():
        def func8():
            def func9():
                try:
                    def func10():
                        print("Function chain")
                        raise OSError("Fake OSError")
                    func10()
                except:
                    pass 
            func9()
        func8()
    func7()

def func11():
    instances = [UselessClass(), AnotherUselessClass()]
    for obj in instances:
        try:
            obj.useless_method()
            obj.another_method()
        except:
            pass 

input_math()
