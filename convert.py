#!/usr/bin/python
# vim: set fileencoding=utf8 :

'''
"SL":["Open Quote",u"여는 따옴표 및 묶음"],
"SD":["Dash", u"이음"],
"SU":["Unit", u"단위 기호"],
"SE":["Elipsys",u"줄임표"],
"SR":["Closing Quote", u" 닫는 따옴표 및 묶음표"],
"SY":["Other Symbols", u"기타 기호"],
"F":["Foreign Word", u"외국어"],
"NCPA":["Action Verb", u"동작성 명사"],
'''
#http://kkma.snu.ac.kr/documents/?doc=postag
convmap = ({
    "SP":["Comma",u"쉼표"],
    "NNG":["General Verb", "일반 명사"],
    "NNP":["Distinct? Verb", "고유 명사"],
    "NNB":["Dependent Verb", "의존 명사"],
    "JKS":["Nominative particle", "주격 조사"],
    "JKM":["Adverbial particle?", "부사격 조사"],
    "MAG":["General Adverb", "일반 부사"],
    "SF":["Punctuation", "기타 접미사"],
    "JKO":["Object particle", "목적격 조사"],
    "JX":["Auxilary Particle (Topic Particle)","보조사"],
    "SS":["Punctuation?",""],
    "EMO":["Emoticon", ""]
})



def convert(pos):
    if(pos in convmap):
        return convmap[pos][0]
    return pos
