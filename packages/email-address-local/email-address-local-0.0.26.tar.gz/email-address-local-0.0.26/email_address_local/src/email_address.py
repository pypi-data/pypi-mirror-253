from database_mysql_local.generic_mapping import GenericMapping
from language_local.lang_code import LangCode
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from logger_local.LoggerLocal import Logger

EMAIL_ADDRESS_LOCAL_PYTHON_COMPONENT_ID = 174
EMAIL_ADDRESS_LOCAL_PYTHON_COMPONENT_NAME = 'email address local'
DEVELOPER_EMAIL = "idan.a@circ.zone"
EMAIL_ADDRESS_SCHEMA_NAME = "email_address"
EMAIL_ADDRESS_ML_TABLE_NAME = "email_address_ml_table"
EMAIL_ADDRESS_TABLE_NAME = "email_address_table"
CONTACT_EMAIL_ADDRESS_TABLE_NAME = "contact_email_address_table"
EMAIL_ADDRESS_VIEW = "email_address_view"
EMAIL_ADDRESS_ID_COLLUMN_NAME = "email_address_id"
EMAIL_ADDRESS_ENTETY_NAME1 = "contact"
EMAIL_ADDRESS_ENTETY_NAME2 = "email_address"
EMAIL_COLLUMN_NAME = "email_address"

# TODO Later, we should consider to move this to contact-email-address-python-package repo
CONTACT_EMAIL_ADDRESS_SCHEMA_NAME = "contact_email_address"
object1 = {
    'component_id': EMAIL_ADDRESS_LOCAL_PYTHON_COMPONENT_ID,
    'component_name': EMAIL_ADDRESS_LOCAL_PYTHON_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': "idan.a@circ.zone"
}
logger = Logger.create_logger(object=object1)


# TODO def process_email( email: str) -> dict:
#          extract organization_name
#          extract top_level_domain (TLD)
#          SELECT profile_id, is_webmain FROM `internet_domain`.`internet_domain_table` WHERE
#          if result set is empty INSERT INTO `internet_domain`.`internet_domain_table`

class EmailAddressesLocal(GenericMapping):
    # TODO Where shall we link email-address_id to person, contact, profile ...?
    # Can we create generic function for that in GenericCRUD and use it multiple times
    # in https://github.com/circles-zone/email-address-local-python-package
    def __init__(self) -> None:
        super().__init__(default_schema_name=EMAIL_ADDRESS_SCHEMA_NAME,
                         default_table_name=EMAIL_ADDRESS_TABLE_NAME,
                         default_id_column_name=EMAIL_ADDRESS_ID_COLLUMN_NAME,
                         default_view_table_name=EMAIL_ADDRESS_VIEW,
                         default_entity_name1=EMAIL_ADDRESS_ENTETY_NAME1,
                         default_entity_name2=EMAIL_ADDRESS_ENTETY_NAME2)

    def insert(self, email_address: str, lang_code: LangCode, name: str, is_test_data: bool = False) -> int or None:  # noqa
        logger.start(object={"email_address": email_address,
                             "lang_code": lang_code.value, "name": name, 'is_test_data': is_test_data})
        data = {
            EMAIL_COLLUMN_NAME: f'{email_address}',
            'is_test_data': is_test_data
        }
        email_address_id = super().insert(data_json=data)
        email_json = {
            "email_address_id": email_address_id,
            "lang_code": lang_code.value,
            "name": name,
            'is_test_data': is_test_data
        }
        super().insert(table_name=EMAIL_ADDRESS_ML_TABLE_NAME, data_json=email_json)
        logger.end(object={'email_address_id': email_address_id})
        return email_address_id

    def update_email_address(self, email_address_id: int, new_email: str) -> None:
        logger.start(
            object={"email_address_id": email_address_id, "new_email": new_email})
        email_json = {EMAIL_COLLUMN_NAME: new_email}
        self.update_by_id(id_column_value=email_address_id, data_json=email_json)
        logger.end()

    def delete(self, email_address_id: int) -> None:
        logger.start(object={"email_id": email_address_id})
        self.delete_by_id(id_column_value=email_address_id)
        logger.end()

    def get_email_address_by_email_address_id(self, email_address_id: int) -> str:
        logger.start(object={"email_address_id": email_address_id})
        result = self.select_multi_tuple_by_id(select_clause_value=EMAIL_COLLUMN_NAME,
                                               id_column_value=email_address_id)
        if result:
            email_address = result[0][0]
        else:
            email_address = None
        logger.end(object={'email_address': email_address})
        return email_address

    def get_email_address_id_by_email_address(self, email_address: str) -> int:
        # TODO: Replace str with EmailAddress Class
        logger.start(object={"email_address": email_address})
        result = self.select_multi_tuple_by_where(
            where=f"{EMAIL_COLLUMN_NAME}='{email_address}'")
        if result:
            email_address_id = result[0][0]
        else:
            email_address_id = None
        logger.end(object={'email_address_id': email_address_id})
        return email_address_id

    def verify_email_address(self, email_address: str) -> None:
        """verify_email_address executed by SmartLink/Action"""
        # TODO Think about creating parent both to verifiy_email_address and verify_phone
        logger.start(object={"email_address": email_address})
        print("verify_email_address called with email_address= ", email_address)
        self.update_by_id(id_column_name=EMAIL_COLLUMN_NAME,
                          id_column_value=email_address, data_json={"is_verified": 1})
        logger.end()

    # TODO def process_email( email: str) -> dict:
    #          extract organization_name
    #          extract top_level_domain (TLD)
    #          SELECT profile_id, is_webmain FROM `internet_domain`.`internet_domain_table` WHERE
    #          if result set is empty INSERT INTO `internet_domain`.`internet_domain_table`
    # todo answer is in url-remote Domain.py currenlty 1/15/24 6am workflow not working

    def process_email(self, contact_id: int, email_address: str, is_test_data: bool = False) -> int | dict:
        """
        Process the given email address for a contact.

        Parameters:
        - contact_id (int): The ID of the contact.
        - email_address (str): The email address to be processed.

        Returns:
        - int: If the email address is already in the system and mapped to the contact,
        the method returns the contact_email_id.
        If the email address is not in the system, it returns a dictionary with
        process information, including email_address_id, contact_email_id,
        email_address, and contact_id.
        """
        logger.start(object={"contact_id": contact_id,
                             "email_address": email_address})
        email_address_id = self.get_email_address_id_by_email_address(
            email_address=email_address)
        if email_address_id:  # email is in the system
            logger.info("email address is in the system")
            self.set_schema(schema_name=CONTACT_EMAIL_ADDRESS_SCHEMA_NAME)
            is_mapped = self.select_multi_mapping_tuple_by_id(entity_name1=EMAIL_ADDRESS_ENTETY_NAME1,
                                                              entity_name2=EMAIL_ADDRESS_ENTETY_NAME2,
                                                              entity_id1=contact_id, entity_id2=email_address_id)
            if is_mapped:  # email is mapped to contact
                logger.info("email address is already mapped to contact")
                data = {
                    'contact_id': contact_id,
                    'email_address_id': email_address_id
                }
                # self.set_schema(EMAIL_ADDRESS_SCHEMA_NAME)
                self.update_by_id(
                    table_name=CONTACT_EMAIL_ADDRESS_TABLE_NAME, id_column_name=EMAIL_ADDRESS_ID_COLLUMN_NAME,
                    id_column_value=email_address, data_json=data)
                logger.end(log_message="email address is already mapped to contact")
                return is_mapped[0][0]
            else:  # email is not mapped to contact
                logger.info("email address is not mapped to contact")
                contact_email_id = self.insert_mapping(entity_name1=EMAIL_ADDRESS_ENTETY_NAME1,
                                                       entity_name2=EMAIL_ADDRESS_ENTETY_NAME2,
                                                       entity_id1=contact_id, entity_id2=email_address_id)
                logger.end(log_message="email address is mapped to contact", object={
                    "contact_email_id": contact_email_id})
                return contact_email_id
        else:  # email is not in the system
            logger.info("email address is not in the system")
            # TODO effective_profile_preferred_lang_code
            user_lang_code = logger.user_context.get_effective_profile_preferred_lang_code()
            name = logger.user_context.get_real_first_name(
            ) + " " + logger.user_context.get_real_last_name()
            self.set_schema(schema_name=EMAIL_ADDRESS_SCHEMA_NAME)
            email_address_id = self.insert(
                email_address=email_address, lang_code=LangCode(user_lang_code), name=name, is_test_data=is_test_data)
            self.set_schema(schema_name=CONTACT_EMAIL_ADDRESS_SCHEMA_NAME)
            contact_email_id = self.insert_mapping(entity_name1=EMAIL_ADDRESS_ENTETY_NAME1,
                                                   entity_name2=EMAIL_ADDRESS_ENTETY_NAME2,
                                                   entity_id1=contact_id, entity_id2=email_address_id)
            process_information = {
                "email_address_id": email_address_id,
                "contact_email_id": contact_email_id,
                "email_address": email_address,
                "contact_id": contact_id,
            }

            logger.end(log_message="email address is mapped to contact", object={
                "process_information": process_information})
            return process_information
