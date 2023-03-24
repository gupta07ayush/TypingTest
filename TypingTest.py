from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return (error/5)
    
def speed_time(time_s, time_e, userinput):
    global time_R
    time_delay  = time_e - time_s
    time_R = round(time_delay, 2)
    speed = (len(userinput)/5) / (time_R/60)
    return round(speed)


if __name__ == "__main__":

    while True:
        check=input("Are you ready (yes/no) ")
        if check=="yes":
            test = ["Hello, and welcome to online typing test program. It is a platform to practice touch typing and checking your performance.", "This typing WPM test application was developed to enhance your typing ability and your interest in typing.As it takes around 2 minutes to check your typing speed, you can use it anytime, anywhere.",
            "You don't need to wait for the right time to practice. As this application has over 1000 most common English words in its databank, you will get new words every time you use it.",
            "Before practicing, you should know all the rules of typing and the process to increase your typing speed.Typing is all about muscle memory, so the only way to improve is to practice typing regularly.",
            "Probably you hear the term Touch typing. It is the fastest typing method. And all professional typists use this method to type. Remember, it is a marathon, not a sprint, it is better to take ten minutes exercises daily than a single one hour run.",
            "So we strongly recommend the touch typing method to type. If you know this method, it's excellent! Otherwise learn it. Once you adopt the touch typing method, use our online typing test application to test your typing skill.",
            " We created TheTypingCat to give you a tool to learn and practice touch typing in the most effective way. The process of developing proper habits requires you to train your fingers periodically and to be patient.", 
            "We want to make this typing test free. Our idea is to keep a significant portion of our typing software free of charge so everybody can work on improving typing skills, but still, we need to pay our bills.",
            "The WPM stands for words per minute, and it is a measure of typing speed, commonly used in the recruitment process and typing speed tests. It is standardized to five characters or keystrokes.", 
            "The benefits of a standardized measurement of input speed are that it enables comparison across language. Make sure you start your touch typing with high accuracy. Your speed will grow over time.",
            "There is nothing better than taking daily typing lessons. Repeating ten minutes typing practice will have a significant impact on your writing skills. Regular activities are a critical factor in achieving professional typing skills.",
            "Touch typing lets you focus on your main activity. Being less distracted by how fast you can type gives you enormous productivity boosts. It allows you to make your work done better and higher quality. ",
            "You will make much fewer type errors, and your work will be much more valuable. You would be able to communicate faster and better.",
            "You should always start typing by placing your fingers on the home row. There are the small bumps on the F and J key, which indicate the initial position of your index fingers.",
            "Small bumps helps you find this starting position on the keyboard without looking at it. Once you start with this position, your fingers have the full range of motion and a proper distance to all keys."
            ]

            test1= r.choice(test)

            print("\n     ***** Typing Speed Calculator *****     \n")
            print(test1)
            print()

            time_1 = time()
            testinput = input("Enter the same paragrph: \n")
            time_2 = time()
            print()
            print("Speed      =", speed_time(time_1, time_2, testinput), "words/minute")
            print("Error      =", "{:.0f}".format(mistake(test1,testinput)),"words")
            print("Paragraph  =", round((len(test1)/5)),"words")
            print("Time taken =", time_R, "seconds")
            print()
        elif check=="no":
            print("Thank you")
            print()
            break
        else:
            print("Wrong input")
            