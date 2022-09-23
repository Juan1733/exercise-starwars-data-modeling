import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table users
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    created_at = Column(Date)
    favorites = relationship("Favorite")

class Favorite(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table favorites.
    
    id = Column(Integer, primary_key=True)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(Integer)
    id_user = Column(Integer, ForeignKey("users.id"))
    id_personaje = Column(Integer, ForeignKey('personajes.id'))
    id_planet = Column(Integer, ForeignKey('planetas.id'))
    personajes = relationship("Personaje", back_populates="favorites", uselist=False)
    planetas = relationship("Planeta", back_populates="favorites", uselist=False)

class Personaje(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table personajes
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    favorites_key = Column(Integer, ForeignKey("favorites.id"))

class Planeta(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table planetas
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites_key = Column(Integer, ForeignKey('favorites.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')