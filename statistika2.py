import json
import matplotlib.pyplot as plt

data = {
    "one_time_purchase": [
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 1737.0,
            "Price": 79900.0,
            "m²": 46.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 1580.0,
            "Price": 118500.0,
            "m²": 75.0,
            "Address": "Ulbrokas 7"
        },
        {
            "Price_per_m²": 897.0,
            "Price": 69999.0,
            "m²": 78.04,
            "Address": "Deglava 108"
        },
        {
            "Price_per_m²": 1181.0,
            "Price": 18900.0,
            "m²": 16.0,
            "Address": "Rencēnu 40"
        },
        {
            "Price_per_m²": 729.0,
            "Price": 29900.0,
            "m²": 41.02,
            "Address": "Dravnieku 12"
        },
        {
            "Price_per_m²": 2067.0,
            "Price": 163300.0,
            "m²": 79.0,
            "Address": "Deglava 174"
        },
        {
            "Price_per_m²": 2516.0,
            "Price": 158500.0,
            "m²": 63.0,
            "Address": "Deglava 174"
        },
        {
            "Price_per_m²": 2421.0,
            "Price": 193700.0,
            "m²": 80.01,
            "Address": "Deglava 174"
        },
        {
            "Price_per_m²": 922.0,
            "Price": 29500.0,
            "m²": 32.0,
            "Address": "Ulbrokas 1"
        },
        {
            "Price_per_m²": 827.0,
            "Price": 66980.0,
            "m²": 80.99,
            "Address": "Dzeņu 10"
        },
        {
            "Price_per_m²": 2139.0,
            "Price": 147618.0,
            "m²": 69.01,
            "Address": "Dravnieku 3 K-2"
        },
        {
            "Price_per_m²": 1933.0,
            "Price": 87000.0,
            "m²": 45.01,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 791.0,
            "Price": 62500.0,
            "m²": 79.01,
            "Address": "Deglava 51"
        },
        {
            "Price_per_m²": 1156.0,
            "Price": 88980.0,
            "m²": 76.97,
            "Address": "Salnas 6"
        },
        {
            "Price_per_m²": 2698.0,
            "Price": 232000.0,
            "m²": 85.99,
            "Address": "Ulbrokas 47"
        },
        {
            "Price_per_m²": 1294.0,
            "Price": 81500.0,
            "m²": 62.98,
            "Address": "Praulienas 10"
        },
        {
            "Price_per_m²": 871.0,
            "Price": 54900.0,
            "m²": 63.03,
            "Address": "Rudens 2"
        },
        {
            "Price_per_m²": 2036.0,
            "Price": 199511.0,
            "m²": 97.99,
            "Address": "Dravnieku 3"
        },
        {
            "Price_per_m²": 2558.0,
            "Price": 133000.0,
            "m²": 51.99,
            "Address": "Dravnieku 1/1"
        },
        {
            "Price_per_m²": 1168.0,
            "Price": 128500.0,
            "m²": 110.02,
            "Address": "Jasmuižas 1"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 50000.0,
            "m²": 50.0,
            "Address": "Saharova 17"
        },
        {
            "Price_per_m²": 1032.0,
            "Price": 65000.0,
            "m²": 62.98,
            "Address": "Kaudzīšu 10"
        },
        {
            "Price_per_m²": 1087.0,
            "Price": 50000.0,
            "m²": 46.0,
            "Address": "Salnas 10"
        },
        {
            "Price_per_m²": 854.0,
            "Price": 29900.0,
            "m²": 35.01,
            "Address": "Salnas 20"
        },
        {
            "Price_per_m²": 823.0,
            "Price": 32100.0,
            "m²": 39.0,
            "Address": "Dzeņu 8"
        },
        {
            "Price_per_m²": 727.0,
            "Price": 40000.0,
            "m²": 55.02,
            "Address": "Dravnieku 7"
        },
        {
            "Price_per_m²": 1512.0,
            "Price": 65000.0,
            "m²": 42.99,
            "Address": "Ilūkstes 11"
        },
        {
            "Price_per_m²": 1016.0,
            "Price": 49800.0,
            "m²": 49.02,
            "Address": "Slāvu 17"
        },
        {
            "Price_per_m²": 1132.0,
            "Price": 56600.0,
            "m²": 50.0,
            "Address": "Salnas 17"
        },
        {
            "Price_per_m²": 1177.0,
            "Price": 73000.0,
            "m²": 62.02,
            "Address": "Saharova 25"
        },
        {
            "Price_per_m²": 896.0,
            "Price": 69900.0,
            "m²": 78.01,
            "Address": "Rudens 3"
        },
        {
            "Price_per_m²": 1159.0,
            "Price": 73000.0,
            "m²": 62.99,
            "Address": "Lubānas 59"
        },
        {
            "Price_per_m²": 867.0,
            "Price": 55500.0,
            "m²": 64.01,
            "Address": "Salnas 28"
        },
        {
            "Price_per_m²": 2107.0,
            "Price": 225498.0,
            "m²": 107.02,
            "Address": "Ilūkstes 24"
        },
        {
            "Price_per_m²": 848.0,
            "Price": 52598.0,
            "m²": 62.03,
            "Address": "Salnas 26"
        },
        {
            "Price_per_m²": 1709.0,
            "Price": 135000.0,
            "m²": 78.99,
            "Address": "Ulbrokas 5"
        },
        {
            "Price_per_m²": 1063.0,
            "Price": 67000.0,
            "m²": 63.03,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 69000.0,
            "m²": 77.97,
            "Address": "Jasmuižas 14"
        },
        {
            "Price_per_m²": 960.0,
            "Price": 74900.0,
            "m²": 78.02,
            "Address": "Sesku 63"
        },
        {
            "Price_per_m²": 1636.0,
            "Price": 175000.0,
            "m²": 106.97,
            "Address": "Pļavnieku 9"
        },
        {
            "Price_per_m²": 1140.0,
            "Price": 57000.0,
            "m²": 50.0,
            "Address": "Jasmuižas 17"
        },
        {
            "Price_per_m²": 877.0,
            "Price": 67500.0,
            "m²": 76.97,
            "Address": "Praulienas 2"
        },
        {
            "Price_per_m²": 1145.0,
            "Price": 71000.0,
            "m²": 62.01,
            "Address": "Rudens 5"
        },
        {
            "Price_per_m²": 1273.0,
            "Price": 42000.0,
            "m²": 32.99,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 1050.0,
            "Price": 42000.0,
            "m²": 40.0,
            "Address": "Salnas 22"
        },
        {
            "Price_per_m²": 742.0,
            "Price": 46000.0,
            "m²": 61.99,
            "Address": "Rudens 10"
        },
        {
            "Price_per_m²": 948.0,
            "Price": 72998.0,
            "m²": 77.0,
            "Address": "Lubānas 117"
        },
        {
            "Price_per_m²": 821.0,
            "Price": 34500.0,
            "m²": 42.02,
            "Address": "Saharova 7"
        },
        {
            "Price_per_m²": 721.0,
            "Price": 31000.0,
            "m²": 43.0,
            "Address": "Lubānas 115"
        },
        {
            "Price_per_m²": 898.0,
            "Price": 44900.0,
            "m²": 50.0,
            "Address": "J. Vācieša 8"
        },
        {
            "Price_per_m²": 2115.0,
            "Price": 143841.0,
            "m²": 68.01,
            "Address": "Dravnieku 3"
        },
        {
            "Price_per_m²": 1200.0,
            "Price": 90000.0,
            "m²": 75.0,
            "Address": "Ulbrokas 7"
        },
        {
            "Price_per_m²": 871.0,
            "Price": 36600.0,
            "m²": 42.02,
            "Address": "Zemes 5"
        },
        {
            "Price_per_m²": 1130.0,
            "Price": 87000.0,
            "m²": 76.99,
            "Address": "Rudens 10"
        },
        {
            "Price_per_m²": 753.0,
            "Price": 33900.0,
            "m²": 45.02,
            "Address": "Ilūkstes 6"
        },
        {
            "Price_per_m²": 1091.0,
            "Price": 120000.0,
            "m²": 109.99,
            "Address": "Kaudzīšu 46"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 41000.0,
            "m²": 41.0,
            "Address": "Dzeņu 6"
        },
        {
            "Price_per_m²": 1212.0,
            "Price": 40000.0,
            "m²": 33.0,
            "Address": "Kaudzīšu 8"
        },
        {
            "Price_per_m²": 2000.0,
            "Price": 172000.0,
            "m²": 86.0,
            "Address": "Dravnieku 3"
        },
        {
            "Price_per_m²": 2160.0,
            "Price": 146890.0,
            "m²": 68.0,
            "Address": "Dravnieku 3"
        },
        {
            "Price_per_m²": 2396.0,
            "Price": 69470.0,
            "m²": 28.99,
            "Address": "Dravnieku 3"
        },
        {
            "Price_per_m²": 1955.0,
            "Price": 91884.0,
            "m²": 47.0,
            "Address": "Rembates 10"
        },
        {
            "Price_per_m²": 1100.0,
            "Price": 55000.0,
            "m²": 50.0,
            "Address": "Salnas 32"
        },
        {
            "Price_per_m²": 1038.0,
            "Price": 51900.0,
            "m²": 50.0,
            "Address": "Dravnieku 10"
        },
        {
            "Price_per_m²": 1138.0,
            "Price": 45500.0,
            "m²": 39.98,
            "Address": "Kaudzīšu 2"
        },
        {
            "Price_per_m²": 789.0,
            "Price": 60000.0,
            "m²": 76.05,
            "Address": "J. Vācieša 6"
        },
        {
            "Price_per_m²": 2319.0,
            "Price": 134500.0,
            "m²": 58.0,
            "Address": "Kupriču 1b"
        },
        {
            "Price_per_m²": 900.0,
            "Price": 31500.0,
            "m²": 35.0,
            "Address": "Pavasara g. 2"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Zemes 10"
        },
        {
            "Price_per_m²": 840.0,
            "Price": 42000.0,
            "m²": 50.0,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 1386.0,
            "Price": 48500.0,
            "m²": 34.99,
            "Address": "Dravnieku 7"
        },
        {
            "Price_per_m²": 2102.0,
            "Price": 107200.0,
            "m²": 51.0,
            "Address": "Rembates 10"
        },
        {
            "Price_per_m²": 2039.0,
            "Price": 157000.0,
            "m²": 77.0,
            "Address": "Rembates 10"
        },
        {
            "Price_per_m²": 817.0,
            "Price": 51500.0,
            "m²": 63.04,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 891.0,
            "Price": 69500.0,
            "m²": 78.0,
            "Address": "Ilūkstes 36"
        },
        {
            "Price_per_m²": 934.0,
            "Price": 46700.0,
            "m²": 50.0,
            "Address": "Saharova 3"
        },
        {
            "Price_per_m²": 938.0,
            "Price": 46900.0,
            "m²": 50.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 2169.0,
            "Price": 229900.0,
            "m²": 105.99,
            "Address": "Ilūkstes 14"
        },
        {
            "Price_per_m²": 859.0,
            "Price": 67000.0,
            "m²": 78.0,
            "Address": "Deglava 152"
        },
        {
            "Price_per_m²": 925.0,
            "Price": 29600.0,
            "m²": 32.0,
            "Address": "Jasmuižas 2"
        },
        {
            "Price_per_m²": 1011.0,
            "Price": 46500.0,
            "m²": 45.99,
            "Address": "Deglava 126"
        },
        {
            "Price_per_m²": 1711.0,
            "Price": 77000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 846.0,
            "Price": 33000.0,
            "m²": 39.01,
            "Address": "Salnas 24"
        },
        {
            "Price_per_m²": 1120.0,
            "Price": 56000.0,
            "m²": 50.0,
            "Address": "Salnas 11"
        },
        {
            "Price_per_m²": 1333.0,
            "Price": 68000.0,
            "m²": 51.01,
            "Address": "Praulienas 2"
        },
        {
            "Price_per_m²": 1410.0,
            "Price": 110000.0,
            "m²": 78.01,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 98700.0,
            "m²": 93.03,
            "Address": "Lubānas 41"
        },
        {
            "Price_per_m²": 2110.0,
            "Price": 109700.0,
            "m²": 51.99,
            "Address": "Rembates 10"
        },
        {
            "Price_per_m²": 1169.0,
            "Price": 76000.0,
            "m²": 65.01,
            "Address": "Rudens 12"
        },
        {
            "Price_per_m²": 1144.0,
            "Price": 38900.0,
            "m²": 34.0,
            "Address": "Salnas 3"
        },
        {
            "Price_per_m²": 1300.0,
            "Price": 65000.0,
            "m²": 50.0,
            "Address": "Deglava 190"
        },
        {
            "Price_per_m²": 2061.0,
            "Price": 177282.0,
            "m²": 86.02,
            "Address": "Dravnieku 3"
        },
        {
            "Price_per_m²": 2066.0,
            "Price": 134274.0,
            "m²": 64.99,
            "Address": "Dravnieku 3"
        },
        {
            "Price_per_m²": 2306.0,
            "Price": 161400.0,
            "m²": 69.99,
            "Address": "Rembates 10"
        },
        {
            "Price_per_m²": 1020.0,
            "Price": 52000.0,
            "m²": 50.98,
            "Address": "Kaudzīšu 42"
        },
        {
            "Price_per_m²": 960.0,
            "Price": 48000.0,
            "m²": 50.0,
            "Address": "Salnas 3"
        },
        {
            "Price_per_m²": 876.0,
            "Price": 43800.0,
            "m²": 50.0,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1167.0,
            "Price": 38500.0,
            "m²": 32.99,
            "Address": "Rencēnu 8"
        },
        {
            "Price_per_m²": 868.0,
            "Price": 53800.0,
            "m²": 61.98,
            "Address": "Salnas 26"
        },
        {
            "Price_per_m²": 900.0,
            "Price": 45000.0,
            "m²": 50.0,
            "Address": "Dravnieku 11"
        },
        {
            "Price_per_m²": 845.0,
            "Price": 35500.0,
            "m²": 42.01,
            "Address": "Sesku 7/K1"
        },
        {
            "Price_per_m²": 2804.0,
            "Price": 157000.0,
            "m²": 55.99,
            "Address": "Kupriču 1E"
        },
        {
            "Price_per_m²": 810.0,
            "Price": 51000.0,
            "m²": 62.96,
            "Address": "Salnas 3"
        },
        {
            "Price_per_m²": 960.0,
            "Price": 48000.0,
            "m²": 50.0,
            "Address": "Salnas 3"
        },
        {
            "Price_per_m²": 1133.0,
            "Price": 85000.0,
            "m²": 75.02,
            "Address": "Deglava 126"
        },
        {
            "Price_per_m²": 1262.0,
            "Price": 53000.0,
            "m²": 42.0,
            "Address": "Sesku 10 k-1"
        },
        {
            "Price_per_m²": 824.0,
            "Price": 75000.0,
            "m²": 91.02,
            "Address": "Dzeņu 10"
        },
        {
            "Price_per_m²": 1037.0,
            "Price": 42500.0,
            "m²": 40.98,
            "Address": "Lubānas 129"
        },
        {
            "Price_per_m²": 2197.0,
            "Price": 156011.0,
            "m²": 71.01,
            "Address": "Dravnieku 3"
        },
        {
            "Price_per_m²": 1016.0,
            "Price": 64000.0,
            "m²": 62.99,
            "Address": "Jasmuižas 11"
        },
        {
            "Price_per_m²": 902.0,
            "Price": 46000.0,
            "m²": 51.0,
            "Address": "Salnas 12"
        },
        {
            "Price_per_m²": 2278.0,
            "Price": 111613.0,
            "m²": 49.0,
            "Address": "Dravnieku 3"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        },
        {
            "Price_per_m²": 978.0,
            "Price": 49900.0,
            "m²": 51.02,
            "Address": "Grestes 12"
        },
        {
            "Price_per_m²": 849.0,
            "Price": 53500.0,
            "m²": 63.02,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 773.0,
            "Price": 34000.0,
            "m²": 43.98,
            "Address": "Pavasara g. 4"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 62000.0,
            "m²": 62.0,
            "Address": "Zemes 7"
        },
        {
            "Price_per_m²": 1185.0,
            "Price": 73500.0,
            "m²": 62.03,
            "Address": "Pavasara g. 6"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 65000.0,
            "m²": 77.01,
            "Address": "Ilūkstes 95"
        },
        {
            "Price_per_m²": 2596.0,
            "Price": 135000.0,
            "m²": 52.0,
            "Address": "Rembates 8"
        },
        {
            "Price_per_m²": 1278.0,
            "Price": 86900.0,
            "m²": 68.0,
            "Address": "J. Vācieša 2C"
        },
        {
            "Price_per_m²": 1889.0,
            "Price": 85000.0,
            "m²": 45.0,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 870.0,
            "Price": 67000.0,
            "m²": 77.01,
            "Address": "J. Vācieša 2"
        },
        {
            "Price_per_m²": 798.0,
            "Price": 49500.0,
            "m²": 62.03,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1222.0,
            "Price": 77000.0,
            "m²": 63.01,
            "Address": "Grestes 5"
        }
    ],
    "monthly": [
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 6.88,
            "Price": 220.0,
            "m²": 31.98,
            "Address": "Jasmuižas 12"
        },
        {
            "Price_per_m²": 8.28,
            "Price": 480.0,
            "m²": 57.97,
            "Address": "Ulbrokas 12k2"
        },
        {
            "Price_per_m²": 10.0,
            "Price": 350.0,
            "m²": 35.0,
            "Address": "Salnas 20"
        },
        {
            "Price_per_m²": 7.78,
            "Price": 350.0,
            "m²": 44.99,
            "Address": "Ilūkstes 2"
        },
        {
            "Price_per_m²": 6.14,
            "Price": 270.0,
            "m²": 43.97,
            "Address": "Ilūkstes 5"
        },
        {
            "Price_per_m²": 11.88,
            "Price": 380.0,
            "m²": 31.99,
            "Address": "Rudens 6"
        },
        {
            "Price_per_m²": 12.11,
            "Price": 460.0,
            "m²": 37.99,
            "Address": "Kaudzīšu 44"
        },
        {
            "Price_per_m²": 9.33,
            "Price": 700.0,
            "m²": 75.03,
            "Address": "Jasmuižas 8"
        },
        {
            "Price_per_m²": 6.27,
            "Price": 320.0,
            "m²": 51.04,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 350.0,
            "m²": 42.02,
            "Address": "Sesku 11/2"
        },
        {
            "Price_per_m²": 6.29,
            "Price": 220.0,
            "m²": 34.98,
            "Address": "Tīnūžu 8"
        },
        {
            "Price_per_m²": 8.73,
            "Price": 550.0,
            "m²": 63.0,
            "Address": "J. Vācieša 3"
        },
        {
            "Price_per_m²": 6.98,
            "Price": 300.0,
            "m²": 42.98,
            "Address": "Ilūkstes 32"
        },
        {
            "Price_per_m²": 6.5,
            "Price": 260.0,
            "m²": 40.0,
            "Address": "Dzeņu 14"
        },
        {
            "Price_per_m²": 8.21,
            "Price": 320.0,
            "m²": 38.98,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.62,
            "Price": 320.0,
            "m²": 41.99,
            "Address": "Pļavnieku 2D"
        },
        {
            "Price_per_m²": 6.45,
            "Price": 400.0,
            "m²": 62.02,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 2.33,
            "Price": 100.0,
            "m²": 42.92,
            "Address": "Salnas 10"
        },
        {
            "Price_per_m²": 14.0,
            "Price": 420.0,
            "m²": 30.0,
            "Address": "Rudens 10"
        },
        {
            "Price_per_m²": 8.52,
            "Price": 460.0,
            "m²": 53.99,
            "Address": "Salnas 21"
        },
        {
            "Price_per_m²": 6.5,
            "Price": 260.0,
            "m²": 40.0,
            "Address": "Ulbrokas 8"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        },
        {
            "Price_per_m²": 7.76,
            "Price": 450.0,
            "m²": 57.99,
            "Address": "Deglava 124"
        },
        {
            "Price_per_m²": 8.0,
            "Price": 400.0,
            "m²": 50.0,
            "Address": "Zemes 15"
        },
        {
            "Price_per_m²": 7.4,
            "Price": 370.0,
            "m²": 50.0,
            "Address": "Jasmuižas 10"
        },
        {
            "Price_per_m²": 7.81,
            "Price": 250.0,
            "m²": 32.01,
            "Address": "Pavasara g. 5"
        },
        {
            "Price_per_m²": 9.18,
            "Price": 450.0,
            "m²": 49.02,
            "Address": "Deglava 164"
        },
        {
            "Price_per_m²": 7.22,
            "Price": 700.0,
            "m²": 96.95,
            "Address": "Kaudzīšu 23"
        },
        {
            "Price_per_m²": 10.77,
            "Price": 420.0,
            "m²": 39.0,
            "Address": "Ulbrokas 10"
        }
    ],
    "daily": [
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.833,
            "Price": 60.0,
            "m²": 72.03,
            "Address": "Saharova 8"
        },
        {
            "Price_per_m²": 0.9,
            "Price": 45.0,
            "m²": 50.0,
            "Address": "Dzeņu 1"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 50.0,
            "m²": 50.0,
            "Address": "Tīnūžu 10"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 50.0,
            "m²": 50.0,
            "Address": "Tīnūžu 4"
        },
        {
            "Price_per_m²": 0.9,
            "Price": 45.0,
            "m²": 50.0,
            "Address": "Dzeņu 1"
        },
        {
            "Price_per_m²": 1.62,
            "Price": 55.0,
            "m²": 33.95,
            "Address": "Deglava 122"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
        },
        {
            "Price_per_m²": 0.735,
            "Price": 25.0,
            "m²": 34.01,
            "Address": "Pļavnieku 6"
        },
        {
            "Price_per_m²": 0.78,
            "Price": 39.0,
            "m²": 50.0,
            "Address": "Dravnieku 13"
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
plt.title('Cena pret m² dzīvokļiem, kas atrodas plavniekos')

# Show the plot
plt.grid(True)
plt.show()