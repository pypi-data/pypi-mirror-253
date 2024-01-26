from pymongo import errors, ASCENDING
from pymongo.errors import DuplicateKeyError

from ... import get_logger
from ...espresso_orm.exception import api_exceptions
from ...espresso_orm.fields import Field

# Configure logging
log = get_logger(__name__)


def check_mongo_connection(client):
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command("ismaster")
    except errors.ConnectionFailure:
        raise api_exceptions.DatabaseConnectionDownException()


def indexing_unique(cls):
    log.debug("Automate create database index for unique field")
    unique_fields = [
        name
        for name in dir(cls)
        if "_" not in name and isinstance(getattr(cls, name), Field) and getattr(cls, name).unique
    ]
    log.debug(
        f"unique_fields in class: {cls.__name__}: {[field_name for field_name in unique_fields]}"
    )

    # check if there is abandon unique index, if it does remove it
    log.debug("# check if there is abandon unique index, if it does remove it")
    unique_indexes = [
        {
            "field": "_".join(index.get("name").split("_")[:-1]),
            "name": index.get("name"),
        }
        for index in cls.collection.list_indexes()
        if index.get("unique")
    ]
    for unique_index in unique_indexes:
        log.debug(f"unique_indexes: {unique_indexes}")
        if unique_index.get("field") not in [field_name for field_name in unique_fields]:
            log.debug(f"removing abandon unique-index name: {unique_index.get('name')}")
            cls.collection.drop_index(unique_index.get("name"))

    # create index for unique field
    log.debug("# create index for unique field")
    try:
        if unique_fields:
            for field_name in unique_fields:
                cls.collection.create_index([(field_name, ASCENDING)], unique=True)
    except DuplicateKeyError as de:
        log.error("seems like the unique key has duplicated value", de)
        raise

    return cls
