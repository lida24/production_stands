import psycopg2
import psycopg2

connection = psycopg2.connect(
              host="localhost",
              user="lida",
              password="12345678",
              database="db_ps"
              )

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor=connection.cursor()
""" cursor.execute('CREATE DATABASE db_ps;')

print('Database created successfully') """

""" cursor.execute('DROP TABLE IF EXISTS comptypes') """
""" cursor.execute('CREATE TABLE comptypes(id serial PRIMARY KEY,'
                                       'name varchar(150) NOT NULL UNIQUE,'
                                       'count integer NOT NULL,'
                                       'decoding varchar(150) NOT NULL UNIQUE);'
                                       ) """

""" cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('server',
                0, 
                'Изделие в сборе (СХД)')
               ) """ 

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('chassis',
                0,
                'Корпус СХД120')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('rail',
                0,
                'Рельса для корпуса (напрвляющая)')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('motherboard',
                0,
                'Материнская плата 1Э8СВ-uATX')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('raid_card',
                0,
                'RAID контроллер MegaRAID SAS 9560')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('network_card',
                0,
                'Сетевая карта Mellanox ConnectX-4')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('ddr4_memory_module',
                0,
                'Модуль памяти DDR4 Micron')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('m2_ssd',
                0,
                'Накопитель SSD М.2 TMI 256Гб')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('sas_expander', 
                0,
                'SAS разветвитель Intel RES3TV360 (экспандер)')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('hdd_backplane',
                0,
                'Модуль объединительный на 30 дисков (бэкплейн)')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('power_module',
                0,
                'Модуль управления питанием')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('indicator_board',
                0,
                'Плата индикации')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('power_supply_2k6',
                0,
                'Блок питания 2.6кВт')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('fan_140',
                0,
                'Вентилятор 140х140мм')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('fan_40',
                0, 
                'Вентилятор 40х40мм')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('fan_control_board',
                0, 
                'Плата управления вентиляторами')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('raiser_2U_board',
                0, 
                'Плата Райзер-2U')
               )

cursor.execute('INSERT INTO comptypes (name, count, decoding)'
               'VALUES (%s, %s, %s)',
               ('raiser_1U_board',
                0, 
                'Плата Райзер-1U')
               )

connection.close()