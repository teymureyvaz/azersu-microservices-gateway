import cx_Oracle
import logging
from datetime import *
#logger qurasdirilmasi ucun funksiya
def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)

setup_logger('consumption_info', 'logs/consumption_info.log')
logger= logging.getLogger('consumption_info')

def connect_ode():
    try:
        conn = cx_Oracle.connect('onlineode/Az10zer90Su99@192.168.9.105:1521/MISDB')
        return conn
    except cx_Oracle.DatabaseError as e:
        logger.error(e)

def connect_web():
    try:
        conn = cx_Oracle.connect('onlineweb/"ow*109099"@testmis.azersu.lan:1521/testmis')
        return conn
    except cx_Oracle.DatabaseError as e:
        logger.error(e)

# son x ədəd ay obyekti qaytaran funksiya
def getLastMonths(last_month_count):
    datelist = list()
    today = datetime.today()
    unchanged_today = datetime.today()
    for i in range(last_month_count):
        appended = today.replace(day=1) - timedelta(days=1)
        appended = str(appended)[0:7]
        datelist.append(appended)
        today = today.replace(day=1) - timedelta(days=1)
    del datelist[-1]
    datelist.insert(0,str(unchanged_today)[0:7])
    return datelist

# vergül ilə olan string tipindəki kəsr ədədlərini float tipinə çevirmək üçün funksiya
def myfloat(float_string):
    float_string = str(float_string)
    errormsg = "ValueError: Input must be decimal or integer string"
    try:
        if float_string.count(".") == 1 and float_string.count(",") == 0:
            return float(float_string)
        else:
            midle_string = list(float_string)
            while midle_string.count(".") != 0:
                midle_string.remove(".")
            out_string = str.replace("".join(midle_string), ",", ".")
        return float(out_string)
    except:
        print(errormsg)
        return None

#Az10zer90Su99 ode
#"ow*109099" web