# -*- coding: utf-8 -*-
"""
Thanks to the author Ruhan Sa, who is the TA of IR project 3 in Fall 2015
"""

import json
import urllib.request

count = 1
with open('D:\\Project 3\\test_query.txt', encoding="utf-8") as f:
    #outf = open('VSM.txt', 'w')
    for line in f:
        query = line.strip('\n').replace(':', '')
        query = urllib.parse.quote(query)
        inurl = 'http://localhost:8983/solr/VSM/select?fl=id,score&indent=on&q=' + query + '&defType=dismax&pf=text_en^2%20+%20text_de^2%20+%20text_ru^2&qf=text_en^2%20+%20text_de^2%20+%20text_ru^2&rows=20&wt=json'
        "qid = count"
        IRModel = 'VSM'
        outf = open(str(count) + '.txt', 'w')
        data = urllib.request.urlopen(inurl).read()
        docs = json.loads(data.decode('utf-8'))['response']['docs']
        rank = 1
        if count<10:
            qid='00' + str(count)
        else:
            qid='0' + str(count)
        for doc in docs:
            outf.write(str(qid) + ' ' + 'Q' + str(count) + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + 'VSM' + '\n')
            rank += 1
        outf.close()
        count += 1







#defType=dismax&fl=id,score&indent=on&pf=text_en^2%20+%20text_de^2%20+%20text_ru^2&q=Russia%27s%20intervention%20in%20Syria&qf=text_en^2%20+%20text_de^2%20+%20text_ru^2&rows=20&start=0&wt=json
