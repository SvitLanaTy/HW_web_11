from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = 'contacts'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), index=True)
    last_name: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(80), unique=True, index=True, nullable=True)
    phone_number: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    birthday: Mapped[str] = mapped_column(Date, nullable=True)
    extra_data: Mapped[str] = mapped_column(String(150), nullable=True)
    
   
