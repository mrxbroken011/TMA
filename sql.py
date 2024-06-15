import threading
from sqlalchemy import create_engine, Column, TEXT, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session



def start() -> scoped_session:
    engine = create_engine("postgresql://sgpostgres:PtU2-lwHUx5BMM8X@SG-brokenx-63530.servers.mongodirector.com/brokenx", client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

BASE = declarative_base()
SESSION = start()

class Broadcast(BASE):
    __tablename__ = "broadcast"
    id = Column(Numeric, primary_key=True)
    user_name = Column(TEXT)

    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name

# Use session context manager for safe session handling
def add_user(id, user_name):
    with SESSION() as session:
        msg = session.query(Broadcast).get(id)
        if not msg:
            usr = Broadcast(id, user_name)
            session.add(usr)
            session.commit()

def query_msg():
    with SESSION() as session:
        query = session.query(Broadcast.id).order_by(Broadcast.id).all()
        return query
