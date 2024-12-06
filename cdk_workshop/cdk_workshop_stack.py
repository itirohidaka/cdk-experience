from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    Tags,
    # aws_iam as iam,
    # aws_sqs as sqs,
    # aws_sns as sns,
    # aws_sns_subscriptions as subs,
    aws_ec2 as ec2
    # aws_s3 as s3
)

class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # vpc = ec2.Vpc(self,"TheVPC",ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"))
        self.vpc_name = 'eks-auto-demo'
        self.vpc_cidr = '10.0.0.0/16'

        self.__create_vpc()
    
    def __create_vpc(self):
        vpc_construct_id = 'vpc'
        subnet_construct_id = 'pubsubnet'
        # audit_bucket_construct_id = 'audit-bucket'
        # audit_bucket_name = 'vpc-demo-audit-bucket'
        # self.audit_bucket = s3.Bucket.from_bucket_name(
        #     self, audit_bucket_construct_id, audit_bucket_name
        # )

        self.vpc: ec2.Vpc = ec2.Vpc(
            self, 
            vpc_construct_id,
            vpc_name=self.vpc_name,
            ip_addresses=ec2.IpAddresses.cidr(self.vpc_cidr),
            # max_azs=3,
            availability_zones=['us-east-1a','us-east-1b','us-east-1c'],
            create_internet_gateway=True,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='Public',
                    cidr_mask=24,
                ), 
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name='Private',
                    cidr_mask=24,
                )
            ],
            nat_gateways=1
        )