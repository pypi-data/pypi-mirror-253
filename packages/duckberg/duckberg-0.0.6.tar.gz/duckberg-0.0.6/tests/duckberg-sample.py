from duckberg import DuckBerg

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

BOTO_SESSION_CONFIG_KEYS = [
    "aws_access_key_id",
    "aws_secret_access_key",
    "aws_session_token",
    "region_name",
    "profile_name",
]

catalog_config: dict[str, str] = {
    "type": "glue",
    "region_name": "eu-west-1",
    "AWS_ACCESS_KEY_ID": "ASIARCC6UKQSJHYFTYU3",
    "AWS_SECRET_ACCESS_KEY": "GOVQOPw/+4uDIiOTyBBaCd5XIiwSi4/L8d81kWKE",
    "AWS_SESSION_TOKEN": "FwoGZXIvYXdzEIj//////////wEaDGBJbs1mx0RRY+WdiyKJAhPVsk7CNbXKBrJwhPW4djBKdon/+3HACgtvRoQmkRNp2A+TiF7zisUk1Fk2NLP23i3AKA1KsPmBS1LylIAHiFAhyij/xegAHRdELLpY8ftvH9q35/7I3eAT7TNjf2q0RSpW1y9/1BT52p87Bmmkj/FYpWQrnTZcGAESHRJJGHwmXwqzTBs93FtdBn+FvRs3ivi+zl3KWe+vc/mXUfgfV3NixjSdu7QuvcuzmL6xylEyyhlUpCu4eikyQ6EFEgYrUdGhBNaiyTtJ9v8tSmurvYh5K04L9aOQXoKnHxZ3KOXUDKMga7vhbnY4bH1dAqocVYD7rV45HLMumbpfwwqw+S8hjJtFL+ThDoUoqPGLrAYyK7LfqaHrcMSg39YFegYdkir6FcDma+Vv1XfjrAY/qwFVDhWqGpfWucRprgQ=",
}

catalog_name = "default"

db = DuckBerg(catalog_name=catalog_name, catalog_config=catalog_config, database_names=["slido_iceberg"])

tables = db.list_tables()

assert len(tables) == 1

# New way of quering data without partition filter
query: str = (
    "SELECT count(*) FROM (SELECT * FROM 'slido_iceberg.taxis' WHERE trip_distance > 40 ORDER BY tolls_amount DESC)"
)
df = db.select(sql=query).read_pandas()
assert df["count_star()"][0] == 2614

# New way of quering data
query: str = "SELECT count(*) FROM (SELECT * FROM 'nyc.taxis' WHERE payment_type = 1 AND trip_distance > 40 ORDER BY tolls_amount DESC)"
df = db.select(sql=query).read_pandas()
assert df["count_star()"][0] == 1673

# Old way of quering data
query: str = "SELECT count(*) FROM (SELECT * FROM 'nyc.taxis' WHERE payment_type = 1 AND trip_distance > 40 ORDER BY tolls_amount DESC)"
df = db.select(sql=query, table="nyc.taxis", partition_filter="payment_type = 1").read_pandas()
assert df["count_star()"][0] == 1673
