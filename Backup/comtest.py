import urllib3
http = urllib3.PoolManager()
#response = http.request("GET", "http://192.168.1.107/command_90,90,3,49,")
s = [2, 3, 1, 4, 5, 3]
print(sorted(range(len(s)), key=lambda k: s[k]))