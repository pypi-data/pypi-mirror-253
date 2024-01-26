import os

from duckberg import DuckBerg

os.environ["AWS_DEFAULT_REGION"] = "eu-west-1"
os.environ["AWS_ACCESS_KEY_ID"] = "ASIARCC6UKQSEPHP3JGZ"
os.environ["AWS_SECRET_ACCESS_KEY"] = "D7oKLEDjuduNvh9kx4vlkThb+lNfnibtWISVwLkR"
os.environ[
    "AWS_SESSION_TOKEN"
] = "FwoGZXIvYXdzEPD//////////wEaDDM8aIRHZ+nHFdccHiKJAi/gWd/fGJrUkEgi97YgF0Iiy6may1PlGxucXKpps6/61rofuO2fuq0sb49tdHsYiJAohu7Hua8crG8Vqz93EY/2H9Is48OsSeQqi7cj3z0drRsWHReqJVJdAg4q6TV4U20l5XH4Fh+9yNx8ip3z0dCXNPdrO8KPRKEwlgwd9s0kUFMGPtGuKg3aUHwZWFeiLsbSFkpgyFOF4rSWIw2uLMTSXIh7Yhu68B28fZDc2gL34fgefR/aBdGan1Czn76K0YRRu400TXMFbL+MnELCiDb3uf5vEzL+blAd6AYZLARU+OnRKzZrwjxgp7F65Z9rYfdiIHT5UGoU5AwNx1tXcmG8j2517piXfAoolr/LrQYyKw/UfgzuMrwk/5DlTAZvDMWoTLApnLbndbSkzkJyrbAQlClmgV9raA9YOy0="


MINIO_URI = "http://localhost:9000/"
MINIO_USER = "admin"
MINIO_PASSWORD = "password"

# catalog_config: dict[str, str] = {
#     "type": "rest",
#     "uri": "http://localhost:8181/",
#     "credentials": "admin:password",
#     "s3.endpoint": MINIO_URI,
#     "s3.access-key-id": MINIO_USER,
#     "s3.secret-access-key": MINIO_PASSWORD,
# }

# BOTO_SESSION_CONFIG_KEYS = ["aws_access_key_id", "aws_secret_access_key", "aws_session_token", "region_name", "profile_name"]

catalog_config: dict[str, str] = {
    "type": "glue",
}

catalog_name = "default"

db = DuckBerg(
    catalog_name=catalog_name, catalog_config=catalog_config, database_names=["slido_iceberg"], table_names=["datapi_questions_iceberg"]
)

tables = db.list_tables()

# New way of quering data without partition filter
query: str = "SELECT * FROM 'slido_iceberg.datapi_questions_iceberg'"
df = db.select(
    sql=query,
    table="slido_iceberg.datapi_questions_iceberg",
    partition_filter="organization_id = '4ad6a753-3252-49bd-9f5d-adaa150ad58a'",
).read_pandas()

print(len(df))

# assert(df['count_star()'][0] == 2614)
#
# # New way of quering data
# query: str = "SELECT count(*) FROM (SELECT * FROM 'nyc.taxis' WHERE payment_type = 1 AND trip_distance > 40 ORDER BY tolls_amount DESC)"
# df = db.select(sql=query).read_pandas()
# assert(df['count_star()'][0] == 1673)
#
# # Old way of quering data
# query: str = "SELECT count(*) FROM (SELECT * FROM 'nyc.taxis' WHERE payment_type = 1 AND trip_distance > 40 ORDER BY tolls_amount DESC)"
# df = db.select(sql=query, table="nyc.taxis", partition_filter="payment_type = 1").read_pandas()
# assert(df['count_star()'][0] == 1673)
