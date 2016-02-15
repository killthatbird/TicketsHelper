import requests
from config import configuration


def search_tickets(query_date, from_station, to_station):
    headers = {'user-agent': configuration.user_agent}
    search_url = configuration.query_url + '?purpose_codes=ADULT' + '&queryDate=' + query_date + '&from_station=' + from_station + '&to_station=' + to_station
    req = requests.get(search_url, headers=headers, verify=False)
    if req.status_code < 400:
        print(req.text)


if __name__ == '__main__':
    search_tickets(query_date='2016-02-17', from_station='JMN', to_station='WCN')
