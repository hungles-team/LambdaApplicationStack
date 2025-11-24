#!/usr/bin/env python3
import aws_cdk as cdk
from lambda_stack import LambdaStack

app = cdk.App()

LambdaStack(
    app,
    "SebasLambdaStack",
    env=cdk.Environment(
        account="128959305182",
        region="us-east-1"
    ),
)

app.synth()
