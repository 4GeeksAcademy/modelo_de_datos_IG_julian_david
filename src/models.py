from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(16), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    post: Mapped["Post"] = db.relationship(back_populates="user")
    following: Mapped[int] = db.relationship(back_populates="following")
    follower: Mapped[int] = db.relationship(back_populates="follower")
    author: Mapped[int] = db.relationship(back_populates="author")


    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name
            # do not serialize the password, its a security breach
        }
    
class Post(db.Model):
    id: Mapped[int] =mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    author: Mapped["User"] = db.relationship(back_populates="posts")

    post: Mapped[int] = db.relationship(back_populates="post")
    post_: Mapped[int] = db.relationship(back_populates="post")

 


    def serialize(self):
        return{
            "id": self.id,
            
        }
    
class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    following_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    following: Mapped[int] = db.relationship(back_populates="following")


    follower_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    follower: Mapped[int] = db.relationship(back_populates="follower")

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(500))

    author_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    author: Mapped[int] = db.relationship(back_populates="author")

    post_id: Mapped[int] = mapped_column(db.ForeignKey("post.id"))
    post: Mapped[int] = db.relationship(back_populates="post")

class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    # type: Mapped[enumerate] = mapped_column()
    url: Mapped[str] = mapped_column(String(500))

    post_id: Mapped[int] = mapped_column(db.ForeignKey("post.id"))
    post_: Mapped[int] = db.relationship(back_populates="post")

