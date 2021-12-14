import logging

from dagster import job, op, repository


@op
def hello(context):
    context.log.info("Hello from Dagster Cloud!")


@job
def hello_dagster_cloud():
    hello()


@repository
def repo():
    return [hello_dagster_cloud]
