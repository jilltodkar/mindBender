   
from tkinter import *
import random as r

home_page=Tk()                                              #create main home page 

home_page.title("mind bender") 

width = home_page.winfo_screenwidth()                       #to create full screen window
height = home_page.winfo_screenheight()

home_page.geometry("%dx%d" % (width,height))

home_page.configure(bg = "black")                           #black background

#home_page.iconbitmap("brain.ico")           

l = Label(home_page, text = "~ M i n d  B e n d e r ~", fg = "yellow", bg = "black")            #game name on homepage

l.configure(font=('Courier 35 bold'))                                               #font style

l.place(relx = 0.5, rely = 0.3, anchor = CENTER)                                    #position the label

def cosmos():                                                                       #implementing first module
    
    cosmos_root = Toplevel()                                                        #create a window on top of another

    cosmos_root.geometry("%dx%d" % (width,height))

    cosmos_root.configure(bg = "black")

    display = Label(cosmos_root, fg = "yellow", bg = "black")           #displays the first letter

    display_hint = Label(cosmos_root, fg = "yellow", bg = "black")      #displays the hint 

    display_status = Label(cosmos_root, fg = "yellow", bg = "black")    #displays whether correct or wrong guess

    words = ["blackhole", "paradox", "galaxy", "planet", "vacuum", "infinity", "supernova", "asteroid", "bigbang", "comet"]          #word list(to-be-guessed)

    hint=[["gravity here overpowers light","happens when a star is dying","we cannot observe them"],["contradiction","logical puzzler","an enigma"],["cluster of stars","we live in one","they form the universe"],["a celestial body", "moves around a star","supposedly influences individuals' personality"],["nothingness","absence of air","outer space is a ______"],["a tired 8","indefintely great in number","thanos was a fan of these stones"],["a stellar explosion", "emits a lot of energy","very bright"],["minor planet", "they are metallic or rocky", "they do not have atmospheres"],["theory of how the universe began", "also a sitcom", "earliest known period"],["small, icy celestial body", "has a tail", "halley discovered this"]]                   #hints 

    done_words = []                                                                 #tracks the words already guessed

    for i in range(3):
        word = r.choice(words)                                                       #word to be guessed
        l = len(word) - 1           #displays the length of the word

        if word not in done_words:
            display.configure(text = word[0] + " _ "*l, font=('Courier 35 bold'))
            display.place(relx = 0.5, rely = 0.2, anchor=CENTER)    #should change the label text, but not working
            n = words.index(word)
           
            for j in range(3):
                display_hint.configure(text = "hint: " + hint[n][j], font = ('Courier 27 bold'))
                display_hint.place(relx = 0.5, rely = 0.3, anchor=CENTER)                              #displays the hint stored in 'hint' according to index subscript
                entry = Entry(cosmos_root, width = 50, borderwidth = 3, justify = CENTER, bg="darkred", fg = "white", font = ('Courier 18 bold'))
                entry.place(relx = 0.5, rely = 0.4, anchor=CENTER)

                def input():
                    global got 
                    got = entry.get()
                    entry.delete(0, END)

                guess_this = Button(cosmos_root, text = "Lock this guess", command = input, bg = "black", fg = "yellow")
                guess_this.pack(ipadx=15, ipady=15)
                
                bool_val = got == word
                if not bool_val:                                                             #displays whether guess is correct or not
                    display_status.configure(text = "Incorrect guess, try again", font=('Courier 18 bold'))
                    display_status.pack(ipadx=25, ipady=25)                              
                else:
                    display_status.configure(text = "BINGO! You figured it out", font=('Courier 35 bold'))        
                    display_status.pack(ipadx=30, ipady=30)                              
                    break
            done_words.append(word)
    

def food():                                                                                #different modules to be implemented in the same way
    
    food_root = Toplevel()

    food_root.geometry("%dx%d" % (width,height))

    food_root.configure(bg = "black")

    display = Label(food_root, text = " ", fg = "yellow", bg = "black")

    display_hint = Label(food_root, text = " ", fg = "yellow", bg = "black")

    display_status = Label(food_root, text = " ", fg = "yellow", bg = "black")

    words = ["pistachio", "banana", "egg", "cheese", "lemon", "cocoa", "popsicle", "potatoe", "spice", "oyster"]

    hint = [["A member of cashew family","Are considered nuts but are acutally fruits","Helps lower your blood pressure"],["A fruit that floats on water","Classified as berry","Humans share about 50% of their DNA with this fruit."],["Chef hats traditionally have pleats equal to the number of ways that they can cook this item","You can fry, poach, bake or boil it","Their shells can be brown,white,blue and green"],["It is a dairy product","Europe's speciality","Usually cooked with macroni"],["A staple citrus fruit","Native to Asia","hybrid of a sour orange and a citron"],["Chocolate is made from these beans","Cacao trees produces these beans","70% of it hails from West Africa"],["Initially was called Epsicle","It's sticks are made from birch wood","Also called ice pops"],["a vegetable that can absobs and reflect wifi signals","Is a good conductor of electricity","the word comes from a spanish word - Patata"],["an aromatic vegetable substance used to flavour food","India is called the capital of this word","cloves,pepper,turmeric,ginger,cumin seeds,etc"],["This item is eaten alive","They don't have central nervous system so they feel no pain","It's shells are reusuable."]]

    done_words = []

    for i in range(3):
        word = r.choice(words)
        l = len(word) - 1
    if word not in done_words:
            display.configure(text = word[0] + " _ "*l, font=('Courier 35 bold'))
            display.place(relx = 0.5, rely = 0.2, anchor=CENTER)    #should change the label text, but not working
            n = words.index(word)
           
            for j in range(3):
                display_hint.configure(text = "hint: " + hint[n][j], font = ('Courier 27 bold'))
                display_hint.place(relx = 0.5, rely = 0.3, anchor=CENTER)                              #displays the hint stored in 'hint' according to index subscript
                entry = Entry(food_root, width = 50, borderwidth = 3, justify = CENTER, bg="darkred", fg = "white", font = ('Courier 18 bold'))
                entry.place(relx = 0.5, rely = 0.4, anchor=CENTER)

                def input():
                    global got 
                    got = entry.get()
                    entry.delete(0, END)

                guess_this = Button(food_root, text = "Lock this guess", command = input, bg = "black", fg = "yellow")
                guess_this.pack(ipadx=15, ipady=15)
                
                bool_val = got == word
                if not bool_val:                                                             #displays whether guess is correct or not
                    display_status.configure(text = "Incorrect guess, try again", font=('Courier 18 bold'))
                    display_status.pack(ipadx=25, ipady=25)                              
                else:
                    display_status.configure(text = "BINGO! You figured it out", font=('Courier 35 bold'))        
                    display_status.pack(ipadx=30, ipady=30)                              
                    break
            done_words.append(word)

def sports():
    sports_root = Toplevel()

    sports_root.geometry("%dx%d" % (width,height))

    sports_root.configure(bg = "black")

    display = Label(sports_root, text = " ", fg = "yellow", bg = "black")

    display_hint = Label(sports_root, text = " ", fg = "yellow", bg = "black")

    display_status = Label(sports_root, text = " ", fg = "yellow", bg = "black")

    words = ["golfball","olympic","formula1","marykom","usainbolt","valorant","kapildev","badminton","serenawilliams","shotput"]

    hint = [["Has 336 dimples","Is spherical in shape","Used to play golf"],["Held every 4 years","It's symbol has 5 rings in it","Atheletes from all over the world compete here"],["World's premier racing competition","It is called the Grand Prix","The team Ferrari is the leader in all it's records."],["5-time world amateur boxing champion","Named as Mangte Chungneijang at birth","She is from Manipur,India."],["Athelete that broke record wearing untied shoes","His winning pose is called Bolting.","He's also known as lightning bolt"],["A team based FPS game","Developed by Riot Games","Players play as one of a set of Agents."],["Former Cricket Indian Team Captain","Nicknamed as The Harayana Hurricane","Born on 6 January 1959"],["It is the 2nd most popular sport in the world","The shuttle is made from the left wing of a goose","It was initially played with the player's feet."],["Player who won 23 Grand Slam Titles","The athlete is from Michigan,U.S","Also won 14 Grand Slam doubles titles"],["A track and field event involving putting","Played with a heavy spherical ball","Ryan Crouser is the best player in this game."]]

    done_words = []

    for i in range(3):
        word = r.choice(words)
        l = len(word) - 1
    if word not in done_words:
            display.configure(text = word[0] + " _ "*l, font=('Courier 35 bold'))
            display.place(relx = 0.5, rely = 0.2, anchor=CENTER)    #should change the label text, but not working
            n = words.index(word)
           
            for j in range(3):
                display_hint.configure(text = "hint: " + hint[n][j], font = ('Courier 27 bold'))
                display_hint.place(relx = 0.5, rely = 0.3, anchor=CENTER)                              #displays the hint stored in 'hint' according to index subscript
                entry = Entry(sports_root, width = 50, borderwidth = 3, justify = CENTER, bg="darkred", fg = "white", font = ('Courier 18 bold'))
                entry.place(relx = 0.5, rely = 0.4, anchor=CENTER)

                def input():
                    global got 
                    got = entry.get()
                    entry.delete(0, END)

                guess_this = Button(sports_root, text = "Lock this guess", command = input, bg = "black", fg = "yellow")
                guess_this.pack(ipadx=15, ipady=15)
                
                bool_val = got == word
                if not bool_val:                                                             #displays whether guess is correct or not
                    display_status.configure(text = "Incorrect guess, try again", font=('Courier 18 bold'))
                    display_status.pack(ipadx=25, ipady=25)                              
                else:
                    display_status.configure(text = "BINGO! You figured it out", font=('Courier 35 bold'))        
                    display_status.pack(ipadx=30, ipady=30)                              
                    break

            done_words.append(word)


def start():                                                                                                 #window for selection of module
    new = Toplevel()

    new.geometry("%dx%d" % (width,height))

    new.configure(bg = "black")

    new.title("mind bender")

    b1 = Button(new, text = "Cosmos", command = cosmos, fg = "yellow", bg = "black")                #creates options of modules
    b2 = Button(new, text = "Food", command = food, fg = "yellow", bg = "black")
    b3 = Button(new, text = "Sports", command = sports, fg = "yellow", bg = "black")

    b1.place(relx = 0.5, rely = 0.5, anchor = CENTER)                                               #placement of module buttons
    b1.configure(font=('Courier 20 bold'))

    b2.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    b2.configure(font=('Courier 20 bold'))

    b3.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    b3.configure(font=('Courier 20 bold'))

    new.mainloop()

b = Button(home_page, text = "Select module: ", fg = "yellow", bg = "black", padx = 9, pady = 9, command = start)       #go to selecting modules

b.place(relx = 0.5, rely = 0.5, anchor = CENTER)                                                    #places the button
b.configure(font=('Courier 20 bold'))

home_page.mainloop()                                                                                #runs the code constantly in the backend
