# Define the database

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key = True)
    fname = Column(String(100))
    lname = Column(String(100))
    rxr = Column(String(10), unique = True)
    nhs = Column(String(15))
    dob = Column(Date)

class Record_sources(Base):
    __tablename__ = 'record_sources'
    id = Column(Integer, primary_key = True)
    short = Column(String(10), unique = True)
    description = Column(String(100))

class Oximetry(Base):
    __tablename__ = 'oximetry'
    id = Column(Integer, primary_key = True)
    subject = Column(Integer, ForeignKey('patient.id'))
    subject_rel = relationship(Patient)
    source = Column(Integer, ForeignKey('record_sources.id'))
    source_rel = relationship(Record_sources)
    study_date = Column(Date)
    odi = Column(Float)
    hri = Column(Float)
    report = Column(Text)

class Spirometry(Base):
    __tablename__ = 'spirometry'
    id = Column(Integer, primary_key = True)
    
    subject = Column(Integer, ForeignKey('patient.id'))
    subject_rel = relationship(Patient)
    source = Column(Integer, ForeignKey('record_sources.id'))
    source_rel = relationship(Record_sources)
    
    study_date = Column(Date)
    
    fev1_pre = Column(Float)
    fev1_pre_pred = Column(Float)
    fev1_pre_percent_pred = Column(Float)
    fev1_pre_SR = Column(Float)

    fvc_pre = Column(Float)
    fvc_pre_pred = Column(Float)
    fvc_pre_percent_pred = Column(Float)
    fvc_pre_SR = Column(Float)

    fev1_post = Column(Float)
    fev1_post_pred = Column(Float)
    fev1_post_percent_pred = Column(Float)
    fev1_post_SR = Column(Float)

    fvc_post = Column(Float)
    fvc_post_pred = Column(Float)
    fvc_post_percent_pred = Column(Float)
    fvc_post_SR = Column(Float)
  
class Lungfunc(Base):
    __tablename__ = 'lungfunc'
    id = Column(Integer, primary_key = True)
    
    subject = Column(Integer, ForeignKey('patient.id'))
    subject_rel = relationship(Patient)
    source = Column(Integer, ForeignKey('record_sources.id'))
    source_rel = relationship(Record_sources)
    spiro = Column(Integer, ForeignKey('spirometry.id'))
    spiro_rel = relationship(Spirometry)

    study_date = Column(Date)

    tlco = Column(Float)
    tlco_pred = Column(Float)
    tlco_percent_pred = Column(Float)
    tlco_SR = Column(Float)
    
    vasb = Column(Float)
    vasb_pred = Column(Float)
    vasb_percent_pred = Column(Float)

    kco = Column(Float)
    kco_pred = Column(Float)
    kco_percent_pred = Column(Float)

    frc = Column(Float)
    frc_pred = Column(Float)
    frc_percent_pred = Column(Float)
    frc_SR = Column(Float)

    vc = Column(Float)
    vc_pred = Column(Float)
    vc_percent_pred = Column(Float)
    vc_SR = Column(Float)

    tlc = Column(Float)
    tlc_pred = Column(Float)
    tlc_percent_pred = Column(Float)
    tlc_SR = Column(Float)

    rv = Column(Float)
    rv_pred = Column(Float)
    rv_percent_pred = Column(Float)
    rv_SR = Column(Float)

    tlcrv = Column(Float)
    tlcrv_pred = Column(Float)
    tlcrv_percent_pred = Column(Float)
    tlcrv_SR = Column(Float)   