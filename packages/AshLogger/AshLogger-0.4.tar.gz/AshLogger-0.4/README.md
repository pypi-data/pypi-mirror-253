[![License: GNU GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/ashfaque/AshLogger/blob/main/LICENSE)



## How to install
```sh
pip install AshLogger
```



## Documentation
```python3
from AshLogger import AshLogger


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
```



## License
[GNU GPLv3](LICENSE)
