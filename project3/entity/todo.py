from sqlmodel import Field, SQLModel


class Todos(SQLModel, table=True):
    __tablename__ = 'todos'

    id: int = Field(primary_key=True, index=True)
    title: str
    description: str
    priority:int
    complete: bool
    #owner_id: int = Field(ForeignKey("users.id"))