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

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions11 (
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
            CREATE TABLE IF NOT EXISTS regions12 (
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
            CREATE TABLE IF NOT EXISTS regions13 (
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
            CREATE TABLE IF NOT EXISTS regions14 (
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
            CREATE TABLE IF NOT EXISTS regions15 (
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
            CREATE TABLE IF NOT EXISTS regions16 (
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
            CREATE TABLE IF NOT EXISTS regions17 (
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
            CREATE TABLE IF NOT EXISTS regions18 (
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
            CREATE TABLE IF NOT EXISTS regions19 (
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
            CREATE TABLE IF NOT EXISTS regions20 (
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
            CREATE TABLE IF NOT EXISTS regions21 (
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
            CREATE TABLE IF NOT EXISTS regions22 (
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
            CREATE TABLE IF NOT EXISTS regions23 (
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
            CREATE TABLE IF NOT EXISTS regions24 (
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
            CREATE TABLE IF NOT EXISTS regions25 (
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

def expand_buildings11():
    return {
        "вул. Запорізька": {
            "buildings": {
                "19": "321116",
                "2А": "321120", "5": "321120", "6": "321120", "11": "321120", "12": "321120",
                "13": "321120", "14": "321120", "16": "321120", "18": "321120", "20": "321120",
                "21": "321120", "23": "321120", "30": "321120"
            }
        },
        "вул. Партизанська": {
            "buildings": {
                "3":"321116","4":"321116","5":"321116","6":"321116","7":"321116",
                "9":"321116","11/15":"321116","18":"321116","23":"321116","25":"321116",
                "33":"321116","35":"321116",
                "20":"321120","34":"321120","36":"321120","37/10":"321120","38":"321120",
                "40":"321120","40/15":"321120","41":"321120","42":"321120","43":"321120",
                "44":"321120","45":"321120","46":"321120","47":"321120","49":"321120",
                "50":"321120","52":"321120","53А":"321120","54":"321120","55":"321116",
                "56":"321120","57":"321120","58":"321120","59":"321120","60":"321120",
                "61":"321120","62":"321120","63":"321120","64":"321120","65":"321120",
                "66":"321120","67":"321120","68А":"321120","69":"321120","70":"321120",
                "71":"321120","72А":"321120","73":"321120","74":"321120","75":"321120",
                "76":"321120","77":"321120","79":"321120","81":"321120","83":"321120",
                "85":"321120","87":"321120","89":"321120","91":"321120","93":"321120",
                "97":"321120"
            }
        },
        "пров. Партизанський перший": {
            "buildings": {
                "1":"321116","11":"321116","17":"321116","20":"321116","21А":"321116",
                "22А":"321116","23/1":"321116","25/25":"321116","30А":"321116",
                "36А":"321116","41":"321116","43":"321116","45":"321116","47":"321116",
                "49":"321116","51":"321116","53":"321116","55":"321116"
            }
        },
        "бульв. Олександрійський": {
            "buildings": {
                "77":"321120","79":"321120","83":"321120","85":"321120","87":"321120",
                "89":"321120","91":"321120","93":"321120","97":"321120","99":"321120",
                "101":"321120","103":"321120","105":"321120","107":"321120","109":"321120",
                "22/22":"321126"
            }
        },
        "вул. Водопійна": {
            "buildings": {
                "40":"321120","35":"321126","41":"321126","43":"321126","44":"321126",
                "45":"321126","46":"321126","46А":"321126","47":"321126","48":"321126",
                "49":"321126","50/1":"321126","51":"321126","52":"321126","53":"321126",
                "54":"321126","55":"321126","56":"321126","57":"321126","58/2":"321126",
                "59/1":"321126","61":"321126","61/2":"321126","62":"321126","63":"321126",
                "64":"321126","65":"321126","66":"321126","68":"321126","70":"321126",
                "70А":"321126","71":"321126","73":"321126","74":"321126","75":"321126",
                "75/20":"321126","76":"321126","76/2":"321126","78/1":"321126",
                "79":"321126","80":"321126","81":"321126","82":"321126","83":"321126",
                "86":"321126","87":"321126","88":"321126","89":"321126","90":"321126",
                "90А":"321126","91":"321126","92":"321126","93":"321126","94":"321126",
                "95":"321126","96":"321126","97":"321126","97А":"321126","98":"321126",
                "99":"321126","100":"321126","100А":"321126","101":"321126","102":"321126",
                "103":"321126","105":"321126","106":"321126","107":"321126","108":"321126",
                "109":"321126","110":"321126","110А":"321126","111":"321126","113":"321126",
                "113А":"321126"
            }
        },
        "вул. Героїв Небесної Сотні": {
            "buildings": {"55":"321126","67":"321126","74":"321126","76":"321126","88":"321126"}
        },
        "вул. Героїв 72-ї Бригади": {
            "buildings": {"12":"321126","12А":"321126","14":"321126","16":"321126","19":"321126",
                          "21":"321126","25/2":"321126","27Б":"321126","31":"321126","33":"321126",
                          "35":"321126","37":"321126","39":"321126"}
        },
        "вул. Гетьманська": {
            "buildings": {
                "3":"321126","4":"321126","5":"321126","6":"321126","7":"321126","8":"321126",
                "9":"321126","10":"321126","11":"321126","13":"321126","14":"321126",
                "15":"321126","15А":"321126","16":"321126","17":"321126","17А":"321126",
                "19":"321126","19А":"321126","20":"321126","21":"321126","22":"321126",
                "23":"321126","24":"321126","25":"321126","26":"321126","27":"321126",
                "28":"321126","29":"321126","30":"321126","31":"321126","32":"321126",
                "33":"321126","34":"321126","35":"321126","36":"321126","38":"321126",
                "40":"321126","42":"321126","46":"321126","64":"321126","82":"321126","94":"321126"
            }
        },
        "пров. Водопійний": {
            "buildings": {
                "3":"321126","4":"321126","5":"321126","6":"321126","7":"321126","8":"321126",
                "9":"321126","10":"321126","10А":"321126","11":"321126","12":"321126","13":"321126",
                "14":"321126","15":"321126","16":"321126","17":"321126","18":"321126","19":"321126",
                "20":"321126","21":"321126","23":"321126","24":"321126","26":"321126","28":"321126",
                "28А":"321126","30":"321126","42":"321126","44":"321126"
            }
        },
        "пров. Водопійний другий": {
            "buildings": {"3":"321126","4":"321126","5":"321126","6":"321126","7":"321126","8":"321126",
                          "10":"321126","11":"321126","12А":"321126","13":"321126","15":"321126","17":"321126"}
        },
        "пров. Водопійний перший": {
            "buildings": {
                "3":"321126","5":"321126","6":"321126","7А":"321126","7Б":"321126","8":"321126",
                "9":"321126","10":"321126","10А":"321126","11":"321126","12":"321126","13":"321126",
                "14":"321126","15":"321126","16":"321126","16А":"321126","17":"321126","20":"321126",
                "22":"321126","24А":"321126","26":"321126","26А":"321126","28А":"321126","30":"321126",
                "36А":"321126","42":"321126","43А":"321126","44":"321126","50":"321126","50А":"321126"
            }
        },
        "пров. Водопійний третій": {
            "buildings": {"2":"321126","4":"321126","6":"321126","8":"321126","10":"321126","12":"321126","14":"321126"}
        }
    }

def expand_buildings12():
    return {
        "вул. Андрея Шептицького": {
            "buildings": {
                "70": "321121",
                "34": "321123", "34/13": "321123", "48": "321123", "50": "321123",
                "52": "321123", "54": "321123", "56": "321123", "58": "321123",
                "60": "321123", "62": "321123", "64": "321123", "65": "321123",
                "66": "321123", "75": "321123", "79": "321123", "80Б": "321123",
                "81": "321123", "83": "321123"
            }
        },
        "вул. Вокзальна": {
            "buildings": {"22": "321121"}
        },
        "вул. Олеся Гончара": {
            "buildings": {**{str(i): "321121" for i in range(2,10)}, "10": "321121", "11": "321121", "12": "321121", "18": "321121", "20": "321121"}
        },
        "вул. Павла Скоропадського": {
            "buildings": {
                "41": "321121", "41А": "321121", "43": "321121",
                "45": "321121", "47": "321121", "51": "321121", "53А": "321121",
                **{str(i): "321121" for i in range(55,77)}, "58А": "321121", "75Б": "321121",
                "78": "321121", "80": "321121", "82": "321121", "69А": "321123"
            }
        },
        "вул. Привокзальна": {
            "buildings": {
                "16": "321121", "26": "321121", "36": "321121", "55": "321121",
                "59": "321121", "61": "321121", "64": "321121", "69": "321121",
                "71": "321121", "73": "321121", "75": "321121", "89": "321121",
                "91": "321121"
            }
        },
        "вул. Симона Петлюри": {
            "buildings": {
                "37": "321121", "39": "321121", "41": "321121",
                "43": "321121", "45": "321121", "48": "321121",
                "50": "321121", "52": "321121", "56": "321121",
                "62": "321121"
            }
        },
        "пров. Курсовий": {
            "buildings": {"12А": "321121"}
        }
    }

def expand_buildings13():
    return {
        "бульв. Олександрійський": {
            "buildings": {
                "75": "321122", "20": "321125", "61": "321125", "61А": "321125",
                "63": "321125", "65": "321125", "67": "321125", "69": "321125"
            }
        },
        "вул. Андрея Шептицького": {
            "buildings": {
                "59": "321122", "69": "321122"
            }
        },
        "вул. Водопійна": {
            "buildings": {
                "1А/44": "321122", "1Б/44": "321122", "2": "321122", "3А": "321122",
                "3": "321122", "4": "321122", "6": "321122", "7А": "321122",
                "7": "321122", "8А": "321122", "8/31": "321122", "9": "321122",
                "11": "321122", "14А": "321122", "14": "321122", "19": "321122",
                "20": "321122", "22": "321122", "24А": "321122", "25": "321122",
                "27А": "321122"
            }
        },
        "вул. Курсова": {
            "buildings": {
                "59": "321122", "59А": "321122", "60А": "321122",
                "61": "321122", "62А": "321122", "62": "321122",
                "64А": "321122", "66А": "321122", "66": "321122",
                "66/2": "321122", "68А": "321122", "68/1": "321122",
                "68": "321122", "69": "321122", "70А": "321122", "70": "321122",
                "78А": "321122", "78А/78Б": "321122"
            }
        },
        "вул. Миколи Леонтовича": {
            "buildings": {**{str(i): "321122" for i in range(3,10)}, **{str(i): "321122" for i in range(11,28)},
                          "27А": "321122", "29": "321122", "33": "321122"}
        },
        "вул. Олеся Гончара": {
            "buildings": {"6А": "321122"}
        },
        "вул. Павла Скоропадського": {
            "buildings": {"37": "321122", "37/7": "321122", "39": "321122", "39/12": "321122",
                          "49": "321122", "52": "321122", "54/10": "321122"}
        },
        "вул. Привокзальна": {
            "buildings": {"51/1": "321122", "53/2": "321122"}
        },
        "пров. Курсовий": {
            "buildings": {"3": "321122", "8": "321122", "10": "321122"}
        },
        "вул. Богдана Хмельницького": {
            "buildings": {
                **{str(i): "321125" for i in range(26,32)}, "33": "321125", "34": "321125",
                "36А": "321125", "36": "321125", "38": "321125", "42/41": "321125", "40": "321125"
            }
        },
        "вул. Героїв 72-ї Бригади": {
            "buildings": {"14А/22": "321125", "51": "321125", "53": "321125", "55А": "321125"}
        },
        "вул. Златопольська": {
            "buildings": {
                "2/13": "321125", **{str(i): "321125" for i in range(3,22)},
                "4А": "321125", "18А": "321125", "20А": "321125",
                "23": "321125", "24": "321125", "25": "321125", "26": "321125",
                "27": "321125", "37": "321125", "38": "321125", "40": "321125",
                "42А": "321125", "42": "321125", "44": "321125", "46": "321125",
                "47": "321125", "48": "321125", "50": "321125"
            }
        },
        "вул. Нова": {
            "buildings": {"3А": "321125", "5": "321125", "10": "321125", "21": "321125"}
        },
        "вул. Підвальна": {
            "buildings": {
                "4/4": "321125", "5": "321125", "6/7": "321125", "7": "321125", "8": "321125",
                **{str(i): "321125" for i in range(9,23)}, "20/8": "321125", "21/6": "321125",
                "23/3": "321125", **{str(i): "321125" for i in range(24,29)}, "29": "321125",
                **{str(i): "321125" for i in range(32,39)}, "32А": "321125", "40": "321125",
                "44": "321125", "46": "321125"
            }
        },
        "вул. Праведників світу": {
            "buildings": {"4": "321125", "5А": "321125", "7": "321125", "9": "321125",
                          "10А": "321125", "10/11": "321125", "11/1": "321125",
                          "11/12": "321125", "15": "321125", "16/40": "321125",
                          **{str(i): "321125" for i in range(17,20)}, "21/1": "321125",
                          "22": "321125", "23/2": "321125", "25": "321125", "27": "321125",
                          "29": "321125", "31": "321125"}
        },
        "вул. Юр’ївська": {
            "buildings": {
                **{str(i): "321122" for i in range(3,8)}, "3А": "321122", "5А": "321122",
                "9": "321122", "11/12": "321122"
            }
        }
    }

def expand_buildings14():
    return {
        "вул. Курсова": {
            "buildings": {
                "18": "321124", "20": "321124", "22": "321124", "26": "321124",
                "28": "321124", "33": "321124", "34": "321124", "35": "321124",
                "37": "321124", "38": "321124", "40": "321124",
                "3А": "321127", "9А": "321127", "17А": "321127"
            }
        },
        "вул. Андрея Шептицького": {
            "buildings": {
                "1А": "321127", "3": "321127", "4": "321127", "5": "321127",
                "6": "321127", "8": "321127", "10": "321127", "11": "321127",
                "13": "321127", "15": "321127", "17": "321127", "19": "321127",
                "21": "321127", "23": "321127", "25": "321127", "26": "321127",
                "27": "321127", "29": "321127", "31": "321127", "32": "321127",
                "33": "321127", "37": "321127", "43": "321127", "45": "321127"
            }
        },
        "вул. Водопійна": {
            "buildings": {
                "9А": "321127"
            }
        },
        "вул. Павла Скоропадського": {
            "buildings": {
                "5": "321127", "7": "321127", "8": "321127", "9": "321127",
                "9А": "321127", "11": "321127", "11А": "321127",
                "12/43": "321127", "15А": "321127", "19Г": "321127",
                "19Б": "321127", "19А": "321127", "26": "321127",
                "26А": "321127", "30": "321127", "32": "321127", "33": "321127",
                "34": "321127", "36": "321127", "36В": "321127", "38": "321127",
                "40": "321127", "42": "321127", "44": "321127", "46": "321127",
                "48": "321127", "50": "321127"
            }
        },
        "вул. Праведників світу": {
            "buildings": {
                "28": "321127", "37": "321127", "37А": "321127"
            }
        },
        "вул. Привокзальна": {
            "buildings": {
                **{str(i): "321127" for i in [4, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]},
                "4А": "321127", "6А": "321127", "7/49": "321127"
            }
        },
        "вул. Симона Петлюри": {
            "buildings": {
                "1/45": "321127", "2/47": "321127",
                **{str(i): "321127" for i in range(3,29)}, "23А": "321127",
                "23Б": "321127", "30": "321127", "32": "321127",
                "32А": "321127", "34": "321127", "36": "321127",
                "38": "321127", "40": "321127", "42": "321127"
            }
        },
        "вул. Ярослава Мудрого": {
            "buildings": {
                "53/1": "321127", "55/2": "321127", "57": "321127",
                "59": "321127", "68": "321127", "70": "321127", "54": "321127"
            }
        },
        "бульв. Михайла Грушевського": {
            "buildings": {
                "4": "321129"
            }
        }
    }

def expand_buildings15():
    return {
        "бульв. Михайла Грушевського": {
            "buildings": {
                "6": "321128", "10": "321128", "12": "321128", "12А": "321128", "40": "321128"
            }
        },
        "вул. Петра Калнишевського": {
            "buildings": {
                "8": "321128", "13": "321128"
            }
        },
        "пров. Грузинський": {
            "buildings": {
                "15": "321128", "23": "321128"
            }
        },
        "вул. Григорія Ковбасюка": {
            "buildings": {
                **{str(i): "321133" for i in range(1,7)}, "11": "321133", "13": "321133"
            }
        },
        "вул. Івана Виговського": {
            "buildings": {
                "11/26": "321133", "12": "321133", "14": "321133", "15": "321133",
                "15/18": "321133", "16": "321133", "17/20": "321133"
            }
        },
        "вул. Ярослава Мудрого": {
            "buildings": {
                "35": "321133", "37": "321133", "39/15": "321133",
                "41": "321133", "42": "321133", "43": "321133", "43А": "321133",
                "44": "321133", "45": "321133", "48": "321133", "49": "321133",
                "50": "321133", "60": "321133", "62": "321133", "64/2": "321133"
            }
        }
    }

def expand_buildings16():
    return {
        "бульв. Михайла Грушевського": {
            "buildings": {"44": "321130", "46": "321130"}
        },
        "вул. Броварна друга": {
            "buildings": {"10": "321130", "17": "321130"}
        },
        "вул. Гоголя": {
            "buildings": {
                "11":"321130","15":"321130","16":"321130","17":"321130","18":"321130",
                "20":"321130","22":"321130","23":"321130","24":"321130","25":"321130",
                "26":"321130","27":"321130","28":"321130","30":"321130","32":"321130","34":"321130","38":"321130"
            }
        },
        "вул. Івана Кожедуба": {
            "buildings": {
                "10":"321130","10/2":"321130","18":"321130","20":"321130","21":"321130",
                "30А":"321130","31":"321130","32":"321130","35А":"321130","35":"321130",
                "36":"321130","37":"321130","38":"321130","39А":"321130","41/6":"321130",
                "43":"321130","44/7":"321130","45":"321130","46А":"321130",
                "47":"321130","49":"321130","53":"321130","55":"321130","55/64":"321130"
            }
        },
        "вул. Інтендантська": {
            "buildings": {
                "7":"321130","8А":"321130","9":"321130","11":"321130","13":"321130",
                "17":"321130","19":"321130","21":"321130","23":"321130","25":"321130",
                "27":"321130","29":"321130","31/43":"321130"
            }
        },
        "вул. Миколи Хрусталенка": {
            "buildings": {str(i): "321130" for i in range(1, 24)}
        },
        "вул. Михайла Чалого": {
            "buildings": {
                "3":"321130","5":"321130","7":"321130","8":"321130","9":"321130","10А":"321130",
                "11":"321130","13":"321130","15":"321130","19":"321130","21":"321130","30":"321130"
            }
        },
        "вул. Павліченко": {
            "buildings": {
                "3":"321130","4":"321130","6А":"321130","8":"321130","10":"321130","12":"321130"
            }
        },
        "пров. Гоголя": {
            "buildings": {
                "3":"321130","5А":"321130","5":"321130","6":"321130","7":"321130","8":"321130",
                "9":"321130","11":"321130","13":"321130","15":"321130","17":"321130","19/13":"321130"
            }
        },
        "пров. Петра Калнишевського": {
            "buildings": {
                "3":"321130","5":"321130","7":"321130","8А":"321130","9":"321130","9А":"321130",
                "11":"321130","17":"321130"
            }
        },
        "вул. Академіка Кононського": {
            "buildings": {
                "1":"321131","2/181":"321131",
                **{str(i): "321131" for i in range(3, 10)}, "8А":"321131","11":"321131",
                **{str(i): "321131" for i in range(13, 29)}, "15А":"321131","20А":"321131",
                "25А":"321131","26А":"321131","30":"321131","32":"321131","43":"321131",
                "47":"321131","49":"321131","51":"321131","53":"321131","55":"321131",
                "55А":"321131","57":"321131","59":"321131","61":"321131","63":"321131",
                "65":"321131","67":"321131","69":"321131","71":"321131","77":"321131",
                "79":"321131","81":"321131","83":"321131","85":"321131","87":"321131",
                "89":"321131","91":"321131","93":"321131","93А":"321131","95":"321131",
                "97":"321131","99":"321131","101":"321131","103":"321131","105":"321131",
                "105А":"321131","109":"321131","111":"321131","113":"321131","115":"321131",
                "117":"321131"
            }
        },
        "вул. Глиняна": {
            "buildings": {
                "58":"321131","58А":"321131","60":"321131","62":"321131","64":"321131",
                "66":"321131","68":"321131","70":"321131","72":"321131","73А":"321131",
                "75А":"321131","76А":"321131","78А":"321131","84А":"321131","85А":"321131",
                **{str(i): "321131" for i in range(93, 106)}, "95А":"321131","96А":"321131",
                "100А":"321131","107":"321131","109":"321131","111":"321131"
            }
        },
        "вул. Луки Долинського": {
            "buildings": {
                "1":"321131","1Б":"321131","1А":"321131","2/71":"321131","3А":"321131",
                **{str(i): "321131" for i in range(4, 14)}, "14А":"321131",
                **{str(i): "321131" for i in range(15, 23)}, "24":"321131","26":"321131","27":"321131",
                "28":"321131","30":"321131","32":"321131","34":"321131","36":"321131",
                "38":"321131","40":"321131","42":"321131","105":"321131"
            }
        },
        "вул. Льодова": {
            "buildings": {
                "1":"321131","1А":"321131","1Б":"321131","3":"321131","4":"321131","5":"321131",
                "7":"321131","8":"321131","10":"321131","11":"321131","12":"321131","13":"321131",
                "14":"321131","15":"321131","16":"321131","17":"321131","18":"321131","19А":"321131",
                "21А":"321131","24/2":"321131","25":"321131","26":"321131","27":"321131","28":"321131",
                "29":"321131","30":"321131","31/1":"321131","32":"321131","34":"321131","35":"321131",
                "36А":"321131","48А":"321131","50А":"321131","53":"321131","54":"321131","55А":"321131",
                "58А":"321131","60А":"321131","70":"321131","71":"321131","72":"321131","72А":"321131",
                "76":"321131","78":"321131","80":"321131","80А":"321131","82":"321131","86":"321131",
                "86А":"321131","88":"321131","90":"321131","92":"321131","94":"321131","96":"321131",
                "98":"321131","100":"321131","102/74":"321131"
            }
        },
        "вул. Любомира Гузара": {
            "buildings": {
                "1/102":"321131","3":"321131","4":"321131","7":"321131","8":"321131",
                **{str(i): "321131" for i in range(9, 47)}, "29А":"321131","29Б":"321131",
                "41А":"321131","47А":"321131","48":"321131","49":"321131","51":"321131",
                "53":"321131","54":"321131","55":"321131","56":"321131","57А":"321131",
                "58":"321131","58А":"321131","59":"321131","60":"321131","61":"321131",
                "61А":"321131","61Б":"321131","63":"321131","64":"321131","65":"321131",
                "66":"321131","67":"321131","68":"321131","69":"321131","70":"321131",
                "71":"321131","73":"321131","74":"321131","75":"321131","77А":"321131",
                "80А":"321131","80Б":"321131","82":"321131","83":"321131","84":"321131",
                "85":"321131","86":"321131","87":"321131","88":"321131","89":"321131",
                "90":"321131","92":"321131","94":"321131","96":"321131","98":"321131",
                "100":"321131","102":"321131","104А":"321131","106А":"321131","111":"321131",
                "111А":"321131","112":"321131","114":"321131","115":"321131","117":"321131",
                "122А":"321131","126А":"321131","128":"321131","128А":"321131","128Б":"321131",
                "130":"321131","130А":"321131","132":"321131","134":"321131","135":"321131",
                "137":"321131","139":"321131","141":"321131","143":"321131","145":"321131",
                "147":"321131","149":"321131","151":"321131","153":"321131","155":"321131",
                "157":"321131","159":"321131","161":"321131","163":"321131","169":"321131",
                "171":"321131","173":"321131","175":"321131","177":"321131","179":"321131",
                "183":"321131","185":"321131","187":"321131","189":"321131","191":"321131",
                "193":"321131","197":"321131","199":"321131","201":"321131","203":"321131",
                "205":"321131","207":"321131","209":"321131","211":"321131","213":"321131",
                "215":"321131","217":"321131","219":"321131","221":"321131","223":"321131",
                "225":"321131","227":"321131","229":"321131","233":"321131","235":"321131",
                "237":"321131","239":"321131","241":"321131","241А":"321131","245":"321131",
                "247":"321131","249":"321131","251":"321131","251/1":"321131","253":"321131",
                "255":"321131"
            }
        },
        "вул. Павліченко": {
            "buildings": {
                "9":"321131","21":"321131","23/1":"321131","25/2":"321131","43/2":"321131"
            }
        },
        "вул. Петра Дяченка": {
            "buildings": {
                "3":"321131","4":"321131","5":"321131","7":"321131","8":"321131","9":"321131",
                "9А":"321131","13":"321131","15":"321131","17":"321131","21":"321131",
                "21/41":"321131","23":"321131","25":"321131"
            }
        },
        "вул. Ротецька": {
            "buildings": {
                "3":"321131","4":"321131","5":"321131","6":"321131","7":"321131","8А":"321131",
                "9А":"321131","10":"321131","11":"321131","12":"321131","13":"321131","14":"321131",
                "15":"321131","16":"321131","17":"321131","18":"321131","19":"321131","20":"321131",
                "21":"321131","22":"321131","24":"321131","26":"321131","27":"321131","29":"321131",
                "31":"321131","33":"321131"
            }
        },
        "пров. Кар’єрний": {
            "buildings": {
                "3А":"321131","3":"321131","4":"321131","5А":"321131","5":"321131","7":"321131",
                "8":"321131","9":"321131","10":"321131","11":"321131","14":"321131","15":"321131",
                "16":"321131","17":"321131","18":"321131","20":"321131","21":"321131","22":"321131",
                "23":"321131","24А":"321131","25":"321131","27":"321131","29":"321131","29А":"321131",
                "33":"321131","35А":"321131","37":"321131","39":"321131"
            }
        },
        "пров. Луки Долинського": {
            "buildings": {
                "1":"321131","2":"321131","3":"321131","5":"321131","6":"321131","7":"321131","8":"321131",
                "9":"321131","12":"321131","14":"321131","15":"321131","16":"321131","17":"321131","18А":"321131",
                "19":"321131","22":"321131","24":"321131","25":"321131","26":"321131","27":"321131","28":"321131"
            }
        },
        "пров. Льодовий": {
            "buildings": {
                "3":"321131","4":"321131","5":"321131","7":"321131","8":"321131","9":"321131","10":"321131",
                "11":"321131","12":"321131","13":"321131","14":"321131","15":"321131","16":"321131","17":"321131",
                "19":"321131","20":"321131","21":"321131","22":"321131","23":"321131","24":"321131","25":"321131",
                "26":"321131","27":"321131","28":"321131","30":"321131","34":"321131","38":"321131","45":"321131"
            }
        }
    }

def expand_buildings17():
    return {
        "вул. Павліченко": {
            "buildings": {
                "12А": "321132", "14А": "321132", "19": "321132", "20": "321132",
                "20Б": "321132", "22": "321132", "26": "321132", "28": "321132",
                "30": "321132", "32": "321132", "34": "321132", "38": "321132",
                "40": "321132",
                "37": "321135", "39": "321135", "43": "321135", "44": "321135"
            }
        },
        "вул. Шолом‑Алейхема": {
            "buildings": {
                "37": "321132", "33": "321135", "35": "321135", "62": "321135",
                "62/48": "321135", "64/33": "321135", "80": "321135", "82": "321135",
                "84": "321135", "86": "321135", "94": "321135", "96А": "321135",
                "96": "321135", "98": "321135", "2260А": "321135"
            }
        },
        "пров. Рокитнянський другий": {
            "buildings": {
                "9А": "321135", "10": "321135", "12": "321135", "13": "321135",
                **{str(i): "321135" for i in range(15,24)}, "25": "321135"
            }
        }
    }

def expand_buildings18():
    return {
        "вул. Базарна": {
            "buildings": {
                **{str(i): "321134" for i in range(3,20)}, "14/9": "321134", "15/15": "321134",
                "17А": "321134", "17Б": "321134", "19/16": "321134", "21/17": "321134",
                "23": "321134", "25": "321134", "25/12": "321134"
            }
        },
        "вул. Ковальська": {
            "buildings": {
                "1": "321134", "2": "321134", "3": "321134", "4": "321134", "5": "321134",
                "5А": "321134", "7": "321134", "8/7": "321134", "8/7А": "321134",
                "11": "321134", "12А": "321134", "11А": "321134", "13": "321134", "14": "321134"
            }
        },
        "вул. Миколи Лозовика": {
            "buildings": {
                **{str(i): "321134" for i in [1,2,3,4,5,6,7,8]}, "1/4": "321134",
                "5А": "321134", "7А": "321134", **{str(i): "321134" for i in range(10,16)}, "10А": "321134",
                "20": "321134"
            }
        },
        "вул. Шолом‑Алейхема": {
            "buildings": {"1": "321134", "21": "321134"}
        },
        "вул. Ярмаркова": {
            "buildings": {
                "1":"321134","3":"321134","7":"321134","9":"321134","13":"321134",
                "15":"321134","33":"321134","35":"321134","12/7":"321134"
            }
        },
        "вул. Ярослава Мудрого": {
            "buildings": {
                "18/1":"321134","19/1":"321134",
                **{str(i): "321134" for i in range(25,35)}, "40":"321134"
            }
        },
        "пров. Ковальський": {
            "buildings": {
                "2":"321134","4":"321134","5":"321134","6":"321134","8":"321134",
                "8/7":"321134","10":"321134","11":"321134","12":"321134","13":"321134",
                "14":"321134"
            }
        },
        "вул. Банкова": {
            "buildings": {"3": "321136", "4": "321136", "5": "321136", "6": "321136", "5А": "321136"}
        },
        "вул. Богдана Хмельницького": {
            "buildings": {
                "1/7":"321136","2/9":"321136","3":"321136","10":"321136","12":"321136","14":"321136",
                "15":"321136", **{str(i): "321136" for i in range(17,24)}
            }
        },
        "вул. Вадима Гетьмана": {
            "buildings": {
                "5":"321136","7":"321136","8":"321136","9":"321136","10":"321136","11":"321136",
                "12":"321136","14":"321136","16":"321136", **{str(i): "321136" for i in [18,19,20]}, "23":"321136"
            }
        },
        "вул. Васильківська": {
            "buildings": {
                "3":"321136","5":"321136","5/3":"321136","6":"321136","6/3":"321136","8/4":"321136",
                "9":"321136","11":"321136","12":"321136","13/5":"321136","15":"321136","15/6":"321136",
                "17":"321136","19/1":"321136","21/2":"321136"
            }
        },
        "вул. Верхня": {
            "buildings": {
                "5А":"321136","7":"321136","8":"321136","9":"321136","10":"321136","11/10":"321136",
                "12":"321136","14":"321136","16":"321136","18":"321136","41":"321136"
            }
        },
        "вул. Героїв Небесної Сотні": {
            "buildings": {
                "1":"321136","3":"321136","7":"321136","13":"321136","18":"321136","19":"321136",
                "20":"321136","26/1":"321136","28":"321136","52":"321136","52/2":"321136",
                "54":"321136","60":"321136","62":"321136","64":"321136"
            }
        },
        "вул. Гоголя": {
            "buildings": {str(i): "321136" for i in range(2,10)}
        },
        "вул. Івана Сошенка": {
            "buildings": {
                "1/12":"321136","2/13":"321136","7":"321136","9":"321136","11":"321136",
                "12/15":"321136","14/28":"321136","20":"321136","24":"321136"
            }
        },
        "вул. Комендантська": {
            "buildings": {str(i): "321136" for i in [2,3,4,5,6,8,10]}
        },
        "вул. М’ясна": {
            "buildings": {
                "2":"321136","3":"321136","4":"321136","5":"321136","6":"321136","2/31":"321136",
                "8":"321136","9":"321136","10":"321136","12":"321136","13/8":"321136","14":"321136",
                "15/12":"321136","16":"321136","20":"321136","22":"321136","24/10":"321136","28":"321136"
            }
        },
        "вул. Северина Наливайка": {
            "buildings": {
                "3/6":"321136","5/9":"321136","6":"321136","8":"321136","10":"321136",
                "12":"321136","14":"321136","16":"321136","18":"321136","22/5":"321136",
                "24":"321136","26/7":"321136"
            }
        },
        "вул. Театральна": {
            "buildings": {"3":"321136","7":"321136","7/6":"321136","10":"321136","11":"321136"}
        },
        "вул. Шамраївська": {
            "buildings": {
                "5":"321136","7":"321136","9":"321136","10":"321136","12":"321136","14":"321136",
                "16":"321136","18":"321136","20":"321136","22":"321136","24":"321136","26":"321136"
            }
        },
        "вул. Ярослава Мудрого": {
            "buildings": {"16/2":"321136","21/2":"321136"}
        },
        "пл. Торгова": {
            "buildings": {
                "1/11":"321136","2/1":"321136","4/27":"321136","16":"321136","18":"321136"
            }
        }
    }

def expand_buildings19():
    return {
        "вул. Голубина": {
            "buildings": {
                **{str(i): "321137" for i in range(4,7)}, "14/15": "321137", "15/24": "321137",
                **{str(i): "321137" for i in range(16,19)}, "22": "321137", "23": "321137",
                "30": "321137", "32/15": "321137", "36": "321137"
            }
        },
        "вул. Надрічна": {
            "buildings": {
                **{str(i): "321137" for i in range(2,21)}, "3А": "321137", "21/1": "321137",
                **{str(i): "321137" for i in range(22,32)}, **{str(i): "321137" for i in range(36,41)},
                "39А": "321137", "42": "321137", "46": "321137", "48": "321137", "50": "321137",
                "58": "321137", "58А": "321137", "60": "321137", "64": "321137", "66": "321137",
                "70": "321137", "72": "321137", "76/34": "321137", "78": "321137", "78/37": "321137",
                "80": "321137", "82": "321137", "84": "321137", "86": "321137", "88": "321137",
                "90": "321137", "92": "321137", "96/32": "321137"
            }
        },
        "вул. Нечуй‑Левицького": {
            "buildings": {
                "2А":"321137", "3":"321137", "5":"321137", "6":"321137",
                **{str(i): "321137" for i in range(7,14)}
            }
        },
        "вул. Петра Лебединцева": {
            "buildings": {"3":"321137","4":"321137","7":"321137","8":"321137"}
        },
        "вул. Смоляно‑Рокитнянська": {
            "buildings": {
                **{str(i): "321137" for i in range(1,9)}, "8/21": "321137",
                "11":"321137","13":"321137","15":"321137","17":"321137"
            }
        },
        "вул. Шевченка": {
            "buildings": {
                "4":"321137","6":"321137","8":"321137", **{str(i): "321137" for i in range(10,15)},
                "17А":"321137","22/10":"321137","23":"321137","24/3":"321137",
                **{str(i): "321137" for i in range(26,32)}, "31/8":"321137",
                **{str(i): "321137" for i in range(33,39)}, "36/2":"321137",
                **{str(i): "321137" for i in range(38,52)}, "52А":"321137",
                **{str(i): "321137" for i in range(53,58)}, "61":"321137",
                **{str(i): "321137" for i in range(66,69)}, "70":"321137","71":"321137",
                "73/36":"321137","76":"321137","78":"321137","80":"321137",
                **{str(i): "321137" for i in range(82,87)}, "88":"321137","90":"321137",
                "92":"321137","94":"321137","94/38":"321137","96":"321137", "118":"321138"
            }
        },
        "вул. Шолом‑Алейхема": {
            "buildings": {
                **{str(i): "321137" for i in range(2,11)}, "2А":"321137","2/47":"321137",
                "11/2":"321137","12":"321137","13":"321137","14":"321137","16":"321137",
                "18":"321137","20":"321137","21А":"321137","22":"321137","24":"321137",
                "26":"321137","28":"321137","29":"321137","32":"321137","34":"321137",
                "36":"321137","36/2":"321137","40":"321137","42":"321137","44":"321137",
                "58":"321137","60":"321137"
            }
        },
        "пров. Петра Лебединцева": {
            "buildings": {"2":"321137","3":"321137","5":"321137","7":"321137","9":"321137","11":"321137","26Б":"321137"}
        },
        "пров. Шевченківський другий": {
            "buildings": {**{str(i): "321137" for i in range(3,17)}, "17/61":"321137","18/66":"321137"}
        },
        "пров. Шевченківський перший": {
            "buildings": {**{str(i): "321137" for i in range(3,8)}, "11":"321137","12":"321137","13":"321137","15":"321137","17":"321137","19":"321137","21":"321137"}
        },
        "вул. Івана Франка": {
            "buildings": {
                **{str(i): "321138" for i in range(24,27)}, "28":"321138","30":"321138","32":"321138",
                **{str(i): "321138" for i in range(36,38)}, "39/10":"321138","40":"321138",
                **{str(i): "321138" for i in range(41,50)}, "47А":"321138","48А":"321138",
                "50/22":"321138","52/25":"321138", **{str(i): "321138" for i in range(53,67)}, "59А":"321138","61А":"321138","63/23":"321138","67/20":"321138","68":"321138","68/2":"321138","69/21":"321138","70":"321138","71":"321138","72":"321138","73":"321138","70/1":"321138","74/54":"321138","75":"321138","77":"321138","79":"321138"
            }
        },
        "вул. Левка Симиренка": {
            "buildings": {
                "3":"321138", **{str(i): "321138" for i in range(5,19)}, "17/24":"321138","20":"321138","22/26":"321138","23/8":"321138",
                **{str(i): "321138" for i in range(25,29)}, "28А":"321138","29/32":"321138","30":"321138",
                **{str(i): "321138" for i in range(33,40)}, "36А":"321138","38/30":"321138","40/33":"321138"
            }
        },
        "вул. Павліченко": {
            "buildings": {
                "45":"321138","48":"321138","49":"321138","51":"321138","52":"321138","53":"321138",
                "54":"321138","55":"321138","56":"321138","61":"321138","64":"321138","65":"321138",
                "67":"321138","68":"321138","69":"321138","70/69":"321138","71":"321138",
                "74":"321138","78":"321138","80":"321138","82":"321138","84":"321138","86":"321138","88":"321138А","88":"321138","91/2":"321138","93":"321138","101":"321138"
            }
        },
        "вул. Садова": {
            "buildings": {
                **{str(i): "321138" for i in range(2,9)}, "2/23":"321138","4/23":"321138","5А":"321138","94":"321138",
                **{str(i): "321138" for i in range(10,19)}, "20":"321138","22":"321138","23/4":"321138","24":"321138","26/6":"321138"
            }
        },
        "вул. Софії Русової": {
            "buildings": {
                "3":"321138","5":"321138","7":"321138","8":"321138","9/51":"321138","20":"321138","21/62":"321138",
                **{str(i): "321138" for i in range(24,30)}, "31":"321138","32":"321138","36":"321138","38":"321138","38А":"321138","39А":"321138","42А":"321138"
            }
        },
        "пров. Івана Франка": {
            "buildings": {
                **{str(i): "321138" for i in range(3,15)}, "14А":"321138","16":"321138","18":"321138","19А":"321138",
                **{str(i): "321138" for i in range(19,30)}, "31":"321138","34":"321138","36":"321138","38":"321138","40":"321138"
            }
        },
        "пров. Левка Симиренка": {"buildings": {str(i): "321138" for i in range(2,7)}, "8":"321138"},
        "пров. Миколи Паукова": {"buildings": {"3":"321138","6":"321138","8":"321138","10":"321138","15":"321138"}},
        "пров. Павліченко": {"buildings": {"8":"321138","10":"321138"}}
    }

def expand_buildings20():
    return {
        "вул. Шевченка": {
            "buildings": {
                "91": "321139", "93": "321139", "95": "321139",
                "108А": "321139", "108Б": "321139", "108В": "321139",
                "108Г": "321139", "108Е": "321139", "109": "321139",
                "111": "321139", "112А": "321139", "112": "321139",
                "120": "321139", "121А": "321139", "122А": "321139",
                **{str(i): "321139" for i in range(122, 126)},  # 122 до 125
                "127": "321139", "129": "321139", "131": "321139",
                "133": "321139", "135": "321139", "137": "321139",
                "139": "321139", "141": "321139", "146": "321139",
                "154": "321139", "158": "321139", "160": "321139",
                "164": "321139", "166": "321139", "168": "321139",
                "170": "321139", "174": "321139", **{str(i): "321139" for i in range(178,181)},  # 178-180
                "182": "321139", "184А": "321139", "184": "321139",
                "186": "321139", "188": "321139", "190": "321139",
                "192": "321139", "194": "321139", "196": "321139",
                "200": "321139", "97": "321140", "99": "321140",
                "103": "321140", "103А": "321140"
            }
        },
        "просп. Князя Володимира": {
            "buildings": {
                "3": "321139"
            }
        }
    }

def expand_buildings21():
    return {
        "вул. Василя Вишиваного": {
            "buildings": {
                "1":"321141","3":"321141","5":"321141","6":"321141","7":"321141",
                **{str(i):"321141" for i in range(9,19)}, # 9–18
                "20":"321141", **{str(i):"321141" for i in range(22,34)},
                "35":"321141","37":"321141","39":"321141"
            }
        },
        "вул. Марії Примаченко": {
            "buildings": {
                "1":"321141","1А":"321141","1Б":"321141","3":"321141","5":"321141",
                "9":"321141","10":"321141","13/2":"321141","15":"321141","15А":"321141",
                "17":"321141","19":"321141","21":"321141","21/2":"321141","23":"321141",
                "25":"321141","25А":"321141","27":"321141","29":"321141","31":"321141",
                "33":"321141","35":"321141","37":"321141","39":"321141","41":"321141",
                "52":"321141","54":"321141","56":"321141","57":"321141","58/1":"321141",
                "58А":"321141","59":"321141","60/2":"321141","61":"321141","62/1":"321141",
                **{str(i):"321141" for i in range(63,88)}, "67А":"321141","82А":"321141",
                "84А":"321141","87А":"321141","88/2":"321141", **{str(i):"321141" for i in range(89,97)},
                "90/1":"321141","92А":"321141","98":"321141","100":"321141",
                **{str(i):"321141" for i in range(102,107)}, "107А":"321141","108":"321141",
                "108А":"321141","109":"321141","111":"321141","112":"321141",
                "113":"321141","114":"321141","115":"321141","115А":"321141","114А":"321141",
                **{str(i):"321141" for i in range(118,126)}, "122А":"321141","127":"321141",
                "129":"321141","131":"321141","133":"321141","133А":"321141",
                "135":"321141","137":"321141","139":"321141","141":"321141",
                "143":"321141","145":"321141","145А":"321141","147":"321141",
                "149":"321141","151":"321141","153":"321141","155":"321141",
                "155А":"321141","155Б":"321141","155В":"321141"
            }
        },
        "вул. Михайла Драгоманова": {
            "buildings": {
                "1":"321141","6":"321141","7":"321141","9":"321141","11":"321141",
                "17":"321141","19":"321141","20":"321141","23":"321141","24":"321141",
                "26":"321141","28":"321141","30":"321141","32":"321141","36":"321141"
            }
        },
        "вул. Михайла Жизневського": {
            "buildings": {"3":"321141","7":"321141","9":"321141","11":"321141"}
        },
        "вул. Пантелеймона Куліша": {
            "buildings": {"3":"321141","5":"321141","6/34":"321141","7":"321141","8":"321141",
                          "9":"321141","10":"321141","11":"321141","12":"321141","16":"321141","17":"321141","18":"321141","19":"321141","22":"321141","24":"321141"}
        },
        "вул. Петера Новотні": {
            "buildings": {"4":"321141","4А":"321141","5":"321141","6":"321141","9/2":"321141",
                          "13/2":"321141","15":"321141","15А":"321141","18":"321141","18А":"321141",
                          "19":"321141","21":"321141","22/2":"321141","23":"321141","24/1":"321141",
                          "25":"321141","26":"321141","27":"321141","28/1":"321141","29":"321141",
                          "30А":"321141","31":"321141","32А":"321141","33":"321141","34":"321141",
                          "35":"321141","36":"321141","37А":"321141","44":"321141","44А":"321141",
                          "48":"321141","50":"321141","52":"321141","53":"321141","54":"321141",
                          "54А":"321141","59А":"321141","60":"321141","61":"321141"}
        },
        "вул. Приміська": {
            "buildings": {
                "2":"321141","4":"321141","10":"321141","12":"321141","14":"321141",
                "16":"321141","18":"321141","20":"321141","22":"321141","22/19":"321141",
                "22/24":"321141","24/22":"321141","26":"321141","28":"321141","32":"321141",
                "34":"321141","36":"321141","50":"321141","56":"321141","60":"321141","66":"321141","74":"321141"
            }
        },
        "вул. Прорізна": {"buildings": {**{str(i):"321141" for i in range(3,16)}, "10А":"321141","17":"321141","18":"321141","20":"321141"}},
        "вул. Роз'їздна": {
            "buildings": {"2":"321141","3":"321141","4":"321141","8":"321141","10":"321141","10А":"321141",
                          "12":"321141","13":"321141","14":"321141","16":"321141","17":"321141","18А":"321141","19":"321141","21":"321141","24":"321141","25":"321141","26":"321141"}
        },
        "вул. Томилівська": {
            "buildings": {"1":"321141", **{str(i):"321141" for i in range(3,9)}, "10":"321141","12":"321141","14":"321141","16":"321141","17А":"321141","18":"321141","18А":"321141","20":"321141","22":"321141","24":"321141","24А":"321141","26":"321141","28":"321141","30":"321141","32":"321141","33":"321141","34":"321141","35":"321141","37":"321141","38":"321141","40":"321141","42":"321141","44":"321141","46":"321141"}
        },
        "вул. Якова Яциневича": {
            "buildings": {"3":"321141","4":"321141","5":"321141","6":"321141","7":"321141","8":"321141","9":"321141","10А":"321141","19А":"321141","26":"321141","28":"321141","30":"321141","32":"321141","34":"321141","36":"321141","40":"321141","42":"321141","44":"321141","46":"321141"}
        },
        "пров. Марії Примаченко другий": {
            "buildings": {"1А":"321141", **{str(i):"321141" for i in range(3,19)}, "9А":"321141","15/2":"321141","19/6":"321141","20/8":"321141"}
        },
        "пров. Марії Примаченко перший": {
            "buildings": {"3":"321141","4":"321141","5":"321141","6":"321141","7":"321141","8":"321141","9А":"321141","13А":"321141","15":"321141","16":"321141","17":"321141","18":"321141","20":"321141","21":"321141","22":"321141","23":"321141","24/2":"321141","25":"321141","25А":"321141","29":"321141"}
        },
        "пров. Петера Новотні другий": {
            "buildings": {"3":"321141","4":"321141","17А":"321141","21":"321141","26/2":"321141"}
        },
        "пров. Петера Новотні перший": {
            "buildings": {"3":"321141","4":"321141","6/1":"321141","9А":"321141","13":"321141","15":"321141","16":"321141","17":"321141","18":"321141","19":"321141","20А":"321141","21":"321141","22":"321141","23":"321141","24":"321141"}
        },
        "пров. Проточний": {
            "buildings": {"4":"321141","6":"321141","7":"321141","8":"321141","9":"321141","11":"321141","11А":"321141","12":"321141","14А":"321141","15":"321141","16":"321141","17":"321141","18":"321141","19":"321141","20":"321141","21":"321141","22":"321141","23А":"321141","25":"321141","26":"321141","27":"321141","28":"321141","29":"321141","30":"321141","31":"321141","32":"321141","33":"321141","34":"321141","35":"321141","36":"321141","38":"321141","40":"321141","42":"321141","44":"321141"}
        },
        "пров. Томилівський": {
            "buildings": {"2":"321141","3":"321141","4":"321141","5":"321141","7":"321141","9":"321141","10":"321141","11":"321141","12":"321141","13":"321141"}
        },
        # округ 21 — ВД 321146
        "вул. Кирила Стеценка": {
            "buildings": {"10":"321146","12":"321146","14":"321146","16":"321146","18":"321146","20":"321146","22":"321146","24":"321146","26":"321146","28":"321146"}
        },
        "вул. Східна": {"buildings": {"20":"321146","26":"321146","28":"321146","32":"321146"}},
        "пров. Володимирський": {"buildings": {"21":"321146","23":"321146","23А":"321146","25":"321146","26":"321146","27":"321146","28А":"321146","29":"321146","31":"321146","32":"321146","33":"321146","35":"321146","59":"321146"}},
        "просп. Незалежності": {"buildings": {"30":"321146","32":"321146"}}
    }

def expand_buildings22():
    return {
        "вул. Петера Новотні": {
            "buildings": {
                "61А": "321142", "65": "321142", "67": "321142"
            }
        },
        "вул. Томилівська": {
            "buildings": {
                "48": "321142", "50/1": "321142", "50/2": "321142", "50": "321142",
                "52": "321142", "54": "321142", "56": "321142", "58А": "321142",
                "58": "321142", "60А": "321142", "60": "321142", "62": "321142",
                "64": "321142", "66": "321142", "68": "321142", "70": "321142",
                "71": "321142"
            }
        },
        "вул. Кагарлицька": {
            "buildings": {
                "1А": "321143", **{str(i): "321143" for i in range(3,7)}, "4А": "321143",
                **{str(i): "321143" for i in range(9,22)}, "24": "321143", "26": "321143", "29": "321143"
            }
        },
        "вул. Митрофанова": {
            "buildings": {"2": "321143", "3": "321143"}
        },
        "вул. Східна": {
            "buildings": {"2": "321143", "4": "321143", "6": "321143", "8": "321143", "10": "321143"}
        },
        "вул. Узинська": {
            "buildings": {"9": "321143", "12": "321143", "22": "321143"}
        },
        "просп. Незалежності": {
            "buildings": {"157": "321143"}
        }
    }

def expand_buildings23():
    return {
        "просп. Незалежності": {
            "buildings": {
                "50/5": "321144", "52/4": "321144", "56А": "321144", "58": "321144",
                "62": "321144", "64": "321144", "66": "321144", "68": "321144",
                "70": "321144", "74": "321144",
                "75": "321148"
            }
        },
        "вул. Максима Глазкова": {
            "buildings": {
                "3": "321148"
            }
        },
        "вул. Митрофанова": {
            "buildings": {
                "9": "321148", "11": "321148", "12/18": "321148"
            }
        },
        "вул. Молодіжна": {
            "buildings": {
                "20": "321148", "22": "321148", "24": "321148", "26": "321148", "34": "321148"
            }
        }
    }

def expand_buildings24():
    return {
        "просп. Незалежності": {
            "buildings": {
                "59": "321149",
                "73": "321149",
                "61": "321150",
                "63": "321150",
                "69": "321150",
                "71": "321150"
            }
        },
        "вул. Митрофанова": {
            "buildings": {
                "13/16": "321150"
            }
        },
        "вул. Молодіжна": {
            "buildings": {
                "6": "321150",
                "8": "321150",
                "12": "321150",
                "14": "321150"
            }
        }
    }

def expand_buildings25():
    return {
        "вул. Митрофанова": {
            "buildings": {
                "1": "321145"
            }
        },
        "вул. Східна": {
            "buildings": {
                "14": "321145",
                "18": "321145",
                "22": "321145",
                "30": "321145"
            }
        },
        "просп. Незалежності": {
            "buildings": {
                "38": "321145",
                "40": "321145",
                "42": "321145",
                "48": "321145",
                "44": "321147",
                "46": "321147"
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

@app.route('/regions11', methods=['GET'])
def region11():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions11")
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
        'region11.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions11/add', methods=['GET', 'POST'])
def add_region11():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region11'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings11()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions11 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            11, district,
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
        return redirect(url_for('region11'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings11()
    return render_template(
        'add_region11.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions11/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region11(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region11'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings11()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions11 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            11, district,
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
        return redirect(url_for('region11'))

    c.execute('SELECT * FROM regions11 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region11'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings11()
    conn.close()

    return render_template(
        'edit_region11.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions11/delete/<int:subscriber_id>', methods=['POST'])
def delete_region11(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region11'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions11 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region11'))

@app.route('/regions12', methods=['GET'])
def region12():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions12")
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
        'region12.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions12/add', methods=['GET', 'POST'])
def add_region12():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region12'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings12()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions12 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            12, district,
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
        return redirect(url_for('region12'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings12()
    return render_template(
        'add_region12.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions12/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region12(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region12'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings12()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions12 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            12, district,
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
        return redirect(url_for('region12'))

    c.execute('SELECT * FROM regions12 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region12'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings12()
    conn.close()

    return render_template(
        'edit_region12.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions12/delete/<int:subscriber_id>', methods=['POST'])
def delete_region12(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region12'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions12 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region12'))

@app.route('/regions13', methods=['GET'])
def region13():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions13")
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
        'region13.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions13/add', methods=['GET', 'POST'])
def add_region13():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region13'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings13()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions13 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            13, district,
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
        return redirect(url_for('region13'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings13()
    return render_template(
        'add_region13.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions13/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region13(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region13'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings13()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions13 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            13, district,
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
        return redirect(url_for('region13'))

    c.execute('SELECT * FROM regions13 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region13'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings13()
    conn.close()

    return render_template(
        'edit_region13.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions13/delete/<int:subscriber_id>', methods=['POST'])
def delete_region13(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region13'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions13 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region13'))

@app.route('/regions14', methods=['GET'])
def region14():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions14")
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
        'region14.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions14/add', methods=['GET', 'POST'])
def add_region14():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region14'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings14()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions14 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            14, district,
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
        return redirect(url_for('region14'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings14()
    return render_template(
        'add_region14.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions14/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region14(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region14'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings14()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions14 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            14, district,
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
        return redirect(url_for('region14'))

    c.execute('SELECT * FROM regions14 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region14'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings14()
    conn.close()

    return render_template(
        'edit_region14.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions14/delete/<int:subscriber_id>', methods=['POST'])
def delete_region14(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region14'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions14 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region14'))

@app.route('/regions15', methods=['GET'])
def region15():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions15")
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
        'region15.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions15/add', methods=['GET', 'POST'])
def add_region15():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region15'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings15()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions15 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            15, district,
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
        return redirect(url_for('region15'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings15()
    return render_template(
        'add_region15.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions15/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region15(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region15'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings15()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions15 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            15, district,
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
        return redirect(url_for('region15'))

    c.execute('SELECT * FROM regions15 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region15'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings15()
    conn.close()

    return render_template(
        'edit_region15.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions15/delete/<int:subscriber_id>', methods=['POST'])
def delete_region15(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region15'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions15 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region15'))

@app.route('/regions16', methods=['GET'])
def region16():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions16")
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
        'region16.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions16/add', methods=['GET', 'POST'])
def add_region16():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region16'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings16()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions16 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            16, district,
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
        return redirect(url_for('region16'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings16()
    return render_template(
        'add_region16.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions16/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region16(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region16'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings16()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions16 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            16, district,
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
        return redirect(url_for('region16'))

    c.execute('SELECT * FROM regions16 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region16'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings16()
    conn.close()

    return render_template(
        'edit_region16.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions16/delete/<int:subscriber_id>', methods=['POST'])
def delete_region16(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region16'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions16 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region16'))

@app.route('/regions17', methods=['GET'])
def region17():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions17")
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
        'region17.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions17/add', methods=['GET', 'POST'])
def add_region17():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region17'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings17()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions17 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            17, district,
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
        return redirect(url_for('region17'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings17()
    return render_template(
        'add_region17.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions17/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region17(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region17'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings17()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions17 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            17, district,
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
        return redirect(url_for('region17'))

    c.execute('SELECT * FROM regions17 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region17'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings17()
    conn.close()

    return render_template(
        'edit_region17.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions17/delete/<int:subscriber_id>', methods=['POST'])
def delete_region17(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region17'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions17 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region17'))

@app.route('/regions18', methods=['GET'])
def region18():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions18")
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
        'region18.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions18/add', methods=['GET', 'POST'])
def add_region18():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region18'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings18()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions18 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            18, district,
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
        return redirect(url_for('region18'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings18()
    return render_template(
        'add_region18.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions18/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region18(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region18'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings18()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions18 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            18, district,
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
        return redirect(url_for('region18'))

    c.execute('SELECT * FROM regions18 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region18'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings18()
    conn.close()

    return render_template(
        'edit_region18.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions18/delete/<int:subscriber_id>', methods=['POST'])
def delete_region18(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region18'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions18 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region18'))

@app.route('/regions19', methods=['GET'])
def region19():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions19")
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
        'region19.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions19/add', methods=['GET', 'POST'])
def add_region19():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region19'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings19()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions19 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            19, district,
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
        return redirect(url_for('region19'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings19()
    return render_template(
        'add_region19.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions19/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region19(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region19'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings19()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions19 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            19, district,
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
        return redirect(url_for('region19'))

    c.execute('SELECT * FROM regions19 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region19'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings19()
    conn.close()

    return render_template(
        'edit_region19.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions19/delete/<int:subscriber_id>', methods=['POST'])
def delete_region19(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region19'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions19 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region19'))

@app.route('/regions20', methods=['GET'])
def region20():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions20")
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
        'region20.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions20/add', methods=['GET', 'POST'])
def add_region20():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region20'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings20()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions20 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            20, district,
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
        return redirect(url_for('region20'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings20()
    return render_template(
        'add_region20.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions20/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region20(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region20'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings20()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions20 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            20, district,
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
        return redirect(url_for('region20'))

    c.execute('SELECT * FROM regions20 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region20'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings20()
    conn.close()

    return render_template(
        'edit_region20.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions20/delete/<int:subscriber_id>', methods=['POST'])
def delete_region20(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region20'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions20 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region20'))

@app.route('/regions21', methods=['GET'])
def region21():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions21")
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
        'region21.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions21/add', methods=['GET', 'POST'])
def add_region21():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region21'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings21()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions21 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            21, district,
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
        return redirect(url_for('region21'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings21()
    return render_template(
        'add_region21.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions21/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region21(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region21'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings21()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions21 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            21, district,
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
        return redirect(url_for('region21'))

    c.execute('SELECT * FROM regions21 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region21'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings21()
    conn.close()

    return render_template(
        'edit_region21.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions21/delete/<int:subscriber_id>', methods=['POST'])
def delete_region21(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region21'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions21 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region21'))

@app.route('/regions22', methods=['GET'])
def region22():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions22")
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
        'region22.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions22/add', methods=['GET', 'POST'])
def add_region22():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region22'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings22()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions22 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            22, district,
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
        return redirect(url_for('region22'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings22()
    return render_template(
        'add_region22.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions22/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region22(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region22'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings22()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions22 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            22, district,
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
        return redirect(url_for('region22'))

    c.execute('SELECT * FROM regions22 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region22'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings22()
    conn.close()

    return render_template(
        'edit_region22.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions22/delete/<int:subscriber_id>', methods=['POST'])
def delete_region22(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region22'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions22 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region22'))

@app.route('/regions23', methods=['GET'])
def region23():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions23")
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
        'region23.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions23/add', methods=['GET', 'POST'])
def add_region23():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region23'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings23()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions23 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            23, district,
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
        return redirect(url_for('region23'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings23()
    return render_template(
        'add_region23.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions23/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region23(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region23'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings23()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions23 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            23, district,
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
        return redirect(url_for('region23'))

    c.execute('SELECT * FROM regions23 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region23'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings23()
    conn.close()

    return render_template(
        'edit_region23.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions23/delete/<int:subscriber_id>', methods=['POST'])
def delete_region23(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region23'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions23 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region23'))

@app.route('/regions24', methods=['GET'])
def region24():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions24")
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
        'region24.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions24/add', methods=['GET', 'POST'])
def add_region24():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region24'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings24()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions24 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            24, district,
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
        return redirect(url_for('region24'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings24()
    return render_template(
        'add_region24.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions24/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region24(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region24'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings24()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions24 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            24, district,
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
        return redirect(url_for('region24'))

    c.execute('SELECT * FROM regions24 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region24'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings24()
    conn.close()

    return render_template(
        'edit_region24.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions24/delete/<int:subscriber_id>', methods=['POST'])
def delete_region24(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region24'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions24 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region24'))

@app.route('/regions25', methods=['GET'])
def region25():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Отримання всіх підписників
    c.execute("SELECT * FROM regions25")
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
        'region25.html',
        data=data,
        activists=activists,
        streets=streets,
        buildings=buildings
    )

@app.route('/regions25/add', methods=['GET', 'POST'])
def add_region25():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('region25'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings25()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            INSERT INTO regions25 (okrug, district, last_name, first_name, middle_name,
                                   birth_date, street, building, apartment, phone, activist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            25, district,
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
        return redirect(url_for('region25'))

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    conn.close()

    address_data = expand_buildings25()
    return render_template(
        'add_region25.html',
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions25/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_region25(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('region25'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        street = request.form['street']
        building = request.form['building']
        address_data = expand_buildings25()
        district = address_data.get(street, {}).get('buildings', {}).get(building, '')

        c.execute('''
            UPDATE regions25 SET
              okrug = ?, district = ?, last_name = ?, first_name = ?, middle_name = ?,
              birth_date = ?, street = ?, building = ?, apartment = ?, phone = ?, activist = ?
            WHERE id = ?
        ''', (
            25, district,
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
        return redirect(url_for('region25'))

    c.execute('SELECT * FROM regions25 WHERE id = ?', (subscriber_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        flash('Підписника не знайдено.')
        return redirect(url_for('region25'))

    subscriber = {
        'id': row[0], 'okrug': row[1], 'district': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'birth_date': row[6], 'street': row[7], 'building': row[8],
        'apartment': row[9], 'phone': row[10], 'activist': row[11]
    }

    c.execute("SELECT last_name, first_name FROM activists")
    acts = [{'name': f"{r[0]} {r[1]}"} for r in c.fetchall()]
    address_data = expand_buildings25()
    conn.close()

    return render_template(
        'edit_region25.html',
        subscriber=subscriber,
        activists=acts,
        address_data=address_data,
        address_data_json=json.dumps(address_data, ensure_ascii=False)
    )

@app.route('/regions25/delete/<int:subscriber_id>', methods=['POST'])
def delete_region25(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('region25'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions25 WHERE id = ?', (subscriber_id,))
    conn.commit()
    conn.close()

    flash('Запис успішно видалено.')
    return redirect(url_for('region25'))
    
# ---------- APP LAUNCH ----------
if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

