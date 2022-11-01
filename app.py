from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.jozqduq.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/notes", methods=["POST"])
def notes_post():
    writer_receive = request.form["writer_give"]
    content_receive = request.form["content_give"]

    doc = {
        'writer': writer_receive,
        'content': content_receive
    }

    db.notes.insert_one(doc)

    return jsonify({'msg':'작성 완료'})

@app.route("/notes", methods=["GET"])
def notes_get():
    comment_list = list(db.notes.find({},{'_id':False}))
    return jsonify({'comment':comment_list})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

   35214