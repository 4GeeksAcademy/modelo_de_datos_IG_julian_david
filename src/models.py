from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(16) unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(120) unique=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(120)unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    post: Mapped["Post"] = db.relationship(back_populates="user")
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
 


    def serialize(self):
        return{
            "id": self.id,
            
        }
    
class Follower(db.Model):
    user_from_id: Mapped[int] = mapped_column(primary_key=True)



    user_to_id: Mapped[int] = mapped_column(primary_key=True)
