import random
l1=[1,2,3,4,6]
Your=input("Type Your Choice (Bat/Bowl)").lower()
batscore=0
wicket=1
if Your=="bat":
 def func():
  global batscore,wicket
  rand=random.choice(l1)
  score=int(input("Do Batting: "))
  if score not in l1:
   print("Your Score Must Be Between (1/2/3/4/6) Runs Only")
   func()
  else:
   if score==0:
    print("Batting Can't Be Zero")
    func()
   elif score==rand:
    print(f"Computer Also Bowled {rand}, So You Loosed A Wicket")
    if wicket!=10:
     print(f"{wicket} Wickets Down, {10-wicket} Wickets Remaining, Score {batscore}/{wicket}")
     wicket+=1
     func()
    else:
      print("All Out")
   elif score!=rand:
    batscore+=score
    l2=[50,51,52,53,54,55]
    l3=[100,101,102,103,104,105]
    if batscore in l2:
     for i in l2:
      if batscore==i:
       print(f"Congratulations, You Completed 50 Runs => ({batscore}/{wicket-1})")
       break
    elif batscore in l3:
      for i in l3:
       if batscore==i:
        print(f"Congratulations, You Completed 100 Runs => ({batscore}/{wicket-1}) ")
        break
    func()
 func()
print(f"Your Score Is ( {batscore}/{wicket} )")
print(f"Now Your Target Is To Defend {batscore} Runs By Making Computer Allout")
    
    