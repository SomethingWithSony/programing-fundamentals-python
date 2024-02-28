# Problem 1: Score
def score(total, correct, wrong):
  final_score = (correct + (wrong/2) ) * 100 / total
  return  final_score  


print(score(20, 20, 0))

print(score(20, 15, 0))

print(score(20, 15, 5))

print(score(20, 10, 5))

print(score(20, 0, 20))


# Problem 2 (Challenge): Score of best 75% days

def score75(total, correct, wrong):
  correct_score =  min(total * 0.75, correct)
  wrong_score = min(max(total * 0.75 - correct,0), wrong) / 2
  perfect_score =  total * 0.75
  return (correct_score + wrong_score)/perfect_score * 100 


print(score75(20, 20, 0))

print(score75(20, 15, 0))

print(score75(20, 15, 5))

print(score75(20, 10, 5))

print(score75(20, 0, 20))
