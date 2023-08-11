#tkinter solution fron gpt edge sidebar
#needs re layout and colouring
import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.master.title("Calculator")
        self.master.resizable(True, True)
        self.master.tk_setPalette(background='#F92F0B')
        self.master.geometry('300x200+100+100')
        self.master.config(cursor="gumby")
        self.master.config(bg="black")
        self.master.config(highlightbackground="green")
        self.master.config(highlightcolor="blue")
        self.master.config(highlightthickness=10)
        self.master.config(relief="flat")
        self.master.config(bd=2)
        self.master.config(width=20)
           


    def createWidgets(self):
        self.display = tk.Entry(self)
        self.display.pack(side="top")

        self.buttons = []
        for text in ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", ".", "0", "=", "/"]:
            button = tk.Button(self, text=text, command=lambda text=text: self.buttonPressed(text))
            button.pack(side="left")
            self.buttons.append(button)

    def buttonPressed(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

root = tk.Tk()
app = Calculator(master=root)
app.mainloop()