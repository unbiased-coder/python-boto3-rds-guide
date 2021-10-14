import boto3_helper

session = boto3_helper.init_aws_session()
rds = session.client('rds')
db_instances = rds.describe_db_instances()['DBInstances']
for db_instance in db_instances:
    db_identifier = db_instance['DBInstanceIdentifier']
    print ('Stopping instance with identifier: %s'%db_identifier)
    rds.stop_db_instance(DBInstanceIdentifier=db_identifier)
