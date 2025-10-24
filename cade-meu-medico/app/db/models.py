import enum 
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Table 
from sqlalchemy.orm import relationship 
from app.db.base_class import Base 
 
class UserRole(str, enum.Enum): 
    user = "user" 
    admin = "admin" 
 
doctor_specialties = Table( 
    'doctor_specialties', 
    Base.metadata, 
    Column('doctor_id', Integer, ForeignKey('doctors.id'), primary_key=True), 
    Column('specialty_id', Integer, ForeignKey('specialties.id'), primary_key=True) 
) 
 
doctor_cities = Table( 
    'doctor_cities', 
    Base.metadata, 
    Column('doctor_id', Integer, ForeignKey('doctors.id'), primary_key=True), 
    Column('city_id', Integer, ForeignKey('cities.id'), primary_key=True) 
) 
 
class User(Base): 
    __tablename__ = 'users' 
    id = Column(Integer, primary_key=True, index=True) 
    full_name = Column(String(100), index=True) 
    email = Column(String(100), unique=True, index=True, nullable=False) 
    hashed_password = Column(String, nullable=False) 
    role = Column(Enum(UserRole), default=UserRole.user, nullable=False) 
 
class Doctor(Base): 
    __tablename__ = 'doctors' 
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(100), index=True, nullable=False) 
    crm = Column(String(20), unique=True, index=True, nullable=False) 
 
    # Relacionamentos 
    specialties = relationship("Specialty", secondary=doctor_specialties, back_populates="doctors") 
    cities = relationship("City", secondary=doctor_cities, back_populates="doctors") 
 
class Specialty(Base): 
    __tablename__ = 'specialties' 
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(100), unique=True, index=True, nullable=False) 
 
    doctors = relationship("Doctor", secondary=doctor_specialties, back_populates="specialties") 
 
class City(Base): 
    __tablename__ = 'cities' 
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(100), nullable=False) 
    state = Column(String(2), nullable=False) # Ex: 'SP', 'PR' 
 
    doctors = relationship("Doctor", secondary=doctor_cities, back_populates="cities") 
