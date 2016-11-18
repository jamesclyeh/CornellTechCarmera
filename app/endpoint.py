from fake_db import FakeDB
from flask import Flask, render_template, request, send_from_directory
import json
import itertools
import sys
app = Flask(__name__)

tmp = FakeDB()
print [(i.image_id, i.GetTags()) for i in tmp.images]

@app.route("/")
def hello():
  all_tags = set(itertools.chain(*[im.GetTags() for im in tmp.images]))
  return render_template('index.html',
      images=tmp.images, data=tmp.data, all_tags=all_tags)

@app.route("/test")
def test():
  return render_template('annotation.html', images=[tmp.images[0]])

@app.route("/filterByTag", methods=['POST'])
def filterByTag():
  print request.args['tags']
  tags = filter(lambda x: x != '', request.args['tags'].split(','))
  print 'Filtering'
  print tags
  images = tmp.FilterByTag(tags)
  print images
  return json.dumps([im.json for im in images])

@app.route('/images/<path:filename>')
def pictures(filename):
  return send_from_directory('images', filename, as_attachment=True)

if __name__ == "__main__":
  app.run(debug=True)
