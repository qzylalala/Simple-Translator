import urllib.request as ur
import urllib.parse as up
import json

for i in range(1, 100):
	word = input('请输入英文: ')
	data = {'kw' : word}
	data_url = up.urlencode(data)

	request = ur.Request(
		url = 'https://fanyi.baidu.com/sug',
		data = data_url.encode('utf-8'),
	)
	response = ur.urlopen(request).read()
	ret = json.loads(response)
	translate = ret['data'][0]['v']
	print(translate)