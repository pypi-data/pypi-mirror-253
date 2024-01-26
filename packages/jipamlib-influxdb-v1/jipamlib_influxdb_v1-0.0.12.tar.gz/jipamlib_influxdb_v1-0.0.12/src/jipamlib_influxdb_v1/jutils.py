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

def write_points(list, host, username, password, database, port=8086, attempts=10, sleep_on_fail=2, batch_size=500, debug=1):
    startx=time.time_ns()
    try:
        continuar=True
        intento=1
        while(continuar):
            try:
                insertx=time.time_ns()
                client = InfluxDBClient(host=host, username=username, password=password, port=port)
                client.switch_database(database)
                r=client.write_points(points=list, batch_size=batch_size)
                log(r,debug)
                if debug:
                    msgx={
                        'msg' : 'INSERT_OK',
                        'rows' : len(list),
                        'task_time_ns' : task_time(startx),
                        'insert_time_ns' : task_time(insertx),
                        'attempt' : intento,
                        'host' : host,
                        'database' : database,
                        'time_ns': time.time_ns()
                    }
                    log(msgx, debug)
                continuar=False
                client.close()
                return 0
            except Exception as err:
                msgx={
                        'msg' : 'ATTEMPT_FAILED',
                        'rows' : len(list),
                        'task_time_ns' : task_time(startx),
                        'insert_time_ns' : -1,
                        'attempt' : intento,
                        'host' : host,
                        'database' : database,
                        'time_ns': time.time_ns()
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
                        'insert_time_ns' : -1,
                        'attempt' : intento,
                        'host' : host,
                        'database' : database,
                        'time_ns': time.time_ns()
                }
                log(msgx, 1)


    msgx={
                        'msg' : 'INSERT_FAILED',
                        'rows' : len(list),
                        'task_time_ns' : task_time(startx),
                        'insert_time_ns' : -1,
                        'attempt' : intento,
                        'host' : host,
                        'database' : database,
                        'time_ns': time.time_ns()
    }
    log(msgx, 1)
    raise ValueError(msgx)

