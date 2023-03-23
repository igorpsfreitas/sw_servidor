lista = [{'id': 8, 'Status': 'OUT', 'UID': 412016766239108128, 'RESULT': 'OK', 'Time_stamp': '13:14:33'},
         {'id': 10, 'Status': 'OUT', 'UID': 43716666239108128, 'RESULT': 'OK', 'Time_stamp': '13:15:18'},
         {'id': 12, 'Status': 'OUT', 'UID': 4201220424516144, 'RESULT': 'OK', 'Time_stamp': '13:16:23'},
         {'id': 20, 'Status': 'OUT', 'UID': 419216866239108128, 'RESULT': 'OK', 'Time_stamp': '14:26:37'},
         {'id': 22, 'Status': 'OUT', 'UID': 414516866239108129, 'RESULT': 'OK', 'Time_stamp': '14:28:14'},
         {'id': 24, 'Status': 'OUT', 'UID': 43116866239108129, 'RESULT': 'OK', 'Time_stamp': '15:28:58'},
         {'id': 26, 'Status': 'OUT', 'UID': 414516866239108128, 'RESULT': 'OK', 'Time_stamp': '15:30:05'},
         {'id': 28, 'Status': 'OUT', 'UID': 4201220424516144, 'RESULT': 'OK', 'Time_stamp': '15:31:25'},
         {'id': 30, 'Status': 'OUT', 'UID': 412016766239108128, 'RESULT': 'OK', 'Time_stamp': '15:32:43'}]

lista2 = [1,2,3,4,5,36,7,12,3,4,5,6,7,2,34,5,6]

t = len(lista2) - 5
print(lista2[t:])
print(lista2[lista2.index(lista2[-1]) - 4: ])