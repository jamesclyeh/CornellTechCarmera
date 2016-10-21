from sqlalchemy import Column, Integer, String, DateTime, Float
from database import Base

class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True),
    image_id = Column(Integer, unique=True),
    captured_on = Column(DateTime, default=datetime.date.utcnow),
    lat = Column(Float),
    lon = Column(Float)

    def __init__(self, name=None, captured_on=None, lat=None, lon=None):
        self.name = name
        self.captured_on = captured_on
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return '<Imgage %r>' % (self.name)

class Tag(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True),
    image_id = Column(Integer, ForeignKey("image.image_id")),
    tag = Column(String(50)),
    h = Column(Float),
    w = Column(Float),
    x = Column(Float),
    y = Column(Float)

    def __init__(self, image_id=None, tag=None, h=None, w=None, x=None, y=None):
        self.name = name
        self.image_id = image_id
        self.tag = tag
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def __repr__(self):
        return '<Tag %r for image %r>' % (self.tag, self.image_id)

