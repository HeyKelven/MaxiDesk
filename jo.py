from tkinter import *
import threading


class App(threading.Thread):

    def __init__(self, tk_root, count):
        self.root = tk_root
        threading.Thread.__init__(self)
        self.count = count
        self.start()

    def run(self):
        loop_active = True
        while loop_active:
            user_input = input("Give me your command! Just type \"exit\" to close: ")
            if user_input == "exit":
                loop_active = False
                self.root.quit()
                self.root.update()
            else:
                label = Label(self.root, text=user_input)
                label.grid(row=self.count)
                self.count += 1


ROOT = Tk()
i = 2
LABEL = Label(ROOT, text="Hello, world!")
LABEL.grid(row=1)
APP = App(ROOT, i)
ROOT.mainloop()