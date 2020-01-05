# encoding:utf-8


import os
import datetime

starttime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
result_pathname = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
os.makedirs('./AutoTest/Result/' + result_pathname)
picture_path = './AutoTest/Result/' + result_pathname