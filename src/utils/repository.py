from abc import ABC, abstractmethod

from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, instance_id):
        raise NotImplementedError

    @abstractmethod
    async def update(self, instance_id, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, instance_id):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, **kwargs) -> int:
        stmt = insert(self.model).values(**kwargs).returning(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def get_all(self, skip: int = 0, limit: int = 100):
        stmt = select(self.model).offset(skip).limit(limit)
        result = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]

    async def get_by_id(self, instance_id):
        stmt = select(self.model).where(self.model.id == instance_id)
        result = await self.session.execute(stmt)
        return result.scalar_one().to_read_model()

    async def update(self, instance_id, **kwargs) -> int:
        stmt = (
            update(self.model)
            .values(**kwargs)
            .filter_by(id=instance_id)
            .returning(self.model.id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def delete(self, instance_id):
        stmt = (
            delete(self.model)
            .where(self.model.id == instance_id)
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one().to_read_model()
