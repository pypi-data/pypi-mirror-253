import logging
from logging.handlers import RotatingFileHandler
import os
import inspect


class AshLogger:
    def __init__(self, file_name : str = 'AshLogger.log', file_location : str = None, max_bytes : int = 1000000 , max_backups : int = 1):
        ''' This will take path of the calling python file '''
        calling_frame = inspect.currentframe().f_back
        self.file_path = inspect.getfile(calling_frame)

        if not file_location:
            # file_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')    # This will take the path of this file, which we do not want, as it will create the `logs` dir in the python package dir.

            ''' Creates the `logs` dir at `file_path` '''
            file_location = os.path.join(os.path.dirname(self.file_path), 'logs')

        if not os.path.exists(file_location):
            os.makedirs(file_location)

        self.file_name = file_name
        self.file_location = file_location
        self.max_bytes = max_bytes
        self.max_backups = max_backups

    def setup_logger(self) -> object:
        ''' It logs in a file and also prints out the same in the terminal '''
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] [%(module)s.%(funcName)s] ===> %(message)s')
        handler = RotatingFileHandler(
                                os.path.join(self.file_location, self.file_name)
                                , maxBytes=self.max_bytes
                                , backupCount=self.max_backups
                )
        handler.setFormatter(formatter)
        # logger = logging.getLogger(__name__)    # This will pick AshLogger
        logger = logging.getLogger(os.path.splitext(os.path.basename(self.file_path))[0])
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.addHandler(logging.StreamHandler())
        return logger

    def setup_no_format_logger(self) -> object:
        ''' It logs in a file and also prints out the same in the terminal '''
        handler = RotatingFileHandler(
                                os.path.join(self.file_location, self.file_name)
                                , maxBytes=self.max_bytes
                                , backupCount=self.max_backups
                )
        logger = logging.getLogger(os.path.splitext(os.path.basename(self.file_path))[0])
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.addHandler(logging.StreamHandler())
        return logger

    # @classmethod
    # def setup_basic_logger(cls, file_name : str = 'AshBasicLogger.log', file_location : str = None) -> object:
    @staticmethod
    def setup_basic_logger(file_name : str = 'AshBasicLogger.log', file_location : str = None) -> object:
        ''' It only logs in a file '''

        ''' This will take path of the calling python file '''
        calling_frame = inspect.currentframe().f_back
        file_path = inspect.getfile(calling_frame)

        if not file_location:
            # file_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')

            ''' Create the `logs` dir at `file_path` '''
            file_location = os.path.join(os.path.dirname(file_path), 'logs')

        if not os.path.exists(file_location):
            os.makedirs(file_location)

        logging.basicConfig(
            # * '../logs/log_file_name.log' will make `logs` one dir back.
            # filename=os.path.join(os.path.dirname(__file__), 'logs/log_file_name.log')    # Py 3.9 onwards always returns absolute path.
            filename=os.path.join(file_location, file_name)    # Py 3.8 or earlier returns relative or absolute path if its provided while running the .py file.
            , filemode='a'
            # , format='[%(asctime)s.%(msecs)d] %(levelname)s [%(name)s:%(lineno)s] [%(module)s.%(funcName)s] [%(process)d.%(thread)d] ===> %(message)s'
            , format='[%(asctime)s.%(msecs)d] %(levelname)s [%(name)s:%(lineno)s] [%(module)s.%(funcName)s] ---> %(message)s'
            , datefmt='%Y-%m-%d %H:%M:%S'
            , level=logging.DEBUG
        )
        # return logging.getLogger(__name__)
        return logging.getLogger(os.path.splitext(os.path.basename(file_path))[0])


if __name__ == '__main__':
    logger_obj = AshLogger(
                    file_name='logger_file_name.log'    # If `file_name` is not given, it will set logger file name as `AshLogger.log`
                    , file_location=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')    # If log file path not given, it will create a log/ dir where the calling python file is located.
                    , max_bytes=20000    # default: 1000000
                    , max_backups=3    # default: 1
                )

    logger = logger_obj.setup_logger()

    # * Testing logger
    logger.info(f'{1} info log')
    logger.debug('%s debug log', 2)
    logger.warning('{0} warning log'.format(3))
    logger.error('4 error log')

    # ! USE ANY ONE TYPE OF LOGGER IN A SINGLE FILE, EITHER ABOVE OR BELOW.

    # No need to make object for the class AshLogger, as @classmethod is used as alternative constructor.
    basic_logger = AshLogger.setup_basic_logger(
                                            file_name='basic_logger_file_name.log'    # If `file_name` is not given, it will set logger file name as `AshBasicLogger.log`.
                                            , file_location=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')    # If log file path not given, it will create a log/ dir where the calling python file is located.
                    )

    # * Testing basic logger
    basic_logger.info(f'{1} info log')
    basic_logger.debug('%s debug log', 2)
    basic_logger.warning('{0} warning log'.format(3))
    basic_logger.error('4 error log')



# ? https://realpython.com/python-logging/
# ? https://note.nkmk.me/en/python-script-file-path/
