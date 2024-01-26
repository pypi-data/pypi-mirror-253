from datetime import datetime
from typing import Optional

from sqlalchemy import func

from fastapix.crud import Field, SQLModel


class PkMixin(SQLModel):
    id: int = Field(default=None, title="ID", primary_key=True, nullable=False, create=False, update=False)


class CreateTimeMixin(SQLModel):
    create_time: datetime = Field(default_factory=datetime.now, title="Create Time", create=False, update=False)


class UpdateTimeMixin(SQLModel):
    update_time: Optional[datetime] = Field(
        default_factory=datetime.now,
        title="Update Time",
        sa_column_kwargs={"onupdate": func.localtimestamp()},
        create=False,
        update=False
    )


class DeleteTimeMixin(SQLModel):
    delete_time: Optional[datetime] = Field(None, title="Delete Time", create=False)


class CUDTimeMixin(CreateTimeMixin, UpdateTimeMixin, DeleteTimeMixin):
    pass
