import logging
import os
from logging.handlers import TimedRotatingFileHandler


class Logger:
    LOG_LEVELS = {
        'w': logging.WARNING,
        'i': logging.INFO
    }

    def __init__(self, logger_name, type_log, when='D', interval=30, backup_count=1, log_directory="logs"):
        self.logger_name = logger_name
        self.type_log = type_log
        self.when = when
        self.interval = interval
        self.backup_count = backup_count
        self.log_directory = log_directory

        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.LOG_LEVELS[self.type_log])
        log_path = os.path.join(self.log_directory, f'{self.logger_name}.log')
        handler = TimedRotatingFileHandler(log_path,
                                           when=self.when,
                                           interval=self.interval,
                                           backupCount=self.backup_count)
        handler.setLevel(self.LOG_LEVELS[self.type_log])
        formatter = logging.Formatter('%(levelname)s %(name)s %(asctime)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def __setattr__(self, name, value):
        if name == "type_log" and value not in self.LOG_LEVELS:
            raise ValueError(f"Invalid type_log provided: {value}. Valid options: {', '.join(self.LOG_LEVELS.keys())}")
        super().__setattr__(name, value)
