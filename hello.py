from flask import Flask, escape, request, render_template
import random
import pyttsx3
from gtts import gTTS

app = Flask(__name__)



@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return render_template('code12.html', filepath="")

@app.route('/speak')
def speak():
    filepath = randomWord()
    return render_template('code12.html', filepath=filepath)
wrong=[]
correct=[]

engine=pyttsx3.init()
# di={'GLADIOLUS':'The word is a type of flower','ALBUMEN':'The white part of an egg','CRUSTACEOLOGY':'The study of crustaceans','SYLLEPSIS':'A figure of speech in which one word simultaneously modifies two or more other words such that the modification must be understood differently with respect to each modified word','SMARAGDINE':'Of or pertaining to emeralds, or having the color of emeralds','ESQUAMULOSE':'Not covered in scales or scale-like objects; smooth-skinned','MACULATURE':'Paper waste and printed materials not intended for reading, a.k.a. junk mail','ELUCUBRATE':'To produce by long and intensive effort','ODONTALGIA':'A fancy word for toothache','ANTEDILUVIAN':'Ancient, antiquated or supremely dated','VIVISEPULTURE':'The act of burying someone alive','EUONYM':'A name well suited to a person, place or thing','CHIAROSCURIST':'Is a style of monochromatic shading used in art','SUCCEDANEUM':'A substitute or replacement for something else, especially in reference to medicine','PROSPICIENCE':'Foresight','POCOCURANTE':'Apathetic or indifferent','URSPRACHE':'A hypothetically reconstructed parent language','GUETAPENS':'This word, which is defined as an ambush or trap','KNAIDEL':"Which is a type of dumpling that's often eaten during Passover"}
di={'different':'The word is a type of flower',
'Language':'The white part of an egg',
'mammal':'The study of crustaceans',
'dessert':'The study of crustaceans','neither':'The study of crustaceans'}

key_list=list(di.keys())
def return_word():
    key_list=list(di.keys())
    key_choice=random.choice(key_list)
    print(di[key_choice])
    del di[key_choice]
    return key_choice

def convert_mp3(word):
    tts=gTTS(text=word,lang='en')
    tts.save("static/"+word+".mp3")

# def pronounce(word):
#     print(word)
#     engine.say(word)
#     engine.runAndWait()


def randomWord():
    # if (not bool(di)):
    #     print('Good Job,you got these words correct:{} and these words wrong:{}'.format(correct,wrong))
    #     break

    word=return_word()
    # pronounce(word)
    convert_mp3(word)

    return "static/"+word+".mp3"
    user=request.form["word"]
    if word==user.upper():
        # print('CORRECT!')
        correct.append(word)
        # print()
    else:
        # print('INCORRECT!')
        wrong.append(word)
        # print(word)





if __name__ == "__main__":
    app.run()
