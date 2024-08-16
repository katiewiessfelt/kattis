#problem: ofugsnuid
#Little Jóna needs a program. The program should read integers and print them in reverse order. 
  #Jóna asks for your help.
#Input-The first line of input contains the integer 𝑛. Then comes a list of 𝑛 integers, each 
  #on its own line.
#Output-The list should be printed in reverse order of input.

from sys import stdin

inputList = list()
for line in stdin:
    inputList.append(line)

position: int = int(inputList[0])
if position>10**5: position = 10**5

while position>0:
    print(inputList[position])
    position -= 1
