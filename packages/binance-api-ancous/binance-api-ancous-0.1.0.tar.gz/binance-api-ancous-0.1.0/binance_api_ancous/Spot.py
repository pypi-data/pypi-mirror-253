"""
pass
"""

import json
import socket
import asyncio
import requests
import websockets.exceptions

from random import randint
from urllib.parse import urlencode


class Spot:
    """
    Класс для работы со спотом

    Attributes:
    base_url (str): базовый url для доступа к споту бирже binance
    base_url_stream (str): базовый url для доступа к стримам спота бирже binance

    Methods:

        Market data endpoints spot:
            connection_check_spot: проверка соединения спота
            get_average_price_spot: текущая средняя цена символа спота
            get_best_price_quantity_spot: лучшая цена и количество для символа или символов спота
            get_candles_spot: информация по свечам спота
            get_day_statistics_spot: статистика изменения цены спота за 24 часа
            get_trading_day_statistics_spot: статистика изменения цены спота за торговый день.
            get_glass_applications_spot: стакан заявок спота
            get_historical_trades_spot: исторические рыночные сделки по "fromId" спота
            get_symbols_info_spot: текущие правила биржевой торговли и информация о символах для спота
            get_latest_price_spot: последняя цена для символа или символов спота
            get_latest_trades_spot: последние рыночные сделки спота
            get_merged_trades_spot: объединенные сделки спота
            get_rolling_statistics_spot: статистика изменения цены спота в скользящем окне
            get_server_time_spot: время сервера спота
            get_uicandles_spot: информация по свечам спота

        Market data streams spot:
            get_stream_best_price_quantity_symbol_spot: лучшая цена и количество спота по символу
            get_stream_candles_spot: свечи спота
            get_stream_info_day_all_spot: информация о всех символах спота за 24 часа
            get_stream_info_day_symbol_spot: информация об определенном символе спота за 24 часа
            get_stream_info_rolling_all_spot: информация о всех символах спота в скользящем окне
            get_stream_info_rolling_symbol_spot: информация об определенном символе спота в скользящем окне
            get_stream_min_info_day_all_spot: минимальная информация о всех символах спота за 24 часа
            get_stream_min_info_day_symbol_spot: минимальная информация об определенном символе спота за 24 часа
            get_stream_order_book_difference_spot: ...
            get_stream_order_book_spot: стакан ордеров спота
            get_stream_id_trades_tape_spot: лента id-сделок спота покупателя и продавца по символу
            get_stream_trades_tape_spot: лента сделок спота по символу
            get_stream_average_price: средняя цена по символам
    """
    base_url = "https://api.binance.com"
    base_url_stream = "wss://stream.binance.com:9443/ws"

    def __init__(self, secret_key: str, api_key: str) -> None:
        """
        Создает ключи при инициализации объекта класса

        Attributes:
        secret_key (str): SECRET KEY Binance
        api_key (str): API KEY Binance

        Methods:
        None
        """

        self.secret_key = secret_key
        self.api_key = api_key

    def connection_check_spot(self) -> dict:
        """
        Запрос:
        Проверка соединения спота

        Полный url:
        "https://api.binance.com/api/v3/ping"

        Вес запроса:
        1

        Параметры:
        None

        Комментарии:
        None

        Ответ:
        {}
        """

        # -------------------------------------------
        end_point = "/api/v3/ping"
        # -------------------------------------------

        complete_request = self.base_url + end_point

        response = requests.get(url=complete_request)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_average_price_spot(self,
                               symbol: str) -> dict:
        """
        Запрос:
        Получить текущею среднюю цену символа спота

        Полный url:
        "https://api.binance.com/api/v3/avgPrice"

        Вес запроса:
        2

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)

        Комментарии:
        - None

        Ответ:
        {
           "mins": 5,
           "price": "0.27282934"
        }
        """

        # ------------------------------------------
        end_point = "/api/v3/avgPrice"
        parameters = {
            "symbol": symbol.upper(),
        }
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_best_price_quantity_spot(self,
                                     list_symbols: list = None) -> dict:
        """
        Запрос:
        Получить лучшую цену и количество для символа или символов спота

        Полный url:
        "https://api.binance.com/api/v3/ticker/bookTicker"

        Вес запроса:
        2 для одного символа, 4 когда параметр символа отсутствует

        Параметры:
        - list_symbols="symbols" (list): актив (["BTCUSDT"], ["BTCUSDT", "ADAUSDT"], ...)

        Комментарии:
        - None

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "bidPrice": "0.27340000",
              "bidQty": "6235.10000000",
              "askPrice": "0.27350000",
              "askQty": "40243.50000000"
           }
        ]
        """

        # ------------------------------------------
        end_point = "/api/v3/ticker/bookTicker"
        if list_symbols:
            parameters = {
                "symbols": [symbol.upper() for symbol in list_symbols]
            }
        else:
            parameters = {}
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = urlencode(parameters).replace('%2C+', ',').replace('%27', '%22')

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_candles_spot(self,
                         symbol: str,
                         interval: str,
                         start_time: str = None,
                         end_time: str = None,
                         time_zone: str = "0",
                         limit: str = "500") -> dict:
        """
        Запрос:
        Получить информацию по свечам спота

        Полный url:
        "https://api.binance.com/api/v3/klines"

        Вес запроса:
        2

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - interval="interval" (str): интервал свечи ("1m", "3m", "5m", "15m", "30m", "1h", "2h",
                                                     "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - time_zone="timeZone" (str): временной интервал часы:минуты-(-1:00, 05:45)
                                                         только часы-(0, 8, 4)()
        - limit="limit" (str): какое количество свечей вывести ("1", ..., "1000")

        Комментарии:
        - "timeZone" принимает диапазон строго от -12:00 до 14:00 включительно.
        - Если указан "timeZone", интервал интерпретируется в этом часовом поясе,
                                                                       а не в формате UTC как start_time или end_time
        - сокращения "interval": [m -> минута; h -> час; d -> день; w -> неделя; M -> месяц]
        - Если "startTime" и "endTime" не отправлены, возвращаются самые последние klines.

        Ответ:
        [
            [
                1681748820000,   (время открытие свечи)
                "29352.00",   (цена открытия свечи)
                "29385.00",   (самая высокая цена свечи)
                "29351.90",   (самая низкая цена свечи)
                "29385.00",   (цена закрытия свечи (или последняя цена))
                "414.755",   (объем в свече)
                1681748879999,   (время закрытия свечи)
                "12180316.04890",   (объем котируемого актива)
                3226,   (сделок в свече)
                "303.985",   (Taker buy base asset volume)
                "8926873.01530",   (Taker buy quote asset volume)
                "0"   (Ignore)
            ],
            [
                1681748880000,
                "29385.00",
                "29385.00",
                "29379.30",
                "29381.30",
                "65.643",
                1681748939999,
                "1928766.40370",
                729,
                "41.395",
                "1216276.73170",
                "0"
            ]
        ]
        """

        # ---------------------------------------------
        end_point = "/api/v3/klines"
        parameters = {
            "symbol": symbol.upper(),
            "interval": interval,
            "limit": limit,
            "startTime": start_time,
            "endTime": end_time,
            "timeZone": time_zone
        }
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_day_statistics_spot(self,
                                list_symbols: list = None,
                                my_type: str = "FULL") -> dict:
        """
        Запрос:
        Получить статистику изменения цены спота за 24 часа

        Полный url:
        "https://api.binance.com/api/v3/ticker/24hr"

        Вес запроса:
        [[list_symbols, вес], [1-20, 2], [21-100: 40], [>101: 80]

        Параметры:
        - list_symbols="symbols" (list): актив (["BTCUSDT"], ["BTCUSDT", "ADAUSDT"], ...)
        - my_type="my_type" (str): ... ("FULL","MINI")

        Комментарии:
        - Будьте осторожны при доступе к этому без символа.

        Ответ:
        {
           "symbol": "ADAUSDT",
           "priceChange": "0.00480",
           "priceChangePercent": "1.231",
           "weightedAvgPrice": "0.38924",
           "lastPrice": "0.39460",
           "lastQty": "319",
           "openPrice": "0.38980",
           "highPrice": "0.39690",
           "lowPrice": "0.38100",
           "volume": "508284698",
           "quoteVolume": "197842455.04000",
           "openTime": 1683219000000,
           "closeTime": 1683305434349,
           "firstId": 915943818,   (Первый идентификатор сделки)
           "lastId": 916332946,   (Последний идентификатор сделки)
           "count": 389059   (Количество сделок)
        }
        """

        # ------------------------------------------
        end_point = "/api/v3/ticker/24hr"
        if list_symbols:
            parameters = {
                "symbols": [symbol.upper() for symbol in list_symbols],
                "type": my_type
            }
        else:
            parameters = {
                "type": my_type
            }
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = urlencode(parameters).replace('%2C+', ',').replace('%27', '%22')

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_trading_day_statistics_spot(self,
                                        list_symbols: list = None,
                                        time_zone: str = "0",
                                        my_type: str = "FULL") -> dict:
        """
        Запрос:
        Получить статистику изменения цен спота за торговый день.

        Полный url:
        "https://api.binance.com/api/v3/ticker/tradingDay"

        Вес запроса:
        4 за каждый запрошенный символ
        Вес этого запроса будет ограничен 200, если количество символов в запросе превысит 50.

        Параметры:
        - list_symbols="symbols" (list): актив (["BTCUSDT"], ["BTCUSDT", "ADAUSDT"], ...)
        - time_zone="timeZone" (str): временной интервал часы:минуты-(-1:00, 05:45)
                                                         только часы-(0, 8, 4)
        - my_type="my_type" (str): ... ("FULL","MINI")

        Комментарии:
        - "timeZone" принимает диапазон строго от -12:00 до 14:00 включительно.
        - Если указан "timeZone", интервал интерпретируется в этом часовом поясе,
                                                                       а не в формате UTC как start_time или end_time

        Ответ:
        [
            {
                "symbol": "BTCUSDT",
                "priceChange": "-83.13000000",
                "priceChangePercent": "-0.317",
                "weightedAvgPrice": "26234.58803036",
                "openPrice": "26304.80000000",
                "highPrice": "26397.46000000",
                "lowPrice": "26088.34000000",
                "lastPrice": "26221.67000000",
                "volume": "18495.35066000",
                "quoteVolume": "485217905.04210480",
                "openTime": 1695686400000,
                "closeTime": 1695772799999,
                "firstId": 3220151555,
                "lastId": 3220849281,
                "count": 697727
            },
            {
                "symbol": "BNBUSDT",
                "priceChange": "2.60000000",
                "priceChangePercent": "1.238",
                "weightedAvgPrice": "211.92276958",
                "openPrice": "210.00000000",
                "highPrice": "213.70000000",
                "lowPrice": "209.70000000",
                "lastPrice": "212.60000000",
                "volume": "280709.58900000",
                "quoteVolume": "59488753.54750000",
                "openTime": 1695686400000,
                "closeTime": 1695772799999,
                "firstId": 672397461,
                "lastId": 672496158,
                "count": 98698
            }
        ]
        """

        # ------------------------------------------
        end_point = "/api/v3/ticker/tradingDay"
        if list_symbols:
            parameters = {
                "symbols": [symbol.upper() for symbol in list_symbols],
                "timeZone": time_zone,
                "type": my_type
            }
        else:
            parameters = {
                "timeZone": time_zone,
                "type": my_type
            }
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = urlencode(parameters).replace('%2C+', ',').replace('%27', '%22')

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_glass_applications_spot(self,
                                    symbol: str,
                                    limit: str = "100") -> dict:
        """
        Запрос:
        Получить стакан заявок спота

        Полный url:
        "https://api.binance.com/api/v3/depth"

        Вес запроса:
        [[limits: вес], [1-100: 5], [101-500: 25], [501-1000: 50], [1001-5000: 250]]

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("1", ..., "5000")

        Комментарии:
        - None

        Ответ:
        {
           "lastUpdateId": 7373908556,
           "bids": [
              [
                 "0.27310000",
                 "53080.10000000"
              ],
              [
                 "0.27300000",
                 "72853.80000000"
              ]
           ],
           "asks": [
              [
                 "0.27320000",
                 "19046.20000000"
              ],
              [
                 "0.27330000",
                 "84362.00000000"
              ]
           ]
        }
        """

        # ---------------------------------------------
        end_point = "/api/v3/depth"
        parameters = {
            "symbol": symbol.upper(),
            "limit": limit
        }
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_historical_trades_spot(self,
                                   symbol: str,
                                   from_id: str = None,
                                   limit: str = "500") -> dict:
        """
        Запрос:
        Получить исторические рыночные сделки по "fromId" спота

        Полный url:
        "https://api.binance.com/api/v3/historicalTrades"

        Вес запроса:
        10

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - from_id="fromId": (str): идентификатор сделки от которой будет произведён вывод следующих сделок ("567887")
        - limit="limit" (str): какое исторических количество сделок вывести ("1", ..., "1000")

        Комментарии:
        - Рыночные сделки означают сделки, заполненные в книге заявок.
        - Если "fromId" не указан показывает самые последние сделки
        - Будут возвращены только рыночные сделки, это означает,
          что сделки страхового фонда и сделки ADL не будут возвращены.

        Ответ:
        [
           {
              "id": 439851294,
              "price": "0.27280000",
              "qty": "631.10000000",
              "quoteQty": "172.16408000",
              "time": 1686675498135,
              "isBuyerMaker": false,
              "isBestMatch": true
           },
           {
              "id": 439851295,
              "price": "0.27270000",
              "qty": "144.10000000",
              "quoteQty": "39.29607000",
              "time": 1686675501547,
              "isBuyerMaker": true,
              "isBestMatch": true
           }
        ]
        """

        # ------------------------------------
        end_point = "/api/v3/historicalTrades"
        parameters = {
            "symbol": symbol.upper(),
            "limit": limit,
            "fromId": from_id,
        }
        # ------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.get(url=complete_request, params=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_symbols_info_spot(self,
                              list_symbols: list = None) -> dict:
        """
        Запрос:
        Получить текущие правила биржевой торговли и информацию о символах для спота

        Полный url:
        "https://api.binance.com/api/v3/exchangeInfo"

        Вес запроса:
        20

        Параметры:
        - list_symbols="symbols" (list): актив (["BTCUSDT"], ["BTCUSDT", "ADAUSDT"], ...)

        Комментарии:
        - None

        Ответ:
        {
           "timezone": "UTC",
           "serverTime": 1686560333688,
           "rateLimits": [
              {
                 "rateLimitType": "REQUEST_WEIGHT",
                 "interval": "MINUTE",
                 "intervalNum": 1,
                 "limit": 1200
              },
              {
                 "rateLimitType": "ORDERS",
                 "interval": "SECOND",
                 "intervalNum": 10,
                 "limit": 50
              },
              {
                 "rateLimitType": "ORDERS",
                 "interval": "DAY",
                 "intervalNum": 1,
                 "limit": 160000
              },
              {
                 "rateLimitType": "RAW_REQUESTS",
                 "interval": "MINUTE",
                 "intervalNum": 5,
                 "limit": 6100
              }
           ],
           "exchangeFilters": [],
           "symbols": [
              {
                 "symbol": "ADAUSDT",
                 "status": "TRADING",
                 "baseAsset": "ADA",
                 "baseAssetPrecision": 8,
                 "quoteAsset": "USDT",
                 "quotePrecision": 8,
                 "quoteAssetPrecision": 8,
                 "baseCommissionPrecision": 8,
                 "quoteCommissionPrecision": 8,
                 "orderTypes": [
                    "LIMIT",
                    "LIMIT_MAKER",
                    "MARKET",
                    "STOP_LOSS_LIMIT",
                    "TAKE_PROFIT_LIMIT"
                 ],
                 "icebergAllowed": true,
                 "ocoAllowed": true,
                 "quoteOrderQtyMarketAllowed": true,
                 "allowTrailingStop": true,
                 "cancelReplaceAllowed": true,
                 "isSpotTradingAllowed": true,
                 "isMarginTradingAllowed": true,
                 "filters": [
                    {
                       "filterType": "PRICE_FILTER",
                       "minPrice": "0.00010000",
                       "maxPrice": "1000.00000000",
                       "tickSize": "0.00010000"
                    },
                    {
                       "filterType": "LOT_SIZE",
                       "minQty": "0.10000000",
                       "maxQty": "900000.00000000",
                       "stepSize": "0.10000000"
                    },
                    {
                       "filterType": "ICEBERG_PARTS",
                       "limit": 10
                    },
                    {
                       "filterType": "MARKET_LOT_SIZE",
                       "minQty": "0.00000000",
                       "maxQty": "2723864.64079221",
                       "stepSize": "0.00000000"
                    },
                    {
                       "filterType": "TRAILING_DELTA",
                       "minTrailingAboveDelta": 10,
                       "maxTrailingAboveDelta": 2000,
                       "minTrailingBelowDelta": 10,
                       "maxTrailingBelowDelta": 2000
                    },
                    {
                       "filterType": "PERCENT_PRICE_BY_SIDE",
                       "bidMultiplierUp": "5",
                       "bidMultiplierDown": "0.2",
                       "askMultiplierUp": "5",
                       "askMultiplierDown": "0.2",
                       "avgPriceMins": 5
                    },
                    {
                       "filterType": "NOTIONAL",
                       "minNotional": "5.00000000",
                       "applyMinToMarket": true,
                       "maxNotional": "9000000.00000000",
                       "applyMaxToMarket": false,
                       "avgPriceMins": 5
                    },
                    {
                       "filterType": "MAX_NUM_ORDERS",
                       "maxNumOrders": 200
                    },
                    {
                       "filterType": "MAX_NUM_ALGO_ORDERS",
                       "maxNumAlgoOrders": 5
                    }
                 ],
                 "permissions": [
                    "SPOT",
                    "MARGIN",
                    "TRD_GRP_005",
                    "TRD_GRP_006"
                 ],
                 "defaultSelfTradePreventionMode": "NONE",
                 "allowedSelfTradePreventionModes": [
                    "NONE",
                    "EXPIRE_TAKER",
                    "EXPIRE_MAKER",
                    "EXPIRE_BOTH"
                 ]
              }
           ]
        }
        """

        # ------------------------------------------
        end_point = "/api/v3/exchangeInfo"
        if list_symbols:
            parameters = {
                "symbols": [symbol.upper() for symbol in list_symbols]
            }
        else:
            parameters = {}
        # ------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = urlencode(parameters).replace('%2C+', ',').replace('%27', '%22')

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_latest_price_spot(self,
                              list_symbols: list = None) -> dict:
        """
        Запрос:
        Получить последнюю цену для символа или символов спота

        Полный url:
        "https://api.binance.com/api/v3/ticker/price"

        Вес запроса:
        2 для одного символа, 4 когда параметр символа отсутствует

        Параметры:
        - list_symbols="symbols" (list): актив (["BTCUSDT"], ["BTCUSDT", "ADAUSDT"], ...)

        Комментарии:
        - None

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "price": "0.27360000"
           }
        ]
        """

        # ------------------------------------------
        end_point = "/api/v3/ticker/price"
        if list_symbols:
            parameters = {
                "symbols": [symbol.upper() for symbol in list_symbols]
            }
        else:
            parameters = {}
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = urlencode(parameters).replace('%2C+', ',').replace('%27', '%22')

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_latest_trades_spot(self,
                               symbol: str,
                               limit: str = "500") -> dict:
        """
        Запрос:
        Получить последние рыночные сделки спота

        Полный url:
        "https://api.binance.com/api/v3/trades"

        Вес запроса:
        10

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - limit="limit" (str): какое количество последних сделок вывести ("1", ..., "1000")

        Комментарии:
        - Рыночные сделки означают сделки, заполненные в книге заявок.
        - Будут возвращены только рыночные сделки, это означает,
          что сделки страхового фонда и сделки ADL не будут возвращены.

        Ответ:
        [
           {
              "id": 439850393,
              "price": "0.27210000",
              "qty": "18.80000000",
              "quoteQty": "5.11548000",
              "time": 1686674419294,
              "isBuyerMaker": false,
              "isBestMatch": true
           },
           {
              "id": 439850394,
              "price": "0.27200000",
              "qty": "56.80000000",
              "quoteQty": "15.44960000",
              "time": 1686674419693,
              "isBuyerMaker": true,
              "isBestMatch": true
           }
        ]
        """

        # ------------------------------------------
        end_point = "/api/v3/trades"
        parameters = {
            "symbol": symbol.upper(),
            "limit": limit
        }
        # ------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_merged_trades_spot(self,
                               symbol: str,
                               from_id: str = None,
                               start_time: str = None,
                               end_time: str = None,
                               limit: str = "500") -> dict:
        """
        Запрос:
        Получить объединенные сделки спота

        Полный url:
        "https://api.binance.com/api/v3/aggTrades"

        Вес запроса:
        2

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - from_id="fromId": (str): идентификатор объединенной сделки от которой будет
          произведён вывод следующих объединенных сделок ("567887", ...)
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): какое количество объединенных сделок вывести ("1", ..., "1000")

        Комментарии:
        - Рыночные сделки, которые занимают 100 мс с одной и той же ценой и одной и той же стороной,
          будут иметь агрегированное количество.
        - Если отправлены и "startTime", и "endTime", время между "startTime" и "endTime" должно быть меньше 1 часа.
        - Если "fromId", "startTime" и "endTime" не отправлены, будут возвращены самые последние совокупные сделки.
        - Только рыночные сделки будут объединены и возвращены, что означает,
          что сделки страхового фонда и сделки ADL не будут объединены.
        - Отправка как "startTime"/"endTime", так и "fromId" может привести к тайм-ауту ответа,
          отправьте либо "fromId", либо "startTime"/"endTime"

        Ответ:
        [
            {
              "a": 1694766796,  (ID сделки)
              "p": "29438.90",  (цена)
              "q": "0.004",  (объем)
              "f": 3576795159,  (ID первой сделки)
              "l": 3576795159,  (ID последней сделки)
              "T": 1681744105358,  (время)
              "m": true  (совершена ли сделка по market trades)
            },
            {
              "a": 1694766797,
              "p": "29439.00",
              "q": "0.067",
              "f": 3576795160,
              "l": 3576795160,
              "T": 1681744105365,
              "m": false
            }
        ]
        """

        # ---------------------------------------------
        end_point = "/api/v3/aggTrades"
        parameters = {
            "symbol": symbol.upper(),
            "limit": limit,
            "fromId": from_id,
            "startTime": start_time,
            "endTime": end_time
        }
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_rolling_statistics_spot(self,
                                    list_symbols: list,
                                    window_size: str = "1d",
                                    my_type: str = "FULL") -> dict:
        """
        Запрос:
        Получить статистику изменения цены спота в скользящем окне

        Полный url:
        "https://api.binance.com/api/v3/ticker"

        Вес запроса:
        4 для каждого запрошенного символа независимо от размера окна
        Макс 200, если количество символов в запросе превысит 50.

        Параметры:
        - list_symbols="symbols" (list): актив (["BTCUSDT"], ["BTCUSDT", "ADAUSDT"], ...)
        - window_size="windowSize" (str): ... ("1m", "7m", "23", ...."59m" - минута, "1h",
                                               "13h", ...."23h" - час, "1d", ..."7d" - день)

        - my_type="my_type" (str): ... ("FULL","MINI")

        Комментарии:
        - Будьте осторожны при доступе к этому без символа.

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "priceChange": "-0.00140000",
              "priceChangePercent": "-0.508",
              "weightedAvgPrice": "0.27829560",
              "openPrice": "0.27540000",
              "highPrice": "0.28960000",
              "lowPrice": "0.26840000",
              "lastPrice": "0.27400000",
              "volume": "164931358.20000000",
              "quoteVolume": "45899670.84442000",
              "openTime": 1686597120000,
              "closeTime": 1686683573607,
              "firstId": 439721518,
              "lastId": 439858217,
              "count": 136700
           }
        ]
        """

        # ------------------------------------------
        end_point = "/api/v3/ticker"
        if list_symbols:
            parameters = {
                "symbols": [symbol.upper() for symbol in list_symbols],
                "windowSize": window_size,
                "type": my_type
            }
        else:
            parameters = {
                "windowSize": window_size,
                "type": my_type
            }
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = urlencode(parameters).replace('%2C+', ',').replace('%27', '%22')

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_server_time_spot(self) -> dict:
        """
        Запрос:
        Получить время сервера спота

        Полный url:
        "https://api.binance.com/api/v3/time"

        Вес запроса:
        1

        Параметры:
        - None

        Комментарии:
        - None

        Ответ:
        {
            "serverTime": 1681510841571
        }
        """

        # ------------------------------------------
        end_point = "/api/v3/time"
        # -------------------------------------------

        complete_request = self.base_url + end_point

        response = requests.get(url=complete_request)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_uicandles_spot(self,
                           symbol: str,
                           interval: str,
                           start_time: str = None,
                           end_time: str = None,
                           time_zone: str = "0",
                           limit: str = "500") -> dict:
        """
        Запрос:
        Получить информацию по свечам спота

        Полный url:
        "https://api.binance.com/api/v3/uiklines"

        Вес запроса:
        2

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - interval="interval" (str): интервал свечи ("1m", "3m", "5m", "15m", "30m", "1h", "2h",
                                                     "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - time_zone="timeZone" (str): временной интервал часы:минуты-(-1:00, 05:45)
                                                         только часы-(0, 8, 4)
        - limit="limit" (str): какое количество свечей вывести ("1", ..., "1500")

        Комментарии:
        - "timeZone" принимает диапазон строго от -12:00 до 14:00 включительно.
        - Если указан "timeZone", интервал интерпретируется в этом часовом поясе,
                                                                       а не в формате UTC как start_time или end_time
        - сокращения "interval": [m -> минута; h -> час; d -> день; w -> неделя; M -> месяц]
        - Если "startTime" и "endTime" не отправлены, возвращаются самые последние klines.

        Ответ:
        [
            [
                1681748820000,   (время открытие свечи)
                "29352.00",   (цена открытия свечи)
                "29385.00",   (самая высокая цена свечи)
                "29351.90",   (самая низкая цена свечи)
                "29385.00",   (цена закрытия свечи (или последняя цена))
                "414.755",   (объем в свече)
                1681748879999,   (время закрытия свечи)
                "12180316.04890",   (объем котируемого актива)
                3226,   (сделок в свече)
                "303.985",   (Taker buy base asset volume)
                "8926873.01530",   (Taker buy quote asset volume)
                "0"   (Ignore)
            ],
            [
                1681748880000,
                "29385.00",
                "29385.00",
                "29379.30",
                "29381.30",
                "65.643",
                1681748939999,
                "1928766.40370",
                729,
                "41.395",
                "1216276.73170",
                "0"
            ]
        ]
        """

        # ---------------------------------------------
        end_point = "/api/v3/uiKlines"
        parameters = {
            "symbol": symbol.upper(),
            "interval": interval,
            "limit": limit,
            "startTime": start_time,
            "endTime": end_time,
            "timeZone": time_zone
        }
        # ---------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters

        response = requests.get(url=complete_request, params=complete_parameters)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    async def get_stream_best_price_quantity_symbol_spot(self,
                                                         list_data: list,
                                                         symbol: list[list[str]],
                                                         method: str = "SUBSCRIBE",
                                                         my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим лучшей цены и количества спота по символу


        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@bookTicker"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: моментально
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "u":400900217,   (идентификатор обновления книги заказов)
            "s":"BNBUSDT",   (символ)
            "b":"25.35190000",   (лучшая цена bid)
            "B":"31.21000000",   (лучшая ставка bid)
            "a":"25.36520000",   (лучшая цена ask)
            "A":"40.66000000"   (лучшая ставка ask)
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@bookTicker" for data in symbol]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим лучшей цены и количества спота по символу запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим лучшей цены и количества спота по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим лучшей цены и количества спота по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_candles_spot(self,
                                      list_data: list,
                                      symbol_interval: list[list[str, str]],
                                      method: str = "SUBSCRIBE",
                                      my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим свечей спота

        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@kline_{interval}"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol_interval (list[list[str, str], ...]): список данных по стриму - символ_интервал ([["btcusdt", "1m"],
                                                                                                ["bnbusdt", "5m"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 1000мс для interval "1c" и 2000мс для всех остальных interval
        - symbol_interval вариант заполнения: [["btcusdt" или "bnbusdt" ..., "1m", "3m", "5m", "15m", "30m",
                                                "1h", "2h", "4h", "6h", 8h, "12h", "1d", "3d", "1w", "1M"], ...]
        - symbol_interval значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e":"kline",   (тип события)
            "E":1607443058651,   (время события)
            "s":"BTCUSDT",   (пара)
            "k":{
                    "t":1607443020000,   (время начала свечи)
                    "T":1607443079999,   (время завершения свечи)
                    "s":"BTCUSDT",   (символ)
                    "i":"1m",   (интервал)
                    "f":116467658886,   (идентификатор первой сделки)
                    "L":116468012423,   (идентификатор последний сделки)
                    "o":"18787.00",   (цена открытия)
                    "c":"18804.04",   (цена закрытия)
                    "h":"18804.04",   (максимальная цена)
                    "l":"18786.54",   (минимальная цена)
                    "v":"197.664",   (объем)
                    "n": 543,   (количество сделок)
                    "x":false,   (закрыта ли свеча?)
                    "q":"3715253.19494",   (объем котируемого актива)
                    "V":"184.769",   (Taker buy volume)
                    "Q":"3472925.84746",   (Taker buy quote asset volume)
                    "B":"0"   (Ignore)
            }
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@kline_{data[1]}" for data in symbol_interval]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим свечей спота запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим свечей спота разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим свечей спота разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_info_day_all_spot(self,
                                           list_data: list,
                                           method: str = "SUBSCRIBE",
                                           my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по информации о всех символах спота за 24 часа

        Полный url:
        "wss://stream.binance.com:9443/ws!ticker@arr"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 1000мс
        - Это НЕ статистика дня UTC, а 24-часовое скользящее окно от времени запроса.
        - Обратите внимание, что в массиве будут присутствовать только измененные тикеры.
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        [
            {
                "e": "24hrTicker",   (тип события)
                "E": 123456789,   (время события)
                "s": "BTCUSDT",   (символ)
                "p": "0.0015",   (изменение цены)
                "P": "250.00",   (изменение цены в процентах)
                "w": "0.0018",   (Weighted average price)
                "x": "0,0009",  (Цена первой сделки (F)-1 (первая сделка до 24-часового скользящего окна))
                "c": "0.0025",  (последняя цена)
                "Q": "10",   (последнее количество)
                "b":"25.35190000",   (лучшая цена bid)
                "B":"31.21000000",   (лучшая ставка bid)
                "a":"25.36520000",   (лучшая цена ask)
                "A":"40.66000000"   (лучшая ставка ask)
                "o": "0.0010",   (цена открытия)
                "h": "0.0025",   (максимальная цена)
                "l": "0.0010",   (минимальная цена)
                "v": "10000",   (общий торгуемый объем базовых активов)
                "q": "18",   (Общий торгуемый объем котировочного актива)
                "O": 0,   (время открытия статистики)
                "C": 86400000,   (время закрытия статистики)
                "F": 0,   (идентификатор первой сделки)
                "L": 18150,   (идентификатор последней сделки)
                "n": 18151   (количество сделок)
            }
        ]
        """

        # ----------------------------------------------
        streams = ["!ticker@arr"]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим по информации о всех символах спота за 24 часа запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим по информации о всех символах спота за 24 часа разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим по информации о всех символах спота за 24 часа разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_info_day_symbol_spot(self,
                                              list_data: list,
                                              symbol: list[list[str]],
                                              method: str = "SUBSCRIBE",
                                              my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по информации об определенном символе спота за 24 часа

        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@ticker"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 1000мс
        - Это НЕ статистика дня UTC, а 24-часовое скользящее окно от времени запроса.
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e": "24hrTicker",   (тип события)
            "E": 123456789,   (время события)
            "s": "BTCUSDT",   (символ)
            "p": "0.0015",   (изменение цены)
            "P": "250.00",   (изменение цены в процентах)
            "w": "0.0018",   (Weighted average price)
            "x": "0,0009",  (Цена первой сделки (F)-1 (первая сделка до 24-часового скользящего окна))
            "c": "0.0025",  (последняя цена)
            "Q": "10",   (последнее количество)
            "b": "0.0024",   (лучшая цена по bid)
            "B": "10",  (лучшие количество по bid)
            "a": "0.0026",   (лучшая цена по ask)
            "A": "100",   (лучшая количество по ask)
            "o": "0.0010",   (цена открытия)
            "h": "0.0025",   (максимальная цена)
            "l": "0.0010",   (минимальная цена)
            "v": "10000",   (общий торгуемый объем базовых активов)
            "q": "18",   (Общий торгуемый объем котировочного актива)
            "O": 0,   (время открытия статистики)
            "C": 86400000,   (время закрытия статистики)
            "F": 0,   (идентификатор первой сделки)
            "L": 18150,   (идентификатор последней сделки)
            "n": 18151   (количество сделок)
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@ticker" for data in symbol]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим по информации об определенном символе спота за 24 часа запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим по информации об определенном символе спота за 24 часа разрыв соединения. Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError."
                )
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим по информации об определенном символе спота за 24 часа разрыв соединения. Восстанавливаем.\n"
                    "Ошибка: socket.gaierror."
                )
                await asyncio.sleep(10)

    async def get_stream_info_rolling_all_spot(self,
                                               list_data: list,
                                               winsizes: str,
                                               method: str = "SUBSCRIBE",
                                               my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по информации о всех символах спота в скользящем окне

        Полный url:
        "wss://stream.binance.com:9443/ws!ticker_{window_size}@arr"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - winsize (str): список размера окна ("1h", "4h", "1d")
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 1000мс
        - Это НЕ статистика дня UTC, а 24-часовое скользящее окно от времени запроса.
        - winsizes значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        [
            {
                "e": "1hTicker",   (тип события)
                "E": 123456789,   (время события)
                "s": "BTCUSDT",   (символ)
                "p": "0.0015",   (изменение цены)
                "P": "250.00",   (изменение цены в процентах)
                "w": "0.0018",   (Weighted average price)
                "o": "0.0010",   (цена открытия)
                "h": "0.0025",   (максимальная цена)
                "l": "0.0010",   (минимальная цена)
                "c": "0.0025",  (последняя цена)
                "v": "10000",   (общий торгуемый объем базовых активов)
                "q": "18",   (Общий торгуемый объем котировочного актива)
                "O": 0,   (время открытия статистики)
                "C": 86400000,   (время закрытия статистики)
                "F": 0,   (идентификатор первой сделки)
                "L": 18150,   (идентификатор последней сделки)
                "n": 18151   (количество сделок)
            }
        ]
        """

        # ----------------------------------------------
        streams = [f"!ticker_{winsizes}@arr"]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим по информации о всех символах спота в скользящем окне запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим по информации о всех символах спота в скользящем окне разрыв соединения. Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError."
                )
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим по информации о всех символах спота в скользящем окне разрыв соединения. Восстанавливаем.\n"
                    "Ошибка: socket.gaierror."
                )
                await asyncio.sleep(10)

    async def get_stream_info_rolling_symbol_spot(self,
                                                  list_data: list,
                                                  symbol_winsizes: list[list[str]],
                                                  method: str = "SUBSCRIBE",
                                                  my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по информации об определенном символе спота в скользящем окне

        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@ticker_{window_size}"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol_winsize (list[list[str, str], ...]): список символ_размер окна ([["btcusdt", "1h"],
                                                                                  ["bnbusdt", "1d"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 1000мс
        - Это НЕ статистика дня UTC, а 24-часовое скользящее окно от времени запроса.
        - symbol_winsizes вариант заполнения: [["btcusdt", "1h"], ["btcusdt", "4h"], ["btcusdt", "1d"], ...]
        - symbol_winsizes значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e": "1hTicker",   (тип события)
            "E": 123456789,   (время события)
            "s": "BTCUSDT",   (символ)
            "p": "0.0015",   (изменение цены)
            "P": "250.00",   (изменение цены в процентах)
            "w": "0.0018",   (Weighted average price)
            "o": "0.0010",   (цена открытия)
            "h": "0.0025",   (максимальная цена)
            "l": "0.0010",   (минимальная цена)
            "c": "0.0025",  (последняя цена)
            "v": "10000",   (общий торгуемый объем базовых активов)
            "q": "18",   (Общий торгуемый объем котировочного актива)
            "O": 0,   (время открытия статистики)
            "C": 86400000,   (время закрытия статистики)
            "F": 0,   (идентификатор первой сделки)
            "L": 18150,   (идентификатор последней сделки)
            "n": 18151   (количество сделок)
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@ticker_{data[1]}" for data in symbol_winsizes]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим по информации об определенном символе спота в скользящем окне запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим по информации об определенном символе спота в скользящем окне разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError."
                )
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим по информации об определенном символе спота в скользящем окне разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: socket.gaierror."
                )
                await asyncio.sleep(10)

    async def get_stream_min_info_day_all_spot(self,
                                               list_data: list,
                                               method: str = "SUBSCRIBE",
                                               my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по минимальной информации о всех символах спота за 24 часа

        Полный url:
        "wss://stream.binance.com:9443/ws!miniTicker@arr"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 1000мс
        - Это НЕ статистика дня UTC, а 24-часовое скользящее окно от времени запроса.
        - Обратите внимание, что в массиве будут присутствовать только измененные тикеры.
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        [
            {
                "e": "24hrMiniTicker",   (тип события)
                "E": 123456789,   (время события)
                "s": "BTCUSDT",   (символ)
                "c": "0.0025",   (цена закрытия)
                "o": "0.0010",   (цена открытия)
                "h": "0.0025",   (максимальная цена)
                "l": "0.0010",   (минимальная цена)
                "v": "10000",   (Total traded base asset volume)
                "q": "18"   (Total traded quote asset volume)
            }
        ]
        """

        # ----------------------------------------------
        streams = ["!miniTicker@arr"]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим по минимальной информации о всех символах спота за 24 часа запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим по минимальной информации о всех символах спота за 24 часа разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError."
                )
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим по минимальной информации о всех символах спота за 24 часа разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: socket.gaierror."
                )
                await asyncio.sleep(10)

    async def get_stream_min_info_day_symbol_spot(self,
                                                  list_data: list,
                                                  symbol: list[list[str]],
                                                  method: str = "SUBSCRIBE",
                                                  my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по минимальной информации об определенном символе спота за 24 часа

        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@miniTicker"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 1000мс
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e": "24hrMiniTicker",   (тип события)
            "E": 123456789,   (время события)
            "s": "BTCUSDT",   (символ)
            "c": "0.0025",   (цена закрытия)
            "o": "0.0010",   (цена открытия)
            "h": "0.0025",   (максимальная цена)
            "l": "0.0010",   (минимальная цена)
            "v": "10000",   (Total traded base asset volume)
            "q": "18"   (Total traded quote asset volume)
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@miniTicker" for data in symbol]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим по минимальной информации об определенном символе спота за 24 часа запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим по минимальной информации об определенном символе спота за 24 часа разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError."
                )
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим по минимальной информации об определенном символе спота за 24 часа разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: socket.gaierror."
                )
                await asyncio.sleep(10)

    async def get_stream_order_book_difference_spot(self,
                                                    list_data: list,
                                                    symbol_speed: list[list[str, str]],
                                                    method: str = "SUBSCRIBE",
                                                    my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        ...

        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@depth@{speed}ms"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol_speed (list[list[str, str]]): список данных по стриму - актив_скорость стрима ([["btcusdt", "100"],
                                                                                            ["bnbusdt", "1000"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 100мс или 1000мс
        - symbol_speed вариант заполнения: [["btcusdt" или "bnbusdt" ...,  "100" или "1000"], ...]
        - symbol_speed значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e": "depthUpdate",   (тип события)
            "E": 1571889248277,   (время события)
            "s": "BTCUSDT",   (символ)
            "U": 390497796,   (Идентификатор первого обновления в событии)
            "u": 390497878,   (Окончательный идентификатор обновления в событии)
            "b": [   (Bids)
                    [
                        "7403.89",  (цена)
                        "0.002"   (количество)
                    ]
            ],
            "a": [   (Asks)
                    [
                        "7405.96",   (цена)
                        "3.340"   (количество)
                    ]
            ]
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@depth@{data[1]}ms" for data in symbol_speed]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим по ... запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим по ... разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим по ... разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_order_book_spot(self,
                                         list_data: list,
                                         symbol_quantity_speed: list[list[str, str, str]],
                                         method: str = "SUBSCRIBE",
                                         my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим стакана ордеров спота

        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@depth{quantity}@{speed}ms"

        Параметры:
        - list_data (list): аргумент в который будут записываться данные стрима ([])
        - symbol_quantity_speed (list[list[str, str, str]]): список данных по стрима -
                                                    актив_глубина стакана_скорость стрима ([["btcusdt", "10", "100"]])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 100мс или 1000мс
        - symbol_quantity_speed вариант заполнения: [["btcusdt" или "bnbusdt" и т.д.,
                                                      "5" или "10" или "20",
                                                      "100" или "1000"]
        - symbol_quantity_speed значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            'lastUpdateId': 7379433651,   (идентификатор последнего обновления)
            'bids':[   (Bids)
                [
                    '0.26080000',   (обновляемый уровень цены)
                    '35190.90000000'   (количество)
                ],
            ],
            'asks':[   (Asks)
                [
                    '0.26090000',   (обновляемый уровень цены)
                    '36457.60000000'   (количество)
                ],
            ]
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@depth{data[1]}@{data[2]}ms" for data in symbol_quantity_speed]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим стакана ордеров спота запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим стакана ордеров спота разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим стакана ордеров спота разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_id_trades_tape_spot(self,
                                             list_data: list,
                                             symbol: list[list[str]],
                                             method: str = "SUBSCRIBE",
                                             my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим ленты id-сделок спота покупателя и продавца по символу

        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@trade"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: моментально
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]
        - Будут агрегированы только рыночные сделки, что означает,
        что сделки страхового фонда и сделки ADL не будут агрегированы.

        Ответ:
        {
            "e": "trade",   (тип события)
            "E": 123456789,   (время события)
            "s": "BNBBTC",   (символ)
            "t": 12345,   (идентификатор сделки)
            "p": "0.001",   (цена)
            "q": "100",   (количество)
            "b": 88,   (идентификатор заказа покупателя)
            "a": 50,   (идентификатор заказа продавца)
            "T": 123456785,   (время совершения сделки)
            "m": true,   (является ли покупатель маркет-мейкером?)
            "M": true   (игнорировать)
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@trade" for data in symbol]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим ленты id-сделок спота покупателя и продавца по символу запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим ленты id-сделок спота покупателя и продавца по символу разрыв соединения. Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим ленты id-сделок спота покупателя и продавца по символу разрыв соединения. Восстанавливаем.\n"
                    "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_trades_tape_spot(self,
                                          list_data: list,
                                          symbol: list[list[str]],
                                          method: str = "SUBSCRIBE",
                                          my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим ленты сделок спота по символу

        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@aggTrade"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: моментально
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]
        - Будут агрегированы только рыночные сделки, что означает,
          что сделки страхового фонда и сделки ADL не будут агрегированы.

        Ответ:
        {
            "e": "aggTrade",   (тип события)
            "E": 123456789,   (время события)
            "s": "BTCUSDT",   (символ)
            "a": 5933014,   (идентификатор сделки)
            "p": "0.001",   (цена)
            "q": "100",   (количество)
            "f": 100,   (идентификатор первой сделки)
            "l": 105,   (идентификатор последний сделки)
            "T": 123456785,   (время торговли)
            "m": true,   (является ли покупатель маркет-мейкером?)
            "M": true   (игнорировать)
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@aggTrade" for data in symbol]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим ленты сделок спота по символу запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим ленты сделок спота по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим ленты сделок спота по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_average_price_spot(self,
                                            list_data: list,
                                            symbol: list[list[str]],
                                            method: str = "SUBSCRIBE",
                                            my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим средней цены по символам

        Полный url:
        "wss://stream.binance.com:9443/ws{symbol}@avgPrice"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - скорость обновления: 1000мс
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e": "avgPrice",    (тип события)
            "E": 1693907033000,    (время события)
            "s": "BTCUSDT",    (символ)
            "i": "5m",    (средний ценовой интервал)
            "w": "25776.86000000",    (средняя цена)
            "T": 1693907032213    (время последней сделки)
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@avgPrice" for data in symbol]
        # ----------------------------------------------

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": streams,
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("Стрим средней цены по символам запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим средней цены по символам разрыв соединения. Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError."
                )
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим средней цены по символам разрыв соединения. Восстанавливаем.\n"
                    "Ошибка: socket.gaierror."
                )
                await asyncio.sleep(10)
