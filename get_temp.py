import subprocess
import pprint
import json
city = "Oskemen"
command = "curl 'https://narodmon.ru/lst/0' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: \"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"' \
  -H 'DNT: 1' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: */*' \
  -H 'Origin: https://narodmon.ru' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://narodmon.ru/' \
  -H 'Accept-Language: en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7' \
  -H 'Cookie: PHPSESSID=vc2bp741lh86sjrfi4346tjqmbjpv19f; uuid=8d4863e21fbebc768e2b72c6e6bee83a; _ym_uid=1610123110729558703; _ym_d=1610123110; _ym_isad=1; nobanner=1; welcome=1; zoom=11; lat=49.882205; lon=82.653701' \
  --data-raw 'ajax=1&types=&ourcam=1&bounds=49.699726,82.562721,50.063993,82.744682' \
  --compressed"

res = subprocess.run(command, shell = True, capture_output = True)
if res.returncode == 0:
	json_val = filter(lambda x: len(x) > 7, json.loads(res.stdout))
	json_val = filter(lambda x: 'Oskemen' in x[5], json_val)
	json_val = filter(lambda x: x[1] == 1, json_val)
	temp = list(map(lambda x: int(x[7]), json_val))
	avg_temp = sum(temp) / len(temp)
	min_temp = min(temp)
	max_temp = max(temp)
	print("min: {0}; max: {1}; avg: {2};".format(min_temp, max_temp, avg_temp))

