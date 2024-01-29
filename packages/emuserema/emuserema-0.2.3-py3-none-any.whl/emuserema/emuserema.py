import logging
from emuserema import Emuserema

def setup_logger():
    # create logger
    logger = logging.getLogger('project')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # create formatter
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

if __name__ == '__main__' and __package__ is None:
     setup_logger()
     emuserema = Emuserema()