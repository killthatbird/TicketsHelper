import xlrd


def readinfo(path):
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_index(0)
    for each_item in sheet._cell_values:
        for each_attr in each_item:
            print(str(each_attr).replace('.0', ''), end='  ')
        print('\r\n')


if __name__ == '__main__':
    readinfo('D:/Users/XuLu/PycharmProjects/TicketsHelper/university.xlsx')
