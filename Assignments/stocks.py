file = open("Assignments/Day1_20.txt", "r")
buffer = file.readlines()
file.close
print(buffer)
print(buffer[0])
print(buffer[1])
print(buffer[2])
msft1 = buffer[0]
amzn1 = buffer[1]
nvda1 = buffer[2]

mean = sum(msft1)/len(msft1)
print(mean)

file = open("Assignments/Day21_40.txt", "r")
buffer = file.readlines()
file.close
print(buffer)
print(buffer[0])
print(buffer[1])
print(buffer[2])
msft2 = buffer[0]
amzn2 = buffer[1]
nvda2 = buffer[2]

avg_filename = "report.txt"