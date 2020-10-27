import json
from typing import Dict, Any, Tuple, MutableMapping
from schematics.models import Model  # type: ignore
from schematics.types import UUIDType, ModelType, StringType, DictType  # type: ignore
from schematics.exceptions import DataError  # type: ignore


class APIConfig(Model):
    id = UUIDType()
    name = StringType()
    short_name = StringType(serialized_name="short-name")
    human_readable_name = StringType(serialized_name="human-readable-name")


class SpecConfig(Model):
    id = UUIDType()
    title = StringType()
    path = StringType()


class APIManifest(Model):
    api = ModelType(APIConfig)
    specs = DictType(ModelType(SpecConfig))


def validate(manifest: MutableMapping[str, Any]) -> Tuple[bool, Dict[str, Any]]:
    try:
        m = APIManifest(manifest)
        m.validate()
        return True, {}
    except DataError as e:
        error_json = json.loads(str(e))
        return False, error_json
