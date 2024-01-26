from datetime import datetime
from typing_extensions import Optional, Annotated

from sqlalchemy import func

from fastapix.crud import Field, SQLModel
from fastapix.common.pydantic import PYDANTIC_V2


class PkMixin(SQLModel):
    id: int = Field(default=None, title="ID", primary_key=True, nullable=False, create=False, update=False)


if PYDANTIC_V2:
    from pydantic.functional_serializers import PlainSerializer
    from fastapix.common.serializer import convert_datetime_to_chinese
    DATETIME = Annotated[datetime, PlainSerializer(convert_datetime_to_chinese)]
else:
    DATETIME = datetime


class CreateTimeMixin(SQLModel):
    create_time: DATETIME = Field(default_factory=DATETIME.now, title="Create Time", create=False, update=False)


class UpdateTimeMixin(SQLModel):
    update_time: Optional[DATETIME] = Field(
        default_factory=DATETIME.now,
        title="Update Time",
        sa_column_kwargs={"onupdate": func.localtimestamp()},
        create=False,
        update=False
    )


class DeleteTimeMixin(SQLModel):
    delete_time: Optional[DATETIME] = Field(None, title="Delete Time", create=False)


class CUDTimeMixin(CreateTimeMixin, UpdateTimeMixin, DeleteTimeMixin):
    pass
