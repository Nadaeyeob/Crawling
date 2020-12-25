import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import simplejson as json
# import json

# Dict(JSON) 선언

data = {}
data['people'] = []
data['people'].append({
    'name' : 'kim',
    'website' : 'naver.com',
    'from' : 'seoul',
    'grade' : [95,77,89,91]
})
data['people'].append({
    'name' : 'park',
    'website' : 'google.com',
    'from' : 'busan',
    'grade' : [80,45,71,97]

})
data['people'].append({
    'name' : 'lee',
    'website' : 'daum.com',
    'from' : 'gwanju',
    'grade' : [100,4,21,17]

})

#JSON 파일쓰기(dump)

with open('c:/crawling/section4/member1.json','w') as outfile:
    json.dump(data, outfile)

with open('c:/crawling/section4/member1.json','r') as infile:
    r = json.load(infile)
    print(type(r))
    print(r)
    print('------')

    for p in r['people']:
        print('name + '+ p['name'])
        print('website + ' + p['website'])
        print('from + ' + p['from'])
        t = p['grade']
        grade = ''
        for g in t:
            grade = grade + ' ' + str(g)
            print('grade + ',grade.lstrip())
            print('')
