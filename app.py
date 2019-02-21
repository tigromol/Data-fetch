#!/usr/bin/env python3
from argparse import ArgumentParser
from datetime import datetime
import re
import os
import urllib.request
import sys
from gen import gen_next_month
import time
from exchanges.codes import codes

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
        file_name = os.path.join(dir_path, file)
        with open(file_name, mode="r", encoding="utf-8") as reader:
            for line in reader:
                match = re.search(r"^.+,\d+,\d+,\d+,(\d+.\d+)$", line)
                if match:
                    data.append(match.group(1))
        yield data



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
    req = urllib.request.Request(url=f"http://export.finam.ru/POLY_170620_170623.txt?market={query['market']}&em={query['em']}&code={query['code']}&apply={query['apply']}&df={query['df']}&mf={query['mf']}&yf={query['yf']}&from={query['from']}&dt={query['dt']}&mt={query['mt']}&yt={query['yt']}&to={query['to']}&p={query['p']}&f={query['f']}&e={query['e']}&cn={query['cn']}&dtf={query['dtf']}&tmf={query['tmf']}&MSOR={query['MSOR']}&mstime={query['mstime']}&mstimever={query['mstimever']}&sep={query['sep']}&sep2={query['sep2']}&datf={query['datf']}&at={query['at']}")
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
    query["mf"] = query['from'].split(".")[1]
    query["yf"] = query['from'].split(".")[2]
    query["dt"] = query['to'].split(".")[0]
    query["mt"] = query['to'].split(".")[1]
    query["yt"] = query['to'].split(".")[2]

def main(argv):
    for arr in get_data(data_path):
        print(arr)
    # dates = parse_args(argv)
    # date_gen = gen_next_month(dates["start"], dates["final"])
    # prev_date = dates["start"]
    # try:
    #     while True:
    #         next_date = next(date_gen).strftime("%d.%m.%Y")
    #         print(prev_date)
    #         print(next_date)
    #         parse_date(prev_date, next_date)
    #         prev_date = next_date

    #         make_query()
    #         time.sleep(1)
    # except StopIteration:
    #     print("Success")

if __name__ == "__main__":
    main(sys.argv[1:])