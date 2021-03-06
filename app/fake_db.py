import datetime
from dateutil import parser
import json
import random

class Singleton(object):
  _instances = {}
  def __new__(class_, *args, **kwargs):
    if class_ not in class_._instances:
        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
    return class_._instances[class_]

class FakeDB(Singleton):
  def __init__(self):
    self.images = []
    with open('images/tagged_data.json') as f:
      self.data = json.load(f)
      for d in self.data:
        self.images.append(Image(d['id'], d['captured_on'], d['lat'], d['lon'], d['tags'], d))

  def FilterByDate(self, days):
    diff = datetime.now() + datetime.timedelta(-days)
    return filter(lambda x: x.captured_on >= diff, self.images)

  def FilterByTag(self, tags):
    if len(tags) == 0:
      return self.images
    tags = set(tags)
    return filter(lambda x: tags & set([t['tag'] for t in x.tags]), self.images)

class Image:
  FAKE_TAGS = ['Pine trees', 'Fire hydrants', 'Handicap accessible entrances',
      'Construction', 'Subway stops', 'Everygreen trees', 'Retail shops']

  def __init__(self, image_id, captured_on, lat, lon, tags, json):
    self.image_id = image_id
    self.captured_on = parser.parse(captured_on)
    self.lat = lat
    self.lon = lon
    self.json = json
    self.tags = []
    if tags:
      self.tags = tags
    """
    else:
      self.tags = []
      for tag in self.FAKE_TAGS:
        if random.random() < 0.3:
          self.tags.append({'tag': tag, 'h': 0, 'w': 0, 'x': 0, 'y': 0})
    self.json['tags'] = self.tags
    """

  def GetTags(self):
    return [t['tag'] for t in self.tags]

  def GetCompleteTags(self):
    return self.tags

  def __repr__(self):
    return '<Image %r>' % (self.image_id)

class Tag:
  def __init__(self, tag, h=0, w=0, x=0, y=0):
    self.tag = tag
    self.h = h
    self.w = w
    self.x = x
    self.y = y

  def __repr__(self):
    return '<Tag %r for image %r>' % (self.tag, self.image_id)

