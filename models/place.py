#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(
            String(60),
            ForeignKey('cities.id'),
            nullable=False)
    user_id = Column(
            String(60),
            ForeignKey('users.id'),
            nullable=False)
    name = Column(
            String(128),
            nullable=False)
    description = Column(
            String(1024),
            nullable=True)
    number_rooms = Column(
            Integer,
            nullable=False,
            default=0)
    number_bathrooms = Column(
            Integer,
            nullable=False,
            default=0)
    max_guest = Column(
            Integer,
            nullable=False,
            default=0)
    price_by_night = Column(
            Integer,
            nullable=False,
            default=0)
    latitude = Column(
            Float,
            nullable=True)
    longitude = Column(
            Float,
            nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE', '') == 'db':
        reviews = relationship(
                'Review',
                backref='place',
                cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            """ returns the list of Reviews instances with place_id
            equals to the current Place.id """
            rev = []
            for r in storage.all('Review').values():
                if self.id == r.place_id:
                    rev.append(r)
            return rev
