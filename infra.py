
''' subindo arquivos no storage '''
# !pip install gcloud --user
from gcloud import storage
client = storage.Client()
bucket = client.bucket('bkt-hackabv22-5')
bucket.location = 'us'
bucket.create()
bucket.exists()
blob = bucket.blob('ID001/partners_me.json')
blob.upload_from_filename('partners_me.json')
# !gsutil ls -r 'gs://bkt-hackabv22-5/'


''' criando dataset no bigquery '''
from google.cloud import bigquery
client = bigquery.Client()
dataset = bigquery.Dataset('hacka-5.uber')
dataset = client.create_dataset(dataset, timeout=30)


''' criando tabela no bigquery '''
dataset_ref = client.dataset('uber')
table_ref = bigquery.TableReference(dataset_ref, 'partners_me')
schemafield_col1 = bigquery.schema.SchemaField("driver_id","STRING")
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
query = """SELECT * FROM `hacka-5.uber.partners_me` """
job = client.query(query)
df = job.to_dataframe()
