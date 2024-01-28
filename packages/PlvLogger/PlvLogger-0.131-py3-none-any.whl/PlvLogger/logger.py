import logging
import os
import threading

class Logger:
    LOG_LEVELS = {
        'w': logging.WARNING,
        'i': logging.INFO
    }

    def __init__(self, logger_name, type_log, log_directory="logs", auto_delete_interval=0):
        if type_log not in self.LOG_LEVELS:
            raise ValueError(f"Invalid type_log provided: {type_log}. Valid options are: {', '.join(self.LOG_LEVELS.keys())}")
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        self.logger = logging.getLogger(logger_name)
        if not self.logger.handlers:
            self.logger.setLevel(self.LOG_LEVELS[type_log])
            log_path = os.path.join(log_directory, f'{logger_name}.log')
            self.log_path = log_path
            handler = logging.FileHandler(log_path)
            handler.setLevel(self.LOG_LEVELS[type_log])
            formatter = logging.Formatter('%(levelname)s %(name)s %(asctime)s %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.delete_interval = auto_delete_interval * 3600  # Конвертируем часы в секунды
        if self.delete_interval > 0:
            self.start_log_deletion_timer()

    def delete_logs(self):
        if os.path.exists(self.log_path):
            os.remove(self.log_path)

    def start_log_deletion_timer(self):
        timer = threading.Timer(self.delete_interval, self.handle_log_deletion)
        timer.daemon = True  # Делаем таймер демон-потоком, чтобы он завершился вместе с основной программой
        timer.start()

    def handle_log_deletion(self):
        self.delete_logs()
        self.start_log_deletion_timer()  # Перезапуск таймера для следующего удаления


# class Logger:
#     LOG_LEVELS = {
#         'w': logging.WARNING,
#         'i': logging.INFO
#     }
#
#     def __init__(self, logger_name, type_log, log_directory="logs"):
#         if type_log not in self.LOG_LEVELS:
#             raise ValueError(f"Invalid type_log provided: {type_log}. Valid options are: {', '.join(self.LOG_LEVELS.keys())}")
#         if not os.path.exists(log_directory):
#             os.makedirs(log_directory)
#
#         self.logger = logging.getLogger(logger_name)
#         if not self.logger.handlers:  # Проверка, есть ли уже обработчики у логгера
#             self.logger.setLevel(self.LOG_LEVELS[type_log])
#             log_path = os.path.join(log_directory, f'{logger_name}.log')
#             handler = logging.FileHandler(log_path)
#             handler.setLevel(self.LOG_LEVELS[type_log])
#             formatter = logging.Formatter('%(levelname)s %(name)s %(asctime)s %(message)s')
#             handler.setFormatter(formatter)
#             self.logger.addHandler(handler)