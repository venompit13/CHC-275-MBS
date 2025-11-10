print("Days 1-20")
file = open("Assignments/Day1_20.txt", "r")
buffer = file.readlines()
file.close()
print(buffer)
print(buffer[0])
print(buffer[1])
print(buffer[2])
msft1 = buffer[0].strip().split(",")
msft1.pop(0)
print(msft1)
amzn1 = buffer[1].strip().split(",")
amzn1.pop(0)
print(amzn1)
nvda1 = buffer[2].strip().split(",")
nvda1.pop(0)
print(nvda1)
for i in range(len(msft1)):
    msft1[i] = int(msft1[i])
    amzn1[i] = int(amzn1[i])
    nvda1[i] = int(nvda1[i])

print("Days 1- 20 Means")
mean0 = sum(msft1)/len(msft1)
print(mean0)
mean1 = sum(amzn1)/len(amzn1)
print(mean1)
mean2 = sum(nvda1)/len(nvda1)
print(mean2)

print("Days 21-40")
file = open("Assignments/Day21_40.txt", "r")
buffer = file.readlines()
file.close
print(buffer)
print(buffer[0])
print(buffer[1])
print(buffer[2])
msft2 = buffer[0].strip().split(",")
msft2.pop(0)
print(msft2)
amzn2 = buffer[1].strip().split(",")
amzn2.pop(0)
print(amzn2)
nvda2 = buffer[2].strip().split(",")
nvda2.pop(0)
print(nvda2)
for i in range(len(msft2)):
    msft2[i] = int(msft2[i])
    amzn2[i] = int(amzn2[i])
    nvda2[i] = int(nvda2[i])

print("Days 21- 40 Means")
mean3 = sum(msft2)/len(msft2)
print(mean3)
mean4 = sum(amzn2)/len(amzn2)
print(mean4)
mean5 = sum(nvda2)/len(nvda2)
print(mean5)

print("What to buy")
buys = []
if mean3 > mean0:
    buys.append("MSFT")
if mean4 > mean1:
    buys.append("AMZN")
if mean5 > mean2:
    buys.append("NVDA")
print(buys)

avg_filename = "report.txt"
file = open(avg_filename, "w")
line0 = f"MSFT avg 1 {mean0} avg 2 {mean3}\n"
line1 = f"AMZN avg 1 {mean1} avg 2 {mean4}\n"
line2 = f"NVDA avg 1 {mean2} avg 2 {mean5}\n"
line3 = f"Buy {buys}"
buffer = [line0, line1, line2, line3]
file.writelines(buffer)
file.close()