# -*- coding: utf-8 -*-
import requests
from tools import format_colon_string

url = 'http://www.dianping.com/beijing/ch95/g25147'

headers = format_colon_string('''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Cookie: cy=2; cye=beijing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16f18125565c8-00f6ff894f1a16-12326b5a-13c680-16f18125565c8; _lxsdk=16f18125565c8-00f6ff894f1a16-12326b5a-13c680-16f18125565c8; _hc.v=d98aa14e-9c4a-d996-6e1c-1907452a629c.1576656853; s_ViewType=10; _lxsdk_s=16f18327094-b9b-1f4-217%7C%7C4
Host: www.dianping.com
Pragma: no-cache
Proxy-Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36''')

req = requests.get(url=url, headers=headers).text

print(req)

