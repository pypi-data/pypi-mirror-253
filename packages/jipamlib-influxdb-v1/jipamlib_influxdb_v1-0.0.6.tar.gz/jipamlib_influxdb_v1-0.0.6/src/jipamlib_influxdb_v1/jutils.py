import datetime
import time
import pandas as pd
import logging
from influxdb import InfluxDBClient
logging.disable(logging.DEBUG)
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

def log(m, debug):
    if debug:
        logging.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ; {m}")

def task_time(startx):
    return time.time_ns() - startx

def write_points(list, host, username, password, database, port=8086, attempts=5, sleep_on_fail=5, batch_size=500, debug=1):
    startx=time.time_ns()
    try:
        continuar=True
        intento=1
        while(continuar):
            try:
                client = InfluxDBClient(host=host, username=username, password=password, port=port)
                client.switch_database(database)
                client.write_points(list)
                if debug:
                    msgx={
                        'msg' : 'INSERT_OK',
                        'rows' : len(list),
                        'task_time_ns' : task_time(startx),
                        'attempt' : intento,
                        'host' : host,
                        'database' : database,
                        'time': time.time_ns()
                    }
                    log(msgx, debug)
                continuar=False
            except Exception as err:
                msgx={
                        'msg' : 'ATTEMPT_FAILED',
                        'rows' : len(list),
                        'task_time_ns' : task_time(startx),
                        'attempt' : intento,
                        'host' : host,
                        'database' : database,
                        'time': time.time_ns()
                }
                log(msgx, debug)
                intento+=1
                if intento>attempts:
                    continuar=False
                else:
                    time.sleep(sleep_on_fail)
            finally:
                client.close()
    except Exception as e:
                msgx={
                        'msg' : e,
                        'rows' : len(list),
                        'task_time_ns' : task_time(startx),
                        'attempt' : intento,
                        'host' : host,
                        'database' : database,
                        'time': time.time_ns()
                }
                log(msgx, 1)

    msgx={
                        'msg' : 'INSERT_FAILED',
                        'rows' : len(list),
                        'task_time_ns' : task_time(startx),
                        'attempt' : intento,
                        'host' : host,
                        'database' : database,
                        'time': time.time_ns()
    }
    log(msgx, 1)
    raise ValueError(msgx)

