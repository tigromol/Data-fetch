from argparse import ArgumentParser
import urllib.request
import sys

query = {
    'market': "1", # Говорит о том, где вращается бумага(инструмент)
    'em': "175924", # Индекс бумаги(инструмента)
    'code': "POLY", # символьная переменная по инструменту
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


def parse(file_path):
    pass

def parse_args(argv):
    pass

def main(argv):
    parse_args(argv)
    req = urllib.request.Request(url=f"http://export.finam.ru/POLY_170620_170623.txt?market={query['market']}&em={query['em']}&code={query['code']}&apply={query['apply']}&df={query['df']}&mf={query['mf']}&yf={query['yf']}&from={query['from']}&dt={query['dt']}&mt={query['mt']}&yt={query['yt']}&to={query['to']}&p={query['p']}&f={query['f']}&e={query['e']}&cn={query['cn']}&dtf={query['dtf']}&tmf={query['tmf']}&MSOR={query['MSOR']}&mstime={query['mstime']}&mstimever={query['mstimever']}&sep={query['sep']}&sep2={query['sep2']}&datf={query['datf']}&at={query['at']}")
    with urllib.request.urlopen(req) as readFile, open("test.txt", mode="w", encoding="utf-8") as writeFile:
        writeFile.write(readFile.read().decode('utf-8'))

if __name__ == "__main__":
    main(sys.argv[1:])