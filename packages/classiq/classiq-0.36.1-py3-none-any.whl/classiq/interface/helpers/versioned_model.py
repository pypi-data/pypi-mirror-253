import pydantic

from classiq.interface._version import VERSION


class VersionedModel(pydantic.BaseModel, extra=pydantic.Extra.forbid):
    version: str = pydantic.Field(default=VERSION)
