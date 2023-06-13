from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
    username = Column(String, nullable=False, unique=True)
    member = Column(Boolean, nullable=False, server_default="FALSE")
    
class Vote(Base):
    __tablename__ = "votes"

    post_id= Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    user_id= Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)

class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True, nullable=False)
    show_name = Column(String, nullable=False)
    show_air_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW(), INTERVAL 1 DAY'))
    show_end_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW(), INTERVAL 1 DAY, INTERVAL 1 HOUR'))



class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, nullable=False)
    page_number= Column(String, nullable=True)
    slug= Column(String, nullable=False)
    segment= Column(String, nullable=False)
    writer= Column(String, nullable=True)
    editor= Column(String, nullable=True)
    source= Column(String, nullable=True)
    mos_objects = Column(ARRAY(String), nullable=True)
    last_modified_by= Column(String, nullable=False)
    estimated_time= Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
    show_id = Column(Integer, ForeignKey('shows.id'), nullable=False)
    show = relationship("Show")

