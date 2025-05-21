
'''if st.button("Run Algorithm"):
    points, hull = algorithms.convex_hull(num_points)
    if type(hull) == str:
        st.write(hull)
    else:
        #plotting
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
        st.pyplot(fig)'''