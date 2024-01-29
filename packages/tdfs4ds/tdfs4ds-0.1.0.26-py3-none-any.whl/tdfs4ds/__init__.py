__version__ = '0.1.0.26'
from tdfs4ds import feature_store
from tdfs4ds import datasets
from tdfs4ds import feature_engineering
from tdfs4ds import process_store
from tdfs4ds import utils
import teradataml as tdml

from tdfs4ds.feature_store import feature_store_catalog_creation
from tdfs4ds.process_store import process_store_catalog_creation
def setup(database, if_exists='fail'):
    feature_store.schema = database
    if if_exists == 'replace':
        try:
            tdml.db_drop_table(table_name = 'FS_FEATURE_CATALOG', schema_name=database)
        except Exception as e:
            print(str(e).split('\n')[0])
        try:
            tdml.db_drop_table(table_name = 'FS_PROCESS_CATALOG', schema_name=database)
        except Exception as e:
            print(str(e).split('\n')[0])
    try:
        feature_catalog_name = feature_store_catalog_creation()
        print('feature catalog table: ', feature_catalog_name, ' in database ', database)
    except Exception as e:
        print(str(e).split('\n')[0])

    try:
        process_catalog_name = process_store_catalog_creation()
        print('process catalog table: ', process_catalog_name, ' in database ', database)
    except Exception as e:
        print(str(e).split('\n')[0])

    return