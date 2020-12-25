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
    'from' : 'seoul'
})
data['people'].append({
    'name' : 'park',
    'website' : 'google.com',
    'from' : 'busan'
})
data['people'].append({
    'name' : 'lee',
    'website' : 'daum.com',
    'from' : 'gwanju'
})

print(type(data)) # <class 'dict'>
print(data)
# {'people': [{'name': 'kim', 'website': 'naver.com', 'from': 'seoul'}, {'name': '[park]', 'website': 'google.com', 'from': 'busan'}, {'name': 'lee', 'website': 'daum.com', 'from': 'gwanju'}]}
print('------')

# dump vs dumps, load vs loads
# Dict(JSON) -> Str
e = json.dumps(data, indent=4) # indent 사용하면 자동으로 들여쓰기
print(type(e)) # <class 'str'>
print(e)

d = json.loads(e)
print(type(d)) # <class 'dict'>
print(d)

with open('c:/crawling/section4/member.json','w') as outfile:
    outfile.write(e)
    #jsoneditoronline.org

with open('c:/crawling/section4/member.json','r') as infile:
    r = json.loads(infile.read())
    print('------')
    print(type(r)) # <class 'dict'>
    print(r)
    for p in r['people']:
        print('name + '+ p['name'])
        print('website + ' + p['website'])
        print('from + ' + p['from'])
