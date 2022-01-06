import random

from guizero import App, Text, TextBox, PushButton, Picture

# array of scientists
sciList = ["Chemist", "Biologist", "Computer Scientist"]

# Create the App 
app = App(title="ScientistPicker",width= 800, height = 600 )

#add widgets here

# first parameter in Text tells us where to put the text
welcomeMessage = Text(app, text="What kind of Scientist are you?", size=40, font="Arial", color="darkGray")



#myName = TextBox(app, width=30)

#This is a function. Order is important. Func must be written before updateText
def getRandomScientist():
    
    #welcomeMessage.value = "Hello " + myName.value
    welcomeMessage.value = random.choice(sciList)
    

updateText = PushButton(app, command=getRandomScientist, text="Display my name")

#pictures must be in .gif format, but animated gifs will only appear as stills.

#groot = Picture(app, image="groot.gif")

app.display()
