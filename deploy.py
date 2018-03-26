from flask import Flask, render_template, request, jsonify
from recommender import ret_name, ret_id
from search import find 

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def main():
    list1=ret_name('101')
    list2=ret_id('101')
    return render_template("index.html",s1=list1,s2=list2)


@app.route('/a',methods=['GET'])
def a():
    if request.method == 'GET':
        song = request.args.get('song_data')
        list1=ret_name(song)
        list2=ret_id(song)
        return jsonify({'s1':list1,'s2':list2})
        
@app.route('/b',methods=['GET'])
def b():
    if request.method == 'GET':
        name=request.args.get('song_name')
        sugg_list=find(name)
        return jsonify({'sugg':sugg_list})

if __name__ == '__main__':
   app.run(debug=True)


   #if request.method == 'GET':
           #song1 = request.form['input']
           #x=request.get_json()

           #song1=request.args.get('song_data')
           #if song1==None:
           #    song1='101'
           #song2= func(song1)
           #return render_template("index.html",s1=song1,s2=song2)
          #return render_template("index.html",{'s1':json.dumps(song1),'s2':json.dumps(song2)})

       #else:
       #    song1=request.json['song_data']
       #    song2=func('102')
       #    return song1
