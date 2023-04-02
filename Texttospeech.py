import tkinter as tk
import pyttsx3

window = tk.Tk()
window.title("Text to Speech Application")
window.configure(background="pink")
window.geometry("400x200")
engine = pyttsx3.init()
gender = tk.StringVar()


def speech():
    voice = gender.get()
    sentence = entry.get()
    # print(voice)
    if voice == "female":
        female_voice = engine.getProperty('voices')[1]
        engine.setProperty('voice', female_voice.id)
        engine.say(sentence)
        volume = engine.getProperty('volume')   
        engine.setProperty('volume',1.0)
        #print (volume) 
        engine.runAndWait()
    elif voice == "male":
        male_voice = engine.getProperty('voices')[0]
        engine.setProperty('voice', male_voice.id)
        engine.say(sentence)
        volume = engine.getProperty('volume')
        engine.setProperty('volume',1.0)
        #print (volume) 
        engine.runAndWait()

    
label1 = tk.Label(text="select voice types", bg="pink")
entry = tk.Entry(bg="white", width=40)

button = tk.Button(
    text="Speech", command=speech, bg="green"

)

R1 = tk.Radiobutton(text="Male", value="male", variable=gender, fg="black",
                    bg="pink",
                    )
R2 = tk.Radiobutton(text="Female", value="female", variable=gender, fg="black",
                    bg="pink",
                    )

entry.grid(row=1, column=0, padx=5, pady=5)
button.grid(row=1, column=1, padx=5, pady=5)
label1.grid(row=2, column=0)
R1.grid(row=2, column=1)
R2.grid(row=2, column=2)
gender.set(None)

window.mainloop()
