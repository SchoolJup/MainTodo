#imported from edge gpt sidebar
#doesnt work
import flet

class Calculator(flet.Frame):
    def __init__(self, master=None):
        flet.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.display = flet.Entry(self)
        self.display.pack(side="top")

        self.buttons = []
        for text in ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", ".", "0", "=", "/"]:
            button = flet.Button(self, text=text, command=lambda text=text: self.buttonPressed(text))
            button.pack(side="left")
            self.buttons.append(button)

    def buttonPressed(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, flet.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, flet.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(flet.END, text)

root = flet.Tk()
app = Calculator(master=root)
app.mainloop()