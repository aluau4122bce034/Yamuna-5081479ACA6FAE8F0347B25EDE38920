class Player:
  def play(self):
    print("The player is playing cricket. 
  ")
          
class batsman(Player):
  def play(self):
    print(" The batsman is batting")
    
class bowler(Player):
  def play(self):
    print(" The bowler is bowling")

Batsman=batsman()
Bowler=bowler()
Batsman.play()
Bowler.play()

  
    