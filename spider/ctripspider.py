import requests

payload = {"biz": 1, "contrl": 3, "facility": 0, "faclist": [], "key": "", "keytp": 0, "pay": 0, "querys": [],
           "setInfo": {"cityId": 477, "dstId": 0, "inDay": "2016-02-24", "outDay": "2016-02-25"},
           "sort": {"dir": 1, "idx": 2, "ordby": 0, "size": 15}, "qbitmap": 0, "alliance": {"ishybrid": 0},
           "head": {"cid": "09031076410193757977", "ctok": "", "cver": "1.0", "lang": "01", "sid": "8888",
                    "syscode": "09", "auth": 'null', "extension": [{"name": "protocal", "value": "http"}]},
           "contentType": "json"}
resp = requests.post('http://m.ctrip.com/restapi/soa2/10932/hotel/Product/HotelGet?_fxpcqlniredt=09031076410193757977',
              data=payload)

print(resp.content)
