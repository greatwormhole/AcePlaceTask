import json
from uuid import UUID
from bson import ObjectId, binary

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID) or isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, binary.Binary):
            return str(obj)
        return json.JSONEncoder.default(self, obj)