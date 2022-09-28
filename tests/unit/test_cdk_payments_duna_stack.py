import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_payments_duna.cdk_payments_duna_stack import CdkPaymentsDunaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_payments_duna/cdk_payments_duna_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPaymentsDunaStack(app, "cdk-payments-duna")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
