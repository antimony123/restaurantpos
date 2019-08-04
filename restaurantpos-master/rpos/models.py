#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import DATETIME, DECIMAL, INTEGER, TINYINT, VARCHAR

from rpos.db import Base

import string, random

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(INTEGER(11), primary_key=True)
    description = Column(VARCHAR(256), nullable=False)
    stock = Column(DECIMAL(precision=10, scale=2, unsigned=True, zerofill=True), nullable=False)
    unit = Column(VARCHAR(50), nullable=False)
    cost = Column(DECIMAL(precision=10, scale=2, unsigned=True, zerofill=True), nullable=False)
    low_threshold = Column(INTEGER(3), nullable=False)

    def __init__(self, description='New Item', stock=0.0, unit='oz', cost=0.00, low_threshold=100):
        self.description = description
        self.stock = stock
        self.unit = unit
        self.cost = cost
        self.low_threshold = low_threshold

    def __repr__(self):
        return '<Ingredient %r>' % (self.description)


class MenuItem(Base):
    __tablename__ = 'menu'
    id = Column(INTEGER(11), primary_key=True)
    description = Column(VARCHAR(256)) # rationale behind menu desc being null by default?
    price = Column(DECIMAL(precision=10, scale=2, unsigned=True, zerofill=True), nullable=False)
    category = Column(VARCHAR(10), nullable=False)

    def __init__(self, description='New Item', price=0, category='Food', cost=0):
        self.description = description
        self.price = price
        self.category = category

    def __repr__(self):
        return '<Menu Item %r>' % (self.description)

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(INTEGER(11), primary_key=True)
    menu_id = Column(INTEGER(11))
    menu_description = Column(VARCHAR(256))
    ingredient_id = Column(INTEGER(11))
    ingredient_description = Column(VARCHAR(256))
    ingredient_quantity = Column(DECIMAL(precision=10, scale=2, unsigned=True, zerofill=True))
    to_show = Column(TINYINT(4), nullable=False)

    def __init__(self, menu_id=None, menu_desciption=None, ingredient_id=None, \
                ingredient_description=None, ingredient_quantity=0, to_show=1):
        self.menu_id = menu_id
        self.menu_desciption = menu_desciption
        self.ingredient_id = ingredient_id
        self.ingredient_description = ingredient_description
        self.ingredient_quantity = ingredient_quantity
        self.to_show = to_show

    def __repr__(self):
        return '<Recipe: Ingredient %r for Menu Item %r>' % (self.ingredient_description, self.menu_desciption)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(10), unique=True, nullable=False)
    password = Column(VARCHAR(2048), nullable=True)
    isadmin = Column(TINYINT(4), nullable=False)

    def __init__(self, username=None, password=None, isadmin=0):
        self.username = "User " + ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        self.password = password
        self.isadmin = isadmin

    def __repr__(self):
        return '<User %r>' % (self.username)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(INTEGER(11), primary_key=True)
    ordertime = Column(DATETIME)
    orderid = Column(VARCHAR(20), nullable=False)
    guestname = Column(VARCHAR(256), nullable=False)
    mainorder = Column(INTEGER(11), nullable=False)
    detail = Column(INTEGER(11))
    quantity = Column(DECIMAL(precision=10, scale=2))
    active = Column(INTEGER(1))

    def __init__(self, orderid=None, ordertime=None, guestname=None, mainorder=None, detail=None, quantity=None, active=0):
        self.orderid = orderid
        self.ordertime = ordertime
        self.guestname = guestname
        self.mainorder = mainorder
        self.detail = detail
        self.quantity = quantity
        self.active = active

    def __repr__(self):
        return '<Order %r>' % (self.orderid)