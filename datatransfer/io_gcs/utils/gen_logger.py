import logging
from unittest.mock import MagicMock

from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer

from env_vars import env_vars


def get_logger(logger_name):
    return MagicMock(), MagicMock()
    connection_string = 'InstrumentationKey=' + env_vars.instrumentationkey
    logging.config.fileConfig('./lib/logging.conf', disable_existing_loggers=False)
    
    logger = logging.getLogger(logger_name)

    # AzureExporter
    exporter = AzureExporter(connection_string=connection_string)

    tracer = Tracer(
        exporter=exporter,
        sampler=ProbabilitySampler(1.0)
    )

    return logger, tracer