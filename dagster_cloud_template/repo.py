import logging

from dagster import job, op, repository


@op
def hello():
    logging.info("Hello from Dagster Cloud!")


@job
def hello_dagster_cloud():
    hello()


@repository
def repo():
    return [hello_dagster_cloud]
