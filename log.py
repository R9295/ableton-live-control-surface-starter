from .utils import get_dir


LOG_FILE_PATH = f'{get_dir()}/log.txt'


def log(message):
    with open(LOG_FILE_PATH, 'a') as log:
        log.write(str(message))
        log.write('\n')
        log.close()


def clear_log():
    with open(LOG_FILE_PATH, 'w') as log:
        log.write('')
        log.close()
