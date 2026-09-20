import random
from tkinter import *
import webbrowser

class MainWindow:
    def __init__(self, master, verbs):
            # Variables
            self.ordened = True
            self.nextActive = True
            self.verbs = verbs
            self.point = 0


            # Frames
                # Start
            self.start = Frame(master, bg="#2C2F33")
            self.start.pack_propagate(False) # Don't let the built-in widgets determine the resolution

                # Quiz
            self.quiz = Frame(master, bg="#2C2F33")
            self.quiz.pack_propagate(False)

                # About
            self.about = Frame(master, bg="#2C2F33")
            self.about.pack_propagate(False)


            # Widgets
                # Start
            self.startImg = PhotoImage(file="images/start.png")
            self.aboutImg = PhotoImage(file="images/about.png")

            self.startBtn = Button(master=self.start, bg="#2C2F33", border=0, image=self.startImg, command=self.startBtn_pressed, activebackground="#2C2F33")
            self.aboutBtn = Button(master=self.start, bg="#2C2F33", border=0, image=self.aboutImg, command=self.aboutBtn_pressed, activebackground="#2C2F33")

            self.startLabel = Label(master=self.start, text="Train irregular verbs", fg="white", bg="#2C2F33", font=("Comic Sans MS", 15, "bold italic"))

            self.randomSett = IntVar()
            self.sortedBtn = Radiobutton(master=self.start, bg="#2C2F33", text="Sorted", variable=self.randomSett, value=0, command=self.settings)
            self.randomBtn = Radiobutton(master=self.start, bg="#2C2F33", text="Random", variable=self.randomSett, value=1, command=self.settings)

                # Quiz
            self.closeImg = PhotoImage(file="images/close.png")
            self.nextImg = PhotoImage(file="images/next.png")
            self.okImg = PhotoImage(file="images/ok.png")
            self.questionImg = PhotoImage(file="images/question.png")
            self.goodImg = PhotoImage(file="images/good.png")
            self.badImg = PhotoImage(file="images/bad.png")

            self.closeqBtn = Button(master=self.quiz, bg="#2C2F33", border=0, image=self.closeImg, command=self.closeBtn_pressed, activebackground="#2C2F33")
            self.activity = Label(master=self.quiz, bg="#2C2F33", image=self.questionImg)
            self.points = Label(master=self.quiz, text="Points: 0", fg="white", bg="#2C2F33", font=("Comic Sans MS", 9, "bold italic"))
            self.quizBtn = Button(master=self.quiz, bg="#2C2F33", border=0, image=self.nextImg, command=self.quizBtn_pressed, activebackground="#2C2F33")

            self.infinitive = Label(master=self.quiz, text="Infinitive", fg="white", bg="#2C2F33", font=("Comic Sans MS", 15, "bold italic"))
            self.simple = Label(master=self.quiz, text="Simple Past", fg="white", bg="#2C2F33", font=("Comic Sans MS", 15, "bold italic"))
            self.participle = Label(master=self.quiz, text="Past Partciciple", fg="white", bg="#2C2F33", font=("Comic Sans MS", 15, "bold italic"))

            self.simpleInput = Entry(master=self.quiz)
            self.participleInput = Entry(master=self.quiz)

                # About
            self.closeBtn = Button(master=self.about, bg="#2C2F33", border=0, image=self.closeImg, command=self.closeBtn_pressed, activebackground="#2C2F33")
                                                                                # This is my final project of the CS50's Introduction to Programming with Python course
            self.info = Label(master=self.about,  fg="white", bg="#2C2F33", text="This is my citizenship project, \nmy name is Rofly António and until next time.", font=("Comic Sans MS", 10, "bold italic"))
            self.me = Label(master=self.about, fg="#4266f5", text="Me",  bg="#2C2F33", font=("Comic Sans MS", 10, "underline"))
            self.credits = Label(master=self.about, text="All images designed by Freepik from Flaticon", fg="#4266f5", bg="#2C2F33", font=("Comic Sans MS", 10, "underline"))
            self.list = Label(master=self.about, text="List of verbs", fg="#4266f5", bg="#2C2F33", font=("Comic Sans MS", 10, "underline"))

            self.me.bind("<Button-1>", lambda a: webbrowser.open_new("https://linktr.ee/srrofly")) # <Button-1> = Left button of mouse, <Button-2> = middle button, ...
            self.credits.bind("<Button-1>", lambda a: webbrowser.open_new("https://www.flaticon.com/authors/freepik"))



            # Packs or Place
                # Start
            self.start.pack(fill=BOTH, expand=1) # To expand the frame to fill app

            self.startLabel.place(relx=0.5, rely=0.35, anchor=CENTER) # Start further north

            self.startBtn.place(relx=0.5, rely=0.5 ,anchor=CENTER)
            self.aboutBtn.place(relx=0.5, rely=0.9 ,anchor=CENTER)
            self.sortedBtn.place(relx=0.2, rely=0.6 ,anchor=CENTER)
            self.randomBtn.place(relx=0.21, rely=0.65 ,anchor=CENTER)

                # Quiz
            self.closeqBtn.place(relx=0.1, rely=0.1, anchor=CENTER)
            self.activity.place(relx=0.5, rely=0.2, anchor=CENTER)
            self.points.place(relx=0.5, rely=0.4, anchor=CENTER)
            self.quizBtn.place(relx=0.5, rely=0.9 ,anchor=CENTER)

            self.infinitive.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.simple.place(relx=0.3, rely=0.5, anchor=CENTER)
            self.participle.place(relx=0.7, rely=0.5, anchor=CENTER)

            self.simpleInput.place(relx=0.3, rely=0.6, anchor=CENTER)
            self.participleInput.place(relx=0.7, rely=0.6, anchor=CENTER)

                # About
            self.closeBtn.place(relx=0.1, rely=0.1, anchor=CENTER)
            self.info.place(relx=0.5, rely=0.3, anchor=CENTER)
            self.me.place(relx=0.5, rely=0.4, anchor=CENTER)
            self.credits.place(relx=0.5, rely=0.5, anchor=CENTER)


    def settings(self):
        if self.randomSett.get() == 0:
            self.ordened = True
        else:
            self.ordened = False


    def closeBtn_pressed(self):
        if self.about.winfo_ismapped():
            self.about.pack_forget()
            self.start.pack(fill=BOTH, expand=1)

        else:
            self.quiz.pack_forget()
            self.start.pack(fill=BOTH, expand=1)

    # Start
    def startBtn_pressed(self):
        self.start.pack_forget()
        self.quiz.pack(fill=BOTH, expand=1)

        if not self.nextActive:
            self.quizBtn_pressed()
        else:
            self.new_verb()
            self.infinitive.config(text=self.i.capitalize())

    def aboutBtn_pressed(self):
        self.start.pack_forget()
        self.about.pack(fill=BOTH, expand=1)

    #Quiz
    def quizBtn_pressed(self):
        if self.nextActive:
            self.nextActive = False
            self.quizBtn.config(image=self.okImg)

            simpler = self.simpleInput.get().lower()
            participler = self.participleInput.get().lower()

            if simpler in self.s and participler in self.p:
                self.activity.config(image=self.goodImg)
                self.point += 1
                self.points.config(text=f"Points: {self.point}")

                self.simple.config(text="Good")
                self.participle.config(text="Good")

            else:
                self.simple.config(text=self.s[0].capitalize())
                self.participle.config(text=self.p[0].capitalize())
                self.activity.config(image=self.badImg)

        else:
            self.nextActive = True

            self.quizBtn.config(image=self.nextImg)
            self.activity.config(image=self.questionImg)

            self.simpleInput.delete(0, END)
            self.participleInput.delete(0, END)

            self.simple.config(text="Simple Past")
            self.participle.config(text="Past Participle")


            del self.verbs[self.i]
            self.new_verb()

            self.infinitive.config(text=self.i.capitalize())


    def new_verb(self): # Not to repeat verbs one after the other, and when there are no more verbs, restore the dic with the backup
        if self.verbs:
            for self.i in self.verbs:
                if not self.ordened:
                    self.i = random.choice(list(self.verbs.keys()))


                self.s = [self.verbs[self.i][0][0]]
                self.p = [self.verbs[self.i][0][1]]

                try:
                    if self.s != self.verbs[self.i][1][0]:
                        self.s.append(self.verbs[self.i][1][0])
                        self.s.append(f"{self.s}/{self.verbs[self.i][1][0]}")

                    if self.p != self.verbs[self.i][1][1]:
                        self.p.append(self.verbs[self.i][1][1])
                        self.p.append(f"{self.s}/{self.verbs[self.i][1][1]}")
                    break
                except:
                    break

        else:
            self.i = "End ✔"
            self.quizBtn.destroy()