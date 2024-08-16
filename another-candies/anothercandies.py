#A class went to a school trip. And, as usually, all 𝑁` kids have got their backpacks stuffed with candy. But soon quarrels started all over the place, as some of the kids had more candies than others. Soon, the teacher realized that he has to step in: "Everybody, listen! Put all the candies you have on this table here!"
#Soon, there was quite a large heap of candies on the teacher’s table. "Now, I will divide the candies into 𝑁  equal heaps and everyone will get one of them." announced the teacher.
#"Wait, is this really possible?" wondered some of the smarter kids.
#Task-You are given the number of candies each child brought. Find out whether the teacher can divide the candies into 𝑁  exactly equal heaps. (For the purpose of this task, all candiesare of the same type.)
#Input-The first line of the input file contains an integer 𝑇, 1 ≤ 𝑇 ≤ 100 specifying the number of test cases. Each test case is preceded by a blank line. Each test case looks as follows: The first line contains 𝑁, 1 ≤ 𝑁  ≤ 20000 – the number of children. Each of the next 𝑁 lines contains the number of candies one child brought. Each child has less than 263.
#Output-For each of the test cases output a single line with a single word "YES" if the candies can be distributed equally, or "NO" otherwise.

T = int() #number of test cases 
N = int() # number of children
from sys import stdin

strList = list()
for line in stdin:
    strList.append(line)

N_case: int = 0
pos: int = 0
T = int(strList[pos])
pos = 2

while N_case < T:
    total: int = 0
    N = int(strList[pos])
    pos += 1
    count: int = 0
    while count < N:
        total += int(strList[pos])
        pos += 1
        count += 1
    if total % N == 0:
        print('YES')
    else:
        print('NO')
    N_case += 1
    pos += 1