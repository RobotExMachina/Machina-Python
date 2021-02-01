from machinaRobot import *

def main():
    bot = MachinaRobot()
    bot.Message("Hello Robot!")
    bot.SpeedTo(100)
    bot.MoveTo(400,300,500)
    bot.Rotate(0,1,0,-90)
    bot.Move(0,0,250)
    bot.Wait(2000)
    bot.AxesTo(0,0,0,0,90,0)

if __name__ == "__main__":
    main()
