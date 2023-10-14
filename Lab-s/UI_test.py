import tkinter as tk
import tkinter.messagebox as mb


all_list=[]
all_dict={}
max= 0

class App (tk.Tk):
    def __init__(self):
        super().__init__()

        btn_info = tk.Button(self, text="Да", command=self.show_info)
        opts = {'padx': 40, 'pady': 5, 'fill': tk.BOTH}
        btn_info.pack(**opts)

        btn_info = tk.Button(self, text="Информационное окно", command=self.show_info)
        opts = {'padx': 40, 'pady': 5, 'fill': tk.BOTH}
        btn_info.pack(**opts)








    def show_info(self):
        msg = "Ваши настройки сохранены"
        mb.showinfo("Информация", msg)

    def create_button(self, dialog, title, message):
        command = lambda: print(dialog(title, message))
        btn = tk.Button(self, text=title, command=command)
        btn.pack(padx=40, pady=5, expand=True, fill=tk.BOTH)



if __name__ == "__main__":
    app = App()
    app.geometry("250x200")
    app.mainloop()