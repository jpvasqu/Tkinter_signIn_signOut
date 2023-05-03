import tkinter as tk

class main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("854x480")
        self.root.title("Main Window")
            
        btn_log_out=tk.Button(master=self.root,text="Log_Out",command=self.log_out)
        btn_log_out.pack()

        self.root.mainloop()


    def log_out(self):
        self.root.destroy()
        import Log_in_app
        Log_in_app.mygui()

        