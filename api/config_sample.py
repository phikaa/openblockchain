#!/usr/bin/env python2.7

import os
import sys
_basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, _basedir)

DEBUG = False

HOST='0.0.0.0'
PORT=5000

BLOCKSTORE_HOST='0.0.0.0'
BLOCKSTORE_PORT=9005

SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@@127.0.0.1:5432/dbname'
RPC_URL = "http://bitcoinrpc:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX@127.0.0.1:8332"
DB_WARNING_FILE = "/home/phil/check_db.txt"
CHECK_LOG_FILE ='/home/phil/check_db.log'
BLOCKSTORE_API_LOG_FILE ='/home/phil/blockstore_api.log'
EXPLORER_API_LOG_FILE ='/home/phil/explorer_api.log'

EMAIL_HOST = 'p.haobtc.com'
EMAIL_HOST_USER = 'notify@haobtc.com'
EMAIL_HOST_PASSWORD = 'xxx'
EMAIL_USE_TLS = True

EMAIL_RECEIVER = ['xxx@xxx.com']

NET_PORT='eth1'

UTX_EXPIRE_TIME = 24 * 60 * 60 #24 hour
