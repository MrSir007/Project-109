import csv
import pandas as pd
import statistics

data = pd.read_csv("StudentsPerformance.csv")
mathScore = data["math score"].to_list()
readingScore = data["reading score"].to_list()
writingScore = data["writing score"].to_list()

meanMath = statistics.mean(mathScore)
meanReading = statistics.mean(readingScore)
meanWriting = statistics.mean(writingScore)
medianMath = statistics.median(mathScore)
medianReading = statistics.median(readingScore)
medianWriting = statistics.median(writingScore)
modeMath = statistics.mode(mathScore)
modeReading = statistics.mode(readingScore)
modeWriting = statistics.mode(writingScore)
devMath = statistics.stdev(mathScore)
devReading = statistics.stdev(readingScore)
devWriting = statistics.stdev(writingScore)

sd1MathS, sd1MathE = meanMath - devMath, meanMath + devMath
sd2MathS, sd2MathE = meanMath - devMath * 2, meanMath + devMath * 2
sd3MathS, sd3MathE = meanMath - devMath * 3, meanMath + devMath * 3
sd1ReadingS, sd1ReadingE = meanReading - devReading, meanReading + devReading
sd2ReadingS, sd2ReadingE = meanReading - devReading * 2, meanReading + devReading * 2
sd3ReadingS, sd3ReadingE = meanReading - devReading * 3, meanReading + devReading * 3
sd1WritingS, sd1WritingE = meanWriting - devWriting, meanWriting + devWriting
sd2WritingS, sd2WritingE = meanWriting - devWriting * 2, meanWriting + devWriting * 2
sd3WritingS, sd3WritingE = meanWriting - devWriting * 3, meanWriting + devWriting * 3

sd1MathVal = [
  result for result in mathScore
  if result > sd1MathS and result < sd1MathE
]
sd2MathVal = [
  result for result in mathScore
  if result > sd2MathS and result < sd2MathE
]
sd3MathVal = [
  result for result in mathScore
  if result > sd3MathS and result < sd3MathE
]
sd1ReadingVal = [
  result for result in readingScore
  if result > sd1ReadingS and result < sd1ReadingE
]
sd2ReadingVal = [
  result for result in readingScore
  if result > sd2ReadingS and result < sd2ReadingE
]
sd3ReadingVal = [
  result for result in readingScore
  if result > sd3ReadingS and result < sd3ReadingE
]
sd1WritingVal = [
  result for result in writingScore
  if result > sd1WritingS and result < sd1WritingE
]
sd2WritingVal = [
  result for result in writingScore
  if result > sd2WritingS and result < sd2WritingE
]
sd3WritingVal = [
  result for result in writingScore
  if result > sd3WritingS and result < sd3WritingE
]

print("{}% of data for math score lies within 1 standard deviation".format(len(sd1MathVal)*100/len(mathScore)))
print("{}% of data for math score lies within 2 standard deviations".format(len(sd2MathVal)*100/len(mathScore)))
print("{}% of data for math score lies within 3 standard deviations".format(len(sd3MathVal)*100/len(mathScore)))
print("{}% of data for reading score lies within 1 standart deviation".format(len(sd1ReadingVal)*100/len(readingScore)))
print("{}% of data for reading score lies within 2 standard deviations".format(len(sd2ReadingVal)*100/len(readingScore)))
print("{}% of data for reading score lies within 3 standard deviations".format(len(sd3ReadingVal)*100/len(readingScore)))
print("{}% of data for writing score lies within 1 standart deviation".format(len(sd1WritingVal)*100/len(writingScore)))
print("{}% of data for writing score lies within 2 standard deviations".format(len(sd2WritingVal)*100/len(writingScore)))
print("{}% of data for writing score lies within 3 standard deviations".format(len(sd3WritingVal)*100/len(writingScore)))