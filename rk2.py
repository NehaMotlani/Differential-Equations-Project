import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
# import matplotlib.pyplot as plt

#The fuction
def dydx(x, y) : 
    return (x + y - 2); 

def rungeKutta(x0, y0, x, h) : 
    n = int(round((x - x0) / h)); 
    y = y0; 
    x_cord = []
    y_cord = []
    for i in range(1, n + 1) : 
        k1 = h * dydx(x0, y); 
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1); 
        y = y + (1.0 / 6.0) * (k1 + 2 * k2); 
        x0 = x0 + h; 
        x_cord.append(x0)
        y_cord.append(y)
    return [x_cord,y_cord]

# Driver Code 
if __name__ == "__main__" : 
    x0 = 0; y = 1; 
    x = 5; h = 0.5; 
    [x1,y1]=rungeKutta(x0, y, x, h)
    [x2,y2]=rungeKutta(x0, y, x, 0.8)
    plt.plot(x1,y1,color='r',label="h=0.2")
    plt.plot(x2,y2,color='g',label="h=0.4")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    # red_patch = mpatches.Patch(color='red', label='h=0.5')
    # green_patch = mpatches.Patch(color='green', label='h=0.8')
    # plt.legend(handles=[red_patch])
    plt.show()
