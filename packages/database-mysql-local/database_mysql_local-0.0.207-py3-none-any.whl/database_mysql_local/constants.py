from logger_local.LoggerComponentEnum import LoggerComponentEnum

DEFAULT_SQL_SELECT_LIMIT = 100

# connector / cursor
DATABASE_MYSQL_PYTHON_PACKAGE_COMPONENT_ID = 13
DATABASE_MYSQL_PYTHON_PACKAGE_COMPONENT_NAME = 'database_mysql_local\\connector'
CONNECTOR_DEVELOPER_EMAIL = 'idan.a@circ.zone'
logger_connector_code_object = {
    'component_id': DATABASE_MYSQL_PYTHON_PACKAGE_COMPONENT_ID,
    'component_name': DATABASE_MYSQL_PYTHON_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': CONNECTOR_DEVELOPER_EMAIL
}
logger_connector_test_object = logger_connector_code_object.copy()
logger_connector_test_object['component_category'] = LoggerComponentEnum.ComponentCategory.Unit_Test.value

# generic_crud
DATABASE_MYSQL_PYTHON_GENERIC_CRUD_COMPONENT_ID = 206
DATABASE_MYSQL_PYTHON_GENERIC_CRUD_COMPONENT_NAME = 'database_mysql_local\\generic_crud'
GENERIC_CRUD_DEVELOPER_EMAIL = 'akiva.s@circ.zone'
logger_crud_code_object = {
    'component_id': DATABASE_MYSQL_PYTHON_GENERIC_CRUD_COMPONENT_ID,
    'component_name': DATABASE_MYSQL_PYTHON_GENERIC_CRUD_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': GENERIC_CRUD_DEVELOPER_EMAIL
}
logger_crud_test_object = logger_crud_code_object.copy()
logger_crud_test_object['component_category'] = LoggerComponentEnum.ComponentCategory.Unit_Test.value

# generic_crud_ml
DATABASE_MYSQL_GENERIC_CRUD_ML_COMPONENT_ID = 7001
DATABASE_MYSQL_GENERIC_CRUD_ML_COMPONENT_NAME = 'database_mysql_local\\generic_crud_ml'
GENERIC_CRUD_ML_DEVELOPER_EMAIL = 'tal.g@circ.zone'
logger_crud_ml_code_object = {
    'component_id': DATABASE_MYSQL_GENERIC_CRUD_ML_COMPONENT_ID,
    'component_name': DATABASE_MYSQL_GENERIC_CRUD_ML_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': GENERIC_CRUD_ML_DEVELOPER_EMAIL
}
logger_crud_ml_test_object = logger_crud_ml_code_object.copy()
logger_crud_ml_test_object['component_category'] = LoggerComponentEnum.ComponentCategory.Unit_Test.value

# generic_mapping
DATABASE_MYSQL_PYTHON_GENERIC_MAPPING_COMPONENT_ID = 7002
DATABASE_MYSQL_PYTHON_GENERIC_MAPPING_COMPONENT_NAME = 'database_mysql_local\\generic_mapping'
GENERIC_MAPPING_DEVELOPER_EMAIL = 'sahar.g@circ.zone'
logger_mapping_code_object = {
    'component_id': DATABASE_MYSQL_PYTHON_GENERIC_MAPPING_COMPONENT_ID,
    'component_name': DATABASE_MYSQL_PYTHON_GENERIC_MAPPING_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': GENERIC_MAPPING_DEVELOPER_EMAIL
}
logger_mapping_test_object = logger_mapping_code_object.copy()
logger_mapping_test_object['component_category'] = LoggerComponentEnum.ComponentCategory.Unit_Test.value
