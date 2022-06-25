import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm

from date.db_session import SqlAlchemyBase


class Post(SqlAlchemyBase, UserMixin):
    __tablename__ = 'post'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_data = sqlalchemy.Column(sqlalchemy.DateTime)

    is_private = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
