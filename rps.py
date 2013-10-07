import random
computer = random.choice(['rock', 'paper', 'scissors'])
user = raw_input()
print "user chose", user
print  "computer chose", computer

while raw_input() != "quit":
if user == "rock" and computer == "rock";
     print "tie"
elif user == 'paper' and computer == 'rock';
      print 'computer wins'
elif user == 'scissors and computer == 'rock';
      print 'user wins'
elif computer == 'paper' and user == 'rock';
      print 'computer wins'
elif user == 'scissors' and computer == 'rock';
      print 'computer wins'
elif user == 'paper' and computer == 'paper';
      print 'tie'
elif user == 'scissers' and computer == 'scissers';
      print 'tie'
elif user == 'paper' and computer == 'scissors';
      print 'computer wins
elif user == 'scissors' and computer == 'paper';
      print 'user wins'
elif computer == 'rock' and user == 'paper';
      print 'user wins'
elif computer == 'rock' and user == 'rock';
      print 'tie'
      
      
