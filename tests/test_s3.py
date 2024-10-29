import boto3
from moto import mock_aws


@mock_aws
def test_s3():
    conn = boto3.resource("s3", region_name="us-east-1")
    conn.create_bucket(Bucket="mybucket")

    s3 = boto3.client("s3", region_name="us-east-1")
    s3.put_object(Bucket="mybucket", Key="steve", Body="is awesome")

    body = conn.Object("mybucket", "steve").get()[
        "Body"].read().decode("utf-8")

    assert body == "is awesome"
