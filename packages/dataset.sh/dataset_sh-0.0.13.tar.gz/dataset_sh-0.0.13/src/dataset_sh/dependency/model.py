from typing import List, Optional
from pydantic import BaseModel, Field


class DatasetDependencyItem(BaseModel):
    name: str

    version: Optional[str] = None
    tag: Optional[str] = None


class DatasetDependencyHostGroup(BaseModel):
    host: str
    datasets: List[DatasetDependencyItem] = Field(default_factory=list)


class DatasetDependencies(BaseModel):
    datasets_by_host: List[DatasetDependencyHostGroup] = Field(default_factory=list)
