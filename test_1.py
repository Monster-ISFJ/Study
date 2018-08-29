# coding:utf-8
import requests
tt = requests.get('http://www.test.com/')
print tt.status_code
print tt.url
print tt.history
