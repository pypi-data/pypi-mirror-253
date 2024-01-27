from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

data_to_insert = []


class UserValidationStatus(Base):
    __tablename__ = 'user_validation_status'

    user_validation_status_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    status_description = Column(String, nullable=False, unique=True)


data_to_insert.extend([
    UserValidationStatus(status_description="pending"),
    UserValidationStatus(status_description="verified")
])


class UserRegistration(Base):
    __tablename__ = 'user_registration'

    user_registration_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    registration_description = Column(String, nullable=False, unique=True)


data_to_insert.extend([
    UserRegistration(registration_description="email")
])


class HashingAlgorithm(Base):
    __tablename__ = 'hashing_algorithm'

    hash_algorithm_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    algorithm_name = Column(String, nullable=False, unique=True)


data_to_insert.extend([
    HashingAlgorithm(algorithm_name="bcrypt")
])


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_email_id = Column(String, nullable=False, unique=True)
    user_password_hash = Column(String, nullable=False, unique=True)
    user_password_salt = Column(String, nullable=False, unique=True)
    user_validation_status_id = Column(Integer, ForeignKey(UserValidationStatus.user_validation_status_id,
                                                           ondelete="RESTRICT", onupdate="RESTRICT"), index=True,
                                       nullable=False)
    user_registration_id = Column(Integer, ForeignKey(UserRegistration.user_registration_id,
                                                      ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False)
    hash_algorithm_id = Column(Integer, ForeignKey(HashingAlgorithm.hash_algorithm_id,
                                                   ondelete="RESTRICT", onupdate="RESTRICT"), nullable=False)