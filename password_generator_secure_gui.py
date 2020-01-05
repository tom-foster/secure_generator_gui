import string
import random

from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class PassGenGUI:
    def __init__(self, master):
        self.master = master
        self.entered_number = 20
        master.title('Password Secure Generator')
        self.label = Label(master, text='Enter')
        self.label.pack()

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.entry.pack()

        self.generate_button = Button(master, text="Generate Password", command=self.gen_password)
        self.generate_button.pack()
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

        

    def password_secure_generator(self, size=20, chars=string.ascii_letters +
                                string.punctuation + string.digits):
        return ''.join(random.SystemRandom().choice(chars) for i in range(size))

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 20
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except AttributeError:
            return False

    def gen_password(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(str(self.password_secure_generator(self.entered_number)))



root = Tk()
pass_gen_gui = PassGenGUI(root)
root.mainloop()