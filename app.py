from argparse import ArgumentParser
import urllib.request
import sys

query = {
    'market': "1", 
    'em': "175924",
    'code': "POLY",
    'apply': "0",
    'df': "20",
    'mf': "4",
    'yf': "2017",
    'from': "20.05.2017", 
    'dt': "23",
    'mt': "5",
    'yt': "2017",
    'to': "23.06.2017",
    'p': "2",
    'f': "test",
    'e': ".txt",
    'cn': "POLY",
    'dtf': "1",
    'tmf': "1",
    'MSOR': "1",
    'mstime': "on",
    'mstimever': "1",
    'sep': "1",
    'sep2': "1",
    'datf': "4",
    'at': "1"
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