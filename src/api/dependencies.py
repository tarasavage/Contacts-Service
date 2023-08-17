from typing import Annotated

from fastapi import Depends

from src.utils.unit_of_work import IUnitOfWork, UnitOfWork

UOWDependency = Annotated[IUnitOfWork, Depends(UnitOfWork)]
