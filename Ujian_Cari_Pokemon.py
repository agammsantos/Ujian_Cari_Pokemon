from flask import redirect, request, Flask, render_template
import json, requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.htm')

@app.route('/hasil', methods=['POST'])
def post():
    name=request.form['nama']
    url='https://pokeapi.co/api/v2/pokemon/'+name
    poke=requests.get(url)
    if str(poke)=='<Response [404]>':
        return redirect('/NotFound')
    filenama=poke.json()['name']
    besar=filenama[0].upper()
    nama=besar+filenama[1:]
    filegambar=poke.json()['sprites']
    gambar=filegambar['front_default']
    idPoke=poke.json()['id']
    berat=poke.json()['weight']
    tinggi=poke.json()['height']
    files=[nama,gambar,idPoke,berat,tinggi]
    return render_template('hasil.htm',x=files)

@app.route('/NotFound')
def notFound():
    return render_template('error.htm')

@app.errorhandler(404)
def notFound404(error):
    return render_template('error.htm')

if __name__=='__main__':
    app.run(debug=True)