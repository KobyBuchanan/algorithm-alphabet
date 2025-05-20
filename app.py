import streamlit as st
import algorithms
import matplotlib.pyplot as plt

#Title
st.title("Algorithm Alphabet")

ALGORITHM = st.selectbox("Choose an algorithm", 
                          ["A* Search", "Convex Hull", "N Queens","Quick Sort"]
                          )
st.write(f"You selected: {ALGORITHM}")

if ALGORITHM == "Convex Hull":
    num_points = st.number_input("Pick Number of points", 0, 10)


if st.button("Run Algorithm"):
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
        st.pyplot(fig)