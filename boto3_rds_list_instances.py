import boto3_helper

session = boto3_helper.init_aws_session()
rds = session.client('rds')
db_instances = rds.describe_db_instances()['DBInstances']
for db_instance in db_instances:
    print ('DB Name: ', db_instance['DBInstanceIdentifier'])
    print ('Engine: ', db_instance['Engine'])
    print ('Status: ', db_instance['DBInstanceStatus'])
    print ('')
