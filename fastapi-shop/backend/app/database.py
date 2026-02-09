
from sqlalchemy.ext.asyncio import async_sessionmaker, async_session, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

class Base(DeclarativeBase):
    pass

engine = create_async_engine(settings.database_url, echo=True)
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    async with new_session() as session:
        yield session
        
async def init_db():
    Base.metadata.create_all(bind=engine)