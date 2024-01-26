from dotenv import load_dotenv
load_dotenv()
from database_mysql_local.generic_crud import GenericCRUD  # noqa402
from logger_local.Logger import Logger  # noqa402
from .event_external_constants import EventExternalLocalConstants  # noqa402
from python_sdk_remote.utilities import validate_url  # noqa402

logger = Logger.create_logger(object=EventExternalLocalConstants.EXTERNAL_EVENT_LOCAL_CODE_LOGGER_OBJECT)


class EventExternalLocal(GenericCRUD):
    def __init__(self, is_test_data: bool = False) -> None:
        super().__init__(default_schema_name=EventExternalLocalConstants.EXTERNAL_EVENT_SCHEMA_NAME,
                         default_table_name=EventExternalLocalConstants.EXTERNAL_EVENT_TABLE_NAME,
                         default_id_column_name=EventExternalLocalConstants.EXTERNAL_EVENT_ID_COLUMN_NAME,
                         default_view_table_name=EventExternalLocalConstants.EXTERNAL_EVENT_VIEW_NAME)
        self.is_test_data = is_test_data

    def insert(self, event_external_json: dict = {}) -> int:
        # adding variables validation might be good
        event_external_json['is_test_data'] = self.is_test_data
        logger.start("start insert event_external", object={'event_external_json': event_external_json})
        url = event_external_json.get("url")
        if url and not validate_url(url):
            logger.error("update_by_event_external_id error, url is not valid")
            logger.end("end insert event_external")
            raise ValueError("url is not valid")
        event_external_id = super().insert(data_json=event_external_json)
        logger.end("end insert event_external", object={
            'event_external_id': event_external_id
        })
        return event_external_id

    def delete_by_event_external_id(self, event_external_id) -> None:
        logger.start("start delete_by_event_external_id",
                     object={'event_external_id': event_external_id})

        super().delete_by_id(id_column_value=event_external_id)
        logger.end("end delete_by_event_external_id event_external")
        return

    def update_by_event_external_id(self, event_external_id: int,
                                    event_external_json: dict) -> None:
        event_external_json['is_test_data'] = self.is_test_data

        logger.start("start update_by_event_external_id event_external",
                     object={'event_external_id': event_external_id, 'event_external_json': event_external_json})

        url = event_external_json.get("url")
        if url and not validate_url(url):
            logger.error("update_by_event_external_id error, url is not valid")
            logger.end("end update_by_event_external_id event_external")
            raise ValueError("url is not valid")

        super().update_by_id(id_column_value=event_external_id,
                             data_json=event_external_json)
        logger.end("end update_by_event_external_id event_external")
        return

    def select_by_event_external_id(self, event_external_id: int) -> dict:
        logger.start("start select_by_event_external_id",
                     object={'event_external_id': event_external_id})

        event_external = super().select_one_dict_by_id(id_column_value=event_external_id)

        logger.end("end select_by_event_external_id",
                   object={'event_external': event_external})
        return event_external

    def get_event_external_test_id(self) -> int:
        return super().get_test_entity_id(entity_name="event_external",
                                          insert_function=self.insert,
                                          view_name="event_external_view",
                                          entity_creator=self.create_test_event)

    def create_test_event(location_id: int = None, is_test_data=True):
        return {
            'is_test_data': is_test_data,
        }
