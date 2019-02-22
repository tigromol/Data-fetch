#!/usr/bin/env python3
from argparse import ArgumentParser
from datetime import datetime
import gc
import re
import os
import urllib.request
import urllib.parse
import sys
from gen import gen_next_month
import that
import time
from exchanges.codes import codes
from pympler.tracker import SummaryTracker

query = {
    'market': "1", # Говорит о том, где вращается бумага(инструмент)
    'em': "175924", # Индекс бумаги(инструмента)
    'code': "PHOR", # символьная переменная по инструменту
    'apply': "0", #
    'df': "20", # начальный день
    'mf': "4", # начальный месяц
    'yf': "2017", # начальный год
    'from': "20.05.2017", # начальная дата дд.мм.гггг
    'dt': "23", # конечный день
    'mt': "5", # конечный месяц
    'yt': "2017", # конечный год
    'to': "23.06.2017", # конечная дата дд.мм.гггг
    'p': "2", # период котировок
    'f': "test", # 
    'e': ".txt", # расширение получаемого файла
    'cn': "POLY", #
    'dtf': "1", # формат даты (1 - ггггммдд, 2 - ггммдд, 3 - ддммгг, 4 - дд/мм/гг, 5 - мм/дд/гг)
    'tmf': "1", # формат времени (1 - ччммсс, 2 - ччмм, 3 - чч: мм: сс, 4- чч: мм)
    'MSOR': "1", # выдавать время (0 - начало свечи, 1 - окончание свечи)
    'mstime': "on", # выдавать время (НЕ московское — mstimever=0; московское — mstime='on', mstimever='1')
    'mstimever': "1", # выдавать время (НЕ московское — mstimever=0; московское — mstime='on', mstimever='1')
    'sep': "1", # параметр разделитель полей (1 — запятая (,), 2 — точка (.), 3 — точка с запятой (;), 4 — табуляция (»), 5 — пробел ( ))
    'sep2': "1", # параметр разделитель разрядов (1 — нет, 2 — точка (.), 3 — запятая (,), 4 — пробел ( ), 5 — кавычка ('))
    'datf': "4", # Перечень получаемых данных (#1 — TICKER, PER, DATE, TIME, OPEN, HIGH, LOW, CLOSE, VOL; 
                 #2 — TICKER, PER, DATE, TIME, OPEN, HIGH, LOW, CLOSE; #3 — TICKER, PER, DATE, TIME, CLOSE, VOL;
                 #4 — TICKER, PER, DATE, TIME, CLOSE; #5 — DATE, TIME, OPEN, HIGH, LOW, CLOSE, VOL; #6 — DATE, TIME, LAST, VOL, ID, OPER).
    'at': "1" # добавлять заголовок в файл (0 — нет, 1 — да)
}

dir = os.path.dirname(__file__)
data_path = os.path.join(dir, "data")

def parse(file_path):
    pass

def get_data(dir_path):
    for file in os.listdir(dir_path):
        data = []
        print(dir_path)
        file_name = os.path.join(dir_path, file)
        with open(file_name, mode="r", encoding="utf-8") as reader:
            reader.readline()
            print('start')
            for line in reader:
                data.append(float(line.split(",")[-1]))
            reader.close()
        yield [data,file_name]



def parse_args(argv):
    parser = ArgumentParser(description='parse files via que request')
    parser.add_argument("code", help="Code of the instrument")
    parser.add_argument("start_date", help="Starting date in dd.mm.yyyy format")
    parser.add_argument("final_date", help="Final date in dd.mm.yyyy format")
    args = parser.parse_args()
    
    if datetime.strptime(args.start_date, "%d.%m.%Y") > datetime.strptime(args.final_date, "%d.%m.%Y"):
        raise Exception("Start date should be less than final")

    query["market"] = codes[args.code][0]
    query["code"] = args.code
    query['cn'] = args.code
    query["em"] = codes[args.code][1]
    return {"start": args.start_date, "final": args.final_date,}

def make_query():
    base_url = "http://export.finam.ru/data.txt?"
    params = urllib.parse.urlencode(query, encoding="utf-8")
    url = base_url + params
    req = urllib.request.Request(url=url)
    file_name = os.path.join(data_path, f"{query['code']}_{query['from']}_{query['to']}.txt")
    with urllib.request.urlopen(req) as read_file, open(file_name, mode="w", encoding="utf-8") as write_file:
        try:
            write_file.write(read_file.read().decode('utf-8'))
        except UnicodeDecodeError:
            print(f"Unable to decode {query['code']}_{query['from']}_{query['to']}.txt")

def parse_date(start_date, final_date):
    query["from"] = start_date
    query["to"] = final_date
    query["df"] = query['from'].split(".")[0]
    query["mf"] = str(int(query['from'].split(".")[1])-1)
    query["yf"] = query['from'].split(".")[2]
    query["dt"] = query['to'].split(".")[0]
    query["mt"] = str(int(query['to'].split(".")[1])-1)
    query["yt"] = query['to'].split(".")[2]

def main(argv):
    
    
    dates = parse_args(argv)
    date_gen = gen_next_month(dates["start"], dates["final"])
    prev_date = dates["start"]
    try:
        while True:
            next_date = next(date_gen).strftime("%d.%m.%Y")
            print(prev_date)
            print(next_date)
            print()
            parse_date(prev_date, next_date)
            prev_date = next_date

            make_query()
            time.sleep(1)
    except StopIteration:
        print("Success")

    generator = get_data(data_path)
    for data in generator:
        that.main(data)
        gc.collect()
        print('.'*50)

if __name__ == "__main__":
    main(sys.argv[1:])