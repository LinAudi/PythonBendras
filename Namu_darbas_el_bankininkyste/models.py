from sqlalchemy import Table, UniqueConstraint, ForeignKey, Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///bankininkyste.sqlite")
Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    surname = Column("surname", String)
    social_security_no = Column("social_security_no", Integer, unique=True)
    phone_no = Column("phone_no", String)
    accounts = relationship("Account", back_populates="person")


class Bank(Base):
    __tablename__ = "bank"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    address = Column("address", String)
    swift_code = Column("swift_code", String)
    accounts = relationship("Account", back_populates="bank")


class Account(Base):
    __tablename__ = "account"
    id = Column("id", Integer, primary_key=True)
    iban_no = Column("iban_no", String)
    balance = Column("balance", Float)
    person_id = Column("person_id", Integer, ForeignKey("person.id"))
    bank_id = Column("bank_id", Integer, ForeignKey("bank.id"))
    person = relationship("Person", back_populates="accounts")
    bank = relationship("Bank", back_populates="accounts")


Base.metadata.create_all(engine)
