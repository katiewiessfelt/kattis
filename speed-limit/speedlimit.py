#Bill and Ted are taking a road trip. But the odometer in their car is broken, so they don’t know how many miles they have driven. Fortunately, Bill has a working stopwatch, so they can record their speed and the total time they have driven. Unfortunately, their record keeping strategy is a little odd, so they need help computing the total distance driven. You are to write a program to do this computation.

#For example, if their log shows

#Speed in miles per hour     |     Total elapsed time in hours
#    20                                  2
#    30                                  6
#    10                                  7
#this means they drove 2 hours at 20 miles per hour, then 6−2=4 hours at 30 miles per hour, then 7−6=1 hour at 10 miles per hour. The distance driven is then 2⋅20+4⋅30+1⋅10=40+120+10=170 miles. Note that the total elapsed time is alays since the beginning of the trip, not since the previous entry in their log.
#Input-The input consists of one or more data sets (at most 10). Each set starts with a line containing an integer 𝑛, 1≤𝑛≤10, followed by 𝑛 pairs of values, one pair per line. The first value in a pair, 𝑠, is the speed in miles per hour and the second value, 𝑡, is the total elapsed time. Both 𝑠 and 𝑡 are integers, 1≤𝑠≤90 and 1≤𝑡≤12. The values for 𝑡 are always in strictly increasing order. A value of −1 for 𝑛 signals the end of the input.
#Output-For each input set, print the distance driven, followed by a space, followed by the word “miles”.

from sys import stdin
#from pudb import set_trace; set_trace()

contentList = list()

for line in stdin:
    contentList.append(line)

entries = int(contentList[0])
count: int = 0
s = int() #speed
t = int() #time
prev: int = 0
pos: int = 1
while entries != -1:
    dailyTot: int = 0
    while count < entries:
        if prev == 0:
            tempList = contentList[pos].split()
            s = int(tempList[0])
            t = int(tempList[1])
            dailyTot = s*t
            prev = t
            count += 1
            pos += 1
        else:
            tempList = contentList[pos].split()
            s = int(tempList[0])
            t = int(tempList[1])
            dailyTot += s*(t-prev)
            prev = t
            count += 1
            pos += 1
    print(f'{dailyTot} miles')
    entries = int(contentList[pos])
    pos += 1
    prev = 0
    count = 0