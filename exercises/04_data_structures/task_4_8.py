# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:

- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате надо добавить два пробела между столбцами)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = "192.168.3.1"


ip_split = ip.split('.')                    # Разбиваем на октеты
hex_ip_split_oct1 = int (ip_split[0],16)
bin_ip_split_oct1 = bin (hex_ip_split_oct1)
oct1 = bin_ip_split_oct1.lstrip('0b')

hex_ip_split_oct2 = int (ip_split[1],16)
bin_ip_split_oct2 = bin (hex_ip_split_oct2)
oct2 = bin_ip_split_oct2.lstrip('0b')

hex_ip_split_oct3 = int (ip_split[2],16)
bin_ip_split_oct3 = bin (hex_ip_split_oct3)
oct3 = bin_ip_split_oct3.lstrip('0b')

hex_ip_split_oct4 = int (ip_split[3],16)
bin_ip_split_oct4 = bin (hex_ip_split_oct4)
oct4 = bin_ip_split_oct4.lstrip('0b')


int_ip1 = int(ip_split[0])
int_ip2 = int(ip_split[1])
int_ip3 = int(ip_split[2])
int_ip4 = int(ip_split[3])


print (f'''
{int_ip1:<9} {int_ip2:<9} {int_ip3:<9} {int_ip4:<9}
{oct1:>09} {oct2:>09} {oct3:>09} {oct4:>09}''')




