from tkinter import *
from tkinter import ttk
#No tutorial, just tkinter documentation and some python stuff I forgot
#NOT A SINGLE AI CODE LINE
#AI was asked only for:
#How does the x0, y0, x1, y1 worked for shapes as I was missunderstaing it
#Also " If i have top left corner, and bottom right corner, how can I calculate the center " It was 2 AM, and I was dense


def display():
    width = 1000
    height = 1000
    center_x = width//2
    center_y = height//2

    root = Tk()
    root.title("Solar System")
    
    canvas = Canvas(root, width=width, height=height, background='#000000')
    canvas.grid(column=0, row=0, sticky='N, W, E, S')
    
    def spawnPlanet(pos_x, pos_y, size, name):
        #Spawns a planet at the center of the window
        #Returns the position of the top left corner and bottom right and its size
        x0, y0, x1, y1 = pos_x-size, pos_y-size, pos_x+size, pos_y+size
        canvas.create_oval(x0,y0,x1,y1, fill='blue',outline='blue', tags=name)
        return (x0, y0, x1, y1, size)
    
    def spawnSatellite(parent, size, speed, mass, distance):
        #Spawns a satellite at X distance from the parent
        #Here we calculate the center of the parent (Currently is the center of the screen, but I will probably add multiple planets [Hopefully])

        planet_x = (parent[0] + parent[2])//2
        planet_y = (parent[1] + parent[3])//2
        #For myself: I need to find a way so that even if the distance is 1, since ovals are a rectangle by tkinker it will appear away from the surface, since the container isnt round, how? no clue,
        #my first instinc was asking AI, but im kinda mad my brain instantly went for that solution, tomorrow I will see what I can find, there has to be an easy way to find that point in space
        #gonna try drawing it
        #Divine intervention im praying for you, gonna go sleep now, cya

        center_x_satellite = planet_x + parent[4] + distance
        center_y_satellite = planet_y + parent[4] + distance

        x0, y0, x1, y1 = center_x_satellite-size, center_y_satellite-size, center_x_satellite+size, center_y_satellite+size

        canvas.create_oval(x0,y0,x1,y1, fill='red',outline='blue', tags='Satellite')

    
    earth = spawnPlanet(center_x, center_y, 100, 'Earth')
    jupiter = spawnPlanet(20, 10, 200, 'Jupiter')
    print(earth)
    spawnSatellite(earth, 20, 100, 50, 200)
    spawnSatellite(jupiter, 20, 100, 50, 1)

    print("Display is printed")
    root.mainloop()


display()

