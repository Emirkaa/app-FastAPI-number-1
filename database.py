from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



engine = create_engine('postgresql://postgres:1232323@localhost/pizza_delivery',
                       echo=True
                       )

#Создание базового класса для определения декларативного класса и присвоение 
Base=declarative_base()
Session=sessionmaker()
