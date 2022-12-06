import tkinter as tk
import maze_maker as mm


class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        master.title("迷えるこうかとん")
        master.resizable(width=False, height=False)

        self.image = tk.PhotoImage(file="fig/2.png")
        self.canvas = tk.Canvas(master, width=1500, height=900, bg="black")
        self.canvas.pack()

        self.mx,self.my = 1, 1
        self.bird = self.canvas.create_image(150,150,image=self.image)

        self.key = ""
        master.bind("<KeyPress>", self.key_down)
        master.bind("<KeyRelease>", self.key_up)

        self.main_proc()

        maze = mm.make_maze(15,9)
        mm.show_maze(self.canvas, maze)
    
    def key_down(self,e):
        self.key = e.keysym

    def key_up(self,e):
        self.key = ""

    def main_proc(self):
        if self.key == "Right":
            self.mx += 1
        elif self.key == "Left":
            self.mx -= 1
        elif self.key == "Down":
            self.my += 1
        elif self.key == "Up":
            self.my -= 1
        self.cx = self.mx*100 + 50
        self.cy = self.my*100 + 50
        self.canvas.coords(self.bird, self.cx, self.cy)
        self.canvas.tag_raise(self.bird)
        self.master.after(70, self.main_proc)




def main():
    win = tk.Tk()
    app = Application(master = win)
    
    app.mainloop()

if __name__ == "__main__":
    main()

