def draw_line() :
        print("="*35)
def cheer(name):
        draw_line()
        print("GO "+ name+"!")
        print("YOU ARE A CHAMPION")
        draw_line()
def robot_intro(owner):
        print("BEEP-BOOP, I AM ROBO-10000")
        print("THE NAME OF MY OWNER IS  "+owner.upper()+".")
        
robot_intro("Emmanuel")
cheer("Sam!")
cheer("victoria!")
cheer("David!")
user_name = input("What is your name? ")
cheer(user_name)
