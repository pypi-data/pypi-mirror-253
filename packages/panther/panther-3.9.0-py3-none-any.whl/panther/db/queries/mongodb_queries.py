from sys import version_info

from panther.db.connection import db
from panther.db.utils import merge_dicts, prepare_id_for_query
from panther.exceptions import DBException

if version_info >= (3, 11):
    from typing import Self
else:
    from typing import TypeVar

    Self = TypeVar('Self', bound='BaseMongoDBQuery')


class BaseMongoDBQuery:
    @classmethod
    def _merge(cls, *args) -> dict:
        prepare_id_for_query(*args, is_mongo=True)
        return merge_dicts(*args)

    # # # # # Find # # # # #
    @classmethod
    def find_one(cls, _data: dict | None = None, /, **kwargs) -> Self | None:
        if document := db.session[cls.__name__].find_one(cls._merge(_data, kwargs)):
            return cls._create_model_instance(document=document)
        return None

    @classmethod
    def find(cls, _data: dict | None = None, /, **kwargs) -> list[Self]:
        documents = db.session[cls.__name__].find(cls._merge(_data, kwargs))
        return [cls._create_model_instance(document=document) for document in documents]

    @classmethod
    def first(cls, _data: dict | None = None, /, **kwargs) -> Self | None:
        return cls.find_one(_data, **kwargs)

    @classmethod
    def last(cls, _data: dict | None = None, /, **kwargs):
        msg = 'last() is not supported in MongoDB yet.'
        raise DBException(msg)

    # # # # # Count # # # # #
    @classmethod
    def count(cls, _data: dict | None = None, /, **kwargs) -> int:
        return db.session[cls.__name__].count_documents(cls._merge(_data, kwargs))

    # # # # # Insert # # # # #
    @classmethod
    def insert_one(cls, _data: dict | None = None, **kwargs) -> Self:
        document = cls._merge(_data, kwargs)
        document['id'] = db.session[cls.__name__].insert_one(document).inserted_id
        return cls._create_model_instance(document=document)

    # # # # # Delete # # # # #
    def delete(self) -> None:
        db.session[self.__class__.__name__].delete_one({'_id': self._id})

    @classmethod
    def delete_one(cls, _data: dict | None = None, /, **kwargs) -> bool:
        result = db.session[cls.__name__].delete_one(cls._merge(_data, kwargs))
        return bool(result.deleted_count)

    @classmethod
    def delete_many(cls, _data: dict | None = None, /, **kwargs) -> int:
        result = db.session[cls.__name__].delete_many(cls._merge(_data, kwargs))
        return result.deleted_count

    # # # # # Update # # # # #
    def update(self, **kwargs) -> None:
        for field, value in kwargs.items():
            setattr(self, field, value)
        update_fields = {'$set': kwargs}
        db.session[self.__class__.__name__].update_one({'_id': self._id}, update_fields)

    @classmethod
    def update_one(cls, _filter: dict, _data: dict | None = None, /, **kwargs) -> bool:
        prepare_id_for_query(_filter, is_mongo=True)
        update_fields = {'$set': cls._merge(_data, kwargs)}

        result = db.session[cls.__name__].update_one(_filter, update_fields)
        return bool(result.matched_count)

    @classmethod
    def update_many(cls, _filter: dict, _data: dict | None = None, /, **kwargs) -> int:
        prepare_id_for_query(_filter, is_mongo=True)
        update_fields = {'$set': cls._merge(_data, kwargs)}

        result = db.session[cls.__name__].update_many(_filter, update_fields)
        return result.modified_count
