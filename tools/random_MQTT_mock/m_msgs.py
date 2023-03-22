from m_mqtt import *
from time import sleep

placas = [
    [4, 30, 168, 66, 239, 108, 129],
    [4, 31, 168, 66, 239, 108, 129],
    [4, 37, 166, 66, 239, 108, 128],
    [4, 120, 167, 66, 239, 108, 128],
    [4, 145, 168, 66, 239, 108, 129],
    [4, 145, 168, 66, 239, 108, 128],
    [4, 192, 168, 66, 239, 108, 128],
    [4, 201, 220, 42, 45, 16, 144] 
]


msg_mpo = {
    "Status": None, # "IN", "OUT"
    "UID": None, #placa
    "Time_stamp": None,
    "RESULT": None # "OK", "NOK"
    }

msg_sld = {
    "Status": None,
    "UID": None, #placa
    "Time_stamp": None, #"00:00:00" 
    "baia": None, #0 a 8
    "RESULT": None # "OK", "NOK"
}

msg_hbw = {
    "Status": None,
    "UID": None, #placa
    "Time_stamp": None, #"00:00:00" 
    "Local": None, #"Debug_FT", "Debug_ICT"
    "Baia": None, #0 a 2
    # Caso ICT:
    "Destino": None, #"Saida" ou "Scrap"
    # Caso FT
    "Next": None, #"Final" ou "Scrap"
}


# Lista de dados pre-fabricados:
mpo_ = [
    '{"Status": "IN", "UID": [4, 201, 220, 42, 45, 16, 144], "Time_stamp": "13:11:36"}',      
    '{"Status": "OUT", "UID": [4, 201, 220, 42, 45, 16, 144], "RESULT": "NOK", "Time_stamp": "13:11:48"}',
    '{"Status": "IN", "UID": [4, 31, 168, 66, 239, 108, 129], "Time_stamp": "13:12:33"}',
    '{"Status": "OUT", "UID": [4, 31, 168, 66, 239, 108, 129], "RESULT": "NOK", "Time_stamp": "13:12:46"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 129], "Time_stamp": "13:13:27"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 129], "RESULT": "NOK", "Time_stamp": "13:13:39"}',
    '{"Status": "IN", "UID": [4, 120, 167, 66, 239, 108, 128], "Time_stamp": "13:14:20"}',
    '{"Status": "OUT", "UID": [4, 120, 167, 66, 239, 108, 128], "RESULT": "OK", "Time_stamp": "13:14:33"}',
    '{"Status": "IN", "UID": [4, 37, 166, 66, 239, 108, 128], "Time_stamp": "13:15:05"}',
    '{"Status": "OUT", "UID": [4, 37, 166, 66, 239, 108, 128], "RESULT": "OK", "Time_stamp": "13:15:18"}',
    '{"Status": "IN", "UID": [4, 201, 220, 42, 45, 16, 144], "Time_stamp": "13:16:10"}',
    '{"Status": "OUT", "UID": [4, 201, 220, 42, 45, 16, 144], "RESULT": "OK", "Time_stamp": "13:16:23"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 128], "Time_stamp": "13:20:45"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 128], "RESULT": "NOK", "Time_stamp": "13:20:58"}',
    '{"Status": "IN", "UID": [4, 192, 168, 66, 239, 108, 128], "Time_stamp": "13:21:43"}',
    '{"Status": "OUT", "UID": [4, 192, 168, 66, 239, 108, 128], "RESULT": "NOK", "Time_stamp": "13:21:56"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 128], "Time_stamp": "13:23:10"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 128], "RESULT": "NOK", "Time_stamp": "13:23:23"}',
    '{"Status": "IN", "UID": [4, 192, 168, 66, 239, 108, 128], "Time_stamp": "13:26:23"}',
    '{"Status": "OUT", "UID": [4, 192, 168, 66, 239, 108, 128], "RESULT": "OK", "Time_stamp": "13:26:37"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 129], "Time_stamp": "13:27:58"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 129], "RESULT": "OK", "Time_stamp": "13:28:14"}',
    '{"Status": "IN", "UID": [4, 31, 168, 66, 239, 108, 129], "Time_stamp": "13:28:46"}',
    '{"Status": "OUT", "UID": [4, 31, 168, 66, 239, 108, 129], "RESULT": "OK", "Time_stamp": "13:28:58"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 128], "Time_stamp": "13:29:53"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 128], "RESULT": "OK", "Time_stamp": "13:30:05"}',
    '{"Status": "IN", "UID": [4, 201, 220, 42, 45, 16, 144], "Time_stamp": "13:31:12"}',
    '{"Status": "OUT", "UID": [4, 201, 220, 42, 45, 16, 144], "RESULT": "OK", "Time_stamp": "13:31:25"}',
    '{"Status": "IN", "UID": [4, 120, 167, 66, 239, 108, 128], "Time_stamp": "13:32:31"}',
    '{"Status": "OUT", "UID": [4, 120, 167, 66, 239, 108, 128], "RESULT": "OK", "Time_stamp": "13:32:43"}'
]

sld_ = [
    '{"Status": "IN", "UID": [4, 120, 167, 66, 239, 108, 128], "baia": 0, "Time_stamp": "13:14:59"}',
    '{"Status": "IN", "UID": [4, 37, 166, 66, 239, 108, 128], "baia": 3, "Time_stamp": "13:15:52"}',
    '{"Status": "IN", "UID": [4, 201, 220, 42, 45, 16, 144], "baia": 6, "Time_stamp": "13:17:01"}',
    '{"Status": "OUT", "UID": [4, 120, 167, 66, 239, 108, 128], "Time_stamp": "13:17:05", "RESULT": "NOK"}',
    '{"Status": "OUT", "UID": [4, 37, 166, 66, 239, 108, 128], "Time_stamp": "13:17:55", "RESULT": "OK"}',
    '{"Status": "OUT", "UID": [4, 201, 220, 42, 45, 16, 144], "Time_stamp": "13:18:55", "RESULT": "OK"}',
    '{"Status": "IN", "UID": [4, 30, 168, 66, 239, 108, 129], "baia": 0, "Time_stamp": "13:22:03"}',
    '{"Status": "IN", "UID": [4, 37, 166, 66, 239, 108, 128], "baia": 3, "Time_stamp": "13:22:36"}',
    '{"Status": "IN", "UID": [4, 120, 167, 66, 239, 108, 128], "baia": 6, "Time_stamp": "13:22:45"}',
    '{"Status": "OUT", "UID": [4, 30, 168, 66, 239, 108, 129], "Time_stamp": "13:24:10", "RESULT": "NOK"}',
    '{"Status": "OUT", "UID": [4, 37, 166, 66, 239, 108, 128], "Time_stamp": "13:24:38", "RESULT": "OK"}',
    '{"Status": "OUT", "UID": [4, 120, 167, 66, 239, 108, 128], "Time_stamp": "13:25:01", "RESULT": "NOK"}',
    '{"Status": "IN", "UID": [4, 192, 168, 66, 239, 108, 128], "baia": 0, "Time_stamp": "13:27:09"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 129], "baia": 3, "Time_stamp": "13:28:42"}',
    '{"Status": "IN", "UID": [4, 31, 168, 66, 239, 108, 129], "baia": 6, "Time_stamp": "13:29:34"}',
    '{"Status": "OUT", "UID": [4, 192, 168, 66, 239, 108, 128], "Time_stamp": "13:30:01", "RESULT": "OK"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 128], "baia": 0, "Time_stamp": "13:30:34"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 129], "Time_stamp": "13:31:19", "RESULT": "OK"}',
    '{"Status": "OUT", "UID": [4, 31, 168, 66, 239, 108, 129], "Time_stamp": "13:31:38", "RESULT": "OK"}',
    '{"Status": "IN", "UID": [4, 201, 220, 42, 45, 16, 144], "baia": 3, "Time_stamp": "13:31:51"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 128], "Time_stamp": "13:32:48", "RESULT": "NOK"}',
    '{"Status": "IN", "UID": [4, 120, 167, 66, 239, 108, 128], "baia": 0, "Time_stamp": "13:33:16"}',
    '{"Status": "OUT", "UID": [4, 201, 220, 42, 45, 16, 144], "Time_stamp": "13:33:53", "RESULT": "OK"}',
    '{"Status": "OUT", "UID": [4, 120, 167, 66, 239, 108, 128], "Time_stamp": "13:36:37", "RESULT": "OK"}'
]

hbw_ = [
    '{"Status": "IN", "UID": [4, 201, 220, 42, 45, 16, 144], "Local": "Debug_ICT", "Baia": 0, "Time_stamp": "13:12:14"}',
    '{"Status": "IN", "UID": [4, 31, 168, 66, 239, 108, 129], "Local": "Debug_ICT", "Baia": 1, "Time_stamp": "13:13:07"}',                                          
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 129], "Local": "Debug_ICT", "Baia": 2, "Time_stamp": "13:14:00"}',
    '{"Status": "OUT", "UID": [4, 201, 220, 42, 45, 16, 144], "Local": "Debug_ICT", "Result": "OK", "Destino": "Saida", "Baia": 0, "Time_stamp": "13:16:00"}',
    '{"Status": "OUT", "UID": [4, 31, 168, 66, 239, 108, 129], "Local": "Debug_ICT", "Result": "OK", "Destino": "Saida", "Baia": 1, "Time_stamp": "13:17:07"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 129], "Local": "Debug_ICT", "Result": "OK", "Destino": "Saida", "Baia": 2, "Time_stamp": "13:18:23"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 128], "Local": "Debug_ICT", "Baia": 0, "Time_stamp": "13:21:26"}',
    '{"Status": "IN", "UID": [4, 192, 168, 66, 239, 108, 128], "Local": "Debug_ICT", "Baia": 1, "Time_stamp": "13:22:17"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 128], "Local": "Debug_ICT", "Result": "OK", "Destino": "Saida", "Baia": 0, "Time_stamp": "13:22:59"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 128], "Local": "Debug_ICT", "Baia": 0, "Time_stamp": "13:23:48"}',
    '{"Status": "IN", "UID": [4, 30, 168, 66, 239, 108, 129], "Local": "Debug_FT", "Baia": 0, "Time_stamp": "13:24:36"}',
    '{"Status": "IN", "UID": [4, 120, 167, 66, 239, 108, 128], "Local": "Debug_FT", "Baia": 1, "Time_stamp": "13:25:25"}',
    '{"Status": "OUT", "UID": [4, 192, 168, 66, 239, 108, 128], "Local": "Debug_ICT", "Result": "OK", "Destino": "Saida", "Baia": 1, "Time_stamp": "13:26:13"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 128], "Local": "Debug_ICT", "Result": "OK", "Destino": "Saida", "Baia": 0, "Time_stamp": "13:29:42"}',
    '{"Status": "OUT", "UID": [4, 30, 168, 66, 239, 108, 129], "Local": "Debug_FT", "Result": "NOK", "Next": "Scrap", "Baia": 0, "Time_stamp": "13:30:46"}',
    '{"Status": "OUT", "UID": [4, 120, 167, 66, 239, 108, 128], "Local": "Debug_FT", "Result": "OK", "Next": "Final", "Baia": 1, "Time_stamp": "13:32:20"}',
    '{"Status": "IN", "UID": [4, 145, 168, 66, 239, 108, 128], "Local": "Debug_FT", "Baia": 0, "Time_stamp": "13:33:22"}',
    '{"Status": "OUT", "UID": [4, 145, 168, 66, 239, 108, 128], "Local": "Debug_FT", "Result": "NOK", "Next": "Scrap", "Baia": 0, "Time_stamp": "13:36:23"}'
]

# Testes:
if __name__ == "__main__":
    client = connect_mqtt(id)
    for i in mpo_:
        publish(client, mpo, i)
        sleep(0.5)
    for i in sld_:
        publish(client, sld, i)
        sleep(0.5)
    for i in hbw_:
        publish(client, hbw, i)
        sleep(0.5)