import requests
from config import configuration
import json

from entity.ticket import ticket


def search_tickets(query_date, from_station, to_station):
    result = list()
    headers = {'user-agent': configuration.user_agent}
    search_url = configuration.query_url + '?purpose_codes=ADULT' + '&queryDate=' + query_date + '&from_station=' + from_station + '&to_station=' + to_station
    req = requests.get(search_url, headers=headers, verify=False)
    if req.status_code == 200:
        datas = req.json()['data'].get('datas')
        for each_data in datas:
            seats_info = {}
            if each_data['yw_num'] is not '--' or each_data['yw_num'] is not '无':
                seats_info['硬卧'] = each_data['yw_num']
            if each_data['wz_num'] is not '--' or each_data['wz_num'] is not '无':
                seats_info['无坐'] = each_data['wz_num']
            if each_data['yz_num'] is not '--' or each_data['yz_num'] is not '无':
                seats_info['硬座'] = each_data['yz_num']
            if each_data['zy_num'] is not '--' or each_data['zy_num'] is not '无':
                seats_info['一等座'] = each_data['zy_num']
            if each_data['ze_num'] is not '--' or each_data['ze_num'] is not '无':
                seats_info['二等座'] = each_data['ze_num']
            if each_data['yz_num'] is not '--' or each_data['yz_num'] is not '无':
                seats_info['软座'] = each_data['yz_num']
            ticket_ = ticket(each_data['from_station_name'], each_data['end_station_name'], seats_info, '暂无票价',
                             each_data['start_time'],
                             each_data['arrive_time'])
            result.append(ticket_)
    else:
        print('error!')

    return result


if __name__ == '__main__':
    query_result = search_tickets(query_date='2016-04-07', from_station='BXP', to_station='GZQ')
    for each_item in query_result:
        print(each_item.from_station_name)
