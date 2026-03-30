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
    
    def spawnPlanet(size, name):
        #Spawns a planet at the center of the window
        x0, y0, x1, y1 = center_x-size, center_y-size, center_x+size, center_y+size
        canvas.create_oval(x0,y0,x1,y1, fill='blue',outline='blue', tags=name)
        return (x0, y0, x1, y1)
    
    def spawnSatellite(parent_pos, size, speed, mass, distance):
        #Spawns a satellite at X distance from the parent

        #Here we calculate the center of the parent (Currently is the center of the screen, but I will probably add multiple planets [Hopefully])
        planet_x = (parent_pos[0] + parent_pos[2])//2
        planet_y = (parent_pos[1] + parent_pos[3])//2

        center_x_satellite = planet_x + distance
        center_y_satellite = planet_y + distance

        canvas.create_oval(parent_pos[0],parent_pos[1],parent_pos[2],parent_pos[3], fill='red',outline='blue', tags='Satellite')

    
    earth = spawnPlanet(100, 'Earth')
    print(earth)
    spawnSatellite(earth, 20, 100, 50)

    print("Display is printed")
    root.mainloop()


display()

