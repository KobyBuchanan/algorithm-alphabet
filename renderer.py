import algorithms
import matplotlib.pyplot as plt
from io import BytesIO
import base64



def render_convex_hull():   
        points, hull = algorithms.convex_hull(10)
        fig, ax = plt.subplots()
        x,y = zip(*points)
        ax.scatter(x,y,label="Points",color='blue')
        #Hull plotting
        hull_points = hull + [hull[0]]
        hx,hy = zip(*hull_points)
        ax.plot(hx,hy,'r-',label='Convex Hull')
        ax.scatter(*zip(*hull), color='red')
        ax.axhline(0, color='gray', lw=0.5)
        ax.axvline(0, color='gray', lw=0.5)
        ax.set_aspect('equal')
        ax.legend()

        #convert image to base64
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)

        return image

def render_cool_algo_here():
        x = [0,1,2,3,4,5]
        y = [5,4,3,2,1,0]
        fig, ax = plt.subplots()
        ax.scatter(x,y,label='Points',color='blue')
        ax.axhline(0, color='gray', lw=0.5)
        ax.axvline(0, color='gray', lw=0.5)
        ax.set_aspect('equal')
        ax.legend()
         #convert image to base64
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)

        return image
