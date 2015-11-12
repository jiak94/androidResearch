import requests
import json
import os

def download(url, filename):
	r = requests.get(url)
	with open(filename, "wb") as code:
		code.write(r.content)


if __name__ == '__main__':
    js_file = open("./hot.json")

    for line in js_file:
        data = json.loads(line)
        url = data['file_urls'][0]
        # filename = "./anzhi_apk/" + data['file_name'][0] + ".apk"
       	#filename = data['file_name'][0].decode("unicode_escape")
        #print type(filename)
        #filename = "./anzhi_apk/" + filename + ".apk"
        # print type(filename)
        r = requests.head(url)
        real_link = r.headers['Location']
        # print filename
        # print url
        # print real_link
        filename = real_link[real_link.rfind("/")+1:]
        print real_link
        download(real_link, filename)