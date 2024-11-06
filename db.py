
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# Создаем движок для SQLite базы данных
engine = create_engine('sqlite:///taskmanager.db', echo=True)

# Создаем локальную сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем базовый класс для других моделей
class Base(DeclarativeBase):
    pass
