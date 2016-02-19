import requests

from config import configuration
from entity.ticket import ticket


def search_tickets(query_date, from_station, to_station):
    result = list()
    headers = {'user-agent': configuration.user_agent, 'referer': 'https://kyfw.12306.cn/otn/lcxxcx/init'}
    search_url = configuration.query_url + '?purpose_codes=ADULT' + '&queryDate=' + query_date + '&from_station=' + from_station + '&to_station=' + to_station
    req = requests.get(search_url, headers=headers, verify=False)
    if req.status_code == 200:
        datas = req.json()['data'].get('datas')
        for each_data in datas:
            seats_info = {}
            if each_data['yw_num'] != '--' and each_data['yw_num'] != '无':
                seats_info['硬卧'] = each_data['yw_num']
            if each_data['wz_num'] != '--' and each_data['wz_num'] != '无':
                seats_info['无坐'] = each_data['wz_num']
            if each_data['yz_num'] != '--' and each_data['yz_num'] != '无':
                seats_info['硬座'] = each_data['yz_num']
            if each_data['zy_num'] != '--' and each_data['zy_num'] != '无':
                seats_info['一等座'] = each_data['zy_num']
            if each_data['ze_num'] != '--' and each_data['ze_num'] != '无':
                seats_info['二等座'] = each_data['ze_num']
            if each_data['rz_num'] != '--' and each_data['rz_num'] != '无':
                seats_info['软座'] = each_data['rz_num']

            if len(seats_info) > 0:
                ticket_ = ticket(each_data['from_station_name'], each_data['to_station_name'], seats_info, '暂无票价',
                                 each_data['start_time'],
                                 each_data['arrive_time'])
                result.append(ticket_)
    else:
        print('error!')

    return result


def make_message(result):
    message_info = ''
    for each_item in result:
        message_info += each_item.from_station_name + ' -- ' + each_item.to_station_name + '\t' + each_item.ticketobj_start_time + ' -- ' + each_item.ticketobj_arrive_time
        for key, value in each_item.seats_info.items():
            message_info = message_info + '\t' + key + ' : ' + value
        message_info += '\r\n'

    return message_info


if __name__ == '__main__':
    query_result = search_tickets(query_date='2016-02-26', from_station='JMN', to_station='WCN')
    message_info = make_message(query_result)
    print(message_info)