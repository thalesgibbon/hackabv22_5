# SCRIPT AUXILIAR PARA CRIAR RECURSOS NA CLOUD A PARTIR DO SDK PYTHON NO NOTEBOOK

BKT = 'bkt-hackabv22-5'
DATASET = 'uber'
TABLE = 'partners_me'
PROJECT = 'hacka-5'
DRIVER_ID = 'ID001'


''' subindo arquivos no storage '''
# !pip install gcloud --user
from gcloud import storage
client = storage.Client()
bucket = client.bucket(BKT)
bucket.location = 'us'
bucket.create()
bucket.exists()
blob = bucket.blob(f'{DRIVER_ID}/{TABLE}.json')
blob.upload_from_filename(f'{TABLE}.json')
# !gsutil ls -r 'gs://bkt-hackabv22-5/'


''' criando dataset no bigquery '''
from google.cloud import bigquery
client = bigquery.Client()
dataset = bigquery.Dataset(f'{PROJECT}.{DATASET}')
dataset = client.create_dataset(dataset, timeout=30)


''' criando tabela no bigquery '''
dataset_ref = client.dataset(DATASET)
table_ref = bigquery.TableReference(dataset_ref, TABLE)
schemafield_col1 = bigquery.schema.SchemaField("driver_id","INTEGER")
schemafield_col2 = bigquery.schema.SchemaField("first_name","INTEGER")
schemafield_col3 = bigquery.schema.SchemaField("last_name","STRING")
schemafield_col4 = bigquery.schema.SchemaField("email","STRING")
schemafield_col5 = bigquery.schema.SchemaField("phone_number","STRING")
schemafield_col6 = bigquery.schema.SchemaField("picture","STRING")
schemafield_col7 = bigquery.schema.SchemaField("rating","INTEGER")
schemafield_col8 = bigquery.schema.SchemaField("date_of_birth","STRING")
schemafield_col9 = bigquery.schema.SchemaField("activation_status","STRING")
schemafield_col10 = bigquery.schema.SchemaField("promo_code","STRING")
schemafield_col11 = bigquery.schema.SchemaField("encrypted_symmetric_key","STRING")
schemafield_col12 = bigquery.schema.SchemaField("driving_license", 'RECORD', mode='REPEATED', fields=(
    bigquery.schema.SchemaField('encrypted_license_number', 'STRING'),
    bigquery.schema.SchemaField('state', 'STRING'),
    bigquery.schema.SchemaField('expiration_date', 'STRING')
))
schemafield_col13 = bigquery.schema.SchemaField("encrypted_national_identifier","STRING")
schemafield_col14 = bigquery.schema.SchemaField("partner_role","STRING")
schemafield_col15 = bigquery.schema.SchemaField("city_name","STRING")
schemafield_col16 = bigquery.schema.SchemaField("city_identifier","INTEGER")
schemafield_list = [
    schemafield_col1 ,
    schemafield_col2 ,
    schemafield_col3 ,
    schemafield_col4 ,
    schemafield_col5 ,
    schemafield_col6 ,
    schemafield_col7 ,
    schemafield_col8 ,
    schemafield_col9 ,
    schemafield_col10,
    schemafield_col11,
    schemafield_col12,
    schemafield_col13,
    schemafield_col14,
    schemafield_col15,
    schemafield_col16,
]
table = bigquery.Table(table_ref, schemafield_list)
client.create_table(table)


''' fazendo query no bigquery '''
query = f"""SELECT * FROM `{PROJECT}.{DATASET}.{TABLE}` """
job = client.query(query)
df = job.to_dataframe()


''' adicionar registro na tabela bigquery '''
job_config = bigquery.LoadJobConfig(schema=schemafield_list, source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON, )
uri = f"gs://{BKT}/{DRIVER_ID}/{TABLE}.json"
load_job = client.load_table_from_uri(
    uri,
    f'{PROJECT}.{DATASET}.{TABLE}',
    location="US",
    job_config=job_config,
)
load_job.result()