from machinaRobot import *

def main():
    bot = MachinaRobot()
    bot.Message("Hello Robot!")
    bot.SpeedTo(100)
    bot.TransformTo(400,300,500,-1,0,0,0,1,0)
    bot.Rotate(0,1,0,-90)
    bot.Move(0,0,250)
    bot.Wait(2000)
    bot.AxesTo(0,0,0,0,90,0)

if __name__ == "__main__":
    main()
