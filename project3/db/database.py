from sqlmodel import Session, create_engine

DATABASE_URL="sqlite:///./todo.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def get_session():
    try:
        with Session(engine) as session:
            yield session
    finally:
        session.close()
