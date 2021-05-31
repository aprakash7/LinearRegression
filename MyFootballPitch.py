
#My own Football Pitch
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
def CreatePitch():
    #Create figure
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,100], color="black")
    plt.plot([0,130],[100,100], color="black")
    plt.plot([130,130],[100,0], color="black")
    plt.plot([130,0],[0,0], color="black")
    plt.plot([65,65],[0,100], color="black")

    #Left Penalty Area
    plt.plot([16.5,16.5],[75,25],color="black")
    plt.plot([0,16.5],[75,75],color="black")
    plt.plot([16.5,0],[25,25],color="black")
        
    #Right Penalty Area
    plt.plot([130,113.5],[75,75],color="black")
    plt.plot([113.5,113.5],[75,25],color="black")
    plt.plot([113.5,130],[25,25],color="black")
    
    #Left 6-yard Box
    plt.plot([0,5.5],[65,65],color="black")
    plt.plot([5.5,5.5],[65,36],color="black")
    plt.plot([5.5,0.5],[36,36],color="black")
    
    #Right 6-yard Box
    plt.plot([130,124.5],[65,65],color="black")
    plt.plot([124.5,124.5],[65,36],color="black")
    plt.plot([124.5,130],[36,36],color="black")
    
    #Prepare Circles
    centreCircle = plt.Circle((65,50),9.15,color="black",fill=False)
    centreSpot = plt.Circle((65,50),0.8,color="black")
    leftPenSpot = plt.Circle((11,50),0.8,color="black")
    rightPenSpot = plt.Circle((119,50),0.8,color="black")
    
    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)
    
    #Prepare Arcs
    leftArc = Arc((11,50),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
    rightArc = Arc((119,50),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)
    
    #Tidy Axes
    plt.axis('off')