import logging
from logging import handlers
import os
from .config import sca_config


level_relations = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'crit': logging.CRITICAL
}  # 日志级别关系映射

LOG_FORMAT = '%(asctime)s [%(threadName)s] - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'

__logger = None

def log_init_config(log_dir="", level='info', when='MIDNIGHT', backCount=7, fmt=LOG_FORMAT):
    global __logger
    if len(log_dir) == 0:
        log_dir = sca_config("settings", "log_dir", ".")
    if not log_dir.endswith("logs"):
        log_dir = os.path.join(log_dir, 'logs')
    if not os.path.exists(log_dir): 
        os.mkdir(log_dir)
    __logger = logging.getLogger("sca")
    format_str = logging.Formatter(fmt)
    __logger.setLevel(level_relations.get(level))
    info_th = handlers.TimedRotatingFileHandler(filename=os.path.join(log_dir, "info.log"), interval=1, when=when, backupCount=backCount, encoding='utf-8')
    info_th.setFormatter(format_str)
    info_th.setLevel(logging.INFO)
    error_th = handlers.TimedRotatingFileHandler(filename=os.path.join(log_dir, "error.log"), interval=1, when=when, backupCount=backCount,
                                            encoding='utf-8')
    error_th.setFormatter(format_str)
    error_th.setLevel(logging.ERROR)
    __logger.addHandler(info_th)
    __logger.addHandler(error_th)

def log_info(message):
    global __logger
    if __logger is None:
        return
    __logger.info(message)


def log_error(message):
    global __logger
    if __logger is None:
        return
    __logger.error(message)
