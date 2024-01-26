import datetime
import time
import pandas as pd
import logging
from influxdb import InfluxDBClient
logging.disable(logging.DEBUG)
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

def log(m, debug=1):
    if debug:
        logging.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ; {m}")

def task_time(startx):
    return time.time_ns() - startx

def write_points(list, host, username, password, database, port=8086, attempts=10, sleep_on_fail=2, batch_size=500, debug=1):
    if len(list)<1:
        log("la lista de puntos no puede estar vacia",1)
        return 1
    elif len(list)<=batch_size:
        r=write_points_real(list, host, username, password, database, port, attempts, sleep_on_fail, batch_size, debug)
        if r:
            log(r,1)
    else:
        for i in range(0, len(list), batch_size):
            try:
                batch = list[i:i + batch_size]
                r=write_points_real(batch, host, username, password, database, port, attempts, sleep_on_fail, batch_size, debug)
                if r:
                    log(r,1)
            except Exception as e:
                log(e,1)

def write_points_real(list, host, username, password, database, port, attempts, sleep_on_fail, batch_size, debug):
    startx=time.time_ns()
    try:
        continuar=True
        intento=1
        while(continuar):
            try:
                insertx=time.time_ns()
                client = InfluxDBClient(host=host, username=username, password=password, port=port)
                client.switch_database(database)
                client.write_points(list)
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
                        'attempt' : intento-1,
                        'host' : host,
                        'database' : database,
                        'time_ns': time.time_ns()
    }
    return msgx


#write_points([],'a','b','c','d', debug=0)
#log("--------------------------------------------------------------------------------------")
#write_points([1,2,3],'a','b','c','d', debug=0)
#log("--------------------------------------------------------------------------------------")
#write_points(list(range(1, 1001)),'a','b','c','d', debug=0)

