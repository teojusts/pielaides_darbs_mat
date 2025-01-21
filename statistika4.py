import json
import matplotlib.pyplot as plt

data = [
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 756.0,
        "Price": 39300.0,
        "m²": 51.98,
        "Address": "Ģertrūdes 103"
    },
    {
        "Price_per_m²": 457.0,
        "Price": 37000.0,
        "m²": 80.96,
        "Address": "Ģertrūdes 110"
    },
    {
        "Price_per_m²": 1733.0,
        "Price": 52000.0,
        "m²": 30.01,
        "Address": "Bruņinieku 104"
    },
    {
        "Price_per_m²": 1648.0,
        "Price": 138435.0,
        "m²": 84.0,
        "Address": "Lāčplēša 36"
    },
    {
        "Price_per_m²": 897.0,
        "Price": 26900.0,
        "m²": 29.99,
        "Address": "Valmieras 21"
    },
    {
        "Price_per_m²": 748.0,
        "Price": 15700.0,
        "m²": 20.99,
        "Address": "Stabu 55"
    },
    {
        "Price_per_m²": 1845.0,
        "Price": 101500.0,
        "m²": 55.01,
        "Address": "Lāčplēša 36"
    },
    {
        "Price_per_m²": 1371.0,
        "Price": 48000.0,
        "m²": 35.01,
        "Address": "Bruņinieku 79"
    },
    {
        "Price_per_m²": 1286.0,
        "Price": 54000.0,
        "m²": 41.99,
        "Address": "Bruņinieku 92"
    },
    {
        "Price_per_m²": 3258.0,
        "Price": 290000.0,
        "m²": 89.01,
        "Address": "Ģertrūdes 22"
    },
    {
        "Price_per_m²": 1500.0,
        "Price": 120000.0,
        "m²": 80.0,
        "Address": "Matīsa 83"
    },
    {
        "Price_per_m²": 1491.0,
        "Price": 170000.0,
        "m²": 114.02,
        "Address": "Lāčplēša 47"
    },
    {
        "Price_per_m²": 1190.0,
        "Price": 25000.0,
        "m²": 21.01,
        "Address": "Artilērijas 59"
    },
    {
        "Price_per_m²": 1891.0,
        "Price": 104000.0,
        "m²": 55.0,
        "Address": "Bruņinieku 121"
    },
    {
        "Price_per_m²": 697.0,
        "Price": 65500.0,
        "m²": 93.97,
        "Address": "Stabu 45"
    },
    {
        "Price_per_m²": 2267.0,
        "Price": 272000.0,
        "m²": 119.98,
        "Address": "Stabu 46/48"
    },
    {
        "Price_per_m²": 1893.0,
        "Price": 195000.0,
        "m²": 103.01,
        "Address": "Ģertrūdes 14"
    },
    {
        "Price_per_m²": 2607.0,
        "Price": 146000.0,
        "m²": 56.0,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 1588.0,
        "Price": 135000.0,
        "m²": 85.01,
        "Address": "Ģertrūdes 103A"
    },
    {
        "Price_per_m²": 2200.0,
        "Price": 33000.0,
        "m²": 15.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 1358.0,
        "Price": 220000.0,
        "m²": 162.0,
        "Address": "Ģertrūdes 5a"
    },
    {
        "Price_per_m²": 2437.0,
        "Price": 143800.0,
        "m²": 59.01,
        "Address": "Stabu 49A"
    },
    {
        "Price_per_m²": 1021.0,
        "Price": 199000.0,
        "m²": 194.91,
        "Address": "Lāčplēša 70a"
    },
    {
        "Price_per_m²": 1700.0,
        "Price": 345000.0,
        "m²": 202.94,
        "Address": "Ģertrūdes 22"
    },
    {
        "Price_per_m²": 1174.0,
        "Price": 27000.0,
        "m²": 23.0,
        "Address": "Avotu 65a"
    },
    {
        "Price_per_m²": 1094.0,
        "Price": 35000.0,
        "m²": 31.99,
        "Address": "Avotu 65a"
    },
    {
        "Price_per_m²": 2633.0,
        "Price": 79000.0,
        "m²": 30.0,
        "Address": "Bruņinieku 93c"
    },
    {
        "Price_per_m²": 979.0,
        "Price": 23500.0,
        "m²": 24.0,
        "Address": "Valmieras 39"
    },
    {
        "Price_per_m²": 1045.0,
        "Price": 23000.0,
        "m²": 22.01,
        "Address": "Stabu 71a"
    },
    {
        "Price_per_m²": 1641.0,
        "Price": 139500.0,
        "m²": 85.01,
        "Address": "Lāčplēša 36"
    },
    {
        "Price_per_m²": 549.0,
        "Price": 50000.0,
        "m²": 91.07,
        "Address": "Matīsa 93"
    },
    {
        "Price_per_m²": 1383.0,
        "Price": 65000.0,
        "m²": 47.0,
        "Address": "Bruņinieku 52"
    },
    {
        "Price_per_m²": 1260.0,
        "Price": 160000.0,
        "m²": 126.98,
        "Address": "Lāčplēša 54"
    },
    {
        "Price_per_m²": 788.0,
        "Price": 189000.0,
        "m²": 239.85,
        "Address": "Stabu 56"
    },
    {
        "Price_per_m²": 2284.0,
        "Price": 169000.0,
        "m²": 73.99,
        "Address": "Lāčplēša 129"
    },
    {
        "Price_per_m²": 2650.0,
        "Price": 53000.0,
        "m²": 20.0,
        "Address": "Lāčplēša 35"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 115500.0,
        "m²": 66.0,
        "Address": "Avotu 3"
    },
    {
        "Price_per_m²": 1627.0,
        "Price": 96000.0,
        "m²": 59.0,
        "Address": "Lāčplēša 36"
    },
    {
        "Price_per_m²": 1888.0,
        "Price": 113300.0,
        "m²": 60.01,
        "Address": "Lāčplēša 36"
    },
    {
        "Price_per_m²": 2276.0,
        "Price": 66000.0,
        "m²": 29.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 587.0,
        "Price": 13500.0,
        "m²": 23.0,
        "Address": "Matīsa 82A"
    },
    {
        "Price_per_m²": 1302.0,
        "Price": 72900.0,
        "m²": 55.99,
        "Address": "Lāčplēša 62"
    },
    {
        "Price_per_m²": 2053.0,
        "Price": 154000.0,
        "m²": 75.01,
        "Address": "Matīsa 29"
    },
    {
        "Price_per_m²": 2292.0,
        "Price": 275000.0,
        "m²": 119.98,
        "Address": "Bruņinieku 28"
    },
    {
        "Price_per_m²": 1583.0,
        "Price": 57000.0,
        "m²": 36.01,
        "Address": "Krāsotāju 25"
    },
    {
        "Price_per_m²": 962.0,
        "Price": 25000.0,
        "m²": 25.99,
        "Address": "Matīsa 44a"
    },
    {
        "Price_per_m²": 1246.0,
        "Price": 71000.0,
        "m²": 56.98,
        "Address": "Zaķu 7"
    },
    {
        "Price_per_m²": 688.0,
        "Price": 44000.0,
        "m²": 63.95,
        "Address": "Ģertrūdes 135A"
    },
    {
        "Price_per_m²": 1227.0,
        "Price": 85900.0,
        "m²": 70.01,
        "Address": "Lienes 9"
    },
    {
        "Price_per_m²": 2593.0,
        "Price": 70000.0,
        "m²": 27.0,
        "Address": "Krāsotāju 13B"
    },
    {
        "Price_per_m²": 1686.0,
        "Price": 118000.0,
        "m²": 69.99,
        "Address": "Stabu 81"
    },
    {
        "Price_per_m²": 1648.0,
        "Price": 133485.0,
        "m²": 81.0,
        "Address": "Lāčplēša 36"
    },
    {
        "Price_per_m²": 220.0,
        "Price": 35000.0,
        "m²": 159.09,
        "Address": "Artilērijas 13"
    },
    {
        "Price_per_m²": 2083.0,
        "Price": 99960.0,
        "m²": 47.99,
        "Address": "Bruņinieku 85"
    },
    {
        "Price_per_m²": 1061.0,
        "Price": 52000.0,
        "m²": 49.01,
        "Address": "Avotu 64A"
    },
    {
        "Price_per_m²": 2872.0,
        "Price": 224000.0,
        "m²": 77.99,
        "Address": "Stabu 19"
    },
    {
        "Price_per_m²": 2276.0,
        "Price": 66000.0,
        "m²": 29.0,
        "Address": "Matīsa 29"
    },
    {
        "Price_per_m²": 2700.0,
        "Price": 321300.0,
        "m²": 119.0,
        "Address": "Ģertrūdes 23"
    },
    {
        "Price_per_m²": 2152.0,
        "Price": 49500.0,
        "m²": 23.0,
        "Address": "Ģertrūdes 55A"
    },
    {
        "Price_per_m²": 2167.0,
        "Price": 195000.0,
        "m²": 89.99,
        "Address": "Ģertrūdes 55A"
    },
    {
        "Price_per_m²": 592.0,
        "Price": 38500.0,
        "m²": 65.03,
        "Address": "Lienes 9"
    },
    {
        "Price_per_m²": 1810.0,
        "Price": 105000.0,
        "m²": 58.01,
        "Address": "Bruņinieku 68А"
    },
    {
        "Price_per_m²": 1095.0,
        "Price": 23000.0,
        "m²": 21.0,
        "Address": "Ādmiņu 5"
    },
    {
        "Price_per_m²": 1520.0,
        "Price": 187000.0,
        "m²": 123.03,
        "Address": "Ģertrūdes 77"
    },
    {
        "Price_per_m²": 1367.0,
        "Price": 41000.0,
        "m²": 29.99,
        "Address": "Bruņinieku 61a"
    },
    {
        "Price_per_m²": 1864.0,
        "Price": 110000.0,
        "m²": 59.01,
        "Address": "Valmieras 28"
    },
    {
        "Price_per_m²": 1300.0,
        "Price": 64999.0,
        "m²": 50.0,
        "Address": "Stabu 116"
    },
    {
        "Price_per_m²": 1675.0,
        "Price": 75380.0,
        "m²": 45.0,
        "Address": "Matīsa 83"
    },
    {
        "Price_per_m²": 1331.0,
        "Price": 59900.0,
        "m²": 45.0,
        "Address": "Stabu 118"
    },
    {
        "Price_per_m²": 2829.0,
        "Price": 113145.0,
        "m²": 39.99,
        "Address": "Stabu 87a"
    },
    {
        "Price_per_m²": 1722.0,
        "Price": 86077.0,
        "m²": 49.99,
        "Address": "Krāsotāju 13"
    },
    {
        "Price_per_m²": 2190.0,
        "Price": 91970.0,
        "m²": 42.0,
        "Address": "Krāsotāju 13"
    },
    {
        "Price_per_m²": 2258.0,
        "Price": 117390.0,
        "m²": 51.99,
        "Address": "Krāsotāju 13"
    },
    {
        "Price_per_m²": 1342.0,
        "Price": 25500.0,
        "m²": 19.0,
        "Address": "Ģertrūdes 91 A"
    },
    {
        "Price_per_m²": 1468.0,
        "Price": 69000.0,
        "m²": 47.0,
        "Address": "Stabu 33"
    },
    {
        "Price_per_m²": 2542.0,
        "Price": 150000.0,
        "m²": 59.01,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 2383.0,
        "Price": 143000.0,
        "m²": 60.01,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 1971.0,
        "Price": 136000.0,
        "m²": 69.0,
        "Address": "Artilērijas 52A"
    },
    {
        "Price_per_m²": 474.0,
        "Price": 14680.0,
        "m²": 30.97,
        "Address": "Artilērijas 67"
    },
    {
        "Price_per_m²": 1962.0,
        "Price": 127500.0,
        "m²": 64.98,
        "Address": "Stabu 46"
    },
    {
        "Price_per_m²": 1472.0,
        "Price": 36800.0,
        "m²": 25.0,
        "Address": "Bruņinieku 119"
    },
    {
        "Price_per_m²": 2209.0,
        "Price": 296000.0,
        "m²": 134.0,
        "Address": "Lāčplēša 123"
    },
    {
        "Price_per_m²": 1625.0,
        "Price": 130000.0,
        "m²": 80.0,
        "Address": "Stabu 29"
    },
    {
        "Price_per_m²": 865.0,
        "Price": 45000.0,
        "m²": 52.02,
        "Address": "Lāčplēša 104A"
    },
    {
        "Price_per_m²": 2224.0,
        "Price": 189000.0,
        "m²": 84.98,
        "Address": "Stabu 29"
    },
    {
        "Price_per_m²": 1817.0,
        "Price": 109000.0,
        "m²": 59.99,
        "Address": "Lāčplēša 21"
    },
    {
        "Price_per_m²": 2333.0,
        "Price": 35000.0,
        "m²": 15.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 2167.0,
        "Price": 39000.0,
        "m²": 18.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 2438.0,
        "Price": 97500.0,
        "m²": 39.99,
        "Address": "Sparģeļu 10"
    },
    {
        "Price_per_m²": 2854.0,
        "Price": 79900.0,
        "m²": 28.0,
        "Address": "Sparģeļu 10"
    },
    {
        "Price_per_m²": 2318.0,
        "Price": 102000.0,
        "m²": 44.0,
        "Address": "Sparģeļu 10"
    },
    {
        "Price_per_m²": 3258.0,
        "Price": 290000.0,
        "m²": 89.01,
        "Address": "Ģertrūdes 22"
    },
    {
        "Price_per_m²": 1083.0,
        "Price": 26000.0,
        "m²": 24.01,
        "Address": "Bruņinieku 82"
    },
    {
        "Price_per_m²": 2209.0,
        "Price": 296000.0,
        "m²": 134.0,
        "Address": "Lāčplēša 123"
    },
    {
        "Price_per_m²": 1500.0,
        "Price": 45000.0,
        "m²": 30.0,
        "Address": "Bruņinieku 89"
    },
    {
        "Price_per_m²": 1560.0,
        "Price": 78000.0,
        "m²": 50.0,
        "Address": "Stabu 95 k-1"
    },
    {
        "Price_per_m²": 2708.0,
        "Price": 130000.0,
        "m²": 48.01,
        "Address": "Stabu 19"
    },
    {
        "Price_per_m²": 2284.0,
        "Price": 169000.0,
        "m²": 73.99,
        "Address": "Lāčplēša 129"
    },
    {
        "Price_per_m²": 2308.0,
        "Price": 120000.0,
        "m²": 51.99,
        "Address": "Matīsa 29"
    },
    {
        "Price_per_m²": 1718.0,
        "Price": 122000.0,
        "m²": 71.01,
        "Address": "Bruņinieku 47"
    },
    {
        "Price_per_m²": 1474.0,
        "Price": 57500.0,
        "m²": 39.01,
        "Address": "Avotu 54"
    },
    {
        "Price_per_m²": 1000.0,
        "Price": 31000.0,
        "m²": 31.0,
        "Address": "Artilērijas 3"
    },
    {
        "Price_per_m²": 1711.0,
        "Price": 130065.0,
        "m²": 76.02,
        "Address": "Krāsotāju 13"
    },
    {
        "Price_per_m²": 2095.0,
        "Price": 132000.0,
        "m²": 63.01,
        "Address": "Stabu 50"
    },
    {
        "Price_per_m²": 1887.0,
        "Price": 113240.0,
        "m²": 60.01,
        "Address": "Lāčplēša 36"
    },
    {
        "Price_per_m²": 1501.0,
        "Price": 51030.0,
        "m²": 34.0,
        "Address": "Lienes 9"
    },
    {
        "Price_per_m²": 1145.0,
        "Price": 63000.0,
        "m²": 55.02,
        "Address": "Matīsa 111"
    },
    {
        "Price_per_m²": 1337.0,
        "Price": 250000.0,
        "m²": 186.99,
        "Address": "Stabu 92"
    },
    {
        "Price_per_m²": 2333.0,
        "Price": 84000.0,
        "m²": 36.01,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 1604.0,
        "Price": 38500.0,
        "m²": 24.0,
        "Address": "Bruņinieku 119"
    },
    {
        "Price_per_m²": 2565.0,
        "Price": 335990.0,
        "m²": 130.99,
        "Address": "Artilērijas 6a"
    },
    {
        "Price_per_m²": 2386.0,
        "Price": 136000.0,
        "m²": 57.0,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 2576.0,
        "Price": 152000.0,
        "m²": 59.01,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 1561.0,
        "Price": 115500.0,
        "m²": 73.99,
        "Address": "Bruņinieku 89"
    },
    {
        "Price_per_m²": 2273.0,
        "Price": 100000.0,
        "m²": 43.99,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 1293.0,
        "Price": 106000.0,
        "m²": 81.98,
        "Address": "Avotu 31"
    },
    {
        "Price_per_m²": 4015.0,
        "Price": 799000.0,
        "m²": 199.0,
        "Address": "Ģertrūdes 23"
    },
    {
        "Price_per_m²": 1465.0,
        "Price": 49800.0,
        "m²": 33.99,
        "Address": "Bruņinieku 93a"
    },
    {
        "Price_per_m²": 2133.0,
        "Price": 160000.0,
        "m²": 75.01,
        "Address": "Ģertrūdes 103B"
    },
    {
        "Price_per_m²": 1172.0,
        "Price": 68000.0,
        "m²": 58.02,
        "Address": "Lāčplēša 72"
    },
    {
        "Price_per_m²": 1882.0,
        "Price": 160000.0,
        "m²": 85.02,
        "Address": "Artilērijas 24"
    },
    {
        "Price_per_m²": 948.0,
        "Price": 18950.0,
        "m²": 19.99,
        "Address": "Avotu 65a"
    },
    {
        "Price_per_m²": 2143.0,
        "Price": 60000.0,
        "m²": 28.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 2538.0,
        "Price": 165000.0,
        "m²": 65.01,
        "Address": "Bruņinieku 12"
    },
    {
        "Price_per_m²": 1922.0,
        "Price": 86500.0,
        "m²": 45.01,
        "Address": "Lāčplēša 36"
    },
    {
        "Price_per_m²": 2625.0,
        "Price": 105000.0,
        "m²": 40.0,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 1290.0,
        "Price": 105800.0,
        "m²": 82.02,
        "Address": "Visvalža 7"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1476.0,
        "Price": 31000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1583.0,
        "Price": 56995.0,
        "m²": 36.0,
        "Address": "Bruņinieku 79B"
    },
    {
        "Price_per_m²": 1875.0,
        "Price": 112500.0,
        "m²": 60.0,
        "Address": "Valmieras 20"
    },
    {
        "Price_per_m²": 1238.0,
        "Price": 26000.0,
        "m²": 21.0,
        "Address": "Artilērijas 59"
    },
    {
        "Price_per_m²": 2048.0,
        "Price": 215000.0,
        "m²": 104.98,
        "Address": "Stabu 105"
    },
    {
        "Price_per_m²": 1571.0,
        "Price": 110000.0,
        "m²": 70.02,
        "Address": "Stabu 81"
    },
    {
        "Price_per_m²": 2000.0,
        "Price": 110000.0,
        "m²": 55.0,
        "Address": "Stabu 15"
    },
    {
        "Price_per_m²": 1286.0,
        "Price": 27000.0,
        "m²": 21.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1056.0,
        "Price": 28500.0,
        "m²": 26.99,
        "Address": "Ģertrūdes 135"
    },
    {
        "Price_per_m²": 1442.0,
        "Price": 64900.0,
        "m²": 45.01,
        "Address": "Stabu 118"
    },
    {
        "Price_per_m²": 1205.0,
        "Price": 92800.0,
        "m²": 77.01,
        "Address": "Lāčplēša 62"
    },
    {
        "Price_per_m²": 2056.0,
        "Price": 146000.0,
        "m²": 71.01,
        "Address": "Stabu 81"
    },
    {
        "Price_per_m²": 1941.0,
        "Price": 165000.0,
        "m²": 85.01,
        "Address": "Stabu 29"
    },
    {
        "Price_per_m²": 1018.0,
        "Price": 49900.0,
        "m²": 49.02,
        "Address": "Avotu 64A"
    },
    {
        "Price_per_m²": 2231.0,
        "Price": 145000.0,
        "m²": 64.99,
        "Address": "Matīsa 69"
    },
    {
        "Price_per_m²": 1547.0,
        "Price": 134550.0,
        "m²": 86.97,
        "Address": "Krāsotāju 6C"
    },
    {
        "Price_per_m²": 3149.0,
        "Price": 179500.0,
        "m²": 57.0,
        "Address": "Stabu 2A"
    },
    {
        "Price_per_m²": 1268.0,
        "Price": 79900.0,
        "m²": 63.01,
        "Address": "Narvas 6"
    },
    {
        "Price_per_m²": 2302.0,
        "Price": 145000.0,
        "m²": 62.99,
        "Address": "Stabu 71"
    },
    {
        "Price_per_m²": 2633.0,
        "Price": 79000.0,
        "m²": 30.0,
        "Address": "Bruņinieku 93"
    },
    {
        "Price_per_m²": 1827.0,
        "Price": 95000.0,
        "m²": 52.0,
        "Address": "Bruņinieku 87A"
    },
    {
        "Price_per_m²": 1719.0,
        "Price": 98000.0,
        "m²": 57.01,
        "Address": "Bruņinieku 87"
    },
    {
        "Price_per_m²": 2846.0,
        "Price": 173600.0,
        "m²": 61.0,
        "Address": "Stabu 19"
    },
    {
        "Price_per_m²": 1239.0,
        "Price": 57000.0,
        "m²": 46.0,
        "Address": "Ģertrūdes 113"
    },
    {
        "Price_per_m²": 922.0,
        "Price": 59000.0,
        "m²": 63.99,
        "Address": "Avotu 8"
    },
    {
        "Price_per_m²": 4000.0,
        "Price": 220000.0,
        "m²": 55.0,
        "Address": "Stabu 18b"
    },
    {
        "Price_per_m²": 3653.0,
        "Price": 401800.0,
        "m²": 109.99,
        "Address": "Stabu 18b"
    },
    {
        "Price_per_m²": 1750.0,
        "Price": 245000.0,
        "m²": 140.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1426.0,
        "Price": 48500.0,
        "m²": 34.01,
        "Address": "Bruņinieku 93a"
    },
    {
        "Price_per_m²": 2692.0,
        "Price": 70000.0,
        "m²": 26.0,
        "Address": "Krāsotāju 13"
    },
    {
        "Price_per_m²": 1375.0,
        "Price": 44000.0,
        "m²": 32.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 2000.0,
        "Price": 90000.0,
        "m²": 45.0,
        "Address": "Avotu 20a"
    },
    {
        "Price_per_m²": 964.0,
        "Price": 27000.0,
        "m²": 28.01,
        "Address": "Lienes 27"
    },
    {
        "Price_per_m²": 2383.0,
        "Price": 143000.0,
        "m²": 60.01,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 2475.0,
        "Price": 99000.0,
        "m²": 40.0,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 547.0,
        "Price": 12580.0,
        "m²": 23.0,
        "Address": "Lāčplēša 129"
    },
    {
        "Price_per_m²": 2386.0,
        "Price": 136000.0,
        "m²": 57.0,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 2404.0,
        "Price": 125000.0,
        "m²": 52.0,
        "Address": "Ģertrūdes 65/2"
    },
    {
        "Price_per_m²": 1800.0,
        "Price": 135000.0,
        "m²": 75.0,
        "Address": "Stabu 41"
    },
    {
        "Price_per_m²": 1763.0,
        "Price": 96950.0,
        "m²": 54.99,
        "Address": "Stabu 87"
    },
    {
        "Price_per_m²": 2650.0,
        "Price": 217300.0,
        "m²": 82.0,
        "Address": "Lāčplēša 7"
    },
    {
        "Price_per_m²": 1726.0,
        "Price": 94955.0,
        "m²": 55.01,
        "Address": "Stabu 87A"
    },
    {
        "Price_per_m²": 1981.0,
        "Price": 53500.0,
        "m²": 27.01,
        "Address": "Bruņinieku 73E"
    },
    {
        "Price_per_m²": 1728.0,
        "Price": 197000.0,
        "m²": 114.0,
        "Address": "Ģertrūdes 103"
    },
    {
        "Price_per_m²": 2292.0,
        "Price": 275000.0,
        "m²": 119.98,
        "Address": "Bruņinieku 28"
    },
    {
        "Price_per_m²": 2163.0,
        "Price": 225000.0,
        "m²": 104.02,
        "Address": "Ģertrūdes 62A"
    },
    {
        "Price_per_m²": 1571.0,
        "Price": 99000.0,
        "m²": 63.02,
        "Address": "Ģertrūdes 103"
    },
    {
        "Price_per_m²": 1391.0,
        "Price": 89000.0,
        "m²": 63.98,
        "Address": "Ģertrūdes 103A"
    },
    {
        "Price_per_m²": 917.0,
        "Price": 22000.0,
        "m²": 23.99,
        "Address": "Bruņinieku 102a"
    },
    {
        "Price_per_m²": 2813.0,
        "Price": 180000.0,
        "m²": 63.99,
        "Address": "Artilērijas 65"
    },
    {
        "Price_per_m²": 1647.0,
        "Price": 100469.0,
        "m²": 61.0,
        "Address": "Avotu 46"
    },
    {
        "Price_per_m²": 3036.0,
        "Price": 85000.0,
        "m²": 28.0,
        "Address": "Krāsotāju 13"
    },
    {
        "Price_per_m²": 712.0,
        "Price": 42000.0,
        "m²": 58.99,
        "Address": "Valmieras 6"
    },
    {
        "Price_per_m²": 950.0,
        "Price": 19000.0,
        "m²": 20.0,
        "Address": "Matīsa 119"
    },
    {
        "Price_per_m²": 987.0,
        "Price": 74980.0,
        "m²": 75.97,
        "Address": "Lāčplēša 112"
    },
    {
        "Price_per_m²": 1944.0,
        "Price": 105000.0,
        "m²": 54.01,
        "Address": "Stabu 91"
    },
    {
        "Price_per_m²": 1206.0,
        "Price": 61500.0,
        "m²": 51.0,
        "Address": "Stabu 84"
    },
    {
        "Price_per_m²": 2480.0,
        "Price": 156250.0,
        "m²": 63.0,
        "Address": "Avotu 46"
    },
    {
        "Price_per_m²": 1818.0,
        "Price": 80000.0,
        "m²": 44.0,
        "Address": "Ģertrūdes 113"
    },
    {
        "Price_per_m²": 569.0,
        "Price": 98500.0,
        "m²": 173.11,
        "Address": "Matīsa 17 k-1"
    },
    {
        "Price_per_m²": 2738.0,
        "Price": 230000.0,
        "m²": 84.0,
        "Address": "Lāčplēša 7"
    },
    {
        "Price_per_m²": 1461.0,
        "Price": 84750.0,
        "m²": 58.01,
        "Address": "Ādmiņu 5"
    },
    {
        "Price_per_m²": 1563.0,
        "Price": 75000.0,
        "m²": 47.98,
        "Address": "Ģertrūdes 93"
    },
    {
        "Price_per_m²": 2172.0,
        "Price": 63000.0,
        "m²": 29.01,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 2170.0,
        "Price": 115000.0,
        "m²": 53.0,
        "Address": "Artilērijas 6"
    },
    {
        "Price_per_m²": 2743.0,
        "Price": 57600.0,
        "m²": 21.0,
        "Address": "Lāčplēša 35"
    },
    {
        "Price_per_m²": 1762.0,
        "Price": 144500.0,
        "m²": 82.01,
        "Address": "Lāčplēša 35"
    },
    {
        "Price_per_m²": 2057.0,
        "Price": 125500.0,
        "m²": 61.01,
        "Address": "Stabu 49a"
    },
    {
        "Price_per_m²": 1981.0,
        "Price": 53500.0,
        "m²": 27.01,
        "Address": "Bruņinieku 73E"
    },
    {
        "Price_per_m²": 1905.0,
        "Price": 80000.0,
        "m²": 41.99,
        "Address": "Ģertrūdes 113"
    },
    {
        "Price_per_m²": 2079.0,
        "Price": 185000.0,
        "m²": 88.99,
        "Address": "Stabu 29"
    },
    {
        "Price_per_m²": 1294.0,
        "Price": 110000.0,
        "m²": 85.01,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 1339.0,
        "Price": 75000.0,
        "m²": 56.01,
        "Address": "Lāčplēša 52"
    },
    {
        "Price_per_m²": 1303.0,
        "Price": 99000.0,
        "m²": 75.98,
        "Address": "Artilērijas 24"
    },
    {
        "Price_per_m²": 1363.0,
        "Price": 84500.0,
        "m²": 62.0,
        "Address": "Artilērijas 11"
    },
    {
        "Price_per_m²": 1314.0,
        "Price": 28900.0,
        "m²": 21.99,
        "Address": "Ādmiņu 5"
    },
    {
        "Price_per_m²": 3325.0,
        "Price": 189500.0,
        "m²": 56.99,
        "Address": "Stabu 2A"
    },
    {
        "Price_per_m²": 2813.0,
        "Price": 180000.0,
        "m²": 63.99,
        "Address": "Artilērijas 65"
    },
    {
        "Price_per_m²": 1827.0,
        "Price": 95000.0,
        "m²": 52.0,
        "Address": "Stabu 61"
    },
    {
        "Price_per_m²": 2273.0,
        "Price": 125000.0,
        "m²": 54.99,
        "Address": "Stabu 19"
    },
    {
        "Price_per_m²": 2487.0,
        "Price": 134275.0,
        "m²": 53.99,
        "Address": "Stabu 87A"
    },
    {
        "Price_per_m²": 702.0,
        "Price": 29500.0,
        "m²": 42.02,
        "Address": "Stabu 45"
    },
    {
        "Price_per_m²": 1755.0,
        "Price": 164999.0,
        "m²": 94.02,
        "Address": "Stabu 92"
    },
    {
        "Price_per_m²": 1466.0,
        "Price": 85000.0,
        "m²": 57.98,
        "Address": "Ādmiņu 5 30/31"
    },
    {
        "Price_per_m²": 1308.0,
        "Price": 140000.0,
        "m²": 107.03,
        "Address": "Stabu 92"
    },
    {
        "Price_per_m²": 1443.0,
        "Price": 88000.0,
        "m²": 60.98,
        "Address": "Lāčplēša 116"
    },
    {
        "Price_per_m²": 1742.0,
        "Price": 95830.0,
        "m²": 55.01,
        "Address": "Stabu 87A"
    },
    {
        "Price_per_m²": 950.0,
        "Price": 19000.0,
        "m²": 20.0,
        "Address": "Avotu 65"
    },
    {
        "Price_per_m²": 657.0,
        "Price": 34800.0,
        "m²": 52.97,
        "Address": "Kurbada 1"
    },
    {
        "Price_per_m²": 1270.0,
        "Price": 155000.0,
        "m²": 122.05,
        "Address": "Ģertrūdes 63"
    },
    {
        "Price_per_m²": 2237.0,
        "Price": 378000.0,
        "m²": 168.98,
        "Address": "Ģertrūdes 9"
    },
    {
        "Price_per_m²": 2115.0,
        "Price": 220000.0,
        "m²": 104.02,
        "Address": "Lāčplēša 21"
    },
    {
        "Price_per_m²": 2774.0,
        "Price": 369000.0,
        "m²": 133.02,
        "Address": "Stabu 18a"
    },
    {
        "Price_per_m²": 1635.0,
        "Price": 129200.0,
        "m²": 79.02,
        "Address": "Matīsa 29"
    },
    {
        "Price_per_m²": 1731.0,
        "Price": 89999.0,
        "m²": 51.99,
        "Address": "Lāčplēša 114"
    },
    {
        "Price_per_m²": 1073.0,
        "Price": 59000.0,
        "m²": 54.99,
        "Address": "Krāsotāju 18"
    },
    {
        "Price_per_m²": 1098.0,
        "Price": 45000.0,
        "m²": 40.98,
        "Address": "Matīsa 93"
    },
    {
        "Price_per_m²": 1100.0,
        "Price": 99000.0,
        "m²": 90.0,
        "Address": "Avotu 2"
    },
    {
        "Price_per_m²": 2069.0,
        "Price": 60000.0,
        "m²": 29.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 560.0,
        "Price": 19590.0,
        "m²": 34.98,
        "Address": "Artilērijas 67"
    },
    {
        "Price_per_m²": 2045.0,
        "Price": 90000.0,
        "m²": 44.01,
        "Address": "Krāsotāju 24"
    },
    {
        "Price_per_m²": 1818.0,
        "Price": 80000.0,
        "m²": 44.0,
        "Address": "Krāsotāju 24"
    },
    {
        "Price_per_m²": 1777.0,
        "Price": 279000.0,
        "m²": 157.01,
        "Address": "Ģertrūdes 103"
    },
    {
        "Price_per_m²": 850.0,
        "Price": 85000.0,
        "m²": 100.0,
        "Address": "Lāčplēša 118"
    },
    {
        "Price_per_m²": 1691.0,
        "Price": 159000.0,
        "m²": 94.03,
        "Address": "Ģertrūdes 51"
    },
    {
        "Price_per_m²": 2872.0,
        "Price": 224000.0,
        "m²": 77.99,
        "Address": "Stabu 19"
    },
    {
        "Price_per_m²": 3609.0,
        "Price": 375345.0,
        "m²": 104.0,
        "Address": "Stabu 18b"
    },
    {
        "Price_per_m²": 1774.0,
        "Price": 110000.0,
        "m²": 62.01,
        "Address": "Stabu 116"
    },
    {
        "Price_per_m²": 2900.0,
        "Price": 89900.0,
        "m²": 31.0,
        "Address": "Lāčplēša 24"
    },
    {
        "Price_per_m²": 1600.0,
        "Price": 112000.0,
        "m²": 70.0,
        "Address": "Stabu 87"
    },
    {
        "Price_per_m²": 2903.0,
        "Price": 180000.0,
        "m²": 62.0,
        "Address": "Artilērijas 65"
    },
    {
        "Price_per_m²": 1569.0,
        "Price": 80000.0,
        "m²": 50.99,
        "Address": "Visvalža 3b"
    },
    {
        "Price_per_m²": 1042.0,
        "Price": 25000.0,
        "m²": 23.99,
        "Address": "Artilērijas 66"
    },
    {
        "Price_per_m²": 2924.0,
        "Price": 119900.0,
        "m²": 41.01,
        "Address": "Avotu 4a"
    },
    {
        "Price_per_m²": 2612.0,
        "Price": 75750.0,
        "m²": 29.0,
        "Address": "Krāsotāju 13"
    },
    {
        "Price_per_m²": 703.0,
        "Price": 23200.0,
        "m²": 33.0,
        "Address": "Krāsotāju 6a"
    },
    {
        "Price_per_m²": 1383.0,
        "Price": 65000.0,
        "m²": 47.0,
        "Address": "Bruņinieku 52"
    },
    {
        "Price_per_m²": 2955.0,
        "Price": 130000.0,
        "m²": 43.99,
        "Address": "Stabu 2A"
    },
    {
        "Price_per_m²": 1021.0,
        "Price": 49000.0,
        "m²": 47.99,
        "Address": "Bruņinieku 73E"
    },
    {
        "Price_per_m²": 2353.0,
        "Price": 120000.0,
        "m²": 51.0,
        "Address": "Stabu 84"
    },
    {
        "Price_per_m²": 1782.0,
        "Price": 139000.0,
        "m²": 78.0,
        "Address": "Stabu 23"
    },
    {
        "Price_per_m²": 1714.0,
        "Price": 240000.0,
        "m²": 140.02,
        "Address": "Ģertrūdes 30"
    },
    {
        "Price_per_m²": 1071.0,
        "Price": 25700.0,
        "m²": 24.0,
        "Address": "Lienes 27"
    },
    {
        "Price_per_m²": 1037.0,
        "Price": 85000.0,
        "m²": 81.97,
        "Address": "Bruņinieku 99"
    },
    {
        "Price_per_m²": 1700.0,
        "Price": 159800.0,
        "m²": 94.0,
        "Address": "Lāčplēša 35"
    },
    {
        "Price_per_m²": 708.0,
        "Price": 59500.0,
        "m²": 84.04,
        "Address": "Lāčplēša 104"
    },
    {
        "Price_per_m²": 1419.0,
        "Price": 44000.0,
        "m²": 31.01,
        "Address": "Avotu 66"
    },
    {
        "Price_per_m²": 1809.0,
        "Price": 85000.0,
        "m²": 46.99,
        "Address": "Avotu 73"
    },
    {
        "Price_per_m²": 897.0,
        "Price": 26900.0,
        "m²": 29.99,
        "Address": "Satekles 15"
    },
    {
        "Price_per_m²": 2182.0,
        "Price": 104720.0,
        "m²": 47.99,
        "Address": "Bruņinieku 85"
    },
    {
        "Price_per_m²": 2941.0,
        "Price": 150000.0,
        "m²": 51.0,
        "Address": "Ģertrūdes 31"
    },
    {
        "Price_per_m²": 2833.0,
        "Price": 85000.0,
        "m²": 30.0,
        "Address": "Stabu 52b"
    },
    {
        "Price_per_m²": 1645.0,
        "Price": 102000.0,
        "m²": 62.01,
        "Address": "Ģertrūdes 31"
    },
    {
        "Price_per_m²": 2299.0,
        "Price": 154000.0,
        "m²": 66.99,
        "Address": "Matīsa 29"
    },
    {
        "Price_per_m²": 1944.0,
        "Price": 105000.0,
        "m²": 54.01,
        "Address": "Stabu 91"
    },
    {
        "Price_per_m²": 1833.0,
        "Price": 165000.0,
        "m²": 90.02,
        "Address": "Lāčplēša 21"
    },
    {
        "Price_per_m²": 1371.0,
        "Price": 48000.0,
        "m²": 35.01,
        "Address": "Bruņinieku 79"
    },
    {
        "Price_per_m²": 1890.0,
        "Price": 155000.0,
        "m²": 82.01,
        "Address": "Lāčplēša 23"
    },
    {
        "Price_per_m²": 2274.0,
        "Price": 120500.0,
        "m²": 52.99,
        "Address": "Artilērijas 6"
    },
    {
        "Price_per_m²": 1231.0,
        "Price": 48000.0,
        "m²": 38.99,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 2261.0,
        "Price": 52000.0,
        "m²": 23.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 1094.0,
        "Price": 35000.0,
        "m²": 31.99,
        "Address": "Bruņinieku 121"
    },
    {
        "Price_per_m²": 2813.0,
        "Price": 180000.0,
        "m²": 63.99,
        "Address": "Artilērijas 65"
    },
    {
        "Price_per_m²": 2394.0,
        "Price": 79000.0,
        "m²": 33.0,
        "Address": "Bruņinieku 93C"
    },
    {
        "Price_per_m²": 1135.0,
        "Price": 29500.0,
        "m²": 25.99,
        "Address": "Ģertrūdes 135"
    },
    {
        "Price_per_m²": 1266.0,
        "Price": 89900.0,
        "m²": 71.01,
        "Address": "Bruņinieku 52"
    },
    {
        "Price_per_m²": 973.0,
        "Price": 110900.0,
        "m²": 113.98,
        "Address": "Stabu 81A"
    },
    {
        "Price_per_m²": 2330.0,
        "Price": 41940.0,
        "m²": 18.0,
        "Address": "Bruņinieku 121"
    },
    {
        "Price_per_m²": 1302.0,
        "Price": 56000.0,
        "m²": 43.01,
        "Address": "Bruņinieku 73"
    },
    {
        "Price_per_m²": 1686.0,
        "Price": 118000.0,
        "m²": 69.99,
        "Address": "Stabu 81"
    },
    {
        "Price_per_m²": 2831.0,
        "Price": 130245.0,
        "m²": 46.01,
        "Address": "Stabu 87a"
    },
    {
        "Price_per_m²": 1575.0,
        "Price": 149650.0,
        "m²": 95.02,
        "Address": "Stabu 29"
    },
    {
        "Price_per_m²": 280.0,
        "Price": 49000.0,
        "m²": 175.0,
        "Address": "Stabu 20"
    },
    {
        "Price_per_m²": 1550.0,
        "Price": 46500.0,
        "m²": 30.0,
        "Address": "Bruņinieku 89"
    },
    {
        "Price_per_m²": 1346.0,
        "Price": 35000.0,
        "m²": 26.0,
        "Address": "Ģertrūdes 9"
    },
    {
        "Price_per_m²": 915.0,
        "Price": 37500.0,
        "m²": 40.98,
        "Address": "Artilērijas 56"
    },
    {
        "Price_per_m²": 2200.0,
        "Price": 110000.0,
        "m²": 50.0,
        "Address": "Artilērijas 25"
    },
    {
        "Price_per_m²": 2963.0,
        "Price": 240000.0,
        "m²": 81.0,
        "Address": "Ģertrūdes 23"
    },
    {
        "Price_per_m²": 2310.0,
        "Price": 67000.0,
        "m²": 29.0,
        "Address": "Matīsa 29"
    },
    {
        "Price_per_m²": 1026.0,
        "Price": 29750.0,
        "m²": 29.0,
        "Address": "Lienes 25A"
    },
    {
        "Price_per_m²": 1962.0,
        "Price": 102000.0,
        "m²": 51.99,
        "Address": "Stabu 61"
    },
    {
        "Price_per_m²": 799.0,
        "Price": 42350.0,
        "m²": 53.0,
        "Address": "Lāčplēša 104 A"
    },
    {
        "Price_per_m²": 1419.0,
        "Price": 44000.0,
        "m²": 31.01,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1899.0,
        "Price": 149995.0,
        "m²": 78.99,
        "Address": "Ģertrūdes 106"
    },
    {
        "Price_per_m²": 2006.0,
        "Price": 341000.0,
        "m²": 169.99,
        "Address": "Ģertrūdes 9"
    },
    {
        "Price_per_m²": 1700.0,
        "Price": 345000.0,
        "m²": 202.94,
        "Address": "Ģertrūdes 22"
    },
    {
        "Price_per_m²": 853.0,
        "Price": 29000.0,
        "m²": 34.0,
        "Address": "Bruņinieku 93a"
    },
    {
        "Price_per_m²": 1266.0,
        "Price": 89900.0,
        "m²": 71.01,
        "Address": "Bruņinieku 52"
    },
    {
        "Price_per_m²": 2769.0,
        "Price": 36000.0,
        "m²": 13.0,
        "Address": "Ģertrūdes 70"
    },
    {
        "Price_per_m²": 1238.0,
        "Price": 26000.0,
        "m²": 21.0,
        "Address": "Artilērijas 59"
    },
    {
        "Price_per_m²": 2565.0,
        "Price": 59000.0,
        "m²": 23.0,
        "Address": "Ģertrūdes 70"
    },
    {
        "Price_per_m²": 2396.0,
        "Price": 115000.0,
        "m²": 48.0,
        "Address": "Krāsotāju 11"
    },
    {
        "Price_per_m²": 1599.0,
        "Price": 119900.0,
        "m²": 74.98,
        "Address": "Bruņinieku 42"
    },
    {
        "Price_per_m²": 1927.0,
        "Price": 119500.0,
        "m²": 62.01,
        "Address": "Avotu 8k1"
    },
    {
        "Price_per_m²": 155.0,
        "Price": 49000.0,
        "m²": 316.13,
        "Address": "Lāčplēša 54"
    },
    {
        "Price_per_m²": 1197.0,
        "Price": 73000.0,
        "m²": 60.99,
        "Address": "Stabu 104"
    },
    {
        "Price_per_m²": 736.0,
        "Price": 39000.0,
        "m²": 52.99,
        "Address": "Lāčplēša 104a"
    },
    {
        "Price_per_m²": 1541.0,
        "Price": 114000.0,
        "m²": 73.98,
        "Address": "Stabu 61k2"
    },
    {
        "Price_per_m²": 1008.0,
        "Price": 110900.0,
        "m²": 110.02,
        "Address": "Stabu 81"
    },
    {
        "Price_per_m²": 1686.0,
        "Price": 118000.0,
        "m²": 69.99,
        "Address": "Stabu 81"
    },
    {
        "Price_per_m²": 1702.0,
        "Price": 80000.0,
        "m²": 47.0,
        "Address": "Bruņinieku 121"
    },
    {
        "Price_per_m²": 1684.0,
        "Price": 144800.0,
        "m²": 85.99,
        "Address": "Stabu 61k2"
    },
    {
        "Price_per_m²": 2159.0,
        "Price": 149000.0,
        "m²": 69.01,
        "Address": "Ģertrūdes 62"
    },
    {
        "Price_per_m²": 1413.0,
        "Price": 65000.0,
        "m²": 46.0,
        "Address": "Avotu 66"
    },
    {
        "Price_per_m²": 1593.0,
        "Price": 309000.0,
        "m²": 193.97,
        "Address": "Artilērijas 33"
    },
    {
        "Price_per_m²": 2737.0,
        "Price": 156000.0,
        "m²": 57.0,
        "Address": "Matīsa 69"
    },
    {
        "Price_per_m²": 1900.0,
        "Price": 114000.0,
        "m²": 60.0,
        "Address": "Valmieras 20"
    },
    {
        "Price_per_m²": 1433.0,
        "Price": 34400.0,
        "m²": 24.01,
        "Address": "Bruņinieku 93"
    },
    {
        "Price_per_m²": 875.0,
        "Price": 28000.0,
        "m²": 32.0,
        "Address": "Avotu 9"
    },
    {
        "Price_per_m²": 1143.0,
        "Price": 48000.0,
        "m²": 41.99,
        "Address": "Ādmiņu 8"
    },
    {
        "Price_per_m²": 2330.0,
        "Price": 41940.0,
        "m²": 18.0,
        "Address": "Bruņinieku 121"
    },
    {
        "Price_per_m²": 2500.0,
        "Price": 70000.0,
        "m²": 28.0,
        "Address": "Krāsotāju 13a"
    },
    {
        "Price_per_m²": 2196.0,
        "Price": 50500.0,
        "m²": 23.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 2143.0,
        "Price": 225000.0,
        "m²": 104.99,
        "Address": "Bruņinieku 38"
    },
    {
        "Price_per_m²": 2679.0,
        "Price": 225000.0,
        "m²": 83.99,
        "Address": "Stabu 93"
    },
    {
        "Price_per_m²": 1034.0,
        "Price": 30000.0,
        "m²": 29.01,
        "Address": "Lienes 25A"
    },
    {
        "Price_per_m²": 1290.0,
        "Price": 25800.0,
        "m²": 20.0,
        "Address": "Ģertrūdes 91a"
    },
    {
        "Price_per_m²": 1393.0,
        "Price": 58500.0,
        "m²": 42.0,
        "Address": "Bruņinieku 92"
    },
    {
        "Price_per_m²": 1709.0,
        "Price": 135000.0,
        "m²": 78.99,
        "Address": "Artilērijas 7"
    },
    {
        "Price_per_m²": 2500.0,
        "Price": 45000.0,
        "m²": 18.0,
        "Address": "Bruņinieku 121"
    },
    {
        "Price_per_m²": 2216.0,
        "Price": 82000.0,
        "m²": 37.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 1904.0,
        "Price": 99000.0,
        "m²": 52.0,
        "Address": "Valmieras 39b"
    },
    {
        "Price_per_m²": 1871.0,
        "Price": 65500.0,
        "m²": 35.01,
        "Address": "Ģertrūdes 106"
    },
    {
        "Price_per_m²": 1857.0,
        "Price": 39000.0,
        "m²": 21.0,
        "Address": "Bruņinieku 1"
    },
    {
        "Price_per_m²": 2037.0,
        "Price": 110000.0,
        "m²": 54.0,
        "Address": "Ģertrūdes 67A"
    },
    {
        "Price_per_m²": 2813.0,
        "Price": 180000.0,
        "m²": 63.99,
        "Address": "Artilērijas 65"
    },
    {
        "Price_per_m²": 1800.0,
        "Price": 90000.0,
        "m²": 50.0,
        "Address": "Avotu 73"
    },
    {
        "Price_per_m²": 2134.0,
        "Price": 350000.0,
        "m²": 164.01,
        "Address": "Ģertrūdes 9"
    },
    {
        "Price_per_m²": 1302.0,
        "Price": 56000.0,
        "m²": 43.01,
        "Address": "Bruņinieku 73"
    },
    {
        "Price_per_m²": 958.0,
        "Price": 46000.0,
        "m²": 48.02,
        "Address": "Visvalža 3a"
    },
    {
        "Price_per_m²": 2596.0,
        "Price": 122000.0,
        "m²": 47.0,
        "Address": "Bruņinieku 49"
    },
    {
        "Price_per_m²": 1600.0,
        "Price": 112000.0,
        "m²": 70.0,
        "Address": "Stabu 87"
    },
    {
        "Price_per_m²": 957.0,
        "Price": 22000.0,
        "m²": 22.99,
        "Address": "Matīsa 82a"
    },
    {
        "Price_per_m²": 2011.0,
        "Price": 380000.0,
        "m²": 188.96,
        "Address": "Matīsa 69"
    },
    {
        "Price_per_m²": 1707.0,
        "Price": 128000.0,
        "m²": 74.99,
        "Address": "Bruņinieku 42"
    },
    {
        "Price_per_m²": 1747.0,
        "Price": 111807.0,
        "m²": 64.0,
        "Address": "Avotu 46a"
    },
    {
        "Price_per_m²": 1686.0,
        "Price": 118000.0,
        "m²": 69.99,
        "Address": "Stabu 81"
    },
    {
        "Price_per_m²": 1500.0,
        "Price": 30000.0,
        "m²": 20.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1287.0,
        "Price": 193000.0,
        "m²": 149.96,
        "Address": "Lāčplēša 62"
    },
    {
        "Price_per_m²": 1627.0,
        "Price": 96000.0,
        "m²": 59.0,
        "Address": "Matīsa 27"
    },
    {
        "Price_per_m²": 2000.0,
        "Price": 110000.0,
        "m²": 55.0,
        "Address": "Stabu 84"
    },
    {
        "Price_per_m²": 2059.0,
        "Price": 35000.0,
        "m²": 17.0,
        "Address": "Ģertrūdes 135"
    },
    {
        "Price_per_m²": 2312.0,
        "Price": 215000.0,
        "m²": 92.99,
        "Address": "Matīsa 69"
    },
    {
        "Price_per_m²": 1500.0,
        "Price": 120000.0,
        "m²": 80.0,
        "Address": "Stabu 91"
    },
    {
        "Price_per_m²": 1986.0,
        "Price": 69500.0,
        "m²": 34.99,
        "Address": "Satekles 15"
    },
    {
        "Price_per_m²": 1764.0,
        "Price": 179900.0,
        "m²": 101.98,
        "Address": "Bruņinieku 87"
    },
    {
        "Price_per_m²": 1904.0,
        "Price": 99000.0,
        "m²": 52.0,
        "Address": "Stabu 20"
    },
    {
        "Price_per_m²": 2281.0,
        "Price": 109480.0,
        "m²": 48.0,
        "Address": "Bruņinieku 85"
    },
    {
        "Price_per_m²": 1358.0,
        "Price": 220000.0,
        "m²": 162.0,
        "Address": "Ģertrūdes 3"
    },
    {
        "Price_per_m²": 857.0,
        "Price": 24000.0,
        "m²": 28.0,
        "Address": "Vagonu 24"
    },
    {
        "Price_per_m²": 1358.0,
        "Price": 72000.0,
        "m²": 53.02,
        "Address": "Stabu 49"
    },
    {
        "Price_per_m²": 1297.0,
        "Price": 96000.0,
        "m²": 74.02,
        "Address": "Lāčplēša 80"
    },
    {
        "Price_per_m²": 723.0,
        "Price": 18800.0,
        "m²": 26.0,
        "Address": "Ģertrūdes 91A"
    },
    {
        "Price_per_m²": 630.0,
        "Price": 14500.0,
        "m²": 23.02,
        "Address": "Matīsa 131"
    },
    {
        "Price_per_m²": 2090.0,
        "Price": 209000.0,
        "m²": 100.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 2041.0,
        "Price": 149000.0,
        "m²": 73.0,
        "Address": "Matīsa 46"
    },
    {
        "Price_per_m²": 1785.0,
        "Price": 116000.0,
        "m²": 64.99,
        "Address": "Artilērijas 8"
    },
    {
        "Price_per_m²": 985.0,
        "Price": 120170.0,
        "m²": 122.0,
        "Address": "Artilērijas 46"
    },
    {
        "Price_per_m²": 1686.0,
        "Price": 118000.0,
        "m²": 69.99,
        "Address": "Stabu 81"
    },
    {
        "Price_per_m²": 3857.0,
        "Price": 135000.0,
        "m²": 35.0,
        "Address": "Avotu 4"
    },
    {
        "Price_per_m²": 1474.0,
        "Price": 89900.0,
        "m²": 60.99,
        "Address": "Lāčplēša 116"
    },
    {
        "Price_per_m²": 1400.0,
        "Price": 49000.0,
        "m²": 35.0,
        "Address": "Matīsa 115"
    },
    {
        "Price_per_m²": 1230.0,
        "Price": 75000.0,
        "m²": 60.98,
        "Address": "Stabu 104"
    },
    {
        "Price_per_m²": 2130.0,
        "Price": 115000.0,
        "m²": 53.99,
        "Address": "Artilērijas 71a"
    },
    {
        "Price_per_m²": 1675.0,
        "Price": 340000.0,
        "m²": 202.99,
        "Address": "Ģertrūdes 22"
    },
    {
        "Price_per_m²": 1788.0,
        "Price": 71500.0,
        "m²": 39.99,
        "Address": "Matīsa 41"
    },
    {
        "Price_per_m²": 1723.0,
        "Price": 112000.0,
        "m²": 65.0,
        "Address": "Ģertrūdes 100"
    },
    {
        "Price_per_m²": 2347.0,
        "Price": 39900.0,
        "m²": 17.0,
        "Address": "Lāčplēša 113"
    },
    {
        "Price_per_m²": 1626.0,
        "Price": 69900.0,
        "m²": 42.99,
        "Address": "Matīsa 19"
    },
    {
        "Price_per_m²": 2333.0,
        "Price": 98000.0,
        "m²": 42.01,
        "Address": "Ģertrūdes 70"
    },
    {
        "Price_per_m²": 2000.0,
        "Price": 90000.0,
        "m²": 45.0,
        "Address": "Krāsotāju 24"
    },
    {
        "Price_per_m²": 1396.0,
        "Price": 74000.0,
        "m²": 53.01,
        "Address": "Ģertrūdes 113"
    },
    {
        "Price_per_m²": 1691.0,
        "Price": 94700.0,
        "m²": 56.0,
        "Address": "Stabu 87A"
    },
    {
        "Price_per_m²": 2000.0,
        "Price": 180000.0,
        "m²": 90.0,
        "Address": "Valmieras 28"
    },
    {
        "Price_per_m²": 1296.0,
        "Price": 92000.0,
        "m²": 70.99,
        "Address": "Lāčplēša 80"
    },
    {
        "Price_per_m²": 2850.0,
        "Price": 125400.0,
        "m²": 44.0,
        "Address": "Avotu 46A"
    },
    {
        "Price_per_m²": 1468.0,
        "Price": 69000.0,
        "m²": 47.0,
        "Address": "Stabu 33"
    },
    {
        "Price_per_m²": 643.0,
        "Price": 37950.0,
        "m²": 59.02,
        "Address": "Vagonu 24"
    },
    {
        "Price_per_m²": 1500.0,
        "Price": 87000.0,
        "m²": 58.0,
        "Address": "Ādmiņu 5-30/31"
    },
    {
        "Price_per_m²": 2600.0,
        "Price": 169000.0,
        "m²": 65.0,
        "Address": "Matīsa 29"
    },
    {
        "Price_per_m²": 2596.0,
        "Price": 148000.0,
        "m²": 57.01,
        "Address": "Matīsa 29"
    },
    {
        "Price_per_m²": 2393.0,
        "Price": 67000.0,
        "m²": 28.0,
        "Address": "Matīsa 29"
    },
    {
        "Price_per_m²": 2850.0,
        "Price": 125400.0,
        "m²": 44.0,
        "Address": "Avotu 46A"
    },
    {
        "Price_per_m²": 2221.0,
        "Price": 139950.0,
        "m²": 63.01,
        "Address": "Avotu 46"
    },
    {
        "Price_per_m²": 1881.0,
        "Price": 79000.0,
        "m²": 42.0,
        "Address": "Artilērijas 56"
    },
    {
        "Price_per_m²": 2297.0,
        "Price": 84999.0,
        "m²": 37.0,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 1559.0,
        "Price": 159000.0,
        "m²": 101.99,
        "Address": "Stabu 2"
    },
    {
        "Price_per_m²": 1405.0,
        "Price": 59000.0,
        "m²": 41.99,
        "Address": "Artilērijas 19"
    },
    {
        "Price_per_m²": 2500.0,
        "Price": 105000.0,
        "m²": 42.0,
        "Address": "Artilērijas 24"
    },
    {
        "Price_per_m²": 2232.0,
        "Price": 125000.0,
        "m²": 56.0,
        "Address": "Ģertrūdes 30"
    },
    {
        "Price_per_m²": 1113.0,
        "Price": 67900.0,
        "m²": 61.01,
        "Address": "Artilērijas 66B"
    },
    {
        "Price_per_m²": 1780.0,
        "Price": 219000.0,
        "m²": 123.03,
        "Address": "Ģertrūdes 37"
    },
    {
        "Price_per_m²": 1944.0,
        "Price": 52500.0,
        "m²": 27.01,
        "Address": "Lāčplēša 117"
    },
    {
        "Price_per_m²": 1705.0,
        "Price": 75000.0,
        "m²": 43.99,
        "Address": "Ģertrūdes 69"
    },
    {
        "Price_per_m²": 833.0,
        "Price": 20000.0,
        "m²": 24.01,
        "Address": "Lienes 17"
    },
    {
        "Price_per_m²": 2647.0,
        "Price": 153500.0,
        "m²": 57.99,
        "Address": "Artilērijas 11"
    },
    {
        "Price_per_m²": 942.0,
        "Price": 49000.0,
        "m²": 52.02,
        "Address": "Lāčplēša 104a"
    },
    {
        "Price_per_m²": 12295.0,
        "Price": 750000.0,
        "m²": 61.0,
        "Address": "Stabu 104"
    },
    {
        "Price_per_m²": 1402.0,
        "Price": 129000.0,
        "m²": 92.01,
        "Address": "Artilērijas 3"
    },
    {
        "Price_per_m²": 1049.0,
        "Price": 128000.0,
        "m²": 122.02,
        "Address": "Artilērijas 46"
    },
    {
        "Price_per_m²": 1700.0,
        "Price": 193800.0,
        "m²": 114.0,
        "Address": "Bruņinieku 8A"
    },
    {
        "Price_per_m²": 2049.0,
        "Price": 125000.0,
        "m²": 61.01,
        "Address": "Artilērijas 11"
    },
    {
        "Price_per_m²": 1345.0,
        "Price": 74000.0,
        "m²": 55.02,
        "Address": "Avotu 8"
    },
    {
        "Price_per_m²": 1408.0,
        "Price": 100000.0,
        "m²": 71.02,
        "Address": "Lāčplēša 80"
    },
    {
        "Price_per_m²": 1900.0,
        "Price": 209000.0,
        "m²": 110.0,
        "Address": "Matīsa 17"
    },
    {
        "Price_per_m²": 1769.0,
        "Price": 230000.0,
        "m²": 130.02,
        "Address": "Ģertrūdes 103"
    },
    {
        "Price_per_m²": 1636.0,
        "Price": 90000.0,
        "m²": 55.01,
        "Address": "Ģertrūdes 103"
    },
    {
        "Price_per_m²": 2250.0,
        "Price": 27000.0,
        "m²": 12.0,
        "Address": "Bruņinieku 93A"
    },
    {
        "Price_per_m²": 2079.0,
        "Price": 185000.0,
        "m²": 88.99,
        "Address": "Stabu 29"
    },
    {
        "Price_per_m²": 2366.0,
        "Price": 220000.0,
        "m²": 92.98,
        "Address": "Matīsa 65"
    },
    {
        "Price_per_m²": 1572.0,
        "Price": 95900.0,
        "m²": 61.01,
        "Address": "Lāčplēša 116"
    },
    {
        "Price_per_m²": 1742.0,
        "Price": 95830.0,
        "m²": 55.01,
        "Address": "Stabu 87A"
    },
    {
        "Price_per_m²": 807.0,
        "Price": 33900.0,
        "m²": 42.01,
        "Address": "Stabu 45"
    },
    {
        "Price_per_m²": 1395.0,
        "Price": 60000.0,
        "m²": 43.01,
        "Address": "Stabu 87A"
    },
    {
        "Price_per_m²": 1900.0,
        "Price": 209000.0,
        "m²": 110.0,
        "Address": "Matīsa 17"
    },
    {
        "Price_per_m²": 500.0,
        "Price": 210000.0,
        "m²": 420.0,
        "Address": "Krāsotāju 9"
    },
    {
        "Price_per_m²": 1900.0,
        "Price": 190000.0,
        "m²": 100.0,
        "Address": "Matīsa 41"
    },
    {
        "Price_per_m²": 1742.0,
        "Price": 95830.0,
        "m²": 55.01,
        "Address": "Stabu 87A"
    },
    {
        "Price_per_m²": 1524.0,
        "Price": 32000.0,
        "m²": 21.0,
        "Address": "Matīsa 84"
    },
    {
        "Price_per_m²": 2190.0,
        "Price": 219000.0,
        "m²": 100.0,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 1577.0,
        "Price": 82000.0,
        "m²": 52.0,
        "Address": "Krāsotāju 18"
    },
    {
        "Price_per_m²": 1778.0,
        "Price": 208000.0,
        "m²": 116.99,
        "Address": "Lāčplēša 51"
    },
    {
        "Price_per_m²": 1780.0,
        "Price": 89000.0,
        "m²": 50.0,
        "Address": "Matīsa 45"
    },
    {
        "Price_per_m²": 1545.0,
        "Price": 170000.0,
        "m²": 110.03,
        "Address": "Stabu 92"
    },
    {
        "Price_per_m²": 2201.0,
        "Price": 162888.0,
        "m²": 74.01,
        "Address": "Pļavas 4"
    },
    {
        "Price_per_m²": 2324.0,
        "Price": 165000.0,
        "m²": 71.0,
        "Address": "Stabu 54"
    },
    {
        "Price_per_m²": 1154.0,
        "Price": 45000.0,
        "m²": 38.99,
        "Address": "Ģertrūdes 53"
    },
    {
        "Price_per_m²": 833.0,
        "Price": 20000.0,
        "m²": 24.01,
        "Address": "Lienes 17"
    },
    {
        "Price_per_m²": 1600.0,
        "Price": 120000.0,
        "m²": 75.0,
        "Address": "Ģertrūdes 71"
    },
    {
        "Price_per_m²": 1666.0,
        "Price": 144900.0,
        "m²": 86.97,
        "Address": "Stabu 61"
    },
    {
        "Price_per_m²": 1766.0,
        "Price": 219000.0,
        "m²": 124.01,
        "Address": "Ģertrūdes 37"
    },
    {
        "Price_per_m²": 1369.0,
        "Price": 89000.0,
        "m²": 65.01,
        "Address": "Ģertrūdes 62A"
    },
    {
        "Price_per_m²": 2611.0,
        "Price": 47000.0,
        "m²": 18.0,
        "Address": "Artilērijas 25"
    },
    {
        "Price_per_m²": 1714.0,
        "Price": 36000.0,
        "m²": 21.0,
        "Address": "Matīsa 59"
    },
    {
        "Price_per_m²": 2556.0,
        "Price": 132900.0,
        "m²": 52.0,
        "Address": "Stabu 49A"
    },
    {
        "Price_per_m²": 2500.0,
        "Price": 70000.0,
        "m²": 28.0,
        "Address": "Krāsotāju 13"
    },
    {
        "Price_per_m²": 1827.0,
        "Price": 169900.0,
        "m²": 92.99,
        "Address": "Stabu 92"
    },
    {
        "Price_per_m²": 2168.0,
        "Price": 127900.0,
        "m²": 58.99,
        "Address": "Stabu 95"
    },
    {
        "Price_per_m²": 2280.0,
        "Price": 57000.0,
        "m²": 25.0,
        "Address": "Bruņinieku 121"
    },
    {
        "Price_per_m²": 1342.0,
        "Price": 34900.0,
        "m²": 26.01,
        "Address": "Krāsotāju 25a"
    },
    {
        "Price_per_m²": 2844.0,
        "Price": 139365.0,
        "m²": 49.0,
        "Address": "Stabu 87a"
    },
    {
        "Price_per_m²": 1762.0,
        "Price": 119800.0,
        "m²": 67.99,
        "Address": "Ģertrūdes 113"
    },
    {
        "Price_per_m²": 2481.0,
        "Price": 129000.0,
        "m²": 52.0,
        "Address": "Stabu 49A"
    },
    {
        "Price_per_m²": 1600.0,
        "Price": 198400.0,
        "m²": 124.0,
        "Address": "Avotu 3"
    },
    {
        "Price_per_m²": 1400.0,
        "Price": 63000.0,
        "m²": 45.0,
        "Address": "Stabu 116"
    },
    {
        "Price_per_m²": 2389.0,
        "Price": 215000.0,
        "m²": 90.0,
        "Address": "Ģertrūdes 62"
    },
    {
        "Price_per_m²": 2000.0,
        "Price": 168000.0,
        "m²": 84.0,
        "Address": "Ģertrūdes 19"
    },
    {
        "Price_per_m²": 1238.0,
        "Price": 26000.0,
        "m²": 21.0,
        "Address": "Artilērijas 59"
    },
    {
        "Price_per_m²": 1844.0,
        "Price": 83000.0,
        "m²": 45.01,
        "Address": "Matīsa 83"
    },
    {
        "Price_per_m²": 1579.0,
        "Price": 150000.0,
        "m²": 95.0,
        "Address": "Avotu 35"
    },
    {
        "Price_per_m²": 1782.0,
        "Price": 139000.0,
        "m²": 78.0,
        "Address": "Stabu 23"
    },
    {
        "Price_per_m²": 745.0,
        "Price": 39500.0,
        "m²": 53.02,
        "Address": "Lāčplēša 104A"
    },
    {
        "Price_per_m²": 1200.0,
        "Price": 56400.0,
        "m²": 47.0,
        "Address": "Ādmiņu 8"
    },
    {
        "Price_per_m²": 1850.0,
        "Price": 111000.0,
        "m²": 60.0,
        "Address": "Ģertrūdes 22"
    },
    {
        "Price_per_m²": 1663.0,
        "Price": 49900.0,
        "m²": 30.01,
        "Address": "Ģertrūdes 99 k"
    },
    {
        "Price_per_m²": 1000.0,
        "Price": 240000.0,
        "m²": 240.0,
        "Address": "Stabu 56"
    },
    {
        "Price_per_m²": 1639.0,
        "Price": 100000.0,
        "m²": 61.01,
        "Address": "Lāčplēša 116"
    },
    {
        "Price_per_m²": 2319.0,
        "Price": 83500.0,
        "m²": 36.01,
        "Address": "Matīsa 101"
    },
    {
        "Price_per_m²": 2603.0,
        "Price": 164000.0,
        "m²": 63.0,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 1250.0,
        "Price": 82500.0,
        "m²": 66.0,
        "Address": "Lāčplēša 23"
    },
    {
        "Price_per_m²": 1107.0,
        "Price": 80800.0,
        "m²": 72.99,
        "Address": "Lāčplēša 104"
    },
    {
        "Price_per_m²": 661.0,
        "Price": 55500.0,
        "m²": 83.96,
        "Address": "Lāčplēša 104"
    },
    {
        "Price_per_m²": 1829.0,
        "Price": 128000.0,
        "m²": 69.98,
        "Address": "Stabu 81"
    },
    {
        "Price_per_m²": 1205.0,
        "Price": 79519.0,
        "m²": 65.99,
        "Address": "Stabu 49a"
    },
    {
        "Price_per_m²": 1286.0,
        "Price": 169794.0,
        "m²": 132.03,
        "Address": "Lāčplēša 35"
    },
    {
        "Price_per_m²": 917.0,
        "Price": 22000.0,
        "m²": 23.99,
        "Address": "Lienes 17"
    },
    {
        "Price_per_m²": 2141.0,
        "Price": 119870.0,
        "m²": 55.99,
        "Address": "Ģertrūdes 55c"
    },
    {
        "Price_per_m²": 2315.0,
        "Price": 62500.0,
        "m²": 27.0,
        "Address": "Lāčplēša 119"
    },
    {
        "Price_per_m²": 1300.0,
        "Price": 141700.0,
        "m²": 109.0,
        "Address": "Ādmiņu 8"
    },
    {
        "Price_per_m²": 2544.0,
        "Price": 229000.0,
        "m²": 90.02,
        "Address": "Artilērijas 15"
    },
    {
        "Price_per_m²": 163.0,
        "Price": 49000.0,
        "m²": 300.61,
        "Address": "Bruņinieku 89"
    },
    {
        "Price_per_m²": 1881.0,
        "Price": 174900.0,
        "m²": 92.98,
        "Address": "Stabu 92"
    },
    {
        "Price_per_m²": 1803.0,
        "Price": 110000.0,
        "m²": 61.01,
        "Address": "Lāčplēša 116"
    },
    {
        "Price_per_m²": 2589.0,
        "Price": 69900.0,
        "m²": 27.0,
        "Address": "Sparģeļu 10"
    },
    {
        "Price_per_m²": 2633.0,
        "Price": 42120.0,
        "m²": 16.0,
        "Address": "Ģertrūdes 70"
    },
    {
        "Price_per_m²": 1431.0,
        "Price": 114500.0,
        "m²": 80.01,
        "Address": "Stabu 57"
    },
    {
        "Price_per_m²": 1491.0,
        "Price": 170000.0,
        "m²": 114.02,
        "Address": "Lāčplēša 47"
    },
    {
        "Price_per_m²": 1221.0,
        "Price": 74500.0,
        "m²": 61.02,
        "Address": "Stabu 57B"
    },
    {
        "Price_per_m²": 1689.0,
        "Price": 76000.0,
        "m²": 45.0,
        "Address": "Avotu 73"
    },
    {
        "Price_per_m²": 1579.0,
        "Price": 120000.0,
        "m²": 76.0,
        "Address": "Bruņinieku 52"
    },
    {
        "Price_per_m²": 1333.0,
        "Price": 52000.0,
        "m²": 39.01,
        "Address": "Ģertrūdes 99"
    },
    {
        "Price_per_m²": 724.0,
        "Price": 55000.0,
        "m²": 75.97,
        "Address": "Valmieras 22"
    },
    {
        "Price_per_m²": 1358.0,
        "Price": 220000.0,
        "m²": 162.0,
        "Address": "Ģertrūdes X"
    },
    {
        "Price_per_m²": 1042.0,
        "Price": 50000.0,
        "m²": 47.98,
        "Address": "Visvalža 3a"
    },
    {
        "Price_per_m²": 1964.0,
        "Price": 165000.0,
        "m²": 84.01,
        "Address": "Stabu 29"
    },
    {
        "Price_per_m²": 1500.0,
        "Price": 37498.0,
        "m²": 25.0,
        "Address": "Krāsotāju 13"
    },
    {
        "Price_per_m²": 1262.0,
        "Price": 26500.0,
        "m²": 21.0,
        "Address": "Artilērijas 59"
    },
    {
        "Price_per_m²": 1500.0,
        "Price": 64500.0,
        "m²": 43.0,
        "Address": "Bruņinieku 73"
    },
    {
        "Price_per_m²": 1185.0,
        "Price": 77000.0,
        "m²": 64.98,
        "Address": "Matīsa 27"
    },
    {
        "Price_per_m²": 1472.0,
        "Price": 78000.0,
        "m²": 52.99,
        "Address": "Ģertrūdes 113"
    },
    {
        "Price_per_m²": 1188.0,
        "Price": 49900.0,
        "m²": 42.0,
        "Address": "Bruņinieku 64"
    },
    {
        "Price_per_m²": 1855.0,
        "Price": 230000.0,
        "m²": 123.99,
        "Address": "Ģertrūdes 37"
    },
    {
        "Price_per_m²": 1723.0,
        "Price": 112000.0,
        "m²": 65.0,
        "Address": "Ģertrūdes 100"
    },
    {
        "Price_per_m²": 2680.0,
        "Price": 260000.0,
        "m²": 97.01,
        "Address": "Artilērijas 65"
    },
    {
        "Price_per_m²": 1286.0,
        "Price": 135000.0,
        "m²": 104.98,
        "Address": "Lāčplēša 62"
    },
    {
        "Price_per_m²": 1619.0,
        "Price": 68000.0,
        "m²": 42.0,
        "Address": "Matīsa 121"
    },
    {
        "Price_per_m²": 2671.0,
        "Price": 74790.0,
        "m²": 28.0,
        "Address": "Ģertrūdes 70"
    },
    {
        "Price_per_m²": 2775.0,
        "Price": 99900.0,
        "m²": 36.0,
        "Address": "Sparģeļu 10"
    },
    {
        "Price_per_m²": 2633.0,
        "Price": 42120.0,
        "m²": 16.0,
        "Address": "Ģertrūdes 70"
    },
    {
        "Price_per_m²": 1942.0,
        "Price": 200000.0,
        "m²": 102.99,
        "Address": "Lāčplēša 17"
    },
    {
        "Price_per_m²": 1548.0,
        "Price": 65000.0,
        "m²": 41.99,
        "Address": "Matīsa 41"
    },
    {
        "Price_per_m²": 861.0,
        "Price": 15500.0,
        "m²": 18.0,
        "Address": "Stabu 55"
    },
    {
        "Price_per_m²": 1788.0,
        "Price": 71500.0,
        "m²": 39.99,
        "Address": "Matīsa 41"
    },
    {
        "Price_per_m²": 1286.0,
        "Price": 27000.0,
        "m²": 21.0,
        "Address": "Artilērijas 59"
    },
    {
        "Price_per_m²": 1655.0,
        "Price": 48000.0,
        "m²": 29.0,
        "Address": "Krāsotāju 25"
    },
    {
        "Price_per_m²": 1622.0,
        "Price": 159000.0,
        "m²": 98.03,
        "Address": "Avotu 20A"
    },
    {
        "Price_per_m²": 1950.0,
        "Price": 78000.0,
        "m²": 40.0,
        "Address": "Matīsa 93"
    },
    {
        "Price_per_m²": 543.0,
        "Price": 67900.0,
        "m²": 125.05,
        "Address": "Bruņinieku 52"
    },
    {
        "Price_per_m²": 1578.0,
        "Price": 161000.0,
        "m²": 102.03,
        "Address": "Stabu 2"
    },
    {
        "Price_per_m²": 2037.0,
        "Price": 167000.0,
        "m²": 81.98,
        "Address": "Bruņinieku 45"
    },
    {
        "Price_per_m²": 1491.0,
        "Price": 170000.0,
        "m²": 114.02,
        "Address": "Lāčplēša 47"
    },
    {
        "Price_per_m²": 1107.0,
        "Price": 80800.0,
        "m²": 72.99,
        "Address": "Lāčplēša 104"
    },
    {
        "Price_per_m²": 958.0,
        "Price": 23000.0,
        "m²": 24.01,
        "Address": "Lienes 17"
    },
    {
        "Price_per_m²": 2650.0,
        "Price": 106000.0,
        "m²": 40.0,
        "Address": "Stabu 49a"
    },
    {
        "Price_per_m²": 1573.0,
        "Price": 140000.0,
        "m²": 89.0,
        "Address": "Ģertrūdes 22"
    },
    {
        "Price_per_m²": 1221.0,
        "Price": 74500.0,
        "m²": 61.02,
        "Address": "Stabu 57b"
    },
    {
        "Price_per_m²": 2600.0,
        "Price": 52000.0,
        "m²": 20.0,
        "Address": "Valmieras 28"
    },
    {
        "Price_per_m²": 1719.0,
        "Price": 110000.0,
        "m²": 63.99,
        "Address": "Ģertrūdes 103"
    },
    {
        "Price_per_m²": 2314.0,
        "Price": 99500.0,
        "m²": 43.0,
        "Address": "Stabu 87"
    },
    {
        "Price_per_m²": 2831.0,
        "Price": 130245.0,
        "m²": 46.01,
        "Address": "Stabu 87A"
    },
    {
        "Price_per_m²": 1825.0,
        "Price": 104000.0,
        "m²": 56.99,
        "Address": "Bruņinieku 87"
    },
    {
        "Price_per_m²": 1236.0,
        "Price": 127277.0,
        "m²": 102.97,
        "Address": "Stabu 49a"
    },
    {
        "Price_per_m²": 1231.0,
        "Price": 66500.0,
        "m²": 54.02,
        "Address": "Kurbada 1А"
    },
    {
        "Price_per_m²": 1567.0,
        "Price": 94000.0,
        "m²": 59.99,
        "Address": "Matīsa 93"
    },
    {
        "Price_per_m²": 1288.0,
        "Price": 94000.0,
        "m²": 72.98,
        "Address": "Avotu 43"
    }
]


data2 = data

# Extract data from "one_time_purchase"
one_time_data = data2

# Prepare the m² and Price data for plotting
m2_values = [entry["m²"] for entry in one_time_data]
price_values = [entry["Price"] for entry in one_time_data]

# Create the plot
plt.figure(figsize=(8, 6))
plt.scatter(m2_values, price_values, color='blue', marker='o')

# Add labels and title
plt.xlabel('m²')
plt.ylabel('cena')
plt.title('Cena pret m² dzīvokļiem, kas atrodas avotos/centrā (dzivokli uz ielām, kuras atrodas abās apkaimēs)')

# Show the plot
plt.grid(True)
plt.show()