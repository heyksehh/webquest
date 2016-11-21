# webquest
from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
    if request.args:
        f = open ('verbs.txt', 'a', encoding = 'utf-8')
        f.write ('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n' % (request.args.get('language'), request.args.get('apple'), \
                 request.args.get('hands'), request.args.get('floor'), request.args.get('teeth'), request.args.get('hair'), \
                 request.args.get('room'), request.args.get('body'), request.args.get('window'), request.args.get('face'), \
                 request.args.get('clothes'), request.args.get('dishes')))
        f.close()
    return render_template('index.html')

@app.route('/stats')
def stats():
    langs = []
    apple = []
    hands = []
    floor = []
    teeth = []
    hair = []
    room = []
    body = []
    window = []
    face = []
    clothes = []
    dishes = []
    
    f = open ('verbs.txt', 'r', encoding = 'utf-8')
    text = f.readlines()
    for line in text:
        x = line.split(', ')
        
        langs.append(x[0])
        apple.append(x[1])
        hands.append(x[2])
        floor.append(x[3])
        teeth.append(x[4])
        hair.append(x[5])
        room.append(x[6])
        body.append(x[7])
        window.append(x[8])
        face.append(x[9])
        clothes.append(x[10])
        dishes.append(x[11])
        
    f.close
    
    langs2 = []
    for i in langs:
        if i not in langs2:
            langs2.append(i)
    linelang = ''
    for lang in langs2:
        linelang += lang + ', '
        
    apple2 = []
    for a in apple:
        if a not in apple2:
           apple2.append(a)
    lineapple = ''
    for appl in apple2:
        lineapple += appl + ', '
        
    hands2 = []
    for h in hands:
        if h not in hands2:
            hands2.append(h)
    linehands = ''
    for hnd in hands2:
        linehands += hnd + ', '
        
    floor2 = []
    for fl in floor:
        if fl not in floor2:
            floor2.append(fl)
    linefloor = ''
    for flr in floor2:
        linefloor += flr + ', '
        
    teeth2 = []
    for t in teeth:
        if t not in teeth2:
            teeth2.append(t)
    lineteeth = ''
    for tth in teeth2:
        lineteeth += tth + ', '
        
    hair2 = []
    for hr in hair:
        if hr not in hair2:
            hair2.append(hr)
    linehair = ''
    for hai in hair2:
        linehair += hai + ', '
        
    room2 = []
    for r in room:
        if r not in room2:
            room2.append(r)
    lineroom = ''
    for rm in room2:
        lineroom += rm + ', '
        
    body2 = []
    for b in body:
        if b not in body2:
            body2.append(b)
    linebody = ''
    for bd in body2:
        linebody += bd + ', '
        
    window2 = []
    for w in window:
        if w not in window2:
            window2.append(w)
    linewindow = ''
    for ww in window2:
        linewindow += ww + ', '
        
    face2 = []
    for fc in face:
        if fc not in face2:
            face2.append(fc)
    lineface = ''
    for fac in face2:
        lineface += fac + ', '
        
    clothes2 = []
    for cl in clothes:
        if cl not in clothes2:
            clothes2.append(cl)
    lineclothes = ''
    for clo in clothes2:
        lineclothes += clo + ', '
        
    dishes2 = []
    for d in dishes:
        if d not in dishes2:
            dishes2.append(d)
    linedishes = ''
    for dis in dishes2:
        linedishes += dis + ', '
        
    return render_template('stats.html', linelang=linelang, lineapple=lineapple, linehands=linehands, \
                           linefloor=linefloor, lineteeth=lineteeth, linehair=linehair, lineroom=lineroom, \
                           linebody=linebody, linewindow=linewindow, lineface=lineface, lineclothes=lineclothes, \
                           linedishes=linedishes)

@app.route('/json')
def jsonfun():
    f = open ('verbs.txt', 'r', encoding = 'utf-8')
    text = f.readlines()
    arr = []
    for line in text:
        x = line.split(', ')
        for i in x:
            arr.append(i)
    f.close()
        
    data = json.dumps(arr, ensure_ascii=False)
    return render_template ('jsons.html', data=data)

@app.route('/search')
def search():
    return 'тут будет поиск'

@app.route('/results')
def results():
    return 'вот что ты искал'

if __name__ == '__main__':
    app.run(debug=True)
