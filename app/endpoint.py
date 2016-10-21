from fake_db import FakeDB
from flask import Flask, render_template, request, send_from_directory
import sys
app = Flask(__name__)

tmp = FakeDB()
print [(i.image_id, i.GetTags()) for i in tmp.images]

@app.route("/")
def hello():
  return render_template('index.html', images=tmp.images)

@app.route("/echo", methods=['POST'])
def echo():
  tags = filter(lambda x: x != '', request.form['text'].split(','))
  images = tmp.FilterByTag(tags)
  return render_template('index.html', images=images)

@app.route('/images/<path:filename>')
def pictures(filename):
  return send_from_directory('images', filename, as_attachment=True)

if __name__ == "__main__":
  app.run(debug=True)
