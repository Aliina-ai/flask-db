from flask import Flask, render_template, request, url_for, redirect, session, flash, json
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DB_PATH = os.getenv("DB_PATH", "/data/db.sqlite")

USERS = {
    'Аліна':     {'password': 'Gk47fBq2', 'role': 'admin'},
    'Наталія':   {'password': 'qF92KsLm', 'role': 'admin'},
    'Сергій':    {'password': 'xP74gVt1', 'role': 'operator'},
    'Геннадій':  {'password': 'zT38mWc9', 'role': 'operator'},
}

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions_large (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                phone TEXT,
                location TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                large_okrug TEXT,
                district_name TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                address TEXT,
                phone TEXT,
                birth_date TEXT,
                location TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS activists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                large_okrug TEXT,
                okrug TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                address TEXT,
                phone TEXT,
                birth_date TEXT,
                subscribers_count INTEGER,
                newspapers_count INTEGER,
                location TEXT
            )
        ''')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS regions1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions2 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions3 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions4 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS regions5 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions6 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions7 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions8 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions9 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions10 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                district TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        conn.commit()

def get_activists():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, last_name, first_name FROM activists')
    activists = [{'id': row[0], 'name': f"{row[1]} {row[2]}"} for row in c.fetchall()]
    conn.close()
    return activists

def expand_buildings():
    b=[]
    b += [str(i) for i in range(1,5)]
    b.append("77/43")
    b += [str(i) for i in range(139,178)]
    b += [str(i) for i in range(181,186)]
    b += [str(i) for i in range(214,216)]
    b += [str(i) for i in range(228,271)]
    b += ["5","6"]
    b += [str(i) for i in range(89,131)]
    b.append("180")
    b += [str(i) for i in range(219,228)]
    b += [str(i) for i in range(399,404)]
    return b

def get_district_by_building(bld):
    try:
        num = int(bld.split('/')[0])
    except:
        return "Невідомо"
    if num in list(range(1,5)) + [77] + list(range(139,178)) + list(range(181,186)) + list(range(214,216)) + list(range(228,271)):
        return "321097"
    if num in [5,6,180] + list(range(89,131)) + list(range(219,228)) + list(range(399,404)):
        return "321098"
    return "Невідомо"

def get_streets_region2():
    return [
        'вул. Волонтерська',
        'вул. Івана Пулюя',
        'вул. Січневого прориву',
        'вул. Сквирське шосе'
    ]

def expand_buildings2():
    buildings = []

    # вул. Волонтерська
    buildings += [str(i) for i in range(12, 30)]  # 12–29
    buildings += ['27А', '1А', '1', '3', '9']     # інші
    # вул. Івана Пулюя
    buildings += [str(i) for i in range(1, 31)]   # 1–30
    buildings += ['32А', '32']
    # вул. Січневого прориву
    buildings += ['29', '31', '35']
    buildings += ['43', '43А', '43Б', '45', '45А', '47']
    buildings += ['49', '49А', '51', '53', '55', '57', '59', '61']
    # вул. Сквирське шосе
    buildings += [str(i) for i in range(221, 224)]  # 221–223
    buildings += [str(i) for i in range(228, 267)]  # 228–266

    return buildings

def get_district_by_building2(street, building):
    address_data = {
        "вул. Волонтерська": {
            "buildings": ["1", "1А", "3", "9", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "27А", "28", "29"],
            "district": "321100"
        },
        "вул. Івана Пулюя": {
            "buildings": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "32", "32А"],
            "district": "321100"
        },
        "вул. Січневого прориву": {
            "buildings": ["29", "31", "35", "43", "43А", "43Б", "45", "45А", "47", "49", "49А", "51", "53", "55", "57", "59", "61"],
            "district": "321100"
        },
        "вул. Сквирське шосе": {
            "buildings": ["221", "222", "223", "228", "229", "230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "241", "242", "243", "244", "245", "246", "247", "248", "249", "250", "251", "252", "253", "254", "255", "256", "257", "258", "259", "260", "261", "262", "263", "264", "265", "266"],
            "district": "321102"
        }
    }

    if street in address_data and building in address_data[street]["buildings"]:
        return address_data[street]["district"]
    return "Невідомо"

def expand_buildings3():
    return {
        "вул. Січневого прориву": {
            "buildings": ["27", "33", "33А", "33Б", "33/35"],
            "district": "321101"
        },
        "вул. Володимира Антоновича": {
            "buildings": [str(i) for i in range(3, 52)] + ["1/7", "2/9", "16А"],
            "district": "321103"
        },
        "вул. Волонтерська": {
            "buildings": ["4", "5", "6", "7", "8", "11"],
            "district": "321103"
        },
        "вул. Добровольчих батальйонів": {
            "buildings": ["2А", "4", "5", "8", "9", "11", "15", "17/17"],
            "district": "321103"
        },
        "вул. Левка Лук’яненка": {
            "buildings": [str(i) for i in range(1, 31)] + ["18А"],
            "district": "321103"
        },
        "вул. Чехословацька": {
            "buildings": [str(i) for i in range(3, 46)],
            "district": "321103"
        }
    }

def expand_buildings4():
    return {
        "вул. Полковника Коновальця": {
            "buildings": ["3", "3/1", "3/4"] + [str(i) for i in range(4, 11)] + ["12", "27", "29", "31", "104"],
            "district": "321099"
        },
        "вул. Гайова": {
            "buildings": ["3", "4", "5", "7", "7/1", "11", "13", "15/1", "17/2"],
            "district": "321105"
        },
        "вул. Січневого прориву": {
            "buildings": [str(i) for i in range(2, 6)],
            "district": "321105"
        },
        "вул. Сквирське шосе": {
            "buildings": ["39", "41"] + [str(i) for i in range(47, 52)] + [
                "214А", "214Б", "214/2", "216", "216А", "218", "218Б", "220", "224А"
            ],
            "district": "321105"
        },
        "пров. Будівельників": {
            "buildings": ["3", "4", "5", "7", "9", "11"],
            "district": "321105"
        }
    }

def expand_buildings5():
    return {
        "бульв. Олександрійський": {
            "buildings": ["98", "102", "104"],
            "district": "321106"
        },
        "вул. Дачна": {
            "buildings": ["66", "72"],
            "district": "321106"
        },
        "вул. Ігоря Каплуненка": {
            "buildings": ["75", "81"],
            "district": "321106"
        },
        "вул. Клінічна": {
            "buildings": ["4/1", "4/2", "6"],
            "district": "321106"
        },
        "вул. Івана Мазепи": {
            "buildings": [str(i) for i in range(3, 99)] + ["1А", "2/17", "3А", "45А", "45Б", "65А", "67А", "81А", "83А", "85А"],
            "district": "321108"
        },
        "вул. Миру": {
            "buildings": [str(i) for i in range(1, 42)] + ["2А", "20А", "27А"],
            "district": "321108"
        }
    }

def expand_buildings6():
    return {
        "бульв.Олександрійський": {
            "buildings": [
                "54Г", "84", "86", "88", "92"
            ] + [str(i) for i in range(159, 218)] + ["181А", "74", "76", "78", "80", "82"],
            "district": "321107"
        },
        "вул.Гетьмана Сагайдачного": {
            "buildings": [str(i) for i in range(126, 144)] + ["126/6"],
            "district": "321107"
        },
        "вул.Колодязна": {
            "buildings": ["6", "6/147", "11", "13", "17"],
            "district": "321107"
        },
        "пров.Олександрійський": {
            "buildings": ["3", "4", "5/124", "8/133", "10", "12", "14А", "15"],
            "district": "321107"
        },
        "вул.Вячеслава Чорновола": {
            "buildings": ["3", "4/35", "5", "6", "9", "15"],
            "district": "321109"
        },
        "вул.Дачна": {
            "buildings": [str(i) for i in range(5, 45)],
            "district": "321109"
        },
        "вул.Ігоря Каплуненка": {
            "buildings": [str(i) for i in range(1, 75)] +
                         [str(i) for i in range(76, 81)] +
                         [str(i) for i in range(82, 87)] +
                         ["5А", "5Б", "7А", "34А", "80А", "80Б"],
            "district": "321109"
        }
    }

def expand_buildings7():
    return {
        "вул. Василя Стуса": {
            "buildings": {
                "10": "321112",
                "20": "321112",
                "23": "321112",
                "24": "321112",
                "25": "321112",
                "26": "321112",
                "27": "321112",
                "28": "321112",
                "29": "321112",
                "30": "321112",
                "31": "321112",
                "32": "321112",
                "33": "321112",
                "34": "321112",
                "44": "321112",
                "50": "321112",
                "52": "321112",
                "70": "321112",
                "71": "321112",
                "72": "321112",
                "73": "321112",
                "74": "321112",
                "75": "321112",
                "76": "321112",
                "2/147": "321113"
            }
        },
        "вул. Володимира Іванціва": {
            "buildings": {
                "5": "321112",
                "6": "321112",
                "7": "321112",
                "8": "321112",
                "9": "321112",
                "10": "321113",  # окрема дільниця
                "12": "321112",
                "13": "321112",
                "14": "321112",
                "15": "321112",
                "16": "321112",
                "17": "321112",
                "18": "321112",
                "19": "321112",
                "20": "321112",
                "21": "321112",
                "22": "321112",
                "23": "321112",
                "24": "321112",
                "25": "321112",
                "26": "321112",
                "27": "321112",
                "28": "321112",
                "29": "321112",
                "30": "321112",
                "31": "321112"
            }
        },
        "вул. Гетьмана Сагайдачного": {
            "buildings": {
                "118": "321112",
                "119": "321112",
                "120": "321112",
                "121": "321112"
            }
        },
        "бульв. Олександрійський": {
            "buildings": {
                "137": "321113",
                "143": "321113",
                "144": "321113",
                "145": "321113",
                "146": "321113",
                "147": "321113",
                "148": "321113",
                "149": "321113",
                "150": "321113",
                "151": "321113",
                "152": "321113",
                "153": "321113",
                "154": "321113",
                "155": "321113",
                "156": "321113",
                "157": "321113"
            }
        }
    }

def expand_buildings8():
    return {
        "бульв. Олександрійський": {
            "buildings": {
                "113": "321111",
                "119": "321111",
                "121": "321111",
                "123": "321111",
                "125": "321111",
                "127": "321111",
                "129": "321111",
                "137": "321111",
                "143": "321111",
                "145": "321111",
                "1В/М": "321110",
                "58": "321110",
                "60": "321110",
                "62": "321110",
                "64": "321110",
                "66": "321110"
            }
        }
    }

def expand_buildings9():
    return {
        "бульв. Олександрійський": {
            "buildings": {
                "131": "321114", "133": "321114", "135": "321114", "141": "321114",
                "111": "321115"
            }
        },
        "вул. Василя Стуса": {
            "buildings": {
                "3": "321114", "5": "321114",
                "13": "321115", "15": "321115", "17": "321115", "17/1": "321115",
                "19/2": "321115", "21": "321115", "39А": "321115", "39": "321115",
                "41": "321115", "43": "321115", "45": "321115", "47": "321115",
                "48": "321115", "49": "321115", "51": "321115", "53": "321115",
                "55": "321115", "57А": "321115", "57": "321115", "59": "321115",
                "61": "321115", "63": "321115", "65": "321115", "67": "321115",
                "67/1": "321115", "69": "321115", "88": "321115", "90": "321115",
                "92": "321115", "94": "321115", "96": "321115", "98": "321115",
                "100": "321115", "104А": "321115", "104": "321115", "106": "321115"
            }
        },
        "вул. Гетьмана Сагайдачного": {
            "buildings": {
                "70": "321114", "72": "321114", "74": "321114", "76": "321114",
                "78": "321114", "80": "321114", "82": "321114", "84": "321114",
                "86": "321114", "88": "321114", "89": "321114", "90": "321114",
                "91": "321114", "92": "321114", "93": "321114", "94": "321114",
                "95": "321114", "96": "321114", "97": "321114", "98": "321114",
                "99": "321114", "97А": "321114", "105": "321114",
                "30": "321115", "32": "321115", "34": "321115", "35": "321115",
                "36": "321115", "37": "321115", "38": "321115", "40": "321115",
                "41А": "321115", "43": "321115", "47А": "321115", "47": "321115",
                "49": "321115", "51": "321115", "53": "321115", "55": "321115",
                "57": "321115", "58": "321115", "59": "321115", "60": "321115",
                "62": "321115", "64": "321115", "65": "321115", "66": "321115",
                "67": "321115", "68": "321115", "69": "321115"
            }
        },
        "вул. Зелена": {
            "buildings": {
                "28": "321114", "30": "321114", "34": "321114", "36": "321114",
                "38": "321114", "40": "321114",
                # для 321115
                **{str(i): "321115" for i in range(3, 18)}, "13А": "321115",
                "19": "321115", "20": "321115", "21": "321115", "22": "321115",
                "24": "321115", "26": "321115"
            }
        },
        "вул. Лазаретна": {
            "buildings": {
                "1/20": "321115", "2/18": "321115", "3": "321115", "5": "321115",
                "7": "321115", "9/18": "321115", "11/33": "321115", "12": "321115",
                "13": "321115", "14/2": "321115", "15": "321115", "16/1": "321115",
                **{str(i): "321115" for i in range(17, 29)},
                **{str(i): "321115" for i in range(30, 34)},
                "23/2": "321115", "28Б": "321115", "28А": "321115", "29/1": "321115",
                "31/2": "321115", "35А": "321115", "35": "321115", "36": "321115",
                "37": "321115", "38/2": "321115", "39": "321115", "39/1": "321115",
                "40/1": "321115", **{str(i): "321115" for i in range(42, 47)},
                "48": "321115", "49": "321115", "50/": "321115", "50А": "321115",
                "50Б": "321115", "52/13": "321115", "54/40": "321115", "55": "321115",
                "57": "321115", "59": "321115", "61": "321115", "63": "321115",
                "64": "321115", "65А": "321115", "65": "321115", "67": "321115",
                "68": "321115", "69А": "321115", "69": "321115", "73": "321115",
                **{str(i): "321115" for i in range(76, 81)}, "82": "321115",
                "83": "321115", "85": "321115", "86А": "321115", "86": "321115",
                "87": "321115", "89": "321115", "91": "321115", "95": "321115"
            }
        },
        "вул. Набережна": {
            "buildings": {
                **{str(i): "321115" for i in range(3, 24)}, "10А": "321115",
                "11А": "321115", "25": "321115", "27": "321115", "29": "321115",
                "31": "321115", "33": "321115", "35": "321115", "37": "321115",
                "39": "321115", "41": "321115", "43": "321115"
            }
        },
        # провулки...
        "пров. Гірський": {
            "buildings": {"3": "321115", "4": "321115", "5": "321115", "8": "321115",
                          "9": "321115", "10": "321115", "11": "321115", "12": "321115",
                          "14": "321115", "14А": "321115", "16": "321115", "19А/2": "321115",
                          "20": "321115", "22": "321115"}
        },
        "пров. Зелений": {"buildings": {"4": "321115", "6": "321115", "9": "321115", "11": "321115"}},
        "пров. Лазаретний другий": {"buildings": {"3/1": "321115", "3": "321115", "4": "321115", "6": "321115", "8": "321115"}},
        "пров. Лазаретний перший": {
            "buildings": {"5": "321115", "6": "321115", "7": "321115", "9": "321115", "10/11": "321115",
                          "11/10": "321115", "13/5": "321115", "14": "321115", "14/7": "321115", "15": "321115", "16/1": "321115", "17": "321115", "41/2": "321115"}
        },
        "пров. Річковий перший": {
            "buildings": {**{str(i): "321115" for i in range(3,13)}, "13Б": "321115",
                           **{str(i): "321115" for i in range(14,18)}, "19": "321115", "21А": "321115", "21": "321115", "23": "321115", "25": "321115", "27": "321115", "29": "321115", "31А": "321115", "31": "321115"}
        },
        "пров. Яровий": {"buildings": {**{str(i): "321115" for i in range(3,14)}, "15": "321115", "16": "321115", "18": "321115", "20": "321115", "22": "321115", "24": "321115", "26": "321115", "30": "321115", "32": "321115"}},
        "тупик Глухий": {"buildings": {"2": "321115", "3": "321115", "4": "321115", "5": "321115", "7": "321115", "8": "321115"}}
    }

def expand_buildings10():
    return {
        "вул. Вокзальна": {
            "buildings": {
                **{str(i): "321118" for i in range(3, 12)},
                "5/приватний": "321118",
                "7/приватний": "321118",
                "8А": "321118", "9Б": "321118", "13": "321118", "18": "321118", "19": "321118"
            }
        },
        "вул. Товарна": {
            "buildings": {
                "3": "321118", "4": "321118", "5": "321118", "7": "321118",
                "8": "321118", "10": "321118", "12": "321118", "13": "321118",
                "14": "321118", "16": "321118", "17/2": "321118", "18": "321118",
                "19А": "321118", "19": "321118", "21": "321118", "22": "321118",
                "23": "321118", "24": "321118", "26": "321118", "31": "321118"
            }
        },
        "пров. Вокзальний": {
            "buildings": {
                **{str(i): "321118" for i in range(7, 20)},
                "3": "321118", "5": "321118", "8А": "321118", "11А": "321118"
            }
        },
        "пров. Курсовий": {
            "buildings": {
                "15/10": "321118", "17А": "321118", "19": "321118", "21": "321118",
                "22": "321118", "23": "321118", "25": "321118", "28": "321118",
                "30": "321118", "35": "321118"
            }
        },
        "пров. Курсовий другий": {
            "buildings": {
                "1": "321118", "5": "321118", **{str(i): "321118" for i in range(8, 13)},
                "14": "321118", "14А": "321118", "16": "321118", "18": "321118"
            }
        },
        "пров. Товарний": {
            "buildings": {
                "1": "321118", **{str(i): "321118" for i in range(3, 7)},
                "8": "321118", "9": "321118", "10": "321118", "11": "321118",
                "13": "321118", "18": "321118", "23": "321118"
            }
        },
        "бульв. Олександрійський": {
            "buildings": {
                "24": "321119", "26": "321119", "28": "321119", "30": "321119",
                "34": "321119", "36": "321119", "38": "321119", "40": "321119",
                "44/2": "321119", "46": "321119", "48А": "321119", "48": "321119",
                "50": "321119", "52": "321119"
            }
        },
        "вул. Златопольська": {
            "buildings": {
                "55": "321119", "59": "321119", "70А": "321119", "70": "321119",
                "72Б": "321119", "72А": "321119", "72": "321119", "74": "321119",
                "76А": "321119", "76": "321119", "78": "321119", "80": "321119",
                "82": "321119", "84": "321119", "86/71": "321119"
            }
        },
        "вул. Фастівська": {
            "buildings": {
                "1": "321119", "2Б": "321119", "2": "321119", **{str(i): "321119" for i in range(3, 10)},
                "9А": "321119", "10/2": "321119", "12": "321119", "13": "321119",
                "14": "321119", "15/1": "321119", "16": "321119", "18": "321119",
                "19": "321119", "20": "321119", "21Б/1": "321119", "21Б/2": "321119",
                "21Г": "321119", "21Д": "321119", "21": "321119", "24": "321119",
                "26": "321119", "28/1": "321119", "28/2": "321119", "29": "321119",
                "33": "321119", "58": "321119", "60": "321119", "62Б": "321119",
                "62А": "321119", "76": "321119"
            }
        }
    }

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = USERS.get(username)
        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
        else:
            error = 'Невірне ім’я або пароль'
    return render_template('login.html', error=error)


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'], role=session['role'])


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ---------- REGIONS LARGE ----------
@app.route('/regions-large')
def regions_large():
    if 'username' not in session:
        return redirect(url_for('login'))

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM regions_large")
        rows = c.fetchall()

    data = [{
        'id': row[0],
        'okrug': row[1],
        'last_name': row[2],
        'first_name': row[3],
        'middle_name': row[4],
        'phone': row[5],
        'location': row[6]
    } for row in rows]

    return render_template('regions_large.html', data=data)


@app.route('/add-region-large', methods=['GET', 'POST'])
def add_region_large():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('regions_large'))

    if request.method == 'POST':
        locations = request.form.getlist('location')
        location_str = ', '.join(locations)

        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO regions_large (okrug, last_name, first_name, middle_name, phone, location)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                request.form['okrug'],
                request.form['last_name'],
                request.form['first_name'],
                request.form['middle_name'],
                request.form['phone'],
                location_str
            ))
            conn.commit()
        return redirect(url_for('regions_large'))

    return render_template('add_region_large.html')


@app.route('/regions-large/edit/<int:region_id>', methods=['GET', 'POST'])
def edit_region_large(region_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати записи.')
        return redirect(url_for('regions_large'))

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()

        if request.method == 'POST':
            locations = request.form.getlist('location')
            location_str = ', '.join(locations)

            c.execute('''
                UPDATE regions_large SET
                    okrug = ?, last_name = ?, first_name = ?, middle_name = ?, phone = ?, location = ?
                WHERE id = ?
            ''', (
                request.form['okrug'],
                request.form['last_name'],
                request.form['first_name'],
                request.form['middle_name'],
                request.form['phone'],
                location_str,
                region_id
            ))
            conn.commit()
            return redirect(url_for('regions_large'))

        c.execute('SELECT * FROM regions_large WHERE id = ?', (region_id,))
        row = c.fetchone()

    if not row:
        flash('Запис не знайдено.')
        return redirect(url_for('regions_large'))

    region = {
        'okrug': row[1],
        'last_name': row[2],
        'first_name': row[3],
        'middle_name': row[4],
        'phone': row[5],
        'location': row[6].split(', ') if row[6] else []
    }

    return render_template('add_region_large.html', edit=True, region=region)


@app.route('/regions-large/delete/<int:region_id>', methods=['POST'])
def delete_region_large(region_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('regions_large'))

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('DELETE FROM regions_large WHERE id = ?', (region_id,))
        conn.commit()

    flash('Запис успішно видалено.')
    return redirect(url_for('regions_large'))


# ---------- REGIONS ----------
@app.route('/regions')
def regions():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM regions")
    rows = c.fetchall()
    conn.close()

    data = [{
        'id': row[0], 'large_okrug': row[1], 'district_name': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'address': row[6], 'phone': row[7], 'birth_date': row[8], 'location': row[9]
    } for row in rows]

    return render_template('regions.html', data=data)


@app.route('/regions/add', methods=['GET', 'POST'])
def add_region():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Недостатньо прав')
        return redirect(url_for('regions'))

    if request.method == 'POST':
        num = int(request.form['okrug_num'])
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT INTO regions (
                large_okrug, district_name, last_name, first_name, middle_name,
                address, phone, birth_date, location
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            ((num - 1) // 7 + 1),
            num,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['address'],
            request.form['phone'],
            request.form['birth_date'],
            request.form['location']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('regions'))

    return render_template('add_edit_region.html', edit=False)

@app.route('/regions/edit/<int:region_id>', methods=['GET', 'POST'])
def edit_region(region_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('regions'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        location = ', '.join(request.form.getlist('location'))

        c.execute('''
            UPDATE regions SET large_okrug=?, district_name=?, last_name=?, first_name=?,
                middle_name=?, address=?, phone=?, birth_date=?, location=?
            WHERE id=?
        ''', (
            request.form['large_okrug'],
            request.form['district_name'],
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['address'],
            request.form['phone'],
            request.form['birth_date'],
            location,
            region_id
        ))

        conn.commit()
        conn.close()
        return redirect(url_for('regions'))

    # GET-запит: отримуємо дані для редагування
    c.execute('SELECT * FROM regions WHERE id=?', (region_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        flash('Підписника не знайдено.')
        return redirect(url_for('regions'))

    region = {
        'id': row[0],
        'large_okrug': row[1],
        'district_name': row[2],
        'okrug_num': int(row[2]) if row[2] else None,
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'address': row[6],
        'phone': row[7],
     }

    return render_template('add_edit_region.html', edit=True, region=region)

@app.route('/regions/delete/<int:region_id>', methods=['POST'])
def delete_region(region_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('regions'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions WHERE id = ?', (region_id,))
    conn.commit()
    conn.close()
    flash('Підписника успішно видалено.')
    return redirect(url_for('regions'))


# ---------- ACTIVISTS ----------
@app.route('/activists')
def activists():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM activists")
    rows = c.fetchall()
    conn.close()

    data = [{
        'id': row[0],
        'large_okrug': row[1],
        'okrug': row[2],
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'address': row[6],
        'phone': row[7],
        'birth_date': row[8],
        'subscribers_count': row[9],
        'newspapers_count': row[10],
        'location': row[11]
    } for row in rows]

    return render_template('activists.html', data=data)


@app.route('/activists/add', methods=['GET', 'POST'])
def add_activist():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('activists'))

    if request.method == 'POST':
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT INTO activists (
                large_okrug, okrug, last_name, first_name, middle_name,
                address, phone, birth_date, subscribers_count,
                newspapers_count, location
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            request.form['large_okrug'],
            request.form['okrug'],
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['address'],
            request.form['phone'],
            request.form['birth_date'],
            request.form['subscribers_count'],
            request.form['newspapers_count'],
            request.form['location']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('activists'))

    return render_template('add_activist.html')


@app.route('/activists/edit/<int:activist_id>', methods=['GET', 'POST'])
def edit_activist(activist_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('activists'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        c.execute('''
            UPDATE activists SET
                large_okrug = ?, okrug = ?, last_name = ?, first_name = ?,
                middle_name = ?, address = ?, phone = ?, birth_date = ?,
                subscribers_count = ?, newspapers_count = ?, location = ?
            WHERE id = ?
        ''', (
            request.form['large_okrug'],
            request.form['okrug'],
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['address'],
            request.form['phone'],
            request.form['birth_date'],
            request.form['subscribers_count'],
            request.form['newspapers_count'],
            request.form['location'],
            activist_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('activists'))

    c.execute('SELECT * FROM activists WHERE id = ?', (activist_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        flash('Активіста не знайдено.')
        return redirect(url_for('activists'))

    activist = {
        'id': row[0],
        'large_okrug': row[1],
        'okrug': row[2],
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'address': row[6],
        'phone': row[7],
        'subscribers_count': row[9],
        'newspapers_count': row[10],
        'location': row[11]
    }

    return render_template('add_activist.html', edit=True, activist=activist)


@app.route('/activists/delete/<int:activist_id>', methods=['POST'])
def delete_activist(activist_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('activists'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM activists WHERE id = ?', (activist_id,))
    conn.commit()
    conn.close()
    flash('Запис успішно видалено.')
    return redirect(url_for('activists'))

# ---------- SUBSCRIBERS ----------
@app.route('/subscribers')
def subscribers_home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('subscribers_home.html')

@app.route('/regions1')
def region1():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримуємо всі записи для округу 1
    c.execute("SELECT * FROM regions1")
    rows = c.fetchall()

    # Формуємо словник з даними
    data = [{
        'id': r[0],
        'okrug': r[1],
        'district': r[2],
        'last_name': r[3],
        'first_name': r[4],
        'middle_name': r[5],
        'birth_date': r[6],
        'street': r[7],
        'building': r[8],
        'apartment': r[9],
        'phone': r[10],
        'activist': r[11]
    } for r in rows]

    # Отримуємо унікальні вулиці для фільтра
    c.execute("SELECT DISTINCT street FROM regions1 WHERE street IS NOT NULL AND street != '' ORDER BY street")
    streets = [row[0] for row in c.fetchall()]

    # Отримуємо унікальні будинки для фільтра
    c.execute("SELECT DISTINCT building FROM regions1 WHERE building IS NOT NULL AND building != '' ORDER BY building")
    buildings = [row[0] for row in c.fetchall()]

    # Отримуємо список активістів для фільтра (уникальні, можна взяти їх з іншої таблиці, якщо є)
    c.execute("SELECT DISTINCT activist FROM regions1 WHERE activist IS NOT NULL AND activist != '' ORDER BY activist")
    activists = [{'name': row[0]} for row in c.fetchall()]

    conn.close()

    return render_template(
        'region1.html',
        data=data,
        streets=streets,
        buildings=buildings,
        activists=activists
    )

@app.route('/regions1/add', methods=['GET','POST'])
def add_region1():
    if 'username' not in session or session.get('role')!='admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('region1'))
    conn=sqlite3.connect(DB_PATH)
    c=conn.cursor()
    if request.method=='POST':
        building = request.form['building']
        district = get_district_by_building(building)
        c.execute('''
            INSERT INTO regions1 (
                okrug, district, last_name, first_name, middle_name,
                birth_date, street, building, apartment, phone, activist
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
        ''', (
            1,
            district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            'вул. Гайок',
            building,
            request.form.get('apartment',''),
            request.form['phone'],
            request.form['activist']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region1'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts=[{'name':f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()
    return render_template('add_region1.html', buildings=expand_buildings(), activists=acts)

@app.route('/regions1/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region1(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region1'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        building = request.form['building']
        district = get_district_by_building(building)

        c.execute('''
            UPDATE regions1 SET
                okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
                birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            1,
            district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            'вул. Гайок',
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            subscriber_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region1'))

    # GET
    c.execute('SELECT * FROM regions1 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()

    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region1'))

    subscriber = {
        'id': row[0],
        'okrug': row[1],
        'district': row[2],
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'birth_date': row[6],
        'street': row[7],
        'building': row[8],
        'apartment': row[9],
        'phone': row[10],
        'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    return render_template('edit_region1.html', subscriber=subscriber, buildings=expand_buildings(), activists=acts)

@app.route('/regions1/delete/<int:subscriber_id>', methods=['POST'])
def delete_region1(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('region1'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions1 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Підписника видалено.')
    return redirect(url_for('region1'))

@app.route('/regions2')
def region2():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримати всі дані підписників округу 2
    c.execute("SELECT * FROM regions2")
    rows = c.fetchall()

    # Формування списку словників
    data = [{
        'id': r[0], 'okrug': r[1], 'district': r[2],
        'last_name': r[3], 'first_name': r[4], 'middle_name': r[5],
        'birth_date': r[6], 'street': r[7], 'building': r[8],
        'apartment': r[9], 'phone': r[10], 'activist': r[11]
    } for r in rows]

    # Унікальні активісти
    c.execute("SELECT DISTINCT activist FROM regions2 WHERE activist IS NOT NULL AND activist != ''")
    activists = sorted([row[0] for row in c.fetchall()])

    # Унікальні вулиці
    c.execute("SELECT DISTINCT street FROM regions2 WHERE street IS NOT NULL AND street != ''")
    streets = sorted([row[0] for row in c.fetchall()])

    # Унікальні будинки
    c.execute("SELECT DISTINCT building FROM regions2 WHERE building IS NOT NULL AND building != ''")
    buildings = sorted([row[0] for row in c.fetchall()])

    conn.close()

    return render_template(
        'region2.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions2/add', methods=['GET','POST'])
def add_region2():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('region2'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        district = get_district_by_building2(street, building)
        c.execute('''
            INSERT INTO regions2 (
                okrug, district, last_name, first_name, middle_name,
                birth_date, street, building, apartment, phone, activist
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
        ''', (
            2,
            district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region2'))

    # GET: Отримати активістів і структуру будинків
    c.execute("SELECT last_name, first_name FROM activists")
    activists = [{'name': f"{row[0]} {row[1]}"} for row in c.fetchall()]
    conn.close()

    buildings = expand_buildings2()  # функція повертає словник {"вулиця": [список будинків]}

    return render_template('add_region2.html',
                           activists=activists,
                           buildings=buildings)


@app.route('/regions2/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region2(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати записи.')
        return redirect(url_for('region2'))

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        district = get_district_by_building2(street, building)

        c.execute('''
            UPDATE regions2 SET
                last_name = ?, first_name = ?, middle_name = ?,
                birth_date = ?, street = ?, building = ?, apartment = ?,
                phone = ?, activist = ?, district = ?
            WHERE id = ?
        ''', (
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            district,
            subscriber_id
        ))

        conn.commit()
        conn.close()
        return redirect(url_for('region2'))

    # GET-запит — отримати поточні дані
    c.execute('SELECT * FROM regions2 WHERE id = ?', (subscriber_id,))
    subscriber = c.fetchone()
    conn.close()

    activists = get_activists()
    buildings = expand_buildings2()

    return render_template('edit_region2.html',
                           subscriber=subscriber,
                           activists=activists,
                           buildings=buildings)


@app.route('/delete_region2/<int:subscriber_id>', methods=['POST'])
def delete_region2(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('region2'))
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions2 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()
    flash('Підписника видалено.')
    return redirect(url_for('region2'))

@app.route('/regions3')
def region3():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM regions3')
    data = c.fetchall()
    conn.close()

    return render_template('region3.html', data=data)

@app.route('/regions3/add', methods=['GET','POST'])
def add_region3():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('region3'))
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        district = request.form['district']
        c.execute('''
            INSERT INTO regions3 (
              okrug, district, last_name, first_name, middle_name,
              birth_date, street, building, apartment, phone, activist
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
        ''', (
            3, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment',''),
            request.form['phone'],
            request.form['activist']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region3'))
    # GET:
    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()
    return render_template('add_region3.html', activists=acts)

@app.route('/regions3/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region3(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region3'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data3 = expand_buildings3()
        district = address_data3.get(street, {}).get('district', '')

        c.execute('''
            UPDATE regions3 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            3, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            subscriber_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region3'))

    # GET — читаємо поточні дані
    c.execute('SELECT * FROM regions3 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region3'))

    subscriber = dict(
        id=row[0], okrug=row[1], district=row[2],
        last_name=row[3], first_name=row[4], middle_name=row[5],
        birth_date=row[6], street=row[7], building=row[8],
        apartment=row[9], phone=row[10], activist=row[11]
    )
    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data3 = expand_buildings3()
    return render_template(
        'edit_region3.html',
        subscriber=subscriber,
        activists=acts,
        address_data3=address_data3,
        address_data_json=json.dumps(address_data3, ensure_ascii=False)
    )

@app.route('/delete_region3/<int:subscriber_id>', methods=['POST'])
def delete_region3(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('region3'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions3 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()
    flash('Підписника видалено успішно.')
    return redirect(url_for('region3'))

@app.route('/regions4')
def region4():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM regions4')
    rows = c.fetchall()
    conn.close()

    data = [{
        'id': row[0],
        'okrug': row[1],
        'district': row[2],
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'birth_date': row[6],
        'street': row[7],
        'building': row[8],
        'apartment': row[9],
        'phone': row[10],
        'activist': row[11]
    } for row in rows]

    return render_template('region4.html', data=data)

@app.route('/regions4/add', methods=['GET', 'POST'])
def add_region4():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('region4'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data4 = expand_buildings4()
        district = address_data4.get(street, {}).get('district', '')

        c.execute('''
            INSERT INTO regions4 (
                okrug, district, last_name, first_name, middle_name,
                birth_date, street, building, apartment, phone, activist
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            4, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist']
        ))

        conn.commit()
        conn.close()
        return redirect(url_for('region4'))

    # Підготовка до GET-запиту
    c.execute("SELECT last_name, first_name FROM activists")
    activists = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data4 = expand_buildings4()
    return render_template(
        'add_region4.html',
        activists=activists,
        address_data=address_data4,
        address_data_json=json.dumps(address_data4, ensure_ascii=False)
    )

@app.route('/regions4/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region4(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region4'))

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings4()
        district = address_data.get(street, {}).get('district', '')

        c.execute('''
            UPDATE regions4 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            4, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            subscriber_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region4'))

    # GET-запит — завантаження підписника
    c.execute('SELECT * FROM regions4 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region4'))

    subscriber = dict(
        id=row['id'], okrug=row['okrug'], district=row['district'],
        last_name=row['last_name'], first_name=row['first_name'], middle_name=row['middle_name'],
        birth_date=row['birth_date'], street=row['street'], building=row['building'],
        apartment=row['apartment'], phone=row['phone'], activist=row['activist']
    )

    # Завантаження активістів
    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r['last_name']} {r['first_name']}"} for r in c.fetchall()]
    conn.close()

    # Завантаження адрес
    address_data = expand_buildings4()

    return render_template(
        'edit_region4.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )


@app.route('/regions4/delete/<int:subscriber_id>', methods=['POST'])
def delete_region4(subscriber_id):
    # Перевірка авторизації (тільки адміністратор)
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('region4'))  # Перенаправлення на список округу 4

    # Видалення з бази даних
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions4 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Підписника видалено успішно.')
    return redirect(url_for('region4'))

@app.route('/regions5')
def region5():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM regions5")
    rows = c.fetchall()
    conn.close()

    data = [{
        'id': row[0],
        'okrug': row[1],
        'district': row[2],
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'birth_date': row[6],
        'street': row[7],
        'building': row[8],
        'apartment': row[9],
        'phone': row[10],
        'activist': row[11]
    } for row in rows]

    return render_template('region5.html', data=data)

@app.route('/regions5/add', methods=['GET', 'POST'])
def add_region5():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('region5'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings5()
        district = address_data.get(street, {}).get('district', '')

        c.execute('''
            INSERT INTO regions5 (
                okrug, district, last_name, first_name, middle_name,
                birth_date, street, building, apartment, phone, activist
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            5, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist']
        ))

        conn.commit()
        conn.close()
        return redirect(url_for('region5'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings5()
    return render_template(
        'add_region5.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions5/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region5(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region5'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings5()
        district = address_data.get(street, {}).get('district', '')

        c.execute('''
            UPDATE regions5 SET
                okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
                birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            5, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            subscriber_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region5'))

    # GET-запит
    c.execute('SELECT * FROM regions5 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region5'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings5()
    return render_template(
        'edit_region5.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions5/delete/<int:subscriber_id>', methods=['POST'])
def delete_region5(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('region5'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions5 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()
    flash('Підписника видалено.')
    return redirect(url_for('region5'))

@app.route('/regions6')
def region6():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM regions6")
    rows = c.fetchall()
    conn.close()

    data = [{
        'id': r[0], 'okrug': r[1], 'district': r[2],
        'last_name': r[3], 'first_name': r[4], 'middle_name': r[5],
        'birth_date': r[6], 'street': r[7], 'building': r[8],
        'apartment': r[9], 'phone': r[10], 'activist': r[11]
    } for r in rows]

    return render_template('region6.html', data=data)

@app.route('/regions6/add', methods=['GET', 'POST'])
def add_region6():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('region6'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings6()
        district = address_data.get(street, {}).get('district', '')

        c.execute('''
            INSERT INTO regions6 (
                okrug, district, last_name, first_name, middle_name,
                birth_date, street, building, apartment, phone, activist
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            6, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist']
        ))

        conn.commit()
        conn.close()
        return redirect(url_for('region6'))

    # Підготовка даних для GET-запиту
    c.execute("SELECT last_name, first_name FROM activists")
    activists = [{'name': f"{row[0]} {row[1]}"} for row in c.fetchall()]
    conn.close()

    address_data = expand_buildings6()
    return render_template(
        'add_region6.html',
        activists=activists,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions6/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region6(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region6'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings6()
        district = address_data.get(street, {}).get('district', '')

        c.execute('''
            UPDATE regions6 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            6, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            subscriber_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region6'))

    c.execute('SELECT * FROM regions6 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region6'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings6()
    return render_template(
        'edit_region6.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )
    
@app.route('/regions6/delete/<int:subscriber_id>', methods=['POST'])
def delete_region6(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('region6'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions6 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Підписника видалено.')
    return redirect(url_for('region6'))

@app.route('/regions7')
def region7():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM regions7")
    rows = c.fetchall()

    # Отримуємо список активістів
    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    data = [{
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    } for row in rows]

    return render_template('region7.html', data=data, activists=acts)

@app.route('/regions7/add', methods=['GET', 'POST'])
def add_region7():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('region7'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings7()

        # Отримуємо дільницю по конкретному будинку
        district = ''
        if street in address_data and 'buildings' in address_data[street]:
            district = address_data[street]['buildings'].get(building, '')

        c.execute('''
            INSERT INTO regions7 (
                okrug, district, last_name, first_name, middle_name,
                birth_date, street, building, apartment, phone, activist
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            7, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist']
        ))

        conn.commit()
        conn.close()
        return redirect(url_for('region7'))

    # GET-запит: підготовка даних для форми
    c.execute("SELECT last_name, first_name FROM activists")
    activists = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings7()
    return render_template(
        'add_region7.html',
        activists=activists,
        streets=list(address_data.keys()),
        buildings7_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions7/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region7(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region7'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings7()

        district = ''
        if street in address_data and 'buildings' in address_data[street]:
            district = address_data[street]['buildings'].get(building, '')

        c.execute('''
            UPDATE regions7 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            7, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            subscriber_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region7'))

    # GET-запит: отримуємо дані підписника
    c.execute('SELECT * FROM regions7 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region7'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    activists = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings7()
    return render_template(
        'edit_region7.html',
        subscriber=subscriber,
        activists=activists,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )
    
@app.route('/regions7/delete/<int:subscriber_id>', methods=['POST'])
def delete_region7(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Недостатньо прав для видалення.')
        return redirect(url_for('region7'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM regions7 WHERE id = ?", (subscriber_id,))
    conn.commit()
    conn.close()
    flash('Запис успішно видалено.')
    return redirect(url_for('region7'))

@app.route('/regions8')
def region8():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання записів округу 8
    c.execute("SELECT * FROM regions8")
    rows = c.fetchall()

    data = [{
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    } for row in rows]

    # Отримання списку активістів
    c.execute("SELECT last_name, first_name FROM activists")
    activists = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]

    # Унікальні вулиці
    streets = sorted({row['street'] for row in data if row['street']})
    
    # Унікальні будинки
    buildings = sorted({row['building'] for row in data if row['building']})

    conn.close()
    return render_template(
        'region8.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions8/add', methods=['GET', 'POST'])
def add_region8():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('region8'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings8()
        # витяг дільниці з вкладеної структури
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions8 (
                okrug, district, last_name, first_name, middle_name,
                birth_date, street, building, apartment, phone, activist
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            8, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region8'))

    # GET-запит: підтягуємо активістів
    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings8()
    return render_template(
        'add_region8.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions8/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region8(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region8'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings8()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions8 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            8, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            subscriber_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region8'))

    c.execute('SELECT * FROM regions8 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region8'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings8()
    return render_template(
        'edit_region8.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )
    
@app.route('/regions8/delete/<int:subscriber_id>', methods=['POST'])
def delete_region8(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region8'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions8 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region8'))

@app.route('/regions9')
def region9():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримуємо всі підписники округу 9
    c.execute("SELECT * FROM regions9")
    rows = c.fetchall()

    data = []
    for row in rows:
        data.append({
            'id': row[0],
            'okrug': row[1],
            'district': row[2],
            'last_name': row[3],
            'first_name': row[4],
            'middle_name': row[5],
            'birth_date': row[6],
            'street': row[7],
            'building': row[8],
            'apartment': row[9],
            'phone': row[10],
            'activist': row[11]
        })

    # Унікальні активісти
    c.execute("SELECT DISTINCT last_name, first_name FROM activists")
    activists = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]

    # Унікальні вулиці
    c.execute("SELECT DISTINCT street FROM regions9")
    streets = [row[0] for row in c.fetchall()]

    # Унікальні будинки
    c.execute("SELECT DISTINCT building FROM regions9")
    buildings = [row[0] for row in c.fetchall()]

    conn.close()

    return render_template(
        'region9.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions9/add', methods=['GET', 'POST'])
def add_region9():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('region9'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings9()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions9 (
                okrug, district, last_name, first_name, middle_name,
                birth_date, street, building, apartment, phone, activist
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            9, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist']
        ))

        conn.commit()
        conn.close()
        return redirect(url_for('region9'))

    # GET-запит — підготовка шаблону
    c.execute("SELECT last_name, first_name FROM activists")
    activists = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings9()
    return render_template(
        'add_region9.html',
        activists=activists,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions9/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region9(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region9'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings9()
        district = address_data.get(street, {}).get("buildings", {}).get(building, '')

        c.execute('''
            UPDATE regions9 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            9, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            subscriber_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region9'))

    # GET — отримання даних
    c.execute('SELECT * FROM regions9 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region9'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    activists = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings9()
    return render_template(
        'edit_region9.html',
        subscriber=subscriber,
        activists=activists,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions9/delete/<int:subscriber_id>', methods=['POST'])
def delete_region9(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('region9'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions9 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()
    flash('Запис успішно видалено.')
    return redirect(url_for('region9'))

@app.route('/regions10', methods=['GET'])
def region10():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions10")
    rows = c.fetchall()

    data = [
        {
            'id': row[0],
            'okrug': row[1],
            'district': row[2],
            'last_name': row[3],
            'first_name': row[4],
            'middle_name': row[5],
            'birth_date': row[6],
            'street': row[7],
            'building': row[8],
            'apartment': row[9],
            'phone': row[10],
            'activist': row[11]
        }
        for row in rows
    ]

    # Отримання активістів
    c.execute("SELECT DISTINCT last_name, first_name FROM activists")
    activists = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]

    # Унікальні вулиці та будинки для фільтрів
    streets = sorted(set(row['street'] for row in data))
    buildings = sorted(set(row['building'] for row in data))

    conn.close()
    return render_template(
        'region10.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions10/add', methods=['GET', 'POST'])
def add_region10():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region10'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings10()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions10 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            10, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region10'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings10()
    return render_template(
        'add_region10.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions10/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region10(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region10'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings10()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions10 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            10, district,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['birth_date'],
            street,
            building,
            request.form.get('apartment', ''),
            request.form['phone'],
            request.form['activist'],
            subscriber_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('region10'))

    c.execute('SELECT * FROM regions10 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region10'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings10()
    conn.close()

    return render_template(
        'edit_region10.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions10/delete/<int:subscriber_id>', methods=['POST'])
def delete_region10(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region10'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions10 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region10'))

# ---------- APP LAUNCH ----------
if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

