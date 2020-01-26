from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import datetime
import re

gate = True
global tame
tame = []
dame = []


class Gui:

    def __init__(self, master):

        self.head = Label(master,
                        text="Subtitle Fixer",
                        font=('Algerian',25),
                        fg="#fff",
                        bg="#000"
                        )

        self.head.grid(column=0,
                     row=0,
                     columnspan=4,
                     pady=20
                     )

        self.s1 = Label(master,
                        text="Step #1",
                        font=('Bradley Hand ITC',18),
                        fg="#fff",
                        bg="#000"
                        )

        self.s1.grid(column=0,
                     row=1,
                     )

        self.mebut = Button(master,
                              text="ME",
                              bg='#fff',
                              fg='#000',
                              font=('Arial Bold',6),
                              relief='ridge',
                              bd=2,
                              command=self.mego
                              )

        

        self.mebut.grid(column=3,
                        row=1,
                                                    )

        self.openbut = Button(master,
                              text="Please Select a File",
                              bg='#fff',
                              fg='#000',
                              font=('Arial Bold',10),
                              relief='ridge',
                              bd=5,
                              command=self.ofile
                              )

        

        self.openbut.grid(column=0,
                          row=2,
                          columnspan=4,
                          pady=15
                          )

        self.s2 = Label(master,
                        text="Step #2",
                        font=('Bradley Hand ITC',18),
                        fg="#fff",
                        bg="#000",
                        )

        self.s2.grid(column=0,
                     row=3,
                     padx=5
                     )

        self.R1 = Radiobutton(root,
                        text="Increment Time",
                        value=1,
                        bg='#fff',
                        fg='#000',
                        font=('Arial Bold',8),
                        relief='ridge',
                        command=self.opadd
                        )

        self.R1.grid(column=0,
                    columnspan=2,
                    row=4,
                    padx=10,
                    pady=15
                    )

        self.R2 = Radiobutton(root,
                         text="Decrement Time",
                         value=2,
                         bg='#fff',
                         fg='#000',
                         font=('Arial Bold',8),
                         relief='ridge',
                         command=self.opsub
                         )

        self.R2.grid(column=2,
                    columnspan=2,
                     row=4,
                     padx=10
                     )

        self.s3 = Label(master,
                        text="Step #3",
                        font=('Bradley Hand ITC',18),
                        fg="#fff",
                        bg="#000",
                       
                        )

        self.s3.grid(column=0,
                     row=5
                     )

        self.hour = Label(master,
                         text="Hours",
                         font=('Arial Bold',10),
                         fg='#fff',
                         bg='#000'
                         )

        self.hour.grid(column=0,
                       columnspan=2,
                       row=6,
                       pady=5
                       )

        self.e1 = Entry(master)

        self.e1.grid(column=1,
                    columnspan=2,
                    row=6
                    )

        self.mins = Label(master,
                         text="Mins",
                         font=('Arial Bold',10),
                         fg='#fff',
                         bg='#000',
                         pady=5

                         )

        self.mins.grid(column=0,
                       columnspan=2,
                       row=7
                       )

        self.e2 = Entry(master)

        self.e2.grid(column=1,
                     columnspan=2,
                     row=7
                     )

        self.sec = Label(master,
                        text="Seconds",
                        font=('Arial Bold',10),
                        fg='#fff',
                        bg='#000',
                        pady=5
                        )

        self.sec.grid(column=0,
                      columnspan=2,
                      row=8
                      )

        self.e3 = Entry(master)

        self.e3.grid(column=1,
                     columnspan=2,
                     row=8
                     )

        self.okbut = Button(master,
                            text="Lets Make New Subtitles File",
                            font=('Arial Bold',12),
                            bg='#fff',
                            fg='#000',
                            command=self.mai
                            )

        self.okbut.grid(column=0,
                        row=9,
                        columnspan=4,
                        pady=17)


    def mego(self):
            messagebox.showinfo( "Contact", "Please Contact the Developer \n\n Gmail - Parmeet757@gmail.com\n Watsapp - 8788042372\n GitHub - @ParmeetAFK\n")   

    def opadd(self):
        self.op = 1

    def opsub(self):
        self.op = 0

    def ofile(self):
        #OPEN FILE CODE FOR GUI 

        opfile = filedialog.askopenfilename(initialdir=r"C:\Users\Parme\Documents\Downloads",title="Select",filetypes=(('TEXT DOCUMENT',"*.txt"),("All Files","")))
        self.path = str(opfile)

    def mai(self):
        self.i = 1
        print("I AM HERE")
        self.take_time()
        self.timex()
        self.daixx()
        for self.abhi,self.j in zip(tame,range(len(dame))):
            self.time_obj()

            if self.op == 0:
                self.time_sub()
            elif self.op == 1:
                self.time_plus()
            else:
                pass

            self.time_incf()
            self.i = self.i + 1

        messagebox.showinfo( "Message", "File is Ready on Desktop")

class Work(Gui):

    def pop(self):
        messagebox.showinfo("Missing Something", "Please Choose your file and Enter All 3 values")

    try:
        def take_time(self):

            ##TAKE TIME FROM GUI
            #CREATES A TIME OBJECT
            #I_TIME
            self.x_hr = int(self.e1.get())
            self.x_min = int(self.e2.get())
            self.x_sec = int(self.e3.get())

            global i_time

            i_time = datetime.timedelta(hours=self.x_hr,minutes=self.x_min,seconds=self.x_sec)

    except Exception:
        self.pop

    try:
        def timex(self):
            #TAKES PATH OF fILE
            #REGEX TO FIND TIME
            #LIST OF TO CHANGE TIME
            global regin
            

            f1 = open(self.path,mode='r')
            self.content = f1.read()

            pat = re.compile(r'\d\d[:]\d\d[:]\d\d[,]\d\d\d\s[-][-][>]\s\d\d[:]\d\d[:]\d\d[,]\d\d\d')

            self.match = pat.findall(self.content)

            for m in self.match:
                tame.append(m)

    except Exception:
        self.pop

    def daixx(self):

        f1 = open(self.path,mode='r')
        self.content2 = f1.read()

        dia = re.sub(r'((\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+))','', self.content2)

        self.newa = dia.split('\n\n')

        for log in range(len(self.newa)):
            if log%2:
                dame.append(self.newa[log])
            else:
                pass


    def time_obj(self):

        self.hr1 = int(self.abhi[0:2])
        self.min1 = int(self.abhi[3:5])
        self.sec1 = int(self.abhi[6:8])
        self.msec1 = int(self.abhi[9:13])
        self.hr2 = int(self.abhi[17:19])
        self.min2 = int(self.abhi[20:22])
        self.sec2 = int(self.abhi[23:25])
        self.msec2 = int(self.abhi[26:30])

        self.time1 = datetime.datetime(2016, 5, 10, self.hr1, self.min1, self.sec1, self.msec1)
        self.time2 = datetime.datetime(2016, 5, 10, self.hr2, self.min2, self.sec2, self.msec2)

    def time_plus(self):

        self.itime1 = self.time1 + i_time
        self.itime2 = self.time2 + i_time

    def time_sub(self):

        self.itime1 = self.time1 - i_time
        self.itime2 = self.time2 - i_time


    def time_incf(self):

        gate = True
        f = open(r"C:\Users\Parme\Desktop\subs.txt",mode='a')
        while(gate == True):
            f.write(str(self.i))
            f.write("\n")
            f.write(str(self.itime1.time()))
            f.write(" --> ")
            f.write(str(self.itime2.time()))
            f.write("\n")
            f.write(dame[self.j])
            f.write("\n")
            f.write("\n")

            gate = False


root = Tk()
root.title("Subtitles Fixer")
root.configure(background='black')
b = Work(root)
root.mainloop()
