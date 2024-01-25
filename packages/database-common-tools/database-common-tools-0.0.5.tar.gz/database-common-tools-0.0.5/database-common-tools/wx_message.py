# -*- coding: utf-8 -*-

import requests
import logging
import os
from logging import handlers

##################################################
# post function
##################################################

LOG_FN = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + '/logs/message.log'
LOG_FT = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
LOG_TH = handlers.TimedRotatingFileHandler(filename=LOG_FN, when='D', backupCount=3, encoding='utf-8')
LOG_TH.setFormatter(LOG_FT)
LOG = logging.getLogger(LOG_FN)
LOG.addHandler(LOG_TH)
LOG.setLevel(logging.INFO)


def sendErrorMessage(receivers, subject, content):
    datas = dict()
    datas['receiver'] = receivers
    datas['subject'] = subject
    datas['content'] = str(content)
    try:
        requests.post('http://notice.ops.m.com/send_wx', data=datas)
    except Exception as e:
        LOG.error('{} exception ... {}\tvalue={}'.format(subject, e, datas))
