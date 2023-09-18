import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes()
x = [1,2,3,4,5,6]
y = [1,4,8,12,6,4]
z = [2,7,10,14,10,8]
plt.title("Book popularity")
plt.xlabel("Time")
plt.ylabel("No. of times Checked Out")
plt.xlim(0,8)
plt.ylim(0,15)
#display plot
plt.plot(x,y,'b--*',label='Book 1')
plt.plot(x,z,'r-D',label='Book 2')
plt.legend(loc = 'upper left')
plt.show()
