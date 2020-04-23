import matplotlib.pyplot as plt
def dydx(x, y): 
	return ((x - y+ (x*x) )/2) 

def rungeKutta(x0, y0, x, h): 
	# Count number of iterations using step size or step height h 
	n = (int)((x - x0)/h) 
	# Iterate for number of iterations 
	y = y0 
	x_cord = []
	y_cord = []
	for i in range(1, n + 1): 
		# "Apply Runge Kutta Formulas to find next value of y"
		k1 = h * dydx(x0, y) 
		k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1) 
		k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2) 
		k4 = h * dydx(x0 + h, y + k3) 
		# Update next value of y 
		y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
		# Update next value of x 
		x0 = x0 + h 
		x_cord.append(x0)
		y_cord.append(y)
	return [x_cord,y_cord]
# Driver method 
x0 = 0
y = 1
x = 2
h = 0.2
[x1,y1]=rungeKutta(x0, y, x, h)
[x2,y2]=rungeKutta(x0, y, x, 0.4)
# [x3,y3]=rungeKutta(x0, y, x, 0.5)
plt.plot(x1,y1,c='g',label="h=0.2")
plt.plot(x2,y2,c='r',label="h=0.5")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
# plt.plot(x3,y3,c='b')
plt.show()


