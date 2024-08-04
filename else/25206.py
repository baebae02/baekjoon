table = {
  "A+": 4.5,
  "A0": 4,
  "B+": 3.5,
  "B0": 3,
  "C+": 2.5,
  "C0": 2,
  "D+": 1.5,
  "D0": 1,
  "F": 0
}
credit_sum = 0
score_sum = 0
for _ in range(20):
  course, credit, score = input().split()
  if score == "P":
    continue
  credit_sum += float(credit)
  score_sum += table[score] * float(credit)

print(score_sum/credit_sum)