import logging


class LogTypeFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'log_type'):
            record.log_type = 'INFO'  # Default log type if not specified
        return True


# Custom log format to include the timestamp, filename, log type, and message
log_format = '%(asctime)s - %(filename)s - %(log_type)s - %(message)s'

# Configure the logging with the custom format
logging.basicConfig(format=log_format, level=logging.INFO)

# Create a logger and add the custom filter
logger = logging.getLogger()
logger.addFilter(LogTypeFilter())
