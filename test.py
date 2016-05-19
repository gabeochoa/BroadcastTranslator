#!/usr/bin/python
# vim: set fileencoding=utf8 :
from konlpy.tag import Kkma
from konlpy.utils import pprint
from convert import convert
import fileinput

kkma = Kkma()
pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
#poss = kkma.pos(u'(오류보고는) "실행환경", 에러메세지와함께 설명을 최대한상세히!^^')


for line in fileinput.input():
    poss = kkma.pos(unicode(line, "utf-8"))
    for tup in poss:
        print tup[0],
        print convert(tup[1])
