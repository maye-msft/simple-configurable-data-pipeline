import cddp.ingestion.autoloader
import cddp.ingestion.azure_eventhub
import cddp.ingestion.azure_adls_gen2
import cddp.ingestion.azure_adls_gen1
import cddp.ingestion.azure_adls_gen2


def start_ingestion_task(task, spark):
    if task['type'] == 'autoloader':
        autoloader.start_ingestion_task(task, spark)
    elif task['type'] == 'azure_eventhub':
        azure_eventhub.start_ingestion_task(task, spark)
    elif task['type'] == 'jdbc':
        jdbc.start_ingestion_task(task, spark)
    elif task['type'] == 'deltalake':
        deltalake_file.start_ingestion_task(task, spark)
    elif task['type'] == 'azure_adls_gen2':
        azure_adls_gen2.start_ingestion_task(task, spark)
    elif task['type'] == 'azure_adls_gen1':
        azure_adls_gen1.start_ingestion_task(task, spark)
    else:
        raise Exception('Unknown ingestion type: ' + task['type'])


if __name__ == '__main__':
    task = {
        'type': 'autoloader',
        'name': 'test',
        'format': 'csv',
        'location': 'test',
        'delimiter': ',',
        'header': True,
        'quote': '"',
        'escape': '\\',
        'encoding': 'utf-8',
        'schema': {
            'fields': [
                {
                    'name': 'id',
                    'type': 'string',
                    'nullable': False,
                    'metadata': {}
                },
                {
                    'name': 'name',
                    'type': 'string',
                    'nullable': False,
                    'metadata': {}
                },
                {
                    'name': 'age',
                    'type': 'integer',
                    'nullable': False,
                    'metadata': {}
                }
            ]
        }
    }
    start_ingest_task(task)