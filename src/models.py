import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(500), nullable=False)
    password = Column(String(500), nullable=False)
    favorites = relationship('Favorites', back_populates='user')

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(800), nullable=False)
    height = Column(String(250), nullable=False)
    weight = Column(String(250), nullable=False)
    favorites = relationship('Favorites', back_populates='characters')

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(800), nullable=False)
    population = Column(String(250), nullable=False)
    weather = Column(String(250), nullable=False)
    favorites = relationship('Favorites', back_populates='planets')

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_characters = Column(Integer, ForeignKey('characters.id'), nullable=True)
    characters = relationship("Characters", back_populates='favorites')
    id_planets = Column(Integer, ForeignKey('planets.id'), nullable=True)
    planets = relationship("Planets", back_populates='favorites')
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates='favorites')
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


##person_id = Column(Integer, ForeignKey('person.id'))
##    person = relationship(Person)