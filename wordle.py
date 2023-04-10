import tkinter as tk

wordspossible = open("wordsweight.txt", "r")
possiblewords = open("possiblewords.txt", "a")
notletters = ""
posletters = ["", "", "", "", ""]
letters = ""
#screen
def gui():
    ## Configures a borderless screen
    window = tk.Tk()
    window.title("Wordle cheeser")
    window["bg"] = "#1f1c1d"
    window.geometry("800x600")

    bh = 3

    entry1 = tk.Text(height=1, width=2,  font=('courier',45,'bold'))
    entry2 = tk.Text(height=1, width=2,  font=('courier',45,'bold'))
    entry3 = tk.Text(height=1, width=2,  font=('courier',45,'bold'))
    entry4 = tk.Text(height=1, width=2,  font=('courier',45,'bold'))
    entry5 = tk.Text(height=1, width=2,  font=('courier',45,'bold'))
    notentry1 = tk.Text(height = bh, width = bh*2,  font=('courier',16,'bold'))
    notentry2 = tk.Text(height = bh, width = bh*2,  font=('courier',16,'bold'))
    notentry3 = tk.Text(height = bh, width = bh*2,  font=('courier',16,'bold'))
    notentry4 = tk.Text(height = bh, width = bh*2,  font=('courier',16,'bold'))
    notentry5 = tk.Text(height = bh, width = bh*2,  font=('courier',16,'bold'))


    lettersin = tk.Text(height = 3, width = 10, bg = "yellow", relief = "solid", borderwidth=4,)
    lettersin.place(x = 10, y = 400)
    lettersout = tk.Text(height = 3, width = 10, bg = "red", relief = "solid", borderwidth=4)
    lettersout.place(x = 10, y = 500)

    def submit():
        wordspossible = open("wordsweight.txt", "r")
        possiblewords = open("possiblewords.txt", "a")
        baibai = open("possiblewords.txt", "w")
        baibai.close
        global notletters
        global posletters
        global letters
        entries = [entry1,entry2,entry3,entry4,entry5]
        letters = lettersin.get("1.0", "end-1c")
        notletters = lettersout.get("1.0", "end-1c")

        no1 = notentry1.get("1.0", "end-1c")
        no2 = notentry2.get("1.0", "end-1c")
        no3 = notentry3.get("1.0", "end-1c")
        no4 = notentry4.get("1.0", "end-1c")
        no5 = notentry5.get("1.0", "end-1c")

        for i in range(5):
            posletters[i] = entries[i].get("1.0","end-1c")

        for i in wordspossible:
            i = [char for char in i]

            for k in [char for char in letters]:
                if not k in i:
                    break
            else:
                if i[0] in no1:
                    pass
                elif i[1] in no2:
                    pass
                elif i[2] in no3:
                    pass
                elif i[3] in no4:
                    pass
                elif i[4] in no5:
                    pass
                else:
                    for j in i:
                        if j in notletters:
                            break
                    else:
                        for j in range(len(posletters)):
                            if not posletters[j] == "":
                                if not i[j] == posletters[j]:
                                    break
                        else:
                            possiblewords.write(''.join(i))
        possiblewords.close()

        wordsread = open("possiblewords.txt", "r")
        wordsread =  wordsread.read().splitlines()
        filewrite = open("possiblewordsweight.txt", "w")
        
        weightletters = ["j" ,"q" ,"x" ,"z" ,"v" ,"w" ,"k" ,"f" ,"b" ,"g" ,"m" ,"p" ,"h" ,"d" ,"y" ,"u" ,"c" ,"n" ,"s" ,"i" ,"l" ,"t" ,"o" ,"r" ,"a" ,"e"]

        wordweights = []
        words = []

        for i in wordsread:
            letteri = [weightletters.index(char) for char in i]
            letteri2 = []
            for j in letteri:
                if(not j in letteri2):
                    letteri2.append(j)
            weighti = sum(letteri2)
            wordweights.append([weighti, i])

        wordweights.sort(reverse = True)

        for j in wordweights:
            words.append(j[1])

        for i in words:
            filewrite.write(i + "\n")

        filewrite.close()

        
        wordstoget = open("possiblewordsweight.txt")

        answer1 = wordstoget.readline()
        answer2 = wordstoget.readline()
        answer3 = wordstoget.readline()
        label1 = tk.Label(text=answer1, wraplength = 300,font=('courier',12,'normal'), bg = "#1f1c1d", fg = "white")
        label2 = tk.Label(text=answer2, wraplength = 300,font=('courier',12,'normal'), bg = "#1f1c1d", fg = "white")
        label3 = tk.Label(text=answer3, wraplength = 300,font=('courier',12,'normal'), bg = "#1f1c1d", fg = "white")

        label1.place(x = 700, y = 300)
        label2.place(x = 700, y = 350)
        label3.place(x = 700, y = 400)


        possiblewords.close()
        wordspossible.close()

    def reset():
        items = [entry1,entry2,entry3,entry4,entry5,lettersin,lettersout, notentry1, notentry2, notentry3, notentry4, notentry5]
        for i in items:
            i.delete("1.0", 'end')

    #placing all the buttons
    spacing = 100
    entries = [entry1,entry2,entry3,entry4,entry5]
    notentries = [notentry1, notentry2, notentry3, notentry4, notentry5]
    for i in range(5):
        entries[i].place(x=150+spacing*i,y=125)
        entries[i]["bg"] = "Green"
        entries[i]["relief"] = "solid"
        entries[i]["borderwidth"] = 4
    spacing = 100
    for i in range(5):
        notentries[i].place(x=150+spacing*i,y=225)
        notentries[i]["bg"] = "Yellow"
        notentries[i]["relief"] = "solid"
        notentries[i]["borderwidth"] = 4



    submitButton = tk.Button(master=window, text="SUBMIT", wraplength = 350,command=submit, relief = "solid", borderwidth=2, width = 10, height = 5,font=("futura", 8, "bold"))
    submitButton["bg"] = "Blue"
    submitButton.place(x=350, y=450)

    resetButton = tk.Button(master=window, text="RESET", wraplength = 350,command=reset, relief = "solid", borderwidth=2, width = 10, height = 5,font=("futura", 8, "bold"))
    resetButton["bg"] = "orange"
    resetButton.place(x=700, y=470)

    window.mainloop()
gui()
