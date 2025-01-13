import json
import matplotlib.pyplot as plt

data = {
    "one_time_purchase": [
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 788.0,
            "Price": 31500.0,
            "m²": 39.97,
            "Address": "Purvciema 50"
        },
        {
            "Price_per_m²": 1600.0,
            "Price": 80000.0,
            "m²": 50.0,
            "Address": "Vaidavas 3A"
        },
        {
            "Price_per_m²": 1320.0,
            "Price": 102960.0,
            "m²": 78.0,
            "Address": "Madonas 19"
        },
        {
            "Price_per_m²": 1047.0,
            "Price": 45000.0,
            "m²": 42.98,
            "Address": "Andromedas g. 5A"
        },
        {
            "Price_per_m²": 769.0,
            "Price": 30000.0,
            "m²": 39.01,
            "Address": "Nīcgales 19"
        },
        {
            "Price_per_m²": 1491.0,
            "Price": 82000.0,
            "m²": 55.0,
            "Address": "Ilūkstes 99"
        },
        {
            "Price_per_m²": 1122.0,
            "Price": 55000.0,
            "m²": 49.02,
            "Address": "Žagatu 20"
        },
        {
            "Price_per_m²": 1053.0,
            "Price": 60000.0,
            "m²": 56.98,
            "Address": "Nīcgales 19"
        },
        {
            "Price_per_m²": 1552.0,
            "Price": 135000.0,
            "m²": 86.98,
            "Address": "Pūces 47"
        },
        {
            "Price_per_m²": 981.0,
            "Price": 26500.0,
            "m²": 27.01,
            "Address": "Ilūkstes 56"
        },
        {
            "Price_per_m²": 2372.0,
            "Price": 185000.0,
            "m²": 77.99,
            "Address": "Žagatu 7"
        },
        {
            "Price_per_m²": 1197.0,
            "Price": 39500.0,
            "m²": 33.0,
            "Address": "Ieriķu 66"
        },
        {
            "Price_per_m²": 746.0,
            "Price": 45500.0,
            "m²": 60.99,
            "Address": "Dzelzavas 61"
        },
        {
            "Price_per_m²": 1306.0,
            "Price": 64000.0,
            "m²": 49.0,
            "Address": "Zvaigznāja g. 14"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 64200.0,
            "m²": 62.03,
            "Address": "Dzelzavas 76k2"
        },
        {
            "Price_per_m²": 2381.0,
            "Price": 159500.0,
            "m²": 66.99,
            "Address": "Stirnu 4"
        },
        {
            "Price_per_m²": 1396.0,
            "Price": 64200.0,
            "m²": 45.99,
            "Address": "Ieriķu 26"
        },
        {
            "Price_per_m²": 1039.0,
            "Price": 80000.0,
            "m²": 77.0,
            "Address": "Madonas 19"
        },
        {
            "Price_per_m²": 1027.0,
            "Price": 76000.0,
            "m²": 74.0,
            "Address": "Stirnu 37a"
        },
        {
            "Price_per_m²": 1020.0,
            "Price": 52000.0,
            "m²": 50.98,
            "Address": "Staiceles 1 k-2"
        },
        {
            "Price_per_m²": 2225.0,
            "Price": 89000.0,
            "m²": 40.0,
            "Address": "Upeņu 19"
        },
        {
            "Price_per_m²": 1031.0,
            "Price": 62900.0,
            "m²": 61.01,
            "Address": "Dzelzavas 76"
        },
        {
            "Price_per_m²": 1098.0,
            "Price": 54900.0,
            "m²": 50.0,
            "Address": "Nīcgales 53"
        },
        {
            "Price_per_m²": 768.0,
            "Price": 43000.0,
            "m²": 55.99,
            "Address": "Ieriķu 37"
        },
        {
            "Price_per_m²": 1474.0,
            "Price": 84000.0,
            "m²": 56.99,
            "Address": "Viršu 5"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 64500.0,
            "m²": 62.02,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 781.0,
            "Price": 50000.0,
            "m²": 64.02,
            "Address": "Staiceles 11"
        },
        {
            "Price_per_m²": 2309.0,
            "Price": 106200.0,
            "m²": 45.99,
            "Address": "Dzelzavas 106"
        },
        {
            "Price_per_m²": 1714.0,
            "Price": 108000.0,
            "m²": 63.01,
            "Address": "Upeņu 17"
        },
        {
            "Price_per_m²": 1838.0,
            "Price": 73500.0,
            "m²": 39.99,
            "Address": "Sesku 7-k1"
        },
        {
            "Price_per_m²": 2125.0,
            "Price": 85000.0,
            "m²": 40.0,
            "Address": "Astras 8k1"
        },
        {
            "Price_per_m²": 1179.0,
            "Price": 33000.0,
            "m²": 27.99,
            "Address": "Marsa g. 6"
        },
        {
            "Price_per_m²": 875.0,
            "Price": 35000.0,
            "m²": 40.0,
            "Address": "Vaidavas 2 k-3"
        },
        {
            "Price_per_m²": 1051.0,
            "Price": 62000.0,
            "m²": 58.99,
            "Address": "Ilūkstes 56"
        },
        {
            "Price_per_m²": 845.0,
            "Price": 35500.0,
            "m²": 42.01,
            "Address": "Vaidavas 2/4"
        },
        {
            "Price_per_m²": 899.0,
            "Price": 62900.0,
            "m²": 69.97,
            "Address": "Zvaigznāja g. 14"
        },
        {
            "Price_per_m²": 1080.0,
            "Price": 54000.0,
            "m²": 50.0,
            "Address": "Varavīksnes g. 18"
        },
        {
            "Price_per_m²": 867.0,
            "Price": 39000.0,
            "m²": 44.98,
            "Address": "Dzelzavas 33"
        },
        {
            "Price_per_m²": 1017.0,
            "Price": 59000.0,
            "m²": 58.01,
            "Address": "Madonas 27"
        },
        {
            "Price_per_m²": 1014.0,
            "Price": 36500.0,
            "m²": 36.0,
            "Address": "Dzelzavas 35"
        },
        {
            "Price_per_m²": 2257.0,
            "Price": 158000.0,
            "m²": 70.0,
            "Address": "Upeņu 21"
        },
        {
            "Price_per_m²": 893.0,
            "Price": 41100.0,
            "m²": 46.02,
            "Address": "Nīcgales 12"
        },
        {
            "Price_per_m²": 1352.0,
            "Price": 82500.0,
            "m²": 61.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1406.0,
            "Price": 67500.0,
            "m²": 48.01,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 878.0,
            "Price": 43000.0,
            "m²": 48.97,
            "Address": "Andromedas g. 4"
        },
        {
            "Price_per_m²": 1782.0,
            "Price": 99800.0,
            "m²": 56.0,
            "Address": "Pūces 47"
        },
        {
            "Price_per_m²": 1091.0,
            "Price": 60000.0,
            "m²": 55.0,
            "Address": "Dudajeva g. 4"
        },
        {
            "Price_per_m²": 2767.0,
            "Price": 249000.0,
            "m²": 89.99,
            "Address": "Astras 8 k-1, Rīg"
        },
        {
            "Price_per_m²": 1083.0,
            "Price": 65000.0,
            "m²": 60.02,
            "Address": "Dzelzavas 63"
        },
        {
            "Price_per_m²": 1024.0,
            "Price": 63500.0,
            "m²": 62.01,
            "Address": "Vaidavas 9"
        },
        {
            "Price_per_m²": 1270.0,
            "Price": 63500.0,
            "m²": 50.0,
            "Address": "Ilūkstes 103/2"
        },
        {
            "Price_per_m²": 1378.0,
            "Price": 67500.0,
            "m²": 48.98,
            "Address": "Dudajeva g. 4"
        },
        {
            "Price_per_m²": 1473.0,
            "Price": 109000.0,
            "m²": 74.0,
            "Address": "Burtnieku 36A"
        },
        {
            "Price_per_m²": 1178.0,
            "Price": 68300.0,
            "m²": 57.98,
            "Address": "Brantkalna 4"
        },
        {
            "Price_per_m²": 934.0,
            "Price": 59800.0,
            "m²": 64.03,
            "Address": "Staiceles 9"
        },
        {
            "Price_per_m²": 1111.0,
            "Price": 30000.0,
            "m²": 27.0,
            "Address": "Dudajeva g. 9"
        },
        {
            "Price_per_m²": 964.0,
            "Price": 37600.0,
            "m²": 39.0,
            "Address": "Andromedas g. 5B"
        },
        {
            "Price_per_m²": 929.0,
            "Price": 39000.0,
            "m²": 41.98,
            "Address": "Vaidavas 2k5"
        },
        {
            "Price_per_m²": 960.0,
            "Price": 72000.0,
            "m²": 75.0,
            "Address": "Dzelzavas 40"
        },
        {
            "Price_per_m²": 2522.0,
            "Price": 151300.0,
            "m²": 59.99,
            "Address": "Dzelzavas 104"
        },
        {
            "Price_per_m²": 2455.0,
            "Price": 108000.0,
            "m²": 43.99,
            "Address": "Dzelzavas 106"
        },
        {
            "Price_per_m²": 2614.0,
            "Price": 188200.0,
            "m²": 72.0,
            "Address": "Dzelzavas 106"
        },
        {
            "Price_per_m²": 2589.0,
            "Price": 145000.0,
            "m²": 56.01,
            "Address": "Dzelzavas 106"
        },
        {
            "Price_per_m²": 1020.0,
            "Price": 35700.0,
            "m²": 35.0,
            "Address": "Ilūkstes 109/1"
        },
        {
            "Price_per_m²": 1154.0,
            "Price": 45000.0,
            "m²": 38.99,
            "Address": "Stirnu 13 b"
        },
        {
            "Price_per_m²": 1729.0,
            "Price": 107200.0,
            "m²": 62.0,
            "Address": "Braslas 27"
        },
        {
            "Price_per_m²": 1016.0,
            "Price": 64000.0,
            "m²": 62.99,
            "Address": "Ilūkstes 109 K-1"
        },
        {
            "Price_per_m²": 770.0,
            "Price": 47000.0,
            "m²": 61.04,
            "Address": "Dzelzavas 61"
        },
        {
            "Price_per_m²": 791.0,
            "Price": 62500.0,
            "m²": 79.01,
            "Address": "Purvciema 20"
        },
        {
            "Price_per_m²": 1871.0,
            "Price": 130960.0,
            "m²": 69.99,
            "Address": "Braslas 53"
        },
        {
            "Price_per_m²": 1125.0,
            "Price": 67500.0,
            "m²": 60.0,
            "Address": "Ūnijas 60"
        },
        {
            "Price_per_m²": 902.0,
            "Price": 46900.0,
            "m²": 52.0,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 1081.0,
            "Price": 46500.0,
            "m²": 43.02,
            "Address": "Kalsnavas 2e"
        },
        {
            "Price_per_m²": 1046.0,
            "Price": 53370.0,
            "m²": 51.02,
            "Address": "Dzelzavas 76/3"
        },
        {
            "Price_per_m²": 1328.0,
            "Price": 77000.0,
            "m²": 57.98,
            "Address": "Brantkalna 6"
        },
        {
            "Price_per_m²": 879.0,
            "Price": 36900.0,
            "m²": 41.98,
            "Address": "Andromedas g. 5A"
        },
        {
            "Price_per_m²": 1268.0,
            "Price": 27888.0,
            "m²": 21.99,
            "Address": "Nīcgales 24"
        },
        {
            "Price_per_m²": 1581.0,
            "Price": 68000.0,
            "m²": 43.01,
            "Address": "Kastrānes 2a"
        },
        {
            "Price_per_m²": 968.0,
            "Price": 61000.0,
            "m²": 63.02,
            "Address": "Dzelzavas 76-k3"
        },
        {
            "Price_per_m²": 2453.0,
            "Price": 157000.0,
            "m²": 64.0,
            "Address": "Dzelzavas 104"
        },
        {
            "Price_per_m²": 1150.0,
            "Price": 115000.0,
            "m²": 100.0,
            "Address": "Brantkalna 19"
        },
        {
            "Price_per_m²": 840.0,
            "Price": 39500.0,
            "m²": 47.02,
            "Address": "Nīcgales 21"
        },
        {
            "Price_per_m²": 1026.0,
            "Price": 78000.0,
            "m²": 76.02,
            "Address": "Žagatu 20"
        },
        {
            "Price_per_m²": 858.0,
            "Price": 37770.0,
            "m²": 44.02,
            "Address": "Stirnu 49C"
        },
        {
            "Price_per_m²": 966.0,
            "Price": 58900.0,
            "m²": 60.97,
            "Address": "Madonas 25"
        },
        {
            "Price_per_m²": 913.0,
            "Price": 42000.0,
            "m²": 46.0,
            "Address": "Madonas 25"
        },
        {
            "Price_per_m²": 914.0,
            "Price": 45700.0,
            "m²": 50.0,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1172.0,
            "Price": 68000.0,
            "m²": 58.02,
            "Address": "Viršu 7"
        },
        {
            "Price_per_m²": 917.0,
            "Price": 55000.0,
            "m²": 59.98,
            "Address": "Dudajeva g. 1"
        },
        {
            "Price_per_m²": 1581.0,
            "Price": 75900.0,
            "m²": 48.01,
            "Address": "Madonas 2"
        },
        {
            "Price_per_m²": 792.0,
            "Price": 47500.0,
            "m²": 59.97,
            "Address": "Ūnijas 30"
        },
        {
            "Price_per_m²": 897.0,
            "Price": 56500.0,
            "m²": 62.99,
            "Address": "Nīcgales 3"
        },
        {
            "Price_per_m²": 705.0,
            "Price": 35250.0,
            "m²": 50.0,
            "Address": "Purvciema 44"
        },
        {
            "Price_per_m²": 883.0,
            "Price": 68000.0,
            "m²": 77.01,
            "Address": "Žagatu 20a"
        },
        {
            "Price_per_m²": 945.0,
            "Price": 35900.0,
            "m²": 37.99,
            "Address": "Stirnu 39"
        },
        {
            "Price_per_m²": 1305.0,
            "Price": 77000.0,
            "m²": 59.0,
            "Address": "Stirnu 13D"
        },
        {
            "Price_per_m²": 1226.0,
            "Price": 65000.0,
            "m²": 53.02,
            "Address": "Vaidavas 6 k-2/3"
        },
        {
            "Price_per_m²": 1060.0,
            "Price": 53000.0,
            "m²": 50.0,
            "Address": "Dzelzavas 25"
        },
        {
            "Price_per_m²": 1034.0,
            "Price": 61000.0,
            "m²": 58.99,
            "Address": "Ilūkstes 103/1"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 63000.0,
            "m²": 63.0,
            "Address": "Kalsnavas 1"
        },
        {
            "Price_per_m²": 854.0,
            "Price": 41000.0,
            "m²": 48.01,
            "Address": "Dzelzavas 35"
        },
        {
            "Price_per_m²": 1043.0,
            "Price": 48000.0,
            "m²": 46.02,
            "Address": "Ilūkstes 101"
        },
        {
            "Price_per_m²": 1320.0,
            "Price": 33000.0,
            "m²": 25.0,
            "Address": "Ieriķu 36"
        },
        {
            "Price_per_m²": 905.0,
            "Price": 67000.0,
            "m²": 74.03,
            "Address": "Kalsnavas 2c"
        },
        {
            "Price_per_m²": 1017.0,
            "Price": 59000.0,
            "m²": 58.01,
            "Address": "Purvciema 15"
        },
        {
            "Price_per_m²": 1125.0,
            "Price": 69750.0,
            "m²": 62.0,
            "Address": "Stirnu 35a"
        },
        {
            "Price_per_m²": 1024.0,
            "Price": 43000.0,
            "m²": 41.99,
            "Address": "Raunas 37"
        },
        {
            "Price_per_m²": 1105.0,
            "Price": 40900.0,
            "m²": 37.01,
            "Address": "Ūnijas 60"
        },
        {
            "Price_per_m²": 1158.0,
            "Price": 22000.0,
            "m²": 19.0,
            "Address": "Ūnijas 32"
        },
        {
            "Price_per_m²": 1048.0,
            "Price": 62900.0,
            "m²": 60.02,
            "Address": "Dzelzavas 35"
        },
        {
            "Price_per_m²": 909.0,
            "Price": 70000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 932.0,
            "Price": 55000.0,
            "m²": 59.01,
            "Address": "Ilūkstes 107/1"
        },
        {
            "Price_per_m²": 778.0,
            "Price": 49000.0,
            "m²": 62.98,
            "Address": "Žagatu 20"
        },
        {
            "Price_per_m²": 902.0,
            "Price": 55000.0,
            "m²": 60.98,
            "Address": "Ieriķu 66"
        },
        {
            "Price_per_m²": 2408.0,
            "Price": 118000.0,
            "m²": 49.0,
            "Address": "Nīcgales 36a"
        },
        {
            "Price_per_m²": 2476.0,
            "Price": 188200.0,
            "m²": 76.01,
            "Address": "Dzelzavas 106"
        },
        {
            "Price_per_m²": 862.0,
            "Price": 52595.0,
            "m²": 61.02,
            "Address": "Stirnu 37"
        },
        {
            "Price_per_m²": 1149.0,
            "Price": 42500.0,
            "m²": 36.99,
            "Address": "Ieriķu 66"
        },
        {
            "Price_per_m²": 1471.0,
            "Price": 125000.0,
            "m²": 84.98,
            "Address": "Braslas 53"
        },
        {
            "Price_per_m²": 1246.0,
            "Price": 76000.0,
            "m²": 61.0,
            "Address": "Purvciema 20"
        },
        {
            "Price_per_m²": 1068.0,
            "Price": 47000.0,
            "m²": 44.01,
            "Address": "Stirnu 19A"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 31000.0,
            "m²": 31.0,
            "Address": "Stirnu 38"
        },
        {
            "Price_per_m²": 1833.0,
            "Price": 110000.0,
            "m²": 60.01,
            "Address": "Dzelzavas 19k3"
        },
        {
            "Price_per_m²": 793.0,
            "Price": 73000.0,
            "m²": 92.06,
            "Address": "Madonas 19"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 32000.0,
            "m²": 27.0,
            "Address": "Dzelzavas 93"
        },
        {
            "Price_per_m²": 1218.0,
            "Price": 88900.0,
            "m²": 72.99,
            "Address": "Lielvārdes 105"
        },
        {
            "Price_per_m²": 908.0,
            "Price": 59000.0,
            "m²": 64.98,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1297.0,
            "Price": 77800.0,
            "m²": 59.98,
            "Address": "Ilūkstes 7k-3"
        },
        {
            "Price_per_m²": 865.0,
            "Price": 54500.0,
            "m²": 63.01,
            "Address": "Stirnu 21"
        },
        {
            "Price_per_m²": 1247.0,
            "Price": 93500.0,
            "m²": 74.98,
            "Address": "Viršu 11"
        },
        {
            "Price_per_m²": 996.0,
            "Price": 39850.0,
            "m²": 40.01,
            "Address": "Vaidavas 2 k4"
        },
        {
            "Price_per_m²": 1861.0,
            "Price": 161875.0,
            "m²": 86.98,
            "Address": "Pūces 45"
        },
        {
            "Price_per_m²": 823.0,
            "Price": 51000.0,
            "m²": 61.97,
            "Address": "Dzelzavas 25"
        },
        {
            "Price_per_m²": 1153.0,
            "Price": 71500.0,
            "m²": 62.01,
            "Address": "Mārcienas 1"
        },
        {
            "Price_per_m²": 962.0,
            "Price": 37500.0,
            "m²": 38.98,
            "Address": "Pūces 19A"
        },
        {
            "Price_per_m²": 744.0,
            "Price": 32000.0,
            "m²": 43.01,
            "Address": "Ilūkstes 54/1"
        },
        {
            "Price_per_m²": 735.0,
            "Price": 49990.0,
            "m²": 68.01,
            "Address": "Deglava 35"
        },
        {
            "Price_per_m²": 907.0,
            "Price": 68900.0,
            "m²": 75.96,
            "Address": "Deglava 59"
        },
        {
            "Price_per_m²": 1299.0,
            "Price": 58455.0,
            "m²": 45.0,
            "Address": "Ieriķu 11"
        },
        {
            "Price_per_m²": 879.0,
            "Price": 51000.0,
            "m²": 58.02,
            "Address": "Viršu 1"
        },
        {
            "Price_per_m²": 898.0,
            "Price": 53000.0,
            "m²": 59.02,
            "Address": "Madonas 27"
        },
        {
            "Price_per_m²": 1044.0,
            "Price": 44890.0,
            "m²": 43.0,
            "Address": "Brantkalna 3"
        },
        {
            "Price_per_m²": 768.0,
            "Price": 29950.0,
            "m²": 39.0,
            "Address": "Purvciema 50"
        },
        {
            "Price_per_m²": 1902.0,
            "Price": 390000.0,
            "m²": 205.05,
            "Address": "Upeņu 4"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 54800.0,
            "m²": 62.99,
            "Address": "Stirnu 21"
        },
        {
            "Price_per_m²": 1130.0,
            "Price": 52000.0,
            "m²": 46.02,
            "Address": "Stirnu 21"
        },
        {
            "Price_per_m²": 1550.0,
            "Price": 44950.0,
            "m²": 29.0,
            "Address": "Deglava 13"
        },
        {
            "Price_per_m²": 1798.0,
            "Price": 35950.0,
            "m²": 19.99,
            "Address": "Deglava 13"
        },
        {
            "Price_per_m²": 1720.0,
            "Price": 56750.0,
            "m²": 32.99,
            "Address": "Deglava 13"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 1829.0,
            "Price": 75000.0,
            "m²": 41.01,
            "Address": "Dzelzavas 13"
        },
        {
            "Price_per_m²": 1357.0,
            "Price": 85500.0,
            "m²": 63.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 919.0,
            "Price": 34000.0,
            "m²": 37.0,
            "Address": "Vaidavas 2"
        },
        {
            "Price_per_m²": 1445.0,
            "Price": 185000.0,
            "m²": 128.03,
            "Address": "Ūnijas 74"
        },
        {
            "Price_per_m²": 931.0,
            "Price": 33500.0,
            "m²": 35.98,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 1193.0,
            "Price": 83500.0,
            "m²": 69.99,
            "Address": "Ūnijas 37"
        },
        {
            "Price_per_m²": 1908.0,
            "Price": 124000.0,
            "m²": 64.99,
            "Address": "Stirnu 12a"
        },
        {
            "Price_per_m²": 952.0,
            "Price": 40000.0,
            "m²": 42.02,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 813.0,
            "Price": 65000.0,
            "m²": 79.95,
            "Address": "Ūnijas 71"
        }
    ],
    "monthly": [
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 600.0,
            "m²": 75.0,
            "Address": "Stirnu 4"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Dzelzavas 37"
        },
        {
            "Price_per_m²": 10.8,
            "Price": 270.0,
            "m²": 25.0,
            "Address": "Nīcgales 64"
        },
        {
            "Price_per_m²": 9.29,
            "Price": 390.0,
            "m²": 41.98,
            "Address": "Dzelzavas 15"
        },
        {
            "Price_per_m²": 6.03,
            "Price": 350.0,
            "m²": 58.04,
            "Address": "Brantkalna 16"
        },
        {
            "Price_per_m²": 7.38,
            "Price": 450.0,
            "m²": 60.98,
            "Address": "Zvaigznāja g. 5"
        },
        {
            "Price_per_m²": 6.36,
            "Price": 350.0,
            "m²": 55.03,
            "Address": "Nīcgales 24"
        },
        {
            "Price_per_m²": 8.57,
            "Price": 360.0,
            "m²": 42.01,
            "Address": "Purvciema 44/1"
        },
        {
            "Price_per_m²": 8.89,
            "Price": 320.0,
            "m²": 36.0,
            "Address": "Žagatu 20A"
        },
        {
            "Price_per_m²": 10.61,
            "Price": 350.0,
            "m²": 32.99,
            "Address": "Zileņu 12"
        },
        {
            "Price_per_m²": 6.67,
            "Price": 300.0,
            "m²": 44.98,
            "Address": "Ieriķu 43"
        },
        {
            "Price_per_m²": 11.11,
            "Price": 300.0,
            "m²": 27.0,
            "Address": "Varavīksnes g. 1"
        },
        {
            "Price_per_m²": 9.2,
            "Price": 690.0,
            "m²": 75.0,
            "Address": "Astras 8 k-1"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Zvaigznāja g. 4"
        },
        {
            "Price_per_m²": 5.69,
            "Price": 330.0,
            "m²": 58.0,
            "Address": "Deglava 51"
        },
        {
            "Price_per_m²": 9.46,
            "Price": 350.0,
            "m²": 37.0,
            "Address": "Ieriķu 58"
        },
        {
            "Price_per_m²": 7.05,
            "Price": 550.0,
            "m²": 78.01,
            "Address": "Nīcgales 36"
        },
        {
            "Price_per_m²": 7.26,
            "Price": 450.0,
            "m²": 61.98,
            "Address": "Madonas 21"
        },
        {
            "Price_per_m²": 8.53,
            "Price": 290.0,
            "m²": 34.0,
            "Address": "Ūnijas 24"
        },
        {
            "Price_per_m²": 9.02,
            "Price": 370.0,
            "m²": 41.02,
            "Address": "Dzelzavas 23"
        },
        {
            "Price_per_m²": 8.75,
            "Price": 350.0,
            "m²": 40.0,
            "Address": "Stirnu 21"
        },
        {
            "Price_per_m²": 11.46,
            "Price": 550.0,
            "m²": 47.99,
            "Address": "Stirnu 40B"
        },
        {
            "Price_per_m²": 12.86,
            "Price": 450.0,
            "m²": 34.99,
            "Address": "Stirnu 40B"
        },
        {
            "Price_per_m²": 6.25,
            "Price": 250.0,
            "m²": 40.0,
            "Address": "Stirnu 19"
        },
        {
            "Price_per_m²": 5.95,
            "Price": 250.0,
            "m²": 42.02,
            "Address": "Nīcgales 40"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 300.0,
            "m²": 36.01,
            "Address": "Purvciema 55"
        },
        {
            "Price_per_m²": 8.53,
            "Price": 640.0,
            "m²": 75.03,
            "Address": "Ainavas 2a"
        },
        {
            "Price_per_m²": 7.68,
            "Price": 215.0,
            "m²": 27.99,
            "Address": "Dudajeva g. 11"
        },
        {
            "Price_per_m²": 8.67,
            "Price": 260.0,
            "m²": 29.99,
            "Address": "Vaidavas 10"
        },
        {
            "Price_per_m²": 5.41,
            "Price": 400.0,
            "m²": 73.94,
            "Address": "Ilūkstes 101"
        },
        {
            "Price_per_m²": 5.95,
            "Price": 250.0,
            "m²": 42.02,
            "Address": "Dzelzavas 11"
        },
        {
            "Price_per_m²": 9.09,
            "Price": 400.0,
            "m²": 44.0,
            "Address": "Ūnijas 64"
        },
        {
            "Price_per_m²": 5.79,
            "Price": 220.0,
            "m²": 38.0,
            "Address": "Dzelzavas 25"
        },
        {
            "Price_per_m²": 9.67,
            "Price": 290.0,
            "m²": 29.99,
            "Address": "Vaidavas 2k5"
        },
        {
            "Price_per_m²": 12.0,
            "Price": 180.0,
            "m²": 15.0,
            "Address": "Varavīksnes g. 10"
        },
        {
            "Price_per_m²": 6.02,
            "Price": 590.0,
            "m²": 98.01,
            "Address": "Madonas 25"
        },
        {
            "Price_per_m²": 13.81,
            "Price": 580.0,
            "m²": 42.0,
            "Address": "Ieriķu 28a"
        },
        {
            "Price_per_m²": 6.2,
            "Price": 310.0,
            "m²": 50.0,
            "Address": "Andromedas g. 6"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 350.0,
            "m²": 42.02,
            "Address": "Ūnijas 71"
        },
        {
            "Price_per_m²": 11.0,
            "Price": 220.0,
            "m²": 20.0,
            "Address": "Burtnieku 33"
        },
        {
            "Price_per_m²": 8.85,
            "Price": 230.0,
            "m²": 25.99,
            "Address": "Marsa g. 12"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.29,
            "Price": 350.0,
            "m²": 48.01,
            "Address": "Dudajeva g. 7"
        },
        {
            "Price_per_m²": 9.0,
            "Price": 450.0,
            "m²": 50.0,
            "Address": "Varavīksnes g. 18"
        },
        {
            "Price_per_m²": 7.62,
            "Price": 320.0,
            "m²": 41.99,
            "Address": "Ķeguma 60"
        },
        {
            "Price_per_m²": 6.6,
            "Price": 310.0,
            "m²": 46.97,
            "Address": "Biķernieku 111"
        },
        {
            "Price_per_m²": 11.0,
            "Price": 550.0,
            "m²": 50.0,
            "Address": "Stirnu 1"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Varavīksnes g. 18"
        },
        {
            "Price_per_m²": 5.66,
            "Price": 300.0,
            "m²": 53.0,
            "Address": "Ķeguma 2"
        },
        {
            "Price_per_m²": 9.27,
            "Price": 380.0,
            "m²": 40.99,
            "Address": "Vaidavas 2 k-5"
        },
        {
            "Price_per_m²": 6.83,
            "Price": 280.0,
            "m²": 41.0,
            "Address": "Dzelzavas 19/1"
        },
        {
            "Price_per_m²": 5.81,
            "Price": 500.0,
            "m²": 86.06,
            "Address": "Vējavas 9c"
        },
        {
            "Price_per_m²": 6.67,
            "Price": 500.0,
            "m²": 74.96,
            "Address": "Brantkalna 4"
        },
        {
            "Price_per_m²": 7.74,
            "Price": 240.0,
            "m²": 31.01,
            "Address": "Ilūkstes 101"
        },
        {
            "Price_per_m²": 6.32,
            "Price": 360.0,
            "m²": 56.96,
            "Address": "Brantkalna 7"
        },
        {
            "Price_per_m²": 5.26,
            "Price": 400.0,
            "m²": 76.05,
            "Address": "Lielvārdes 103"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 270.0,
            "m²": 37.97,
            "Address": "Dudajeva g. 6"
        },
        {
            "Price_per_m²": 6.8,
            "Price": 340.0,
            "m²": 50.0,
            "Address": "Pūces 51"
        },
        {
            "Price_per_m²": 6.75,
            "Price": 270.0,
            "m²": 40.0,
            "Address": "Andromedas g. 5a"
        },
        {
            "Price_per_m²": 5.83,
            "Price": 350.0,
            "m²": 60.03,
            "Address": "Ūnijas 72"
        },
        {
            "Price_per_m²": 6.3,
            "Price": 170.0,
            "m²": 26.98,
            "Address": "Purvciema 67"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 250.0,
            "m²": 36.02,
            "Address": "Nīcgales 4"
        },
        {
            "Price_per_m²": 7.33,
            "Price": 220.0,
            "m²": 30.01,
            "Address": "Raunas 58"
        },
        {
            "Price_per_m²": 6.56,
            "Price": 210.0,
            "m²": 32.01,
            "Address": "Ilūkstes 103"
        },
        {
            "Price_per_m²": 6.22,
            "Price": 230.0,
            "m²": 36.98,
            "Address": "Ieriķu 60"
        },
        {
            "Price_per_m²": 6.12,
            "Price": 300.0,
            "m²": 49.02,
            "Address": "Dzelzavas 59"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Zvaigznāja g. 3"
        }
    ],
    "daily": [
        {
            "Price_per_m²": 1.02,
            "Price": 45.0,
            "m²": 44.12,
            "Address": "Purvciema 24"
        },
        {
            "Price_per_m²": 0.729,
            "Price": 35.0,
            "m²": 48.01,
            "Address": "Purvciema 53"
        },
        {
            "Price_per_m²": 0.814,
            "Price": 35.0,
            "m²": 43.0,
            "Address": "Ieriķu 58"
        },
        {
            "Price_per_m²": 1.09,
            "Price": 50.0,
            "m²": 45.87,
            "Address": "Stirnu 13a"
        },
        {
            "Price_per_m²": 0.4,
            "Price": 20.0,
            "m²": 50.0,
            "Address": "Nīcgales 6"
        },
        {
            "Price_per_m²": 1.02,
            "Price": 50.0,
            "m²": 49.02,
            "Address": "Vaidavas 6/3"
        },
        {
            "Price_per_m²": 1.28,
            "Price": 55.0,
            "m²": 42.97,
            "Address": "Dzelzavas 19/3"
        },
        {
            "Price_per_m²": 1.25,
            "Price": 30.0,
            "m²": 24.0,
            "Address": "Nīcgales 46 а"
        },
        {
            "Price_per_m²": 0.833,
            "Price": 25.0,
            "m²": 30.01,
            "Address": "Braslas 27"
        },
        {
            "Price_per_m²": 0.814,
            "Price": 35.0,
            "m²": 43.0,
            "Address": "Ieriķu 58"
        },
        {
            "Price_per_m²": 0.69,
            "Price": 29.0,
            "m²": 42.03,
            "Address": "Deglava 7"
        }
    ]
}


data2 = data

# Extract data from "one_time_purchase"
one_time_data = data2["one_time_purchase"]

# Prepare the m² and Price data for plotting
m2_values = [entry["m²"] for entry in one_time_data]
price_values = [entry["Price"] for entry in one_time_data]

# Create the plot
plt.figure(figsize=(8, 6))
plt.scatter(m2_values, price_values, color='blue', marker='o')

# Add labels and title
plt.xlabel('m²')
plt.ylabel('cena')
plt.title('Cena pret m² dzīvokļiem, kas atrodas purvciema')

# Show the plot
plt.grid(True)
plt.show()
