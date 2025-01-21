import json
import matplotlib.pyplot as plt

data = {
    "one_time_purchase": [
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1168.0,
            "Price": 89900.0,
            "m²": 76.97,
            "Address": "Bruknas 12"
        },
        {
            "Price_per_m²": 711.0,
            "Price": 39800.0,
            "m²": 55.98,
            "Address": "Bauskas 101c"
        },
        {
            "Price_per_m²": 2000.0,
            "Price": 150000.0,
            "m²": 75.0,
            "Address": "Vienības g. 186-A"
        },
        {
            "Price_per_m²": 1652.0,
            "Price": 190000.0,
            "m²": 115.01,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1264.0,
            "Price": 139000.0,
            "m²": 109.97,
            "Address": "Bikstu 6"
        },
        {
            "Price_per_m²": 1167.0,
            "Price": 70000.0,
            "m²": 59.98,
            "Address": "Ozolciema 22/2"
        },
        {
            "Price_per_m²": 986.0,
            "Price": 34500.0,
            "m²": 34.99,
            "Address": "Ozolciema 42"
        },
        {
            "Price_per_m²": 1351.0,
            "Price": 63500.0,
            "m²": 47.0,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 1833.0,
            "Price": 220000.0,
            "m²": 120.02,
            "Address": "Vienības g. 87b"
        },
        {
            "Price_per_m²": 1753.0,
            "Price": 135000.0,
            "m²": 77.01,
            "Address": "Bauskas 33"
        },
        {
            "Price_per_m²": 1049.0,
            "Price": 53500.0,
            "m²": 51.0,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1909.0,
            "Price": 63000.0,
            "m²": 33.0,
            "Address": "Dignājas 3"
        },
        {
            "Price_per_m²": 1233.0,
            "Price": 71500.0,
            "m²": 57.99,
            "Address": "Ozolciema 24"
        },
        {
            "Price_per_m²": 1409.0,
            "Price": 155000.0,
            "m²": 110.01,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 1053.0,
            "Price": 60000.0,
            "m²": 56.98,
            "Address": "Bērzupes 13"
        },
        {
            "Price_per_m²": 1436.0,
            "Price": 145000.0,
            "m²": 100.97,
            "Address": "Bātas 3a"
        },
        {
            "Price_per_m²": 2222.0,
            "Price": 160000.0,
            "m²": 72.01,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 2193.0,
            "Price": 96500.0,
            "m²": 44.0,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 2100.0,
            "Price": 161700.0,
            "m²": 77.0,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 2661.0,
            "Price": 74500.0,
            "m²": 28.0,
            "Address": "Bauskas 45"
        },
        {
            "Price_per_m²": 1896.0,
            "Price": 127000.0,
            "m²": 66.98,
            "Address": "Komētas 16"
        },
        {
            "Price_per_m²": 1240.0,
            "Price": 62000.0,
            "m²": 50.0,
            "Address": "Ozolciema 46 k-5"
        },
        {
            "Price_per_m²": 1176.0,
            "Price": 72900.0,
            "m²": 61.99,
            "Address": "Dižozolu 27"
        },
        {
            "Price_per_m²": 974.0,
            "Price": 75000.0,
            "m²": 77.0,
            "Address": "Valdeķu 60k. 3"
        },
        {
            "Price_per_m²": 1955.0,
            "Price": 129000.0,
            "m²": 65.98,
            "Address": "Komētas 8"
        },
        {
            "Price_per_m²": 1348.0,
            "Price": 44500.0,
            "m²": 33.01,
            "Address": "Īslīces 14"
        },
        {
            "Price_per_m²": 1500.0,
            "Price": 69000.0,
            "m²": 46.0,
            "Address": "Putnu 20"
        },
        {
            "Price_per_m²": 1319.0,
            "Price": 62000.0,
            "m²": 47.01,
            "Address": "Vaiņodes 24A"
        },
        {
            "Price_per_m²": 1190.0,
            "Price": 75000.0,
            "m²": 63.03,
            "Address": "Valdeķu 60/3"
        },
        {
            "Price_per_m²": 1957.0,
            "Price": 95900.0,
            "m²": 49.0,
            "Address": "Bauskas 57"
        },
        {
            "Price_per_m²": 1286.0,
            "Price": 45000.0,
            "m²": 34.99,
            "Address": "Ēbeļmuižas 24"
        },
        {
            "Price_per_m²": 1375.0,
            "Price": 82500.0,
            "m²": 60.0,
            "Address": "Ozolciema 20/2"
        },
        {
            "Price_per_m²": 1949.0,
            "Price": 115000.0,
            "m²": 59.0,
            "Address": "Ziepniekkalna 70"
        },
        {
            "Price_per_m²": 2168.0,
            "Price": 258000.0,
            "m²": 119.0,
            "Address": "Putnu 3"
        },
        {
            "Price_per_m²": 917.0,
            "Price": 27500.0,
            "m²": 29.99,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 1025.0,
            "Price": 61500.0,
            "m²": 60.0,
            "Address": "Ozolciema 18"
        },
        {
            "Price_per_m²": 1732.0,
            "Price": 164500.0,
            "m²": 94.98,
            "Address": "Vienības g. 186A"
        },
        {
            "Price_per_m²": 810.0,
            "Price": 63990.0,
            "m²": 79.0,
            "Address": "Valdeķu 66/2"
        },
        {
            "Price_per_m²": 1043.0,
            "Price": 49000.0,
            "m²": 46.98,
            "Address": "Bauskas 63k1"
        },
        {
            "Price_per_m²": 1077.0,
            "Price": 56000.0,
            "m²": 52.0,
            "Address": "Bauskas 201"
        },
        {
            "Price_per_m²": 1930.0,
            "Price": 137000.0,
            "m²": 70.98,
            "Address": "Vienības g. 192"
        },
        {
            "Price_per_m²": 1178.0,
            "Price": 73050.0,
            "m²": 62.01,
            "Address": "Ozolciema 56 k-1"
        },
        {
            "Price_per_m²": 2200.0,
            "Price": 149600.0,
            "m²": 68.0,
            "Address": "Graudu 40"
        },
        {
            "Price_per_m²": 452.0,
            "Price": 57000.0,
            "m²": 126.11,
            "Address": "Īslīces 14"
        },
        {
            "Price_per_m²": 926.0,
            "Price": 50000.0,
            "m²": 54.0,
            "Address": "Valdeķu 61"
        },
        {
            "Price_per_m²": 2088.0,
            "Price": 144060.0,
            "m²": 68.99,
            "Address": "Bauskas 57"
        },
        {
            "Price_per_m²": 1980.0,
            "Price": 136600.0,
            "m²": 68.99,
            "Address": "Bauskas 57"
        },
        {
            "Price_per_m²": 1009.0,
            "Price": 58500.0,
            "m²": 57.98,
            "Address": "Ozolciema 12/3"
        },
        {
            "Price_per_m²": 1257.0,
            "Price": 44000.0,
            "m²": 35.0,
            "Address": "Ēbeļmuižas 20"
        },
        {
            "Price_per_m²": 2100.0,
            "Price": 161700.0,
            "m²": 77.0,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 2193.0,
            "Price": 96500.0,
            "m²": 44.0,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1047.0,
            "Price": 45000.0,
            "m²": 42.98,
            "Address": "Tadaiķu 7"
        },
        {
            "Price_per_m²": 1225.0,
            "Price": 49000.0,
            "m²": 40.0,
            "Address": "Pīpeņu 10"
        },
        {
            "Price_per_m²": 884.0,
            "Price": 49500.0,
            "m²": 56.0,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 1300.0,
            "Price": 65000.0,
            "m²": 50.0,
            "Address": "Ozolciema 42k2"
        },
        {
            "Price_per_m²": 1705.0,
            "Price": 75000.0,
            "m²": 43.99,
            "Address": "Kartupeļu 48"
        },
        {
            "Price_per_m²": 2040.0,
            "Price": 297900.0,
            "m²": 146.03,
            "Address": "Ziepniekkalna 75"
        },
        {
            "Price_per_m²": 2300.0,
            "Price": 115000.0,
            "m²": 50.0,
            "Address": "Stērstu 15"
        },
        {
            "Price_per_m²": 376.0,
            "Price": 9777.0,
            "m²": 26.0,
            "Address": "Zaļenieku 40-17"
        },
        {
            "Price_per_m²": 1209.0,
            "Price": 52000.0,
            "m²": 43.01,
            "Address": "Bauskas 187"
        },
        {
            "Price_per_m²": 1221.0,
            "Price": 41500.0,
            "m²": 33.99,
            "Address": "Ēbeļmuižas 20"
        },
        {
            "Price_per_m²": 578.0,
            "Price": 18500.0,
            "m²": 32.01,
            "Address": "Bauskas 149c"
        },
        {
            "Price_per_m²": 2087.0,
            "Price": 192000.0,
            "m²": 92.0,
            "Address": "Svētes 1"
        },
        {
            "Price_per_m²": 875.0,
            "Price": 49000.0,
            "m²": 56.0,
            "Address": "Ozolciema 18"
        },
        {
            "Price_per_m²": 2764.0,
            "Price": 99500.0,
            "m²": 36.0,
            "Address": "Stērstu 4"
        },
        {
            "Price_per_m²": 1019.0,
            "Price": 54000.0,
            "m²": 52.99,
            "Address": "Ķekavas 5"
        },
        {
            "Price_per_m²": 2018.0,
            "Price": 115000.0,
            "m²": 56.99,
            "Address": "Basu 3A"
        },
        {
            "Price_per_m²": 1032.0,
            "Price": 79500.0,
            "m²": 77.03,
            "Address": "Valdeķu 55"
        },
        {
            "Price_per_m²": 1397.0,
            "Price": 95000.0,
            "m²": 68.0,
            "Address": "Bauskas 43a"
        },
        {
            "Price_per_m²": 829.0,
            "Price": 34000.0,
            "m²": 41.01,
            "Address": "Ozolciema 30"
        },
        {
            "Price_per_m²": 970.0,
            "Price": 48500.0,
            "m²": 50.0,
            "Address": "Līvciema 57"
        },
        {
            "Price_per_m²": 2468.0,
            "Price": 153000.0,
            "m²": 61.99,
            "Address": "Tumes 25"
        },
        {
            "Price_per_m²": 2250.0,
            "Price": 135000.0,
            "m²": 60.0,
            "Address": "Tumes 25"
        },
        {
            "Price_per_m²": 2452.0,
            "Price": 152000.0,
            "m²": 61.99,
            "Address": "Tumes 25"
        },
        {
            "Price_per_m²": 2377.0,
            "Price": 164000.0,
            "m²": 68.99,
            "Address": "Tumes 25"
        },
        {
            "Price_per_m²": 1471.0,
            "Price": 50000.0,
            "m²": 33.99,
            "Address": "Īslīces 14"
        },
        {
            "Price_per_m²": 1054.0,
            "Price": 78000.0,
            "m²": 74.0,
            "Address": "Ozolciema 12/3"
        },
        {
            "Price_per_m²": 662.0,
            "Price": 13900.0,
            "m²": 21.0,
            "Address": "Vienības g. 126"
        },
        {
            "Price_per_m²": 1000.0,
            "Price": 47000.0,
            "m²": 47.0,
            "Address": "Ozolciema 34"
        },
        {
            "Price_per_m²": 1246.0,
            "Price": 86000.0,
            "m²": 69.02,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 1217.0,
            "Price": 56000.0,
            "m²": 46.01,
            "Address": "Ziepju 9"
        },
        {
            "Price_per_m²": 1900.0,
            "Price": 85500.0,
            "m²": 45.0,
            "Address": "Bauskas 41"
        },
        {
            "Price_per_m²": 1136.0,
            "Price": 87500.0,
            "m²": 77.02,
            "Address": "Valdeķu 51"
        },
        {
            "Price_per_m²": 958.0,
            "Price": 47900.0,
            "m²": 50.0,
            "Address": "Ēbeļmuižas 12"
        },
        {
            "Price_per_m²": 1039.0,
            "Price": 53000.0,
            "m²": 51.01,
            "Address": "Bauskas 203"
        },
        {
            "Price_per_m²": 2863.0,
            "Price": 114500.0,
            "m²": 39.99,
            "Address": "Tumes 25"
        },
        {
            "Price_per_m²": 1065.0,
            "Price": 99000.0,
            "m²": 92.96,
            "Address": "Ozolciema 18"
        },
        {
            "Price_per_m²": 936.0,
            "Price": 73000.0,
            "m²": 77.99,
            "Address": "Valdeķu 53"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        },
        {
            "Price_per_m²": 1451.0,
            "Price": 148000.0,
            "m²": 102.0,
            "Address": "Vienības g. 87"
        },
        {
            "Price_per_m²": 1035.0,
            "Price": 59000.0,
            "m²": 57.0,
            "Address": "Līvciema 9"
        },
        {
            "Price_per_m²": 1456.0,
            "Price": 115000.0,
            "m²": 78.98,
            "Address": "Kaplavas 5"
        },
        {
            "Price_per_m²": 2192.0,
            "Price": 160000.0,
            "m²": 72.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1904.0,
            "Price": 199900.0,
            "m²": 104.99,
            "Address": "Dignājas 4"
        },
        {
            "Price_per_m²": 1061.0,
            "Price": 52000.0,
            "m²": 49.01,
            "Address": "Dižozolu 25"
        },
        {
            "Price_per_m²": 1040.0,
            "Price": 52000.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 700.0,
            "Price": 35000.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 844.0,
            "Price": 37995.0,
            "m²": 45.02,
            "Address": "Valdeķu 64"
        },
        {
            "Price_per_m²": 2071.0,
            "Price": 159500.0,
            "m²": 77.02,
            "Address": "Komētas 30"
        },
        {
            "Price_per_m²": 885.0,
            "Price": 46000.0,
            "m²": 51.98,
            "Address": "Līvciema 49"
        }
    ],
    "monthly": [
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 8.33,
            "Price": 250.0,
            "m²": 30.01,
            "Address": "Irbenes 5"
        },
        {
            "Price_per_m²": 7.14,
            "Price": 500.0,
            "m²": 70.03,
            "Address": "Bruknas 16"
        },
        {
            "Price_per_m²": 4.1,
            "Price": 250.0,
            "m²": 60.98,
            "Address": "Kartupeļu 47"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Zaļenieku 21"
        },
        {
            "Price_per_m²": 5.95,
            "Price": 220.0,
            "m²": 36.97,
            "Address": "Vadakstes 20"
        },
        {
            "Price_per_m²": 6.67,
            "Price": 260.0,
            "m²": 38.98,
            "Address": "Ozolciema 40k1"
        },
        {
            "Price_per_m²": 8.14,
            "Price": 350.0,
            "m²": 43.0,
            "Address": "Valdeķu 65"
        },
        {
            "Price_per_m²": 8.97,
            "Price": 350.0,
            "m²": 39.02,
            "Address": "Ozolciema 40"
        },
        {
            "Price_per_m²": 7.18,
            "Price": 560.0,
            "m²": 77.99,
            "Address": "Īslīces 5"
        },
        {
            "Price_per_m²": 6.94,
            "Price": 430.0,
            "m²": 61.96,
            "Address": "Ziepniekkalna 64/1"
        },
        {
            "Price_per_m²": 6.33,
            "Price": 500.0,
            "m²": 78.99,
            "Address": "Kartupeļu 45"
        },
        {
            "Price_per_m²": 14.02,
            "Price": 1500.0,
            "m²": 106.99,
            "Address": "Putnu 3"
        },
        {
            "Price_per_m²": 7.11,
            "Price": 320.0,
            "m²": 45.01,
            "Address": "Bērzupes 33"
        },
        {
            "Price_per_m²": 15.31,
            "Price": 490.0,
            "m²": 32.01,
            "Address": "Stērstu 15a"
        },
        {
            "Price_per_m²": 7.06,
            "Price": 360.0,
            "m²": 50.99,
            "Address": "Valdeķu 60"
        },
        {
            "Price_per_m²": 10.75,
            "Price": 430.0,
            "m²": 40.0,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.73,
            "Price": 480.0,
            "m²": 54.98,
            "Address": "Vienības g. 186A"
        },
        {
            "Price_per_m²": 5.61,
            "Price": 230.0,
            "m²": 41.0,
            "Address": "Ozolciema 36"
        },
        {
            "Price_per_m²": 5.0,
            "Price": 350.0,
            "m²": 70.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 6.0,
            "Price": 300.0,
            "m²": 50.0,
            "Address": "Ēbeļmuižas 6"
        },
        {
            "Price_per_m²": 6.6,
            "Price": 330.0,
            "m²": 50.0,
            "Address": "Bauskas 61"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Valdeķu 68"
        },
        {
            "Price_per_m²": 11.14,
            "Price": 390.0,
            "m²": 35.01,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 8.77,
            "Price": 500.0,
            "m²": 57.01,
            "Address": "Liesmas 4"
        },
        {
            "Price_per_m²": 5.29,
            "Price": 550.0,
            "m²": 103.97,
            "Address": "Ozolciema 40a"
        },
        {
            "Price_per_m²": 8.45,
            "Price": 245.0,
            "m²": 28.99,
            "Address": "Valdeķu 5"
        },
        {
            "Price_per_m²": 7.0,
            "Price": 350.0,
            "m²": 50.0,
            "Address": "Ozolciema 28"
        },
        {
            "Price_per_m²": 7.97,
            "Price": 550.0,
            "m²": 69.01,
            "Address": "Vadakstes 17"
        },
        {
            "Price_per_m²": 10.83,
            "Price": 650.0,
            "m²": 60.02,
            "Address": "Skaistkalnes 17"
        },
        {
            "Price_per_m²": 8.7,
            "Price": 470.0,
            "m²": 54.02,
            "Address": "Dignājas 3B"
        },
        {
            "Price_per_m²": 8.93,
            "Price": 250.0,
            "m²": 28.0,
            "Address": "Ozolciema 8"
        }
    ],
    "daily": [
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.7,
            "Price": 35.0,
            "m²": 50.0,
            "Address": "Ozolciema 18"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 0.429,
            "Price": 15.0,
            "m²": 34.97,
            "Address": "Kartupeļu 14"
        },
        {
            "Price_per_m²": 1.0,
            "Price": 35.0,
            "m²": 35.0,
            "Address": "Kartupeļu 14"
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
plt.title('Cena pret m² dzīvokļiem, kas atrodas ziepniekkalns')

# Show the plot
plt.grid(True)
plt.show()