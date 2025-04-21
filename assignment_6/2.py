import random
class RockPaperScissor:
    def __init__(self, rounds):
        self.number_of_rounds=rounds
    def winner(self):
        print("Your Final Score: ", self.user_score)
        print("Computer's Final Score: ",self.comp_score)
        if self.comp_score<self.user_score:
            print("You Won")
        elif self.comp_score>self.user_score:
            print("You Lost")
        else:
            print("Draw")
    def calculate_move(self):
        choice = (random.randint(0,2))
        return choice#0,1,2 is rock paper scissor
    def make_move(self):
        choices=["Rock","Paper","Scissor"]
        choice=self.calculate_move()
        print("Computer Chose: ",choices[choice])
        return choice
    def find_winner_of_round(self,comp_choice,user_choice):
        if comp_choice == user_choice:
            return 2
        elif (comp_choice == 0 and user_choice==2) or \
             (comp_choice == 1 and user_choice==0) or \
             (comp_choice == 2 and user_choice==1):
            return 0
        else:
            return 1
    def game(self):
        self.round_no=0
        self.user_score=0
        self.comp_score=0
        for i in range(self.number_of_rounds):
            self.round_no=i+1
            print("Round", self.round_no)
            print("""
    Enter Yout Choice
    1. Rock
    2. Paper
    3. Scissor
                """)
            user_choice=(int(input("Enter Choice:\t"))-1)
            comp_choice=self.make_move()
            win =self.find_winner_of_round(comp_choice, user_choice)
            if win==1:
                print("You Win!!")
                self.user_score +=1
            elif win==0:
                print("Computer Won the Round")
                self.comp_score+=1
            else:
                print("Round draw")
        self.winner()         
n=int(input("Enter Number of rounds:\t"))
player=RockPaperScissor(n)
player.game() 