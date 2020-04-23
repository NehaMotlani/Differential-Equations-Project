import matplotlib.pyplot as plt

def func( x, y ): 
	return (x + y + x * y) 
	
def euler( x0, y, h, x ): 
	temp = -0
	x_cord = []
	y_cord = []
	# Iterating till the point at which we 
	# need approximation 
	while x0 < x: 
		temp = y 
		y = y + h * func(x0, y) 
		x0 = x0 + h 
		x_cord.append(x0)
		y_cord.append(y)
	print("Approximate solution at x = ", x, " is ", "%.6f"% y) 
	return [x_cord,y_cord]
	
# Driver Code 
# Initial Values 
x0 = 0
y0 = 1
h = 0.3

# Value of x at which we need approximation 
x = 1

[x1,y1] = euler(x0, y0, h, x) 
[x2,y2] = euler(x0,y0,0.45,x)

plt.plot(x1,y1,c='g')
plt.plot(x2,y2,c='r')
plt.show()
