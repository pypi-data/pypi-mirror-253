from .contact_persons_local_constants import CONTACT_PERSONS_PYTHON_PACKAGE_CODE_LOGGER_OBJECT
from logger_local.LoggerLocal import Logger
from database_mysql_local.generic_mapping import GenericMapping
from person_local.src.persons_local import PersonsLocal
from person_local.src.persons_local import Person

logger = Logger.create_logger(object=CONTACT_PERSONS_PYTHON_PACKAGE_CODE_LOGGER_OBJECT)

DEFAULT_SCHEMA_NAME = 'contact_person'
DEFAULT_ENTITY_NAME1 = 'contact'
DEFAULT_ENTITY_NAME2 = 'person'
DEFAULT_ID_COLUMN_NAME = 'contact_person_id'
DEFAULT_TABLE_NAME = 'contact_person_table'
DEFAULT_VIEW_TABLE_NAME = 'contact_person_view'

GENDER_ID = 8  # = Prefer not to respond


class ContactPersonsLocal(GenericMapping):
    def __init__(self, default_schema_name: str = DEFAULT_SCHEMA_NAME, default_entity_name1: str = DEFAULT_ENTITY_NAME1,
                 default_entity_name2: str = DEFAULT_ENTITY_NAME2, default_id_column_name: str = DEFAULT_ID_COLUMN_NAME,
                 default_table_name: str = DEFAULT_TABLE_NAME, default_view_table_name: str = DEFAULT_VIEW_TABLE_NAME,
                 is_test_data: bool = False):

        super().__init__(default_schema_name=default_schema_name, default_entity_name1=default_entity_name1,
                         default_entity_name2=default_entity_name2, default_id_column_name=default_id_column_name,
                         default_table_name=default_table_name, default_view_table_name=default_view_table_name,
                         is_test_data=is_test_data)
        self.persons_local = PersonsLocal()

    def insert_contact_and_link_to_existing_or_new_person(self, contact_dict: dict, contact_email_address: str,
                                                          contact_id: int) -> int:
        """
        Insert contact and link to existing or new person
        :param contact_dict: contact dict
        :param contact_id: contact id
        :param is_test_data: is test data
        :return: contact_person_id
        """
        logger.start(object={"contact_dict": contact_dict, "contact_email_address": contact_email_address,
                             "contact_id": contact_id})
        person_id = self.persons_local.get_person_id_by_email_address(email_address=contact_email_address)
        if person_id is None:
            # create new person and add it to person_table
            logger.info(log_message="person_id is None, creating new person")
            person_object = self._proccess_contact_dict_to_person_class(contact_dict=contact_dict,
                                                                        contact_email_address=contact_email_address)
            result = self.persons_local.insert_if_not_exists(person=person_object)
            if result:
                person_id = result[0]
            contact_person_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                    entity_name2=self.default_entity_name2,
                                                    entity_id1=contact_id, entity_id2=person_id)
        else:
            # link to existing person
            logger.info(log_message="person_id is not None, linking to existing person")
            mapping_tuple = self.select_multi_mapping_tuple_by_id(entity_name1=self.default_entity_name1,
                                                                  entity_name2=self.default_entity_name2,
                                                                  entity_id1=contact_id, entity_id2=person_id)
            if not mapping_tuple:
                logger.info(log_message="mapping_tuple is None, creating new mapping")
                contact_person_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                        entity_name2=self.default_entity_name2,
                                                        entity_id1=contact_id, entity_id2=person_id)
            else:
                # TODO: update person when persons-local will have a more generic update method
                logger.info(log_message="mapping_tuple is not None")
                contact_person_id = mapping_tuple[0][0]

        logger.end()
        return contact_person_id

    def get_person_ids_by_contact_id(self, contact_id: int, limit: int = 1, order_by: str = "contact_person_id DESC") -> list:
        """
        Get person id by contact id
        :param contact_id: contact id
        :param limit: limit
        :param order_by: order by
        :return: person id
        """
        logger.start(object={"contact_id": contact_id})
        person_ids_tuple_list = self.select_multi_tuple_by_id(select_clause_value="person_id",
                                                              id_column_name="contact_id",
                                                              id_column_value=contact_id,
                                                              limit=limit,
                                                              order_by=order_by)
        person_ids = [person_id_tuple[0] for person_id_tuple in person_ids_tuple_list]
        logger.end(object={"person_ids": person_ids})
        return person_ids

    def _proccess_contact_dict_to_person_class(self, contact_dict: dict, contact_email_address: str) -> Person:
        """
        Process contact dict to person dict
        :param contact_dict: contact dict
        :return: person dict
        """
        logger.start(object={"contact_dict": contact_dict})
        person_object = Person(gender_id=GENDER_ID,
                               birthday_date=contact_dict['birthday'],
                               first_name=contact_dict['first_name'],
                               last_name=contact_dict['last_name'],
                               main_email_address=contact_email_address,
                               is_test_data=self.is_test_data)
        return person_object
