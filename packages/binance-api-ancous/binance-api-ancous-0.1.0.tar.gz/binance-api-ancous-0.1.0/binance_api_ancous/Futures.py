"""
pass
"""

import hmac
import json
import socket
import asyncio
import hashlib
import requests
import websockets.exceptions

from typing import Any
from random import randint
from urllib.parse import urlencode


class Futures:
    """
    Класс для работы с фьючерсами

    Attributes:
    base_url (str): базовый url для доступа к фьючерсам бирже binance
    base_url_stream (str): базовый url для доступа к стримам фьючерса бирже binance

    Methods:

        Market data endpoints futures:
            connection_check: проверка соединения
            get_best_price_quantity_futures: лучшая цена и количество для символа или символов
            get_candles_futures: информация по свечам
            get_candles_blvt_nav_futures: информация по историческим свечам BLVT NAV
            get_candles_contract_futures: информация по свечам для определенного контракта
            get_candles_indexprice_futures: информация по свечам для Index Price
            get_candles_markprice_futures: информация по свечам для Mark Price
            get_day_statistics_futures: статистика изменения цены за 24 часа
            get_glass_applications_futures: стакан заявок
            get_history_funding_rate_futures: история ставок финансирования
            get_info_funding_rate_futures: информация о ставках финансирования
            get_historical_trades_futures: исторические рыночные сделки по "fromId"
            get_index_composite_symbol_futures: информация о символах составного индекса
            get_symbols_info_futures: текущие правила биржевой торговли и информация о символах
            get_latest_price_futures: последняя цена для символа или символов
            get_latest_trades_futures: последние рыночные сделки
            get_mark_price_funding_rate_futures: цена маркировки и ставки финансирования
            get_merged_trades_futures: объединенные сделки
            get_multiassets_futures: индекс активов для режима Multi-Assets
            get_ratio_long_short_account_futures: общее соотношение количества long/short счетов
            get_server_time_futures: время сервера
            get_top_ratio_long_short_account_futures: общее соотношение количества long/short счетов ведущих трейдеров
            get_top_ratio_long_short_position_futures: общее соотношение количества long/short позиций ведущих трейдеров
            get_volume_buy_sell_futures: объем покупок и продаж
            get_current_open_interest_futures: текущий открытый интерес
            get_historical_open_interest_futures: история открытого интереса
            get_basis_futures: информация по basis
            get_quarterly_settlement_price_contract_futures: расчетная цена контракта по кварталу
            get_index_price_components_futures: составляющие индекс цены символа

        Market data streams futures:
            get_stream_best_price_quantity_all_futures: лучшая цена и количество всех символов
            get_stream_best_price_quantity_symbol_futures: лучшая цена и количество по символу
            get_stream_candles_futures: свечи
            get_stream_candles_contract_futures: свечи по контракту
            get_stream_composite_index_futures: стакан ордеров составного индекса
            get_stream_contract_info_futures: ...
            get_stream_info_day_all_futures: информация о всех символах за 24 часа
            get_stream_info_day_symbol_futures: информация об определенном символе за 24 часа
            get_stream_liquidated_orders_all_futures: ликвидированные ордера по всем символам
            get_stream_liquidated_orders_symbol_futures: ликвидированные ордера по символу
            get_stream_mark_price_funding_rate_all_futures: mark price и ставка финансирования всех символов
            get_stream_mark_price_funding_rate_symbol_futures: mark price и ставка финансирования по символу
            get_stream_min_info_day_all_futures: минимальная информация о всех символах за 24 часа
            get_stream_min_info_day_symbol_futures: минимальная информация об определенном символе за 24 часа
            get_stream_order_book_futures: стакан ордеров
            get_stream_order_book_difference_futures: ...
            get_stream_trades_tape_futures: лента сделок по символу
            get_stream_asset_index_in_multi_assets: индексы активов в режиме мультиактива

        Trading endpoints futures:
            post_leverage_futures: изменить кредитное плечо
            post_margin_futures: изменить количество маржи изолированной позиции
            post_margin_type_futures: изменить маржинальное поле ("ИЗОЛИРОВАННАЯ", "ПЕРЕСКРЕСТНАЯ")
            get_balance_account_futures: баланс фьючерсного счета
            get_commission_rate_futures: ставки комиссии актива
            get_estimation_adl_futures: оценки ADL позиций
            get_force_orders_futures: принудительные сделки
            get_ftqri_futures: ...
            get_income_history_futures: история доходов
            get_info_account_futures: текущая информация об учетной записи
            get_margin_change_history_futures: история изменения маржи
            get_nl_brackets_futures: ...
            get_update_order_history_futures: история изменений ордеров
            get_id_deals_futures: идентификатор для загрузки истории сделок с фьючерсами
            get_link_deals_futures: ссылка для скачивания истории сделок с фьючерсами по идентификатору
            get_id_orders_futures: идентификатор для загрузки истории заказов с фьючерсами
            get_link_orders_futures: ссылка для скачивания истории заказов с фьючерсами по идентификатору
            get_id_trades_futures: идентификатор для загрузки истории торговли с фьючерсами
            get_link_trades_futures: ссылка для скачивания истории торговли с фьючерсами по идентификатору
            post_multi_asset_futures: изменить режим мультиактива
            get_multi_asset_futures: режим мультиактива
            post_position_futures: изменить режим позиции
            get_positions_futures: режим позиции
            post_limit_futures: ордер LIMIT
            post_market_futures: ордер MARKET
            post_profit_limit_futures: ордер TAKE_PROFIT
            post_profit_market_futures: ордер TAKE_PROFIT_MARKET
            post_stop_limit_futures: ордер STOP
            post_stop_market_futures: ордер STOP_MARKET
            post_trailing_stop_market_futures: ордер TRAILING_STOP_MARKET
            put_limit_futures: обновить ордер LIMIT
            delete_order_futures: закрыть ордер по идентификатору
            post_multiple_limit_futures: множественный ордер LIMIT
            post_multiple_market_futures: множественный ордер MARKER
            post_multiple_profit_limit_futures: множественный ордер TAKE_PROFIT
            post_multiple_profit_market_futures: множественный ордер TAKE_PROFIT_MARKET
            post_multiple_stop_limit_futures: множественный ордер STOP
            post_multiple_stop_market_futures: множественный ордер STOP_MARKET
            post_multiple_trailing_stop_market_futures: множественный ордер TRAILING_STOP_MARKET
            put_multiple_limit_futures: обновить несколько ордеров LIMIT
            delete_multiple_order_id_futures: закрыть несколько ордеров по идентификатору
            delete_multiple_order_symbol_futures: закрыть несколько ордеров по символу
            delete_multiple_orders_time_futures: закрыть все ордера по символу через заданное время
            get_current_position_symbol_futures: информация о текущей позиции по символу
            get_open_order_id_futures: информация об открытом ордере по идентификатору
            get_open_orders_all_futures: информация о всех открытых ордерах
            get_orders_all_futures: информация о всех ордерах аккаунта
            get_trades_futures: информация о сделках

        User data streams futures:
            start_user_data_stream_futures: запуск стрима по данным пользователя
            connect_user_data_streams_futures: cтрим данных пользователя
            keepalive_user_data_stream_futures: обновление стрима по данным пользователя
            delete_user_data_stream_futures: закрытие стрима по данным пользователя
    """
    base_url = "https://fapi.binance.com"
    base_url_stream = "wss://fstream.binance.com/ws"

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

    def connection_check_futures(self) -> dict:
        """
        Запрос:
        Проверка соединения

        Полный url:
        "https://fapi.binance.com/fapi/v1/ping"

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
        end_point = "/fapi/v1/ping"
        # -------------------------------------------

        complete_request = self.base_url + end_point

        response = requests.get(url=complete_request)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_best_price_quantity_futures(self, symbol: str = "") -> dict:
        """
        Запрос:
        Получить лучшую цену и количество для символа или символов

        Полный url:
        "https://fapi.binance.com/fapi/v1/ticker/bookTicker"

        Вес запроса:
        2 для одного символа, 5 когда параметр символа отсутствует

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)

        Комментарии:
        - None

        Ответ:
        {
           "symbol": "ADAUSDT",
           "bidPrice": "0.39640",
           "bidQty": "94458",
           "askPrice": "0.39650",
           "askQty": "47959",
           "time": 1683303936182
        }
        """

        # ------------------------------------------
        end_point = "/fapi/v1/ticker/bookTicker"
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

    def get_candles_futures(self,
                            symbol: str,
                            interval: str,
                            start_time: str = None,
                            end_time: str = None,
                            limit: str = "500") -> dict:
        """
        Запрос:
        Получить информацию по свечам

        Полный url:
        "https://fapi.binance.com/fapi/v1/klines"

        Вес запроса:
        [[limits, вес], [1-100, 1], [101-500: 2], [501-1000: 5], [1001-1500: 10]]

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - interval="interval" (str): интервал свечи ("1m", "3m", "5m", "15m", "30m", "1h", "2h",
                                                     "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): какое количество свечей вывести ("1", ..., "1500")

        Комментарии:
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
        end_point = "/fapi/v1/klines"
        parameters = {
            "symbol": symbol.upper(),
            "interval": interval,
            "limit": limit,
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

    def get_candles_blvt_nav_futures(self,
                                     symbol: str,
                                     interval: str,
                                     start_time: str = None,
                                     end_time: str = None,
                                     limit: str = "500") -> dict:
        """
        Запрос:
        Получить информацию по историческим свечам BLVT NAV

        Полный url:
        "https://fapi.binance.com/fapi/v1/lvtKlines"

        Вес запроса:
        5

        Параметры:
        - symbol="symbol" (str): актив ("BTCDOWN", ...)
        - interval="interval" (str): интервал свечи ("1m", "3m", "5m", "15m", "30m", "1h", "2h",
                                                     "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): какое количество свечей вывести ("1", ..., "1000")

        Комментарии:
        - сокращения "interval": [m -> минута; h -> час; d -> день; w -> неделя; M -> месяц]
        - Рыночные сделки означают сделки, заполненные в книге заявок.
        - Будут возвращены только рыночные сделки, это означает,
          что сделки страхового фонда и сделки ADL не будут возвращены.

        Ответ:
        [
            [
                1598371200000,  (время открытия)
                "5.88275270",   (цена открытая цена NAV)
                "6.03142087",   (самая высокая цена NAV)
                "5.85749741",   (самая низкая цена NAV)
                "5.99403551",   (цена закрытия NAV (или последняя))
                "2.28602984",   (реальное кредитное плечо)
                1598374799999,   (время закрытия)
                "0",   (Ignore)
                6209,   (Количество обновлений NAV)
                "14517.64507907",   (Ignore)
                "0",   (Ignore)
                "0"   (Ignore)
            ]
        ]
        """

        # ---------------------------------------------
        end_point = "/fapi/v1/lvtKlines"
        parameters = {
            "symbol": symbol.upper(),
            "interval": interval,
            "limit": limit,
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

    def get_candles_contract_futures(self,
                                     symbol: str,
                                     interval: str,
                                     start_time: str = None,
                                     end_time: str = None,
                                     limit: str = "500",
                                     contract_type: str = "PERPETUAL") -> dict:
        """
        Запрос:
        Получить информацию по свечам для определенного контракта

        Полный url:
        "https://fapi.binance.com/fapi/v1/continuousKlines"

        Вес запроса:
        [[limits, вес], [1-100, 1], [101-500: 2], [501-1000: 5], [1001-1500: 10]]

        Параметры:
        - symbol="pair" (str): актив ("BTCUSDT", ...)
        - interval="interval" (str): интервал свечи ("1m", "3m", "5m", "15m", "30m", "1h", "2h",
                                                     "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): какое количество свечей вывести ("1", ..., "1500")
        - contract_type="contractType" (str): тип контракта ("PERPETUAL", "CURRENT_QUARTER", "NEXT_QUARTER")

        Комментарии:
        - "contractType" возможные варианты: ["PERPETUAL": - бессрочный, "CURRENT_MONTH" - текущий месяц,
                                              "NEXT_MONTH" - следующий месяц, "CURRENT_QUARTER" - текущий квартал,
                                              "NEXT_QUARTER" - следующий квартал,
                                              "PERPETUAL_DELIVERING" - постоянная доставка]
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
        end_point = "/fapi/v1/continuousKlines"
        parameters = {
            "pair": symbol.upper(),
            "interval": interval,
            "limit": limit,
            "startTime": start_time,
            "endTime": end_time,
            "contractType": contract_type
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

    def get_candles_indexprice_futures(self,
                                       symbol: str,
                                       interval: str,
                                       start_time: str = None,
                                       end_time: str = None,
                                       limit: str = "500") -> dict:
        """
        Запрос:
        Получить информацию по свечам для Index Price

        Полный url:
        "https://fapi.binance.com/fapi/v1/indexPriceKlines"

        Вес запроса:
        [[limits: вес], [1-100: 1], [101-500: 2], [501-1000: 5], [1001-1500: 10]]

        Параметры:
        - symbol="pair" (str): актив ("BTCUSDT", ...)
        - interval="interval" (str): интервал свечи ("1m", "3m", "5m", "15m", "30m", "1h", "2h",
                                                     "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("1", ..., "1500")

        Комментарии:
        - сокращения "interval": [m -> минута; h -> час; d -> день; w -> неделя; M -> месяц]
        - Если startTime и endTime не отправлены, возвращаются самые последние klines.

        Ответ:
        [
           [
              1683099900000,   (время открытие свечи)
              "0.38450809",   (цена открытия свечи)
              "0.38452420",   (самая высокая цена свечи)
              "0.38431132",   (самая низкая цена свечи)
              "0.38439531",   (цена закрытия свечи (или последняя цена))
              "0",   (Ignore)
              1683100199999,   (время закрытие свечи)
              "0",   (Ignore)
              300,   (Ignore)
              "0",   (Ignore)
              "0",   (Ignore)
              "0"   (Ignore)
           ],
           [
              1683100200000,   (время открытие свечи)
              "0.38439528",   (цена открытия свечи)
              "0.38439531",   (самая высокая цена свечи)
              "0.38433281",   (самая низкая цена свечи)
              "0.38433327",   (цена закрытия свечи (или последняя цена))
              "0",   (Ignore)
              1683100499999,   (время закрытие свечи)
              "0",   (Ignore)
              29,   (Ignore)
              "0",   (Ignore)
              "0",   (Ignore)
              "0"   (Ignore)
           ]
        ]
        """

        # ---------------------------------------------
        end_point = "/fapi/v1/indexPriceKlines"
        parameters = {
            "pair": symbol.upper(),
            "interval": interval,
            "limit": limit,
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

    def get_candles_markprice_futures(self,
                                      symbol: str,
                                      interval: str,
                                      start_time: str = None,
                                      end_time: str = None,
                                      limit: str = "500") -> dict:

        """
        Запрос:
        Получить информацию по свечам для Mark Price

        Полный url:
        "https://fapi.binance.com/fapi/v1/indexPriceKlines"

        Вес запроса:
        [[limits: вес], [1-100: 1], [101-500: 2], [501-1000: 5], [1001-1500: 10]]

        Параметры:
        - symbol="pair" (str): актив ("BTCUSDT", ...)
        - interval="interval" (str): интервал свечи ("1m", "3m", "5m", "15m", "30m", "1h", "2h",
                                                     "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("1", ..., "1500")

        Комментарии:
        - сокращения "interval": [m -> минута; h -> час; d -> день; w -> неделя; M -> месяц]
        - Если startTime и endTime не отправлены, возвращаются самые последние klines.

        Ответ:
        [
           [
              1683106200000,   (время открытие свечи)
              "0.38511536",   (цена открытия свечи)
              "0.38538294",   (самая высокая цена свечи)
              "0.38491268",   (самая низкая цена свечи)
              "0.38527970",   (цена закрытия свечи (или последняя цена))
              "0",   (Ignore)
              1683106499999,   (время закрытие свечи)
              "0",   (Ignore)
              300,   (Ignore)
              "0",   (Ignore)
              "0",   (Ignore)
              "0"   (Ignore)
           ],
           [
              1683106500000,   (время открытие свечи)
              "0.38527972",   (цена открытия свечи)
              "0.38536943",   (самая высокая цена свечи)
              "0.38512590",   (самая низкая цена свечи)
              "0.38531733",   (цена закрытия свечи (или последняя цена))
              "0",   (Ignore)
              1683106799999,   (время закрытие свечи)
              "0",   (Ignore)
              192,   (Ignore)
              "0",   (Ignore)
              "0",   (Ignore)
              "0"   (Ignore)
           ]
        ]
        """

        # ---------------------------------------------
        end_point = "/fapi/v1/indexPriceKlines"
        parameters = {
            "pair": symbol.upper(),
            "interval": interval,
            "limit": limit,
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

    def get_day_statistics_futures(self,
                                   symbol: str = "") -> dict:
        """
        Запрос:
        Получить статистику изменения цены за 24 часа

        Полный url:
        "https://fapi.binance.com/fapi/v1/ticker/24hr"

        Вес запроса:
        1 для одного символа, 40 когда параметр символа отсутствует

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)

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
        end_point = "/fapi/v1/ticker/24hr"
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

    def get_glass_applications_futures(self,
                                       symbol: str,
                                       limit: str = "500") -> dict:
        """
        Запрос:
        Получить стакан заявок

        Полный url:
        "https://fapi.binance.com/fapi/v1/depth"

        Вес запроса:
        [[limits: вес], [5, 10, 30, 50: 2], [100: 5], [500: 10], [1000: 20]]

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("5", "10", "20",
                                                                                     "50", "100", "500", "1000")

        Комментарии:
        - None

        Ответ:
        {
           "lastUpdateId": 2740723675122,
           "E": 1681512613548,  (Время вывода сообщения)
           "T": 1681512613528,  (Время транзакции)
           "bids": [
              [
                 "0.43920",  (цена)
                 "18403"  (количество)
              ],
              [
                 "0.43910",
                 "120359"
              ],
              [
                 "0.43900",
                 "105792"
              ],
              [
                 "0.43890",
                 "98038"
              ],
              [
                 "0.43880",
                 "234323"
              ]
           ],
           "asks": [
              [
                 "0.43930",
                 "82740"
              ],
              [
                 "0.43940",
                 "90407"
              ],
              [
                 "0.43950",
                 "186146"
              ],
              [
                 "0.43960",
                 "115142"
              ],
              [
                 "0.43970",
                 "127414"
              ]
           ]
        }
        """

        # ---------------------------------------------
        end_point = "/fapi/v1/depth"
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

    def get_history_funding_rate_futures(self,
                                         symbol: str = "",
                                         start_time: str = None,
                                         end_time: str = None,
                                         limit: str = "500") -> dict:
        """
        Запрос:
        Получить историю ставок финансирования

        Полный url:
        "https://fapi.binance.com/fapi/v1/fundingRate"

        Вес запроса:
        None

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("1", ..., "1000")

        Комментарии:
        - Если "startTime" и "endTime" не отправлены, возвращаются самые последние данные лимита.

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "fundingTime": 1683273600000,
              "fundingRate": "0.00010000"
           },
           {
              "symbol": "ADAUSDT",
              "fundingTime": 1683302400000,
              "fundingRate": "0.00010000"
           }
        ]
        """

        # ------------------------------------------
        end_point = "/fapi/v1/fundingRate"
        parameters = {
            "symbol": symbol.upper(),
            "limit": limit,
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

    def get_info_funding_rate_futures(self) -> dict:
        """
        Запрос:
        Получить информацию о ставках финансирования

        Полный url:
        "https://fapi.binance.com/fapi/v1/fundingInfo"

        Вес запроса:
        None

        Параметры:
        - None

        Комментарии:
        - Запросить информацию о ставке финансирования для символов, которые имеют настройку
                                                                FundingRateCap/ FundingRateFloor/ fundingIntervalHours

        Ответ:
        [
            {
                "symbol": "BLZUSDT",
                "adjustedFundingRateCap": "0.02500000",
                "adjustedFundingRateFloor": "-0.02500000",
                "fundingIntervalHours": 8,
                "disclaimer": false    (игнор)
            }
        ]
        """

        # ------------------------------------------
        end_point = "/fapi/v1/fundingInfo"
        # ---------------------------------------------

        complete_request = self.base_url + end_point

        response = requests.get(url=complete_request)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_historical_trades_futures(self,
                                      symbol: str,
                                      from_id: str = None,
                                      limit: str = "500") -> dict:
        """
        Запрос:
        Получить исторические рыночные сделки по "fromId"

        Полный url:
        "https://fapi.binance.com/fapi/v1/historicalTrades"

        Вес запроса:
        20

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
              "id": 3576730350,
              "price": "29341.00",
              "qty": "0.181",
              "quoteQty": "5310.72",
              "time": 1681742589853,
              "isBuyerMaker": true
           },
           {
              "id": 3576730351,
              "price": "29341.00",
              "qty": "0.174",
              "quoteQty": "5105.33",
              "time": 1681742589870,
              "isBuyerMaker": true
           }
        ]
        """

        # ------------------------------------
        end_point = "/fapi/v1/historicalTrades"
        api_key = self.api_key
        parameters = {
            "symbol": symbol.upper(),
            "limit": limit,
            "fromId": from_id,
        }
        # ------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": api_key
        }

        response = requests.get(url=complete_request, params=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_index_composite_symbol_futures(self,
                                           symbol: str = "") -> dict:
        """
        Запрос:
        Получить информацию о символе составного индекса

        Полный url:
        "https://fapi.binance.com/fapi/v1/indexInfo"

        Вес запроса:
        10

        Параметры:
        - symbol="symbol" (str): актив ("DEFIUSDT", ...)

        Комментарии:
        - Только для символов составного индекса

        Ответ:
        [
            {
                "symbol": "DEFIUSDT",
                "time": 1589437530011,   (текущее время)
                "component": "baseAsset",   (Актив компонента)
                "baseAssetList":[
                    {
                        "baseAsset":"BAL",
                        "quoteAsset": "USDT",
                        "weightInQuantity":"1.04406228",
                        "weightInPercentage":"0.02783900"
                    },
                    {
                        "baseAsset":"BAND",
                        "quoteAsset": "USDT",
                        "weightInQuantity":"3.53782729",
                        "weightInPercentage":"0.03935200"
                    }
                ]
            }
        ]
        """

        # ------------------------------------------
        end_point = "/fapi/v1/indexInfo"
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

    def get_symbols_info_futures(self) -> dict:
        """
        Запрос:
        Получить текущие правила биржевой торговли и информацию о символах

        Полный url:
        "https://fapi.binance.com/fapi/v1/exchangeInfo"

        Вес запроса:
        1

        Параметры:
        - None

        Комментарии:
        - None

        Ответ:
        {
            "exchangeFilters": [],
            "rateLimits": [
                {
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 2400,
                    "rateLimitType": "REQUEST_WEIGHT"
                },
                {
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "rateLimitType": "ORDERS"
                }
            ],
            "serverTime": 1565613908500,  (ignore)
            "assets": [ (информация об активах)
                {
                    "asset": "BUSD",
                    "marginAvailable": true,  (можно ли использовать актив в качестве маржи в режиме Multi-Assets)
                    "autoAssetExchange": 0  (порог автоматического обмена в режиме маржи Multi-Assets)
                },
                {
                    "asset": "USDT",
                    "marginAvailable": true,
                    "autoAssetExchange": 0
                },
                {
                    "asset": "BNB",
                    "marginAvailable": false,
                    "autoAssetExchange": null
                }
            ],
            "symbols": [
                {
                    "symbol": "BLZUSDT",
                    "pair": "BLZUSDT",
                    "contractType": "PERPETUAL",
                    "deliveryDate": 4133404800000,
                    "onboardDate": 1598252400000,
                    "status": "TRADING",
                    "maintMarginPercent": "2.5000",  (ignore)
                    "requiredMarginPercent": "5.0000",  (ignore)
                    "baseAsset": "BLZ",
                    "quoteAsset": "USDT",
                    "marginAsset": "USDT",
                    "pricePrecision": 5,  (пожалуйста, не используйте его как tickSize)
                    "quantityPrecision": 0,  (пожалуйста, не используйте его как stepSize)
                    "baseAssetPrecision": 8,
                    "quotePrecision": 8,
                    "underlyingType": "COIN",
                    "underlyingSubType": ["STORAGE"],
                    "settlePlan": 0,
                    "triggerProtect": "0.15",  (порог для алгоритмического заказа с "priceProtect")
                    "filters": [
                        {
                            "filterType": "PRICE_FILTER",
                            "maxPrice": "300",
                            "minPrice": "0.0001",
                            "tickSize": "0.0001"
                        },
                        {
                            "filterType": "LOT_SIZE",
                            "maxQty": "10000000",
                            "minQty": "1",
                            "stepSize": "1"
                        },
                        {
                            "filterType": "MARKET_LOT_SIZE",
                            "maxQty": "590119",
                            "minQty": "1",
                            "stepSize": "1"
                        },
                        {
                            "filterType": "MAX_NUM_ORDERS",
                            "limit": 200
                        },
                        {
                            "filterType": "MAX_NUM_ALGO_ORDERS",
                            "limit": 100
                        },
                        {
                            "filterType": "MIN_NOTIONAL",
                            "notional": "5.0",
                        },
                        {
                            "filterType": "PERCENT_PRICE",
                            "multiplierUp": "1.1500",
                            "multiplierDown": "0.8500",
                            "multiplierDecimal": 4
                        }
                    ],
                    "OrderType": [
                        "LIMIT",
                        "MARKET",
                        "STOP",
                        "STOP_MARKET",
                        "TAKE_PROFIT",
                        "TAKE_PROFIT_MARKET",
                        "TRAILING_STOP_MARKET"
                    ],
                    "timeInForce": [
                        "GTC",
                        "IOC",
                        "FOK",
                        "GTX"
                    ],
                    "liquidationFee": "0.010000",  (ставка ликвидационного сбора)
                    "marketTakeBound": "0.30",  (максимальная разница в цене (от цены маркировки),
                                                 которую может сделать рыночный ордер)
                }
            ],
            "timezone": "UTC"
        }
        """

        # ------------------------------------------
        end_point = "/fapi/v1/exchangeInfo"
        # ------------------------------------------

        complete_request = self.base_url + end_point

        response = requests.get(url=complete_request)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_latest_price_futures(self,
                                 symbol: str = "") -> dict:
        """
        Запрос:
        Получить последнюю цену для символа или символов.

        Полный url:
        "https://fapi.binance.com/fapi/v2/ticker/price"

        Вес запроса:
        1 для одного символа, 2 когда параметр символа отсутствует

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)

        Комментарии:
        - None

        Ответ:
        {
           "symbol": "ADAUSDT",
           "price": "0.39480",
           "time": 1683304657958
        }
        """

        # ------------------------------------------
        end_point = "/fapi/v2/ticker/price"
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

    def get_latest_trades_futures(self,
                                  symbol: str,
                                  limit: str = "500") -> dict:
        """
        Запрос:
        Получить последние рыночные сделки

        Полный url:
        "https://fapi.binance.com/fapi/v1/trades"

        Вес запроса:
        5

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
              "id": 3576719543,
              "price": "29377.90",
              "qty": "0.001",
              "quoteQty": "29.37",
              "time": 1681742436170,
              "isBuyerMaker": false
           },
           {
              "id": 3576719544,
              "price": "29377.90",
              "qty": "0.064",
              "quoteQty": "1880.18",
              "time": 1681742436170,
              "isBuyerMaker": false
           }
        ]
        """

        # ------------------------------------------
        end_point = "/fapi/v1/trades"
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

    def get_mark_price_funding_rate_futures(self,
                                            symbol: str = "") -> dict:
        """
        Запрос:
        Получить цену маркировки и ставку финансирования

        Полный url:
        "https://fapi.binance.com/fapi/v1/premiumIndex"

        Вес запроса:
        10

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)

        Комментарии:
        - None

        Ответ:
        {
           "symbol": "ADAUSDT",
           "markPrice": "0.39400632",   (цена маркировки)
           "indexPrice": "0.39409565",   (цена индекса)
           "estimatedSettlePrice": "0.39385576",   (ориентировочная расчетная цена,
                                                    полезная только в последний час перед началом расчета.)
           "lastFundingRate": "0.00010000",   (ставка финансирования)
           "interestRate": "0.00010000",
           "nextFundingTime": 1683331200000,
           "time": 1683311719000
        }
        """

        # ------------------------------------------
        end_point = "/fapi/v1/premiumIndex"
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

    def get_merged_trades_futures(self,
                                  symbol: str,
                                  from_id: str = None,
                                  start_time: str = None,
                                  end_time: str = None,
                                  limit: str = "500") -> dict:
        """
        Запрос:
        Получить объединенные сделки

        Полный url:
        "https://fapi.binance.com/fapi/v1/aggTrades"

        Вес запроса:
        20

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - from_id="fromId": (str): идентификатор объединенной сделки от которой
          будет произведён вывод следующих объединенных сделок ("567887", ...)
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
        end_point = "/fapi/v1/aggTrades"
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

    def get_multiassets_futures(self,
                                symbol: str = "") -> dict:
        """
        Запрос:
        Получить индекс активов для режима Multi-Assets

        Полный url:
        "https://fapi.binance.com/fapi/v1/assetIndex"

        Вес запроса:
        1 для одного символа, 10 когда параметр символа отсутствует

        Параметры:
        - symbol="symbol" (str): актив ("ADAUSD", ...)

        Комментарии:
        - None

        Ответ:
        {
            "symbol": "ADAUSD",
            "time": 1635740268004,
            "index": "1.92957370",
            "bidBuffer": "0.10000000",
            "askBuffer": "0.10000000",
            "bidRate": "1.73661633",
            "askRate": "2.12253107",
            "autoExchangeBidBuffer": "0.05000000",
            "autoExchangeAskBuffer": "0.05000000",
            "autoExchangeBidRate": "1.83309501",
            "autoExchangeAskRate": "2.02605238"
        }
        """

        # ------------------------------------------
        end_point = "/fapi/v1/assetIndex"
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

    def get_ratio_long_short_account_futures(self,
                                             symbol: str,
                                             period: str,
                                             start_time: str = None,
                                             end_time: str = None,
                                             limit: str = "30") -> dict:
        """
        Запрос:
        Получить общее соотношение количества длинных/коротких счетов

        Полный url:
        "https://fapi.binance.com/futures/data/globalLongShortAccountRatio"

        Вес запроса:
        None

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - period="period" (str): период для высчитывания ("5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("1", ..., "500")

        Комментарии:
        - Если startTime и endTime не отправлены, возвращаются самые последние данные.
        - Доступны только данные за последние 30 дней.

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "longAccount": "0.7525",   (общее соотношение количества длинных счетов)
              "longShortRatio": "3.0404",   (общее соотношение количества длинных/коротких счетов)
              "shortAccount": "0.2475",   (общее соотношение количества коротких счетов)
              "timestamp": 1683297300000
           },
           {
              "symbol": "ADAUSDT",
              "longAccount": "0.7497",   (общее соотношение количества длинных счетов)
              "longShortRatio": "2.9952",   (общее соотношение количества длинных/коротких счетов)
              "shortAccount": "0.2503",   (общее соотношение количества коротких счетов)
              "timestamp": 1683297600000
           }
        ]
        """

        # ------------------------------------------
        end_point = "/futures/data/globalLongShortAccountRatio"
        parameters = {
            "symbol": symbol.upper(),
            "period": period,
            "limit": limit,
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

    def get_server_time_futures(self) -> dict:
        """
        Запрос:
        Получить время сервера

        Полный url:
        "https://fapi.binance.com/fapi/v1/time"

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
        end_point = "/fapi/v1/time"
        # -------------------------------------------

        complete_request = self.base_url + end_point

        response = requests.get(url=complete_request)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_top_ratio_long_short_account_futures(self,
                                                 symbol: str,
                                                 period: str,
                                                 start_time: str = None,
                                                 end_time: str = None,
                                                 limit: str = "30") -> dict:
        """
        Запрос:
        Получить общее соотношение количества длинных/коротких счетов ведущих трейдеров

        Полный url:
        "https://fapi.binance.com/futures/data/topLongShortAccountRatio"

        Вес запроса:
        None

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - period="period" (str): период для высчитывания ("5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("1", ..., "500")

        Комментарии:
        - Если startTime и endTime не отправлены, возвращаются самые последние данные.
        - Доступны только данные за последние 30 дней.

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "longAccount": "0.7525",   (общее соотношение количества длинных счетов)
              "longShortRatio": "3.0404",   (общее соотношение количества длинных/коротких счетов)
              "shortAccount": "0.2475",   (общее соотношение количества коротких счетов)
              "timestamp": 1683297300000
           },
           {
              "symbol": "ADAUSDT",
              "longAccount": "0.7497",   (общее соотношение количества длинных счетов)
              "longShortRatio": "2.9952",   (общее соотношение количества длинных/коротких счетов)
              "shortAccount": "0.2503",   (общее соотношение количества коротких счетов)
              "timestamp": 1683297600000
           }
        ]
        """

        # ------------------------------------------
        end_point = "/futures/data/topLongShortAccountRatio"
        parameters = {
            "symbol": symbol.upper(),
            "period": period,
            "limit": limit,
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

    def get_top_ratio_long_short_position_futures(self,
                                                  symbol: str,
                                                  period: str,
                                                  start_time: str = None,
                                                  end_time: str = None,
                                                  limit: str = "30") -> dict:
        """
        Запрос:
        Получить общее соотношение количества длинных/коротких позиций ведущих трейдеров

        Полный url:
        "https://fapi.binance.com/futures/data/topLongShortPositionRatio"

        Вес запроса:
        None

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - period="period" (str): период для высчитывания ("5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("1", ..., "500")

        Комментарии:
        - Если startTime и endTime не отправлены, возвращаются самые последние данные.
        - Доступны только данные за последние 30 дней.

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "longAccount": "0.7525",   (общее соотношение количества длинных счетов)
              "longShortRatio": "3.0404",   (общее соотношение количества длинных/коротких счетов)
              "shortAccount": "0.2475",   (общее соотношение количества коротких счетов)
              "timestamp": 1683297300000
           },
           {
              "symbol": "ADAUSDT",
              "longAccount": "0.7497",   (общее соотношение количества длинных счетов)
              "longShortRatio": "2.9952",   (общее соотношение количества длинных/коротких счетов)
              "shortAccount": "0.2503",   (общее соотношение количества коротких счетов)
              "timestamp": 1683297600000
           }
        ]
        """

        # ------------------------------------------
        end_point = "/futures/data/topLongShortPositionRatio"
        parameters = {
            "symbol": symbol.upper(),
            "period": period,
            "limit": limit,
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

    def get_volume_buy_sell_futures(self,
                                    symbol: str,
                                    period: str,
                                    start_time: str = None,
                                    end_time: str = None,
                                    limit: str = "30") -> dict:
        """
        Запрос:
        Получить объем покупок и продаж

        Полный url:
        "https://fapi.binance.com/futures/data/takerlongshortRatio"

        Вес запроса:
        None

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - period="period" (str): период для высчитывания ("5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("1", ..., "500")

        Комментарии:
        - Если startTime и endTime не отправлены, возвращаются самые последние данные.
        - Доступны только данные за последние 30 дней.

        Ответ:
        [
           {
              "buySellRatio": "0.9337",
              "sellVol": "948384.0000",
              "buyVol": "885474.0000",
              "timestamp": 1683296100000
           },
           {
              "buySellRatio": "1.2189",
              "sellVol": "1046295.0000",
              "buyVol": "1275321.0000",
              "timestamp": 1683296400000
           }
        ]
        """

        # ------------------------------------------
        end_point = "/futures/data/takerlongshortRatio"
        parameters = {
            "symbol": symbol.upper(),
            "period": period,
            "limit": limit,
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

    def get_current_open_interest_futures(self,
                                          symbol: str) -> dict:
        """
        Запрос:
        Получить текущий открытый интерес

        Полный url:
        "https://fapi.binance.com/fapi/v1/openInterest"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)

        Комментарии:
        - None

        Ответ:
        {
           "symbol": "ADAUSDT",
           "openInterest": "197547968",
           "time": 1683302122501
        }
        """

        # ------------------------------------------
        end_point = "/fapi/v1/openInterest"
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

    def get_historical_open_interest_futures(self,
                                             symbol: str,
                                             period: str,
                                             start_time: str = None,
                                             end_time: str = None,
                                             limit: str = "500") -> dict:
        """
        Запрос:
        Получить историю открытого интереса

        Полный url:
        "https://fapi.binance.com/futures/data/openInterestHist"

        Вес запроса:
        None

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - period="period" (str): период для высчитывания ("5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): количество выводимых заявок в стакане в одну сторону ("1", ..., "1500")

        Комментарии:
        - Если startTime и endTime не отправлены, возвращаются самые последние данные.
        - Доступны только данные за последние 30 дней.

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "sumOpenInterest": "196816286.00000000",   (общий открытый интерес)
              "sumOpenInterestValue": "77093214.76900040",   (общая стоимость открытого интереса)
              "timestamp": 1683300600000
           },
           {
              "symbol": "ADAUSDT",
              "sumOpenInterest": "196952337.00000000",   (общий открытый интерес)
              "sumOpenInterestValue": "77205316.10400000",   (общая стоимость открытого интереса)
              "timestamp": 1683300900000
           }
        ]
        """

        # ------------------------------------------
        end_point = "/futures/data/openInterestHist"
        parameters = {
            "symbol": symbol.upper(),
            "period": period,
            "limit": limit,
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

    def get_basis_futures(self,
                          symbol: str,
                          period: str,
                          start_time: str = None,
                          end_time: str = None,
                          limit: str = "30",
                          contract_type: str = "PERPETUAL") -> dict:
        """
        Запрос:
        Получить информацию по basis

        Полный url:
        "https://fapi.binance.com/futures/data/basis"

        Вес запроса:
        - None

        Параметры:
        - symbol="pair" (str): актив ("BTCUSDT", ...)
        - period="period" (str): интервал свечи ("5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d")
        - start_time="startTime" (str):  время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): какое количество свечей вывести ("1", ..., "500")
        - contract_type="contractType" (str): тип контракта ("PERPETUAL", "CURRENT_QUARTER", "NEXT_QUARTER")

        Комментарии:
        - "contractType" возможные варианты: ["PERPETUAL": - бессрочный, "CURRENT_MONTH" - текущий месяц,
                                              "NEXT_MONTH" - следующий месяц, "CURRENT_QUARTER" - текущий квартал,
                                              "NEXT_QUARTER" - следующий квартал,
                                              "PERPETUAL_DELIVERING" - постоянная доставка]
        - сокращения "period": [m -> минута; h -> час; d -> день]
        - Если "startTime" и "endTime" не отправлены, возвращаются самые последние klines.

        Ответ:
        [
            {
                "indexPrice": "34400.15945055",
                "contractType": "PERPETUAL",
                "basisRate": "0.0004",
                "futuresPrice": "34414.10",
                "annualizedBasisRate": "",
                "basis": "13.94054945",
                "pair": "BTCUSDT",
                "timestamp": 1698742800000
            }
        ]
        """

        # ---------------------------------------------
        end_point = "/futures/data/basis"
        parameters = {
            "pair": symbol.upper(),
            "period": period,
            "limit": limit,
            "startTime": start_time,
            "endTime": end_time,
            "contractType": contract_type
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

    def get_quarterly_settlement_price_contract_futures(self,
                                                        symbol: str) -> dict:
        """
        Запрос:
        Получить расчетную цену контракта по кварталу

        Полный url:
        "https://fapi.binance.com/futures/data/delivery-price"

        Вес запроса:
        - None

        Параметры:
        - symbol="pair" (str): актив ("BTCUSDT", ...)

        Комментарии:
        - None

        Ответ:
        [
            {
                "deliveryTime": 1695945600000,
                "deliveryPrice": 27103.00000000
            },
            {
                "deliveryTime": 1688083200000,
                "deliveryPrice": 30733.60000000
            },
            {
                "deliveryTime": 1680220800000,
                "deliveryPrice": 27814.20000000
            },
            {
                "deliveryTime": 1648166400000,
                "deliveryPrice": 44066.30000000
            }
        ]
        """

        # ------------------------------------------
        end_point = "/futures/data/delivery-price"
        parameters = {
            "pair": symbol.upper(),
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

    def get_index_price_components_futures(self,
                                           symbol: str) -> dict:
        """
        Запрос:
        Получить составляющие индекс цены символа

        Полный url:
        "https://fapi.binance.com/fapi/v1/constituents"

        Вес запроса:
        2

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)

        Комментарии:
        - None

        Ответ:
        {
            "symbol": "BTCUSDT",
            "time": 1697421272043,
            "constituents": [
                {
                    "exchange": "binance",
                    "symbol": "BTCUSDT"
                },
                {
                    "exchange": "okex",
                    "symbol": "BTC-USDT"
                },
                {
                    "exchange": "huobi",
                    "symbol": "btcusdt"
                },
                {
                    "exchange": "coinbase",
                    "symbol": "BTC-USDT"
                }
            ]
        }
        """

        # ------------------------------------------
        end_point = "/fapi/v1/constituents"
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

    def post_leverage_futures(self,
                              symbol: str,
                              leverage: str,
                              time_stamp: str,
                              recv_window: str = "5000") -> dict:
        """
        Запрос:
        Изменить кредитное плечо

        Полный url:
        "https://fapi.binance.com/fapi/v1/leverage"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - leverage="leverage" (str): кредитное плечо ("1", ..., "125")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - None

        Ответ:
        {
           "symbol": "ADAUSDT",
           "leverage": 2,
           "maxNotionalValue": "30000000"
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/leverage"
        parameters = {
            "symbol": symbol.upper(),
            "leverage": leverage,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_margin_futures(self,
                            symbol: str,
                            amount: str,
                            my_type: str,
                            time_stamp: str,
                            position_side: str = "BOTH",
                            recv_window: str = "5000") -> dict:
        """
        Запрос:
        Изменить количество маржи изолированной позиции

        Полный url:
        "https://fapi.binance.com/fapi/v1/positionMargin"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - amount="amount" (str): количество добавленной или убранной маржи ("65", ...)
        - my_type="type" (str): что делать с маржой ("1", "2")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - position_side="positionSide" (str): ... ("BOTH", "LONG", "SHORT")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Работает только для изолированного актива
        - "type" возможные варианты: [1 - добавить маржу позиции, 2 - уменьшить маржу позиции]

        Ответ:
        {
           "code": 200,
           "msg": "Successfully modify position margin.",
           "amount": 5.0,
           "type": 1
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/positionMargin"
        parameters = {
            "symbol": symbol.upper(),
            "amount": amount,
            "type": my_type,
            "positionSide": position_side,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_margin_type_futures(self,
                                 symbol: str,
                                 time_stamp: str,
                                 margin_type: str = "ISOLATED",
                                 recv_window: str = "5000") -> dict:
        """
        Запрос:
        Изменить маржинальное поле ("ИЗОЛИРОВАННАЯ", "ПЕРЕСКРЕСТНАЯ")

        Полный url:
        "https://fapi.binance.com/fapi/v1/marginType"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - margin_type="marginType" (str): какую маржу использовать ("ISOLATED", "CROSSED")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - None

        Ответ:
        {
           "code": 200,
           "msg": "success"
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/marginType"
        parameters = {
            "symbol": symbol.upper(),
            "timestamp": time_stamp,
            "marginType": margin_type,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_balance_account_futures(self,
                                    time_stamp: str,
                                    recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить баланс фьючерсного счета

        Полный url:
        "https://fapi.binance.com/fapi/v2/balance"

        Вес запроса:
        5

        Параметры:
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - None

        Ответ:
        [
            {
                "accountAlias": "FzSguXAumYAumY",   (уникальный код счета)
                "asset": "ETH",   (имя актива)
                "balance": "0.00000000",   (баланс актива)
                "crossWalletBalance": "0.00000000",   (сокращённый баланс актива)
                "crossUnPnl": "0.00000000",   (нереализованная прибыль пересеченных позиций)
                "availableBalance": "0.00000000",   (доступные средства)
                "maxWithdrawAmount": "0.00000000",   (максимальная сумма для перевода)
                "marginAvailable": true,   (можно ли использовать актив в качестве маржи в режиме Multi-Assets)
                "updateTime": 0   (последние время взаимодействия с ордером)
            },
            {
                "accountAlias": "FzSguXAumYAumY",   (уникальный код счета)
                "asset": "USDT",   (имя актива)
                "balance": "86.87857855",   (баланс актива)
                "crossWalletBalance": "86.87857855",   (сокращённый баланс актива)
                "crossUnPnl": "0.00000000",   (нереализованная прибыль пересеченных позиций)
                "availableBalance": "86.87857855",   (доступные средства)
                "maxWithdrawAmount": "86.87857855",   (максимальная сумма для перевода)
                "marginAvailable": true,   (можно ли использовать актив в качестве маржи в режиме Multi-Assets)
                "updateTime": 1682009841851   (последние время взаимодействия с ордером)
            }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v2/balance"
        parameters = {
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_commission_rate_futures(self,
                                    symbol: str,
                                    time_stamp: str,
                                    recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить ставки комиссии актива

        Полный url:
        "https://fapi.binance.com/fapi/v1/commissionRate"

        Вес запроса:
        20

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Ответ:
        {
           "symbol": "BTCUSDT",
           "makerCommissionRate": "0.000200",
           "takerCommissionRate": "0.000400"
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/commissionRate"
        parameters = {
            "symbol": symbol.upper(),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_estimation_adl_futures(self,
                                   time_stamp: str,
                                   symbol: str = "",
                                   recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить оценки ADL позиций

        Полный url:
        "https://fapi.binance.com/fapi/v1/adlQuantile"

        Вес запроса:
        5

        Параметры:
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Значения обновляются каждые 30 секунд.
        - Значения 0, 1, 2, 3, 4 показывают позицию в очереди и возможность ADL от низкого до высокого.
        - Для позиций символа в одностороннем режиме или изолированных маржей в режиме хеджирования будут возвращены
          «LONG», «SHORT» и «BOTH», чтобы показать квантили adl позиций для разных сторон позиции.
        - Если позиции символа пересекаются с маржой в режиме хеджирования:
            - "HEDGE" будет одним из ключей в ответе вместо "BOTH"
            - Когда есть позиции как по длинным, так и по коротким сторонам, рассчитанное для нереализованных PnL,
              будет отображаться одно и то же значение как для "LONG" так и для "SHORT".

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "adlQuantile": {
                 "LONG": 0,
                 "SHORT": 0,
                 "BOTH": 0
              }
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/adlQuantile"
        parameters = {
            "timestamp": time_stamp,
            "symbol": symbol.upper(),
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_force_orders_futures(self,
                                 time_stamp: str,
                                 symbol: str = "",
                                 auto_close_type: str = "",
                                 start_time: str = "",
                                 end_time: str = "",
                                 limit: str = "50",
                                 recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить принудительные сделки

        Полный url:
        "https://fapi.binance.com/fapi/v1/forceOrders"

        Вес запроса:
        10 с указанным "symbol", 50 без указанного

        Параметры:
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - auto_close_type="autoCloseType" (str): ... ("LIQUIDATION", "ADL")
        - start_time="startTime" (str): время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): выводимое количество ("5", ..., "100")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Если "autoCloseType" не отправлен, будут возвращены ордера с обоими типами
        - Если «startTime» не отправлено, можно запросить данные за 7 дней до «endTime».

        Ответ:
        [
          {
            "orderId": 6071832819,
            "symbol": "BTCUSDT",
            "status": "FILLED",
            "clientOrderId": "autoclose-1596107620040000020",
            "price": "10871.09",
            "avgPrice": "10913.21000",
            "origQty": "0.001",
            "executedQty": "0.001",
            "cumQuote": "10.91321",
            "timeInForce": "IOC",
            "type": "LIMIT",
            "reduceOnly": false,
            "closePosition": false,
            "side": "SELL",
            "positionSide": "BOTH",
            "stopPrice": "0",
            "workingType": "CONTRACT_PRICE",
            "origType": "LIMIT",
            "time": 1596107620044,
            "updateTime": 1596107620087
          }
          {
            "orderId": 6072734303,
            "symbol": "BTCUSDT",
            "status": "FILLED",
            "clientOrderId": "adl_autoclose",
            "price": "11023.14",
            "avgPrice": "10979.82000",
            "origQty": "0.001",
            "executedQty": "0.001",
            "cumQuote": "10.97982",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "reduceOnly": false,
            "closePosition": false,
            "side": "BUY",
            "positionSide": "SHORT",
            "stopPrice": "0",
            "workingType": "CONTRACT_PRICE",
            "origType": "LIMIT",
            "time": 1596110725059,
            "updateTime": 1596110725071
          }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/forceOrders"
        parameters = {
            "timestamp": time_stamp,
            "symbol": symbol.upper(),
            "autoCloseType": auto_close_type,
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_ftqri_futures(self,
                          time_stamp: str,
                          symbol: str = "",
                          recv_window: str = "5000") -> dict:
        """
        Запрос:
        ...

        Полный url:
        "https://fapi.binance.com/fapi/v1/apiTradingStatus"

        Вес запроса:
        1 с указанным "symbol", 10 без указанного "symbol"

        Параметры:
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - None

        Ответ:
        {
            "indicators": {
                "BTCUSDT": [
                    {
                        "isLocked": true,
                        "plannedRecoverTime": 1545741270000,
                        "indicator": "UFR",  (Незаполненный коэффициент (UFR))
                        "value": 0.05,   (Текущее значение)
                        "triggerValue": 0.995   (Значение триггера)
                    },
                    {
                        "isLocked": true,
                        "plannedRecoverTime": 1545741270000,
                        "indicator": "IFER",   (Коэффициент экспирации IOC/FOK (IFER))
                        "value": 0.99,   (Текущее значение)
                        "triggerValue": 0.99   (Значение триггера)
                    },
                    {
                        "isLocked": true,
                        "plannedRecoverTime": 1545741270000,
                        "indicator": "GCR",   (Коэффициент отмены GTC (GCR))
                        "value": 0.99,   (Текущее значение)
                        "triggerValue": 0.99   (Значение триггера)
                    },
                    {
                        "isLocked": true,
                        "plannedRecoverTime": 1545741270000,
                        "indicator": "DR",   (Запыленность (DR))
                        "value": 0.99,   (Текущее значение)
                        "triggerValue": 0.99   (Значение триггера)
                    }
                ]
            }
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/apiTradingStatus"
        parameters = {
            "timestamp": time_stamp,
            "symbol": symbol.upper(),
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_income_history_futures(self,
                                   time_stamp: str,
                                   symbol: str = "",
                                   income_type: str = "",
                                   start_time: str = "",
                                   end_time: str = "",
                                   limit: str = "100",
                                   recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить историю доходов

        Полный url:
        "https://fapi.binance.com/fapi/v1/income"

        Вес запроса:
        30

        Параметры:
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - income_type="incomeType" (str): тип дохода ("TRANSFER", "WELCOME_BONUS", "REALIZED_PNL", "FUNDING_FEE",
                                                      "COMMISSION", "INSURANCE_CLEAR", "REFERRAL_KICKBACK",
                                                      "COMMISSION_REBATE", "API_REBATE", "CONTEST_REWARD",
                                                      "CROSS_COLLATERAL_TRANSFER", "OPTIONS_PREMIUM_FEE",
                                                      "OPTIONS_SETTLE_PROFIT", "INTERNAL_TRANSFER", "AUTO_EXCHANGE",
                                                      "DELIVERED_SETTELMENT", "COIN_SWAP_DEPOSIT", "COIN_SWAP_WITHDRAW",
                                                      "POSITION_LIMIT_INCREASE_FEE")
        - start_time="startTime" (str): время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): какое количество сделок (информация о доходе) вывести ("5", ..., "1000")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Если "startTime" и "endTime" не отправлены, будут возвращены данные за последние 7 дней.
        - Если не передан "incomeType", будут возвращены все виды дохода.
        - История доходов содержит данные только за последние три месяца.

        Ответ:
        [
           {
              "symbol": "ADAUSDT",   (торговый символ, если он есть)
              "incomeType": "REALIZED_PNL",   (тип дохода)
              "income": "0.01680000",   (сумма дохода)
              "asset": "USDT",   (доходный актив)
              "time": 1682287762000,
              "info": "910576696",   (дополнительная информация)
              "tranId": 90241910576696,   (идентификатор транзакции)
              "tradeId": "910576696"   (идентификатор сделки, если он есть)
           },
           {
              "symbol": "ADAUSDT",
              "incomeType": "COMMISSION",
              "income": "-0.00644448",
              "asset": "USDT",
              "time": 1682287762000,
              "info": "910576696",
              "tranId": 90241910576696,
              "tradeId": "910576696"
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/income"
        parameters = {
            "timestamp": time_stamp,
            "symbol": symbol.upper(),
            "incomeType": income_type,
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_info_account_futures(self,
                                 time_stamp: str,
                                 recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить текущую информацию об учетной записи

        Полный url:
        "https://fapi.binance.com/fapi/v2/account"

        Вес запроса:
        5

        Параметры:
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - None

        Ответ:
        - режим single-asset

        {
            "feeTier": 0,   (уровень комиссии счета)
            "canTrade": true,   ("true" если можно торговать, "false" нельзя торговать)
            "canDeposit": true,   ("true" если можно перевести актив, "false" нельзя перевести актив)
            "canWithdraw": true,   ("true" если можно вывести актив, "false" нельзя вывести актив)
            "updateTime": 0,   (ignore)
            "multiAssetsMargin": false,
            "totalInitialMargin": "0.00000000",   (необходимая начальная маржа с текущей ценой маркировки
                                                   (бесполезно с изолированными позициями), только для актива USDT)
            "totalMaintMargin": "0.00000000",   (необходимая поддерживающая маржа, только для актива USDT)
            "totalWalletBalance": "23.72469206",   (баланс кошелька, только для актива USDT)
            "totalUnrealizedProfit": "0.00000000",   (нереализованная прибыль, только для актива USDT)
            "totalMarginBalance": "23.72469206",   (баланс маржи, только для актива USDT)
            "totalPositionInitialMargin": "0.00000000",   (начальная маржа необходимая для позиций
                                                           с текущей ценой маркировки, только для актива USDT)
            "totalOpenOrderInitialMargin": "0.00000000",   (начальная маржа, необходимая для открытых ордеров
                                                            с текущей ценой маркировки, только для актива USDT)
            "totalCrossWalletBalance": "23.72469206",   (перекрёстный баланс кошелька, только для актива USDT)
            "totalCrossUnPnl": "0.00000000",  (нереализованная прибыль по пересеченным позициям, только для актива USDT)
            "availableBalance": "23.72469206",   (доступный баланс, только для актива USDT)
            "maxWithdrawAmount": "23.72469206"   (максимальная сумма для вывода, только для актива USDT)
            "assets": [
                {
                    "asset": "USDT",   (название актива)
                    "walletBalance": "23.72469206",   (баланс кошелька)
                    "unrealizedProfit": "0.00000000",   (нереализованная прибыль)
                    "marginBalance": "23.72469206",   (баланс маржи)
                    "maintMargin": "0.00000000",   (необходимая поддерживающая маржа)
                    "initialMargin": "0.00000000",   (необходимая начальная маржа с текущей ценой маркировки)
                    "positionInitialMargin": "0.00000000",   (начальная маржа, необходимая для позиций
                                                              с текущей ценой маркировки)
                    "openOrderInitialMargin": "0.00000000",   (начальная маржа, необходимая для открытых ордеров
                                                               с текущей ценой маркировки)
                    "crossWalletBalance": "23.72469206",   (сокращённый баланс кошелька)
                    "crossUnPnl": "0.00000000"   (нереализованная прибыль пересеченных позиций)
                    "availableBalance": "23.72469206",   (доступный баланс)
                    "maxWithdrawAmount": "23.72469206",   (максимальная сумма для вывода)
                    "marginAvailable": true, ("true" можно использовать актив в качестве маржи в режиме Multi-Assets,
                                              "false" нельзя использовать актив в качестве маржи в режиме Multi-Assets)
                    "updateTime": 1625474304765   (время последнего обновления)
                },
                {
                    "asset": "BUSD",   (название актива)
                    "walletBalance": "103.12345678",   (баланс кошелька)
                    "unrealizedProfit": "0.00000000",   (нереализованная прибыль)
                    "marginBalance": "103.12345678",   (баланс маржи)
                    "maintMargin": "0.00000000",   (maintenance margin required)
                    "initialMargin": "0.00000000",   (необходимая начальная маржа с текущей ценой маркировки)
                    "positionInitialMargin": "0.00000000",   (начальная маржа, необходимая для позиций
                                                              с текущей ценой маркировки)
                    "openOrderInitialMargin": "0.00000000",   (начальная маржа, необходимая для открытых ордеров
                                                               с текущей ценой маркировки)
                    "crossWalletBalance": "103.12345678",   (сокращённый баланс кошелька)
                    "crossUnPnl": "0.00000000"   (нереализованная прибыль пересеченных позиций)
                    "availableBalance": "103.12345678",   (доступный баланс)
                    "maxWithdrawAmount": "103.12345678",   (максимальная сумма для вывода)
                    "marginAvailable": true,  ("true" можно использовать актив в качестве маржи в режиме Multi-Assets,
                                               "false" нельзя использовать актив в качестве маржи в режиме Multi-Assets)
                    "updateTime": 1625474304765   (время последнего обновления)
                }
            ],
            "positions": [   (возвращаются позиции всех символов на рынке. В одностороннем режиме будут возвращены
                         только "BOTH" позиции. В режиме хеджирования будут возвращены только "LONG" и "SHORT" позиции)
                {
                    "symbol": "BTCUSDT",  (название символа)
                    "initialMargin": "0",  (необходимая начальная маржа с текущей ценой маркировки)
                    "maintMargin": "0",  (необходимая поддерживающая маржа)
                    "unrealizedProfit": "0.00000000",  (нереализованная прибыль)
                    "positionInitialMargin": "0",  (начальная маржа, необходимая для позиций с текущей ценой маркировки)
                    "openOrderInitialMargin": "0",  (начальная маржа, необходимая для открытых ордеров
                                                     с текущей ценой маркировки)
                    "leverage": "100",  (текущее начальное плечо)
                    "isolated": true,  ("true" если позиция изолирована)
                    "entryPrice": "0.00000",  (средняя цена входа)
                    "maxNotional": "250000",  (максимально доступный номинал с текущим кредитным плечом)
                    "bidNotional": "0",  (ignore)
                    "askNotional": "0",  (ignore)
                    "positionSide": "BOTH",  (сторона позиции)
                    "positionAmt": "0",  (сумма позиции)
                    "updateTime": 0  (время последнего обновления)
                }
            ]
        }

        - Режим multi-assets

        {
            "feeTier": 0,  (уровень комиссии счета)
            "canTrade": true,  ("true" если можно торговать, "false" нельзя торговать)
            "canDeposit": true,  ("true" если можно перевести актив, "false" нельзя перевести актив)
            "canWithdraw": true,  ("true" если можно вывести актив, "false" нельзя вывести актив)
            "updateTime": 0,  (ignore)
            "multiAssetsMargin": true,
            "totalInitialMargin": "0.00000000",  (сумма стоимости всех кросс-позиций/начальной маржи открытого ордера
                                                  в долларах США)
            "totalMaintMargin": "0.00000000",  (сумма долларовой стоимости всех кросс-позиций, поддерживающих маржу)
            "totalWalletBalance": "126.72469206",  (баланс кошелька в долларах США)
            "totalUnrealizedProfit": "0.00000000",  (нереализованная прибыль в долларах США)
            "totalMarginBalance": "126.72469206",  (баланс маржи в долларах США)
            "totalPositionInitialMargin": "0.00000000",  (сумма стоимости начальной маржи всех кросс-позиций
                                                          в долларах США)
            "totalOpenOrderInitialMargin": "0.00000000",  (необходимая начальная маржа для открытых ордеров
                                                           с текущей ценой маркировки в долларах США)
            "totalCrossWalletBalance": "126.72469206",  (баланс кошелька в долларах США)
            "totalCrossUnPnl": "0.00000000",  (нереализованная прибыль пересеченных позиций в долларах США)
            "availableBalance": "126.72469206",  (доступный баланс в долларах США)
            "maxWithdrawAmount": "126.72469206"  (доступный баланс в долларах США)
            "assets": [
                {
                    "asset": "USDT",  (название актива)
                    "walletBalance": "23.72469206",  (баланс кошелька)
                    "unrealizedProfit": "0.00000000",  (нереализованная прибыль)
                    "marginBalance": "23.72469206",  (баланс маржи)
                    "maintMargin": "0.00000000",  (необходимая поддерживающая маржа)
                    "initialMargin": "0.00000000",  (необходимая начальная маржа с текущей ценой маркировки)
                    "positionInitialMargin": "0.00000000",  (начальная маржа, необходимая для позиций
                                                             с текущей ценой маркировки)
                    "openOrderInitialMargin": "0.00000000",  (начальная маржа, необходимая для открытых ордеров
                                                              с текущей ценой маркировки)
                    "crossWalletBalance": "23.72469206",  (сокращённый баланс кошелька)
                    "crossUnPnl": "0.00000000",  (нереализованная прибыль пересеченных позиций)
                    "availableBalance": "23.72469206",  (доступный баланс)
                    "maxWithdrawAmount": "23.72469206",  (максимальная сумма для вывода)
                    "marginAvailable": true, (("true" можно использовать актив в качестве маржи в режиме Multi-Assets,
                                              "false" нельзя использовать актив в качестве маржи в режиме Multi-Assets))
                    "updateTime": 1625474304765  (время последнего обновления)
                },
                {
                    "asset": "BUSD",  (название актива)
                    "walletBalance": "103.12345678",  (баланс кошелька)
                    "unrealizedProfit": "0.00000000",  (нереализованная прибыль)
                    "marginBalance": "103.12345678",  (баланс маржи)
                    "maintMargin": "0.00000000",  (необходимая поддерживающая маржа)
                    "initialMargin": "0.00000000",  (необходимая начальная маржа с текущей ценой маркировки)
                    "positionInitialMargin": "0.00000000",  (начальная маржа, необходимая для позиций
                                                             с текущей ценой маркировки)
                    "openOrderInitialMargin": "0.00000000",  (начальная маржа, необходимая для открытых ордеров
                                                              с текущей ценой маркировки)
                    "crossWalletBalance": "103.12345678",  (сокращённый баланс кошелька)
                    "crossUnPnl": "0.00000000",  (нереализованная прибыль пересеченных позиций)
                    "availableBalance": "103.12345678",  (доступный баланс)
                    "maxWithdrawAmount": "103.12345678",  (максимальная сумма для вывода)
                    "marginAvailable": true, (("true" можно использовать актив в качестве маржи в режиме Multi-Assets,
                                              "false" нельзя использовать актив в качестве маржи в режиме Multi-Assets))
                    "updateTime": 1625474304765  (время последнего обновления)
                }
            ],
            "positions": [   (возвращаются позиции всех символов на рынке. В одностороннем режиме будут возвращены
                              только "BOTH" позиции. В режиме хеджирования будут возвращены только "LONG" и "SHORT")

                {
                    "symbol": "BTCUSDT",  (название символа)
                    "initialMargin": "0",  (необходимая начальная маржа с текущей ценой маркировки)
                    "maintMargin": "0",  (необходимая поддерживающая маржа)
                    "unrealizedProfit": "0.00000000",  (нереализованная прибыль)
                    "positionInitialMargin": "0",  (начальная маржа, необходимая для позиций с текущей ценой маркировки)
                    "openOrderInitialMargin": "0",  (начальная маржа, необходимая для открытых
                                                     ордеров с текущей ценой маркировки)
                    "leverage": "100",  (текущее начальное плечо)
                    "isolated": true,  ("true" если позиция изолирована)
                    "entryPrice": "0.00000",  (средняя цена входа)
                    "maxNotional": "250000",  (максимально доступный номинал с текущим кредитным плечом)
                    "bidNotional": "0",  (ignore)
                    "askNotional": "0",  (ignore)
                    "positionSide": "BOTH",  (сторона позиции)
                    "positionAmt": "0",  (сумма позиции)
                    "updateTime": 0  (время последнего обновления)
                }
            ]
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v2/account"
        parameters = {
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_margin_change_history_futures(self,
                                          symbol: str,
                                          time_stamp: str,
                                          my_type: str = "",
                                          start_time: str = "",
                                          end_time: str = "",
                                          limit: str = "500",
                                          recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить историю изменения маржи

        Полный url:
        "https://fapi.binance.com/fapi/v1/positionMargin/history"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - my_type="type" (str): какое действие с маржой показывать ("1", "2")
        - start_time="startTime" (str): время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): какое количество вывести ("5", ..., "1000")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - "type" возможные варианты: [1 - показать добавление маржи, 2 - показать уменьшение маржи]

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "type": 1,
              "deltaType": "TRADE",
              "amount": "4.04422425",
              "asset": "USDT",
              "time": 1606982998900,
              "positionSide": "BOTH",
              "clientTranId": ""
           },
           {
              "symbol": "ADAUSDT",
              "type": 2,
              "deltaType": "TRADE",
              "amount": "-4.04422425",
              "asset": "USDT",
              "time": 1606983593938,
              "positionSide": "BOTH",
              "clientTranId": ""
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/positionMargin/history"
        parameters = {
            "symbol": symbol.upper(),
            "type": my_type,
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_nl_brackets_futures(self,
                                time_stamp: str,
                                symbol: str = "",
                                recv_window: str = "5000") -> dict:
        """
        Запрос:
        ...

        Полный url:
        "https://fapi.binance.com/fapi/v1/leverageBracket"

        Вес запроса:
        1

        Параметры:
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - None

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "brackets": [
                 {
                    "bracket": 1,   (условная скобка)
                    "initialLeverage": 75,   (Максимальное начальное кредитное плечо для этой группы)
                    "notionalCap": 5000,   (Ограничение условного обозначения этой скобки)
                    "notionalFloor": 0,   (Условный порог этой скобки)
                    "maintMarginRatio": 0.005,   (Коэффициент поддержки для этой группы)
                    "cum": 0.0   (Вспомогательное число для быстрого расчета)
                 },
                 {...},
                 {...},
                 {...},
                 {...},
                 {...},
                 {...},
                 {...},
                 {...},
                 {...}
              ]
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/leverageBracket"
        parameters = {
            "symbol": symbol.upper(),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_update_order_history_futures(self,
                                         symbol: str,
                                         time_stamp: str,
                                         start_time: str = "",
                                         end_time: str = "",
                                         order_id: str = "",
                                         orig_client_order_id: str = "",
                                         limit: str = "50",
                                         recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить историю изменений ордеров

        Полный url:
        "https://fapi.binance.com/fapi/v1/orderAmendment"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - start_time="startTime" (str): время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - order_id="orderId" (str): самозаполняющимся идентификатор для каждой сделки ("567834287", ...)
        - orig_client_order_id="origClientOrderId" (str): идентификатор сделки  ("567887", ...)
        - limit="limit" (str): какое количество вывести ("5", ..., "500")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Необходимо обязательно отправить либо order_id, либо orig_client_order_id.
        - orderId имеет преимущественную силу, если отправлены оба.

        Ответ:
        [
           {
              "amendmentId": 51045853,
              "symbol": "ADAUSDT",
              "pair": "ADAUSDT",
              "orderId": 32717797178,
              "clientOrderId": "74707",
              "time": 1686134330452,
              "amendment": {
                 "price": {
                    "before": "0.33000",
                    "after": "0.31000"
                 },
                 "origQty": {
                    "before": "17",
                    "after": "68"
                 },
                 "count": 1
              }
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/orderAmendment"
        parameters = {
            "symbol": symbol.upper(),
            "timestamp": time_stamp,
            "startTime": start_time,
            "endTime": end_time,
            "orderId": order_id,
            "origClientOrderId": orig_client_order_id,
            "limit": limit,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_id_deals_futures(self,
                             start_time: str,
                             end_time: str,
                             time_stamp: str,
                             recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить идентификатор для загрузки истории сделок с фьючерсами

        Полный url:
        "https://fapi.binance.com/fapi/v1/income/asyn"

        Вес запроса:
        1500

        Параметры:
        - start_time="startTime" (str): время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Ограничение запроса — максимум 5 раз в месяц
        - время между "startTime" и "endTime" не может превышать 1 год

        Ответ:
        {
           "avgCostTimestampOfLast30d": 380288,   (Среднее время загрузки данных за последние 30 дней)
           "downloadId": "705896703002431488"
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/income/asyn"
        parameters = {
            "startTime": start_time,
            "endTime": end_time,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_link_deals_futures(self,
                               download_id: str,
                               time_stamp: str,
                               recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить ссылку для скачивания истории сделок с фьючерсами по идентификатору

        Полный url:
        "https://fapi.binance.com/fapi/v1/income/asyn/id"

        Вес запроса:
        10

        Параметры:
        - download_id="downloadId" (str): идентификатор загрузки ("132131234", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - "downloadId" можно получит по url "https://fapi.binance.com/fapi/v1/income/asyn"
        - Срок действия ссылки для скачивания: 24 часа

        Ответ:
        - Если результат ответ завершен ("completed"):

        {
           "downloadId": "705897285947772928",
           "status": "completed",   ("completed"-завершено или "processing"-обработка)
           "url": "https://bin-prod-user-rebate-bucket.s3.amazonaws.com/data-download-task/usdt_margined_futures/...
                                                                        (Ссылка сопоставлена с идентификатором загрузки)
           "s3Link": null,
           "notified": true,   (ignore)
           "expirationTimestamp": 1683668866000,   (Срок действия ссылки истекает после этой метки времени)
           "isExpired": null
        }

        - Если результат ответ в обработке ("processing"):

        {
            "downloadId": "545923594199212032",
            "status": "processing",
            "url": "",
            "notified": false,
            "expirationTimestamp": -1,
            "isExpired":null,
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/income/asyn/id"
        parameters = {
            "downloadId": download_id,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_id_orders_futures(self,
                              start_time: str,
                              end_time: str,
                              time_stamp: str,
                              recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить идентификатор для загрузки истории заказов с фьючерсами

        Полный url:
        "https://fapi.binance.com/fapi/v1/order/asyn"

        Вес запроса:
        1500

        Параметры:
        - start_time="startTime" (str): время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - ограничение запроса — максимум 10 раз в месяц
        - время между "startTime" и "endTime" не может превышать 1 год

        Ответ:
        {
           "avgCostTimestampOfLast30d": 380288,   (Среднее время загрузки данных за последние 30 дней)
           "downloadId": "705896703002431488"
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order/asyn"
        parameters = {
            "startTime": start_time,
            "endTime": end_time,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_link_orders_futures(self,
                                download_id: str,
                                time_stamp: str,
                                recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить ссылку для скачивания истории заказов с фьючерсами по идентификатору

        Полный url:
        "https://fapi.binance.com/fapi/v1/order/asyn/id"

        Вес запроса:
        10

        Параметры:
        - download_id="downloadId" (str): идентификатор загрузки ("132131234", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - "downloadId" можно получит по url "https://fapi.binance.com/fapi/v1/order/asyn"
        - Срок действия ссылки для скачивания: 24 часа

        Ответ:
        - Если результат ответ завершен ("completed"):

        {
           "downloadId": "705897285947772928",
           "status": "completed",   ("completed"-завершено или "processing"-обработка)
           "url": "https://bin-prod-user-rebate-bucket.s3.amazonaws.com/data-download-task/usdt_margined_futures/...
                                                                        (Ссылка сопоставлена с идентификатором загрузки)
           "s3Link": null,
           "notified": true,   (ignore)
           "expirationTimestamp": 1683668866000,   (Срок действия ссылки истекает после этой метки времени)
           "isExpired": null
        }

        - Если результат ответ в обработке ("processing"):

        {
            "downloadId": "545923594199212032",
            "status": "processing",
            "url": "",
            "notified": false,
            "expirationTimestamp": -1,
            "isExpired":null,
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order/asyn/id"
        parameters = {
            "downloadId": download_id,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_id_trades_futures(self,
                              start_time: str,
                              end_time: str,
                              time_stamp: str,
                              recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить идентификатор для загрузки истории торговли с фьючерсами

        Полный url:
        "https://fapi.binance.com/fapi/v1/trade/asyn"

        Вес запроса:
        1500

        Параметры:
        - start_time="startTime" (str): время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - ограничение запроса — максимум 5 раз в месяц
        - время между "startTime" и "endTime" не может превышать 1 год

        Ответ:
        {
           "avgCostTimestampOfLast30d": 380288,   (Среднее время загрузки данных за последние 30 дней)
           "downloadId": "705896703002431488"
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/trade/asyn"
        parameters = {
            "startTime": start_time,
            "endTime": end_time,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_link_trades_futures(self,
                                download_id: str,
                                time_stamp: str,
                                recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить ссылку для скачивания истории торговли с фьючерсами по идентификатору

        Полный url:
        "https://fapi.binance.com/fapi/v1/trade/asyn/id"

        Вес запроса:
        10

        Параметры:
        - download_id="downloadId" (str): идентификатор загрузки ("132131234", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - "downloadId" можно получит по url "https://fapi.binance.com/fapi/v1/order/asyn"
        - Срок действия ссылки для скачивания: 24 часа

        Ответ:
        - Если результат ответ завершен ("completed"):

        {
           "downloadId": "705897285947772928",
           "status": "completed",   ("completed"-завершено или "processing"-обработка)
           "url": "https://bin-prod-user-rebate-bucket.s3.amazonaws.com/data-download-task/usdt_margined_futures/...
                                                                        (Ссылка сопоставлена с идентификатором загрузки)
           "s3Link": null,
           "notified": true,   (ignore)
           "expirationTimestamp": 1683668866000,   (Срок действия ссылки истекает после этой метки времени)
           "isExpired": null
        }

        - Если результат ответ в обработке ("processing"):

        {
            "downloadId": "545923594199212032",
            "status": "processing",
            "url": "",
            "notified": false,
            "expirationTimestamp": -1,
            "isExpired":null,
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/trade/asyn/id"
        parameters = {
            "downloadId": download_id,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def post_multi_asset_futures(self,
                                 multi_assets_margin: str,
                                 time_stamp: str,
                                 recv_window: str = "5000") -> dict:
        """
        Запрос:
        Изменить режим мультиактива

        Полный url:
        "https://fapi.binance.com/fapi/v1/multiAssetsMargin"

        Вес запроса:
        1

        Параметры:
        - multi_assets_margin="multiAssetsMargin" (str): режим мультиактива ("True", "False")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - изменить режим мультиактива на КАЖДОМ символе пользователя (режим Single-Asset или режим Multi-Assets)
        - "multiAssetsMargin" возможные варианты: ["false" - режим Single-Asset, "true" - режим Multi-Assets]

        Ответ:
        {
            "code": 200,
            "msg": "success"
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/multiAssetsMargin"
        parameters = {
            "multiAssetsMargin": multi_assets_margin,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_multi_asset_futures(self,
                                time_stamp: str,
                                recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить режим мультиактива

        Полный url:
        "https://fapi.binance.com/fapi/v1/multiAssetsMargin"

        Вес запроса:
        30

        Параметры:
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Получить режим мультиактива на КАЖДОМ символе пользователя (режим Single-Asset или режим Multi-Assets)

        Ответ:
        {
            "multiAssetsMargin": true  ("false": режим Single-Asset; "true": режим Multi-Assets)
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/multiAssetsMargin"
        parameters = {
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def post_position_futures(self,
                              dual_side_position: str,
                              time_stamp: str,
                              recv_window: str = "5000") -> dict:
        """
        Запрос:
        Изменить режим позиции

        Полный url:
        "https://fapi.binance.com/fapi/v1/positionSide/dual"

        Вес запроса:
        1

        Параметры:
        - dual_side_position="dualSidePosition" (str): режим позиции ("True", "False")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Изменить режим позиции на КАЖДОМ символе пользователя (односторонний режим или режим хеджирования)
        - "dualSidePosition" возможные варианты: ["false": односторонний режим, "true": режим хеджирования]

        Ответ:
        {
            "code": 200,
            "msg": "success"
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/positionSide/dual"
        parameters = {
            "dualSidePosition": dual_side_position,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_positions_futures(self,
                              time_stamp: str,
                              recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить режим позиции

        Полный url:
        "https://fapi.binance.com/fapi/v1/positionSide/dual"

        Вес запроса:
        30

        Параметры:
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Получить режим позиции на КАЖДОМ символе пользователя (односторонний режим или режим хеджирования)

        Ответ:
        {
            "dualSidePosition": true  ("false": односторонний режим; "true": режим хеджирования)
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/positionSide/dual"
        parameters = {
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def post_limit_futures(self,
                           symbol: str,
                           side: str,
                           quantity: str,
                           price: str,
                           time_stamp: str,
                           my_type: str = "LIMIT",
                           time_in_force: str = "GTC",
                           new_order_resp_type: str = "RESULT",
                           new_client_order_id: str = str(randint(1, 100000)),
                           working_type: str = "CONTRACT_PRICE",
                           price_protect: str = "FALSE",
                           position_side: str = "BOTH",
                           recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить ордер LIMIT

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        0

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - side="side" (str): сторона сделки ("BUY", "SELL")
        - quantity="quantity" (str): количества актива в сделки ("16", ...)
        - price="price" (str): по какой цене разместится limit_order ("26234", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - my_type="type" (str): вид ордера ("LIMIT")
        - time_in_force="timeInForce" (str): режим исполнения ("GTC", "IOC", "FOK", "GTD", "GTX")
        - new_order_resp_type="newOrderRespType" (str): развёрнутость ответа ("ACK", "RESULT", "FULL")
        - new_client_order_id="newClientOrderId" (str): идентификатор сделки ("567887", ...)
        - working_type="workingType" (str): ... ("CONTRACT_PRICE", "MARK_PRICE")
        - price_protect="priceProtect" (str): ... ("FALSE", "TRUE")
        - position_side="positionSide" (str): ... ("BOTH", "LONG", "SHORT")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Все аргументы заполняются заглавными буквами
        - минимальное значение "quantity" рассчитывается как (
        end_point /fapi/v1/exchangeInfo
        float(["symbols"][если "symbol" == "symbol"]["filters"][если "filterType" == "MIN_NOTIONAL"]["notional"]) /
        end_point /fapi/v1/ticker/price
        float(["price"]
        )
        - "side" возможные варианты: ["BUY" - купить, "SELL"- продать]
        - "timeInForce" возможные варианты: ["GTC" – ордер будет висеть до тех пор, пока его не отменят,
                                             "IOC" – будет куплено то количество, которое можно купить немедленно.
                                                     Все, что не удалось купить, будет отменено,
                                             "FOK" – либо будет куплено все указанное количество немедленно,
                                                     либо не будет куплено вообще ничего, ордер отменится,
                                              "GTD" - до определённой даты или до конца дня,
                                              "GTX" - ....
        - "newOrderRespType" возможные варианты: ["ACK" - короткий ответ,
                                                  "RESULT" - оптимальный ответ,
                                                  "FULL" - полный ответ]

        Ответ:
        {
           "orderId": 31424006568,
           "symbol": "ADAUSDT",
           "status": "NEW",
           "clientOrderId": "7266",
           "price": "0.35900",
           "avgPrice": "0.00000",
           "origQty": "14",
           "executedQty": "0",
           "cumQty": "0",
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "LIMIT",
           "reduceOnly": false,
           "closePosition": false,   (if Close-All)
           "side": "BUY",
           "positionSide": "BOTH",
           "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "LIMIT",
           "updateTime": 1682112624857
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "quantity": quantity,
            "price": price,
            "positionSide": position_side,
            "type": my_type,
            "timeInForce": time_in_force,
            "newClientOrderId": new_client_order_id,
            "workingType": working_type,
            "priceProtect": price_protect,
            "newOrderRespType": new_order_resp_type,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_market_futures(self,
                            symbol: str,
                            side: str,
                            quantity: str,
                            time_stamp: str,
                            my_type: str = "MARKET",
                            new_order_resp_type: str = "RESULT",
                            new_client_order_id: str = str(randint(1, 100000)),
                            working_type: str = "CONTRACT_PRICE",
                            price_protect: str = "FALSE",
                            position_side: str = "BOTH",
                            recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить ордер MARKET

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        0

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - side="side" (str): сторона сделки ("BUY", "SELL")
        - quantity="quantity" (str): количества актива в сделки ("16", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - my_type="type" (str): вид ордера ("MARKET")
        - new_order_resp_type="newOrderRespType" (str): развёрнутость ответа ("ACK", "RESULT", "FULL")
        - new_client_order_id="newClientOrderId" (str): идентификатор сделки ("567887", ...)
        - working_type="workingType" (str): ... ("CONTRACT_PRICE", "MARK_PRICE")
        - price_protect="priceProtect" (str): ... ("FALSE", "TRUE")
        - position_side="positionSide" (str): ... ("BOTH", "LONG", "SHORT")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Все аргументы заполняются заглавными буквами
        - минимальное значение "quantity" рассчитывается как (
        end_point /fapi/v1/exchangeInfo
        float(["symbols"][если "symbol" == "symbol"]["filters"][если "filterType" == "MIN_NOTIONAL"]["notional"]) /
        end_point /fapi/v1/ticker/price
        float(["price"]
        )
        - "side" возможные варианты: ["BUY" - купить, "SELL"- продать]
        - "newOrderRespType" возможные варианты: ["ACK" - короткий ответ,
                                                  "RESULT" - оптимальный ответ,
                                                  "FULL" - полный ответ]

        Ответ:
        {
           "orderId": 31424034902,
           "symbol": "ADAUSDT",
           "status": "FILLED",
           "clientOrderId": "87391",
           "price": "0",
           "avgPrice": "0.38270",
           "origQty": "14",
           "executedQty": "14",
           "cumQty": "14",
           "cumQuote": "5.35780",
           "timeInForce": "GTC",
           "type": "MARKET",
           "reduceOnly": false,
           "closePosition": false,  (if Close-All)
           "side": "SELL",
           "positionSide": "BOTH",
           "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "MARKET",
           "updateTime": 1682112737188
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "quantity": quantity,
            "positionSide": position_side,
            "type": my_type,
            "newClientOrderId": new_client_order_id,
            "workingType": working_type,
            "priceProtect": price_protect,
            "newOrderRespType": new_order_resp_type,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_profit_limit_futures(self,
                                  symbol: str,
                                  side: str,
                                  quantity: str,
                                  price: str,
                                  stop_price: str,
                                  time_stamp: str,
                                  my_type: str = "TAKE_PROFIT",
                                  time_in_force: str = "GTC",
                                  new_order_resp_type: str = "RESULT",
                                  new_client_order_id: str = str(randint(1, 100000)),
                                  working_type: str = "CONTRACT_PRICE",
                                  price_protect: str = "FALSE",
                                  position_side: str = "BOTH",
                                  recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить ордер TAKE_PROFIT

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        0

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - side="side" (str): сторона сделки ("BUY", "SELL")
        - quantity="quantity" (str): количества актива в сделки ("16", ...)
        - price="price" (str): по достижению какой цены активируется "stop_price" ("26234", ...)
        - stop_price="stopPrice" (str): по какой цене разместится profit_order ("27328", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - my_type="type" (str): вид ордера ("TAKE_PROFIT")
        - time_in_force="timeInForce" (str): режим исполнения ("GTC", "IOC", "FOK", "GTD", "GTX")
        - new_order_resp_type="newOrderRespType" (str): развёрнутость ответа ("ACK", "RESULT", "FULL")
        - new_client_order_id="newClientOrderId" (str): идентификатор сделки ("567887", ...)
        - working_type="workingType" (str): ... ("CONTRACT_PRICE", "MARK_PRICE")
        - price_protect="priceProtect" (str): ... ("FALSE", "TRUE")
        - position_side="positionSide" (str): ... ("BOTH", "LONG", "SHORT")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Все аргументы заполняются заглавными буквами
        - минимальное значение "quantity" рассчитывается как (
        end_point /fapi/v1/exchangeInfo
        float(["symbols"][если "symbol" == "symbol"]["filters"][если "filterType" == "MIN_NOTIONAL"]["notional"]) /
        end_point /fapi/v1/ticker/price
        float(["price"]
        )
        - "side" возможные варианты: ["BUY" - купить, "SELL"- продать]
        - "stop_price" используется если "type" == ("STOP", "STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET")
        - "timeInForce" возможные варианты: ["GTC" – ордер будет висеть до тех пор, пока его не отменят,
                                             "IOC" – будет куплено то количество, которое можно купить немедленно.
                                                     Все, что не удалось купить, будет отменено,
                                             "FOK" – либо будет куплено все указанное количество немедленно,
                                                     либо не будет куплено вообще ничего, ордер отменится,
                                             "GTD" - до определённой даты или до конца дня,
                                             "GTX" - ....
        - "newOrderRespType" возможные варианты: ["ACK" - короткий ответ,
                                                  "RESULT" - оптимальный ответ,
                                                  "FULL" - полный ответ]
        - если "side" == "BUY", то "stopPrice" должен быть больше "price" и
                                                                меньше end_point /fapi/v1/ticker/price float(["price"])
        - если "side" == "SELL", то "stopPrice" должен быть меньше "price" и
                                                                больше end_point /fapi/v1/ticker/price float(["price"])

        Ответ:
        {
           "orderId": 31424113323,
           "symbol": "ADAUSDT",
           "status": "NEW",
           "clientOrderId": "25357",
           "price": "0.20000",
           "avgPrice": "0.00000",
           "origQty": "14",
           "executedQty": "0",
           "cumQty": "0",
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "TAKE_PROFIT",
           "reduceOnly": false,
           "closePosition": false,   (if Close-All)
           "side": "BUY",
           "positionSide": "BOTH",
           "stopPrice": "0.30000",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "TAKE_PROFIT",
           "updateTime": 1682113007235
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "quantity": quantity,
            "price": price,
            "stopPrice": stop_price,
            "positionSide": position_side,
            "type": my_type,
            "timeInForce": time_in_force,
            "newClientOrderId": new_client_order_id,
            "workingType": working_type,
            "priceProtect": price_protect,
            "newOrderRespType": new_order_resp_type,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_profit_market_futures(self,
                                   symbol: str,
                                   side: str,
                                   quantity: str,
                                   stop_price: str,
                                   time_stamp: str,
                                   my_type: str = "TAKE_PROFIT_MARKET",
                                   time_in_force: str = "GTC",
                                   new_order_resp_type: str = "RESULT",
                                   new_client_order_id: str = str(randint(1, 100000)),
                                   reduce_only: str = "FALSE",
                                   close_position: str = "FALSE",
                                   working_type: str = "CONTRACT_PRICE",
                                   price_protect: str = "FALSE",
                                   position_side: str = "BOTH",
                                   recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить ордер TAKE_PROFIT_MARKET

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        0

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - side="side" (str): сторона сделки ("BUY", "SELL")
        - quantity="quantity" (str): количества актива в сделки ("16", ...)
        - stop_price="stopPrice" (str): по какой цене разместится profit_order ("268234", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - my_type="type" (str): вид ордера ("TAKE_PROFIT_MARKET")
        - time_in_force="timeInForce" (str): режим исполнения ("GTC", "IOC", "FOK", "GTD", "GTX")
        - new_order_resp_type="newOrderRespType" (str): развёрнутость ответа ("ACK", "RESULT", "FULL")
        - new_client_order_id="newClientOrderId" (str): идентификатор сделки ("567887", ...)
        - reduce_only="reduceOnly" (str): ... ("FALSE", "TRUE")
        - close_position="closePosition" (str): ... ("FALSE", "TRUE")
        - working_type="workingType" (str): ... ("CONTRACT_PRICE", "MARK_PRICE")
        - price_protect="priceProtect" (str): ... ("FALSE", "TRUE")
        - position_side="positionSide" (str): ... ("BOTH", "LONG", "SHORT")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Все аргументы заполняются заглавными буквами
        - минимальное значение "quantity" рассчитывается как (
        end_point /fapi/v1/exchangeInfo
        float(["symbols"][если "symbol" == "symbol"]["filters"][если "filterType" == "MIN_NOTIONAL"]["notional"]) /
        end_point /fapi/v1/ticker/price
        float(["price"]
        )
        - "side" возможные варианты: ["BUY" - купить, "SELL"- продать]
        - "stop_price" используется если "type" == ("STOP", "STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET")
        - "timeInForce" возможные варианты: ["GTC" – ордер будет висеть до тех пор, пока его не отменят,
                                             "IOC" – будет куплено то количество, которое можно купить немедленно.
                                                     Все, что не удалось купить, будет отменено,
                                             "FOK" – либо будет куплено все указанное количество немедленно,
                                                     либо не будет куплено вообще ничего, ордер отменится,
                                             "GTD" - до определённой даты или до конца дня,
                                             "GTX" - ....
        - "reduceOnly" не может быть отправлен в режиме хеджирования
           так же нельзя отправить с параметром closePosition="True"
        - "newOrderRespType" возможные варианты: ["ACK" - короткий ответ,
                                                  "RESULT" - оптимальный ответ,
                                                  "FULL" - полный ответ]
        - если "side" == "BUY", то "stopPrice" должен быть меньше end_point /fapi/v1/ticker/price float(["price"])
        - если "side" == "SELL", то "stopPrice" должен быть больше end_point /fapi/v1/ticker/price float(["price"])

        Ответ:
        {
           "orderId": 31424170469,
           "symbol": "ADAUSDT",
           "status": "NEW",
           "clientOrderId": "46901",
           "price": "0",
           "avgPrice": "0.00000",
           "origQty": "13",
           "executedQty": "0",
           "cumQty": "0",
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "TAKE_PROFIT_MARKET",
           "reduceOnly": false,
           "closePosition": false,   (if Close-All)
           "side": "BUY",
           "positionSide": "BOTH",
           "stopPrice": "0.30000",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "TAKE_PROFIT_MARKET",
           "updateTime": 1682113177309
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "quantity": quantity,
            "stopPrice": stop_price,
            "positionSide": position_side,
            "type": my_type,
            "timeInForce": time_in_force,
            "reduceOnly": reduce_only,
            "newClientOrderId": new_client_order_id,
            "closePosition": close_position,
            "workingType": working_type,
            "priceProtect": price_protect,
            "newOrderRespType": new_order_resp_type,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_stop_limit_futures(self,
                                symbol: str,
                                side: str,
                                quantity: str,
                                price: str,
                                stop_price: str,
                                time_stamp: str,
                                my_type: str = "STOP",
                                time_in_force: str = "GTC",
                                new_order_resp_type: str = "RESULT",
                                new_client_order_id: str = str(randint(1, 100000)),
                                working_type: str = "CONTRACT_PRICE",
                                price_protect: str = "FALSE",
                                position_side: str = "BOTH",
                                recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить ордер STOP

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        0

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - side="side" (str): сторона сделки ("BUY", "SELL")
        - quantity="quantity" (str): количества актива в сделки ("16", ...)
        - price="price" (str): по достижению какой цены активируется "stop_price" ("26234", ...)
        - stop_price="stopPrice" (str): по какой цене разместится stop_order ("27328", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - my_type="type" (str): вид ордера ("STOP")
        - time_in_force="timeInForce" (str): режим исполнения ("GTC", "IOC", "FOK", "GTD", "GTX")
        - new_order_resp_type="newOrderRespType" (str): развёрнутость ответа ("ACK", "RESULT", "FULL")
        - new_client_order_id="newClientOrderId" (str): идентификатор сделки ("567887", ...)
        - working_type="workingType" (str): ... ("CONTRACT_PRICE", "MARK_PRICE")
        - price_protect="priceProtect" (str): ... ("FALSE", "TRUE")
        - position_side="positionSide" (str): ... ("BOTH", "LONG", "SHORT")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Все аргументы заполняются заглавными буквами
        - минимальное значение "quantity" рассчитывается как (
        end_point /fapi/v1/exchangeInfo
        float(["symbols"][если "symbol" == "symbol"]["filters"][если "filterType" == "MIN_NOTIONAL"]["notional"]) /
        end_point /fapi/v1/ticker/price
        float(["price"]
        )
        - "side" возможные варианты: ["BUY" - купить, "SELL"- продать]
        - "stop_price" используется если "type" == ("STOP", "STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET")
        - "timeInForce" возможные варианты: ["GTC" – ордер будет висеть до тех пор, пока его не отменят,
                                             "IOC" – будет куплено то количество, которое можно купить немедленно.
                                                     Все, что не удалось купить, будет отменено,
                                             "FOK" – либо будет куплено все указанное количество немедленно,
                                                     либо не будет куплено вообще ничего, ордер отменится,
                                             "GTD" - до определённой даты или до конца дня,
                                             "GTX" - ....
        - "newOrderRespType" возможные варианты: ["ACK" - короткий ответ,
                                                  "RESULT" - оптимальный ответ,
                                                  "FULL" - полный ответ]
        - если "side" == "BUY", то "stopPrice" должен быть больше "price" и
                                                                больше end_point /fapi/v1/ticker/price float(["price"])
        - если "side" == "SELL", то "stopPrice" должен быть меньше "price" и
                                                                меньше end_point /fapi/v1/ticker/price float(["price"])

        Ответ:
        {
           "orderId": 31424065822,
           "symbol": "ADAUSDT",
           "status": "NEW",
           "clientOrderId": "68961",
           "price": "0.40000",
           "avgPrice": "0.00000",
           "origQty": "14",
           "executedQty": "0",
           "cumQty": "0",
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "STOP",
           "reduceOnly": false,
           "closePosition": false,   (if Close-All)
           "side": "SELL",
           "positionSide": "BOTH",
           "stopPrice": "0.30000",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "STOP",
           "updateTime": 1682112835383
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "quantity": quantity,
            "price": price,
            "stopPrice": stop_price,
            "positionSide": position_side,
            "type": my_type,
            "timeInForce": time_in_force,
            "newClientOrderId": new_client_order_id,
            "workingType": working_type,
            "priceProtect": price_protect,
            "newOrderRespType": new_order_resp_type,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_stop_market_futures(self,
                                 symbol: str,
                                 side: str,
                                 quantity: str,
                                 stop_price: str,
                                 time_stamp: str,
                                 my_type: str = "STOP_MARKET",
                                 time_in_force: str = "GTC",
                                 new_order_resp_type: str = "RESULT",
                                 new_client_order_id: str = str(randint(1, 100000)),
                                 reduce_only: str = "FALSE",
                                 close_position: str = "FALSE",
                                 working_type: str = "CONTRACT_PRICE",
                                 price_protect: str = "FALSE",
                                 position_side: str = "BOTH",
                                 recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить ордер STOP_MARKET

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        0

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - side="side" (str): сторона сделки ("BUY", "SELL")
        - quantity="quantity" (str): количества актива в сделки ("16", ...)
        - stop_price="stopPrice" (str): по какой цене разместится stop_order ("268234", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - my_type="type" (str): вид ордера ("STOP_MARKET")
        - time_in_force="timeInForce" (str): режим исполнения ("GTC", "IOC", "FOK", "GTD", "GTX")
        - new_order_resp_type="newOrderRespType" (str): развёрнутость ответа ("ACK", "RESULT", "FULL")
        - new_client_order_id="newClientOrderId" (str): идентификатор сделки ("567887", ...)
        - reduce_only="reduceOnly" (str): ... ("FALSE", "TRUE")
        - close_position="closePosition" (str): ... ("FALSE", "TRUE")
        - working_type="workingType" (str): ... ("CONTRACT_PRICE", "MARK_PRICE")
        - price_protect="priceProtect" (str): ... ("FALSE", "TRUE")
        - position_side="positionSide" (str): ... ("BOTH", "LONG", "SHORT")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Все аргументы заполняются заглавными буквами
        - минимальное значение "quantity" рассчитывается как (
        end_point /fapi/v1/exchangeInfo
        float(["symbols"][если "symbol" == "symbol"]["filters"][если "filterType" == "MIN_NOTIONAL"]["notional"]) /
        end_point /fapi/v1/ticker/price
        float(["price"]
        )
        - "side" возможные варианты: ["BUY" - купить, "SELL"- продать]
        - "stop_price" используется если "type" == ("STOP", "STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET")
        - "timeInForce" возможные варианты: ["GTC" – ордер будет висеть до тех пор, пока его не отменят,
                                             "IOC" – будет куплено то количество, которое можно купить немедленно.
                                                     Все, что не удалось купить, будет отменено,
                                             "FOK" – либо будет куплено все указанное количество немедленно,
                                                     либо не будет куплено вообще ничего, ордер отменится,
                                             "GTD" - до определённой даты или до конца дня,
                                             "GTX" - ....
        - "reduceOnly" не может быть отправлен в режиме хеджирования
           так же нельзя отправить с параметром closePosition="True"
        - "newOrderRespType" возможные варианты: ["ACK" - короткий ответ,
                                                  "RESULT" - оптимальный ответ,
                                                  "FULL" - полный ответ]
        - если "side" == "BUY", то "stopPrice" должен быть больше end_point /fapi/v1/ticker/price float(["price"])
        - если "side" == "SELL", то "stopPrice" должен быть меньше end_point /fapi/v1/ticker/price float(["price"])

        Ответ:
        {
           "orderId": 31424144991,
           "symbol": "ADAUSDT",
           "status": "NEW",
           "clientOrderId": "32810",
           "price": "0",
           "avgPrice": "0.00000",
           "origQty": "13",
           "executedQty": "0",
           "cumQty": "0",
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "STOP_MARKET",
           "reduceOnly": false,
           "closePosition": false,   (if Close-All)
           "side": "BUY",
           "positionSide": "BOTH",
           "stopPrice": "0.50000",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "STOP_MARKET",
           "updateTime": 1682113105248
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "quantity": quantity,
            "stopPrice": stop_price,
            "positionSide": position_side,
            "type": my_type,
            "timeInForce": time_in_force,
            "reduceOnly": reduce_only,
            "newClientOrderId": new_client_order_id,
            "closePosition": close_position,
            "workingType": working_type,
            "priceProtect": price_protect,
            "newOrderRespType": new_order_resp_type,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_trailing_stop_market_futures(self,
                                          symbol: str,
                                          side: str,
                                          quantity: str,
                                          activation_price: str,
                                          callback_rate: str,
                                          time_stamp: str,
                                          my_type: str = "TRAILING_STOP_MARKET",
                                          time_in_force: str = "GTC",
                                          new_order_resp_type: str = "RESULT",
                                          new_client_order_id: str = str(randint(1, 100000)),
                                          working_type: str = "CONTRACT_PRICE",
                                          position_side: str = "BOTH",
                                          recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить ордер TRAILING_STOP_MARKET

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        0

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - side="side" (str): сторона сделки ("BUY", "SELL")
        - quantity="quantity" (str): количества актива в сделки ("16", ...)
        - activation_price="activationPrice" (str): ... ("23032", ...)
        - callback_rate="callbackRate" (str): ... ("0.1", ..., "5.0")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - my_type="type" (str): вид ордера ("TRAILING_STOP_MARKET")
        - time_in_force="timeInForce" (str): режим исполнения ("GTC", "IOC", "FOK", "GTD", "GTX")
        - new_order_resp_type="newOrderRespType" (str): развёрнутость ответа ("ACK", "RESULT", "FULL")
        - new_client_order_id="newClientOrderId" (str): идентификатор сделки ("567887", ...)
        - working_type="workingType" (str): ... ("CONTRACT_PRICE", "MARK_PRICE")
        - position_side="positionSide" (str): ... ("BOTH", "LONG", "SHORT")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Все аргументы заполняются заглавными буквами
        - минимальное значение "quantity" рассчитывается как (
        end_point /fapi/v1/exchangeInfo
        float(["symbols"][если "symbol" == "symbol"]["filters"][если "filterType" == "MIN_NOTIONAL"]["notional"]) /
        end_point /fapi/v1/ticker/price
        float(["price"]
        )
        - "side" возможные варианты: ["BUY" - купить, "SELL"- продать]
        - "timeInForce" возможные варианты: ["GTC" – ордер будет висеть до тех пор, пока его не отменят,
                                             "IOC" – будет куплено то количество, которое можно купить немедленно.
                                                     Все, что не удалось купить, будет отменено,
                                             "FOK" – либо будет куплено все указанное количество немедленно,
                                                     либо не будет куплено вообще ничего, ордер отменится,
                                             "GTD" - до определённой даты или до конца дня,
                                             "GTX" - ....
        - "newOrderRespType" возможные варианты: ["ACK" - короткий ответ,
                                                  "RESULT" - оптимальный ответ,
                                                  "FULL" - полный ответ]
        - если "side" == "BUY", то "activationPrice" должен быть меньше end_point /fapi/v1/ticker/price float(["price"])
        - если "side" == "SELL", то "activationPrice"должен быть больше end_point /fapi/v1/ticker/price float(["price"])

        Ответ:
        {
           "orderId": 31424210277,
           "symbol": "ADAUSDT",
           "status": "NEW",
           "clientOrderId": "30856",
           "price": "0",
           "avgPrice": "0.00000",
           "origQty": "14",
           "executedQty": "0",
           "cumQty": "0",
           "activatePrice": "0.30970",   (в ответе только если ордер TRAILING_STOP_MARKET)
           "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "TRAILING_STOP_MARKET",
           "reduceOnly": false,
           "closePosition": false,   (if Close-All)
           "side": "BUY",
           "positionSide": "BOTH",
           "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "TRAILING_STOP_MARKET",
           "updateTime": 1682113313628
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "quantity": quantity,
            "activationPrice": activation_price,
            "callbackRate": callback_rate,
            "positionSide": position_side,
            "type": my_type,
            "timeInForce": time_in_force,
            "newClientOrderId": new_client_order_id,
            "workingType": working_type,
            "newOrderRespType": new_order_resp_type,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def put_limit_futures(self,
                          symbol: str,
                          side: str,
                          quantity: str,
                          price: str,
                          time_stamp: str,
                          order_id: str = "",
                          orig_client_order_id: str = "",
                          recv_window: str = "5000") -> dict:
        """
        Запрос:
        Обновить ордер LIMIT

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - side="side" (str): сторона сделки ("BUY", "SELL")
        - quantity="quantity" (str): количества актива в сделки ("16", ...)
        - price="price" (str): по какой цене выставится limit_order ("26234", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - order_id="orderId" (str): самозаполняющимся идентификатор для каждой сделки ("567834287", ...)
        - orig_client_order_id="origClientOrderId" (str): идентификатор сделки  ("567887", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Необходимо обязательно отправить либо order_id, либо orig_client_order_id.
        - orderId имеет преимущественную силу, если отправлены оба.
        - Должны быть отправлены и отличаться от старого заказа или количество или цена.
        - Один заказ может быть изменен не более 10000 раз

        Ответ:
        {
           "orderId": 32717294490,
           "symbol": "ADAUSDT",
           "status": "NEW",
           "clientOrderId": "31699",
           "price": "0.33000",
           "avgPrice": "0.00000",
           "origQty": "17",
           "executedQty": "0",
           "cumQty": "0",
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "LIMIT",
           "reduceOnly": false,
           "closePosition": false,
           "side": "BUY",
           "positionSide": "BOTH",
           "stopPrice": "0",
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,
           "origType": "LIMIT",
           "updateTime": 1686133002234
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "quantity": quantity,
            "price": price,
            "timestamp": time_stamp,
            "orderId": order_id,
            "origClientOrderId": orig_client_order_id,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.put(url=complete_request, params=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def delete_order_futures(self,
                             symbol: str,
                             time_stamp: str,
                             order_id: str = "",
                             orig_client_order_id: str = "",
                             recv_window: str = "5000") -> dict:
        """
        Запрос:
        Закрыть ордер по идентификатору

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - order_id="orderId" (str): самозаполняющимся идентификатор для каждой сделки ("567834287", ...)
        - orig_client_order_id="origClientOrderId" (str): идентификатор сделки  ("567887", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Закрывает ордера, не открытые позиции!!!
        - Необходимо обязательно отправить либо order_id, либо orig_client_order_id
        - order_id является самозаполняющимся для каждого конкретного символа

        Ответ:
        {
           "orderId": 31425266183,
           "symbol": "ADAUSDT",
           "status": "CANCELED",
           "clientOrderId": "9766",
           "price": "0",
           "avgPrice": "0.00000",
           "origQty": "14",
           "executedQty": "0",
           "cumQty": "0",
           "activatePrice": "0.30970",   (в ответе только если ордер TRAILING_STOP_MARKET)
           "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "TRAILING_STOP_MARKET",
           "reduceOnly": false,
           "closePosition": false,   (if Close-All)
           "side": "BUY",
           "positionSide": "BOTH",
           "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "TRAILING_STOP_MARKET",
           "updateTime": 1682117049586
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "orderId": order_id,
            "origClientOrderId": orig_client_order_id,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.delete(url=complete_request, params=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_multiple_limit_futures(self,
                                    data_list: list[list[str]],
                                    time_stamp: str,
                                    recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить множественный ордер LIMIT

        Полный url:
        "https://fapi.binance.com/fapi/v1/batchOrders"

        Вес запроса:
        5

        Параметры:
        - data_list="batchOrders" (list[list[str, ...], ...]): список сделок в строковом формате
        ("[{"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0",
            "price": "0.3896", "positionSide": "BOTH", "type": "LIMIT",
            "timeInForce": "GTC", "newClientOrderId": "232", "workingType": "CONTRACT_PRICE",
            "priceProtect": "FALSE", "newOrderRespType": "RESULT"},
           {"symbol": "BTCUSDT", "side": "BUY", "quantity": "1.0",
            "price": "45596", "positionSide": "BOTH", "type": "MARKET",
            "timeInForce": "GTC", "newClientOrderId": "232112", "workingType": "CONTRACT_PRICE",
            "priceProtect": "FALSE", "newOrderRespType": "RESULT"}, ...]")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Максимально можно сделать запрос на 5 ордеров
        - Все данные в списках заполняются заглавными буквами
        - порядок записи данных в data_list: ["symbol", "side", "quantity", "price", "positionSide", "type",
                                "timeInForce", "newClientOrderId", "workingType", "priceProtect", "newOrderRespType"]
        - возможные варианты записи data_list:  [[<"ADAUSDT">, <"BUY", "SELL">, <"14.0">, <"0.3896">,
                                                  <"BOTH", "LONG", "SHORT">, <"LIMIT">,
                                                  <"GTC", "IOC", "FOK", "GTD", "GTX">, <"2312">,
                                                  <"CONTRACT_PRICE", "MARK_PRICE">, <"FALSE", "TRUE">,
                                                  <"ACK", "RESULT", "FULL">], ...]

        Ответ:
        [
           {
              "orderId": 31424362832,
              "symbol": "ADAUSDT",
              "status": "FILLED",
              "clientOrderId": "97481",
              "price": "0.38960",
              "avgPrice": "0.38110",
              "origQty": "14",
              "executedQty": "14",
              "cumQty": "14",
              "cumQuote": "5.33540",
              "timeInForce": "GTC",
              "type": "LIMIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "LIMIT",
              "updateTime": 1682113878772
           },
           {
              "orderId": 31424362831,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "14018",
              "price": "0.37960",
              "avgPrice": "0.00000",
              "origQty": "32",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "LIMIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "LIMIT",
              "updateTime": 1682113878772
           },
           {
              "orderId": 31424362828,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "6820",
              "price": "0.36960",
              "avgPrice": "0.00000",
              "origQty": "16",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "LIMIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "LIMIT",
              "updateTime": 1682113878772
           },
           {
              "orderId": 31424362829,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "29448",
              "price": "0.35960",
              "avgPrice": "0.00000",
              "origQty": "17",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "LIMIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "LIMIT",
              "updateTime": 1682113878772
           },
           {
              "orderId": 31424362830,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "93504",
              "price": "0.34960",
              "avgPrice": "0.00000",
              "origQty": "20",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "LIMIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "LIMIT",
              "updateTime": 1682113878772
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/batchOrders"

        list_batch_orders = list()

        key_list = ["symbol", "side", "quantity", "price", "positionSide", "type", "timeInForce", "newClientOrderId",
                    "workingType", "priceProtect", "newOrderRespType"]

        for count, values_list in enumerate(data_list):
            result_list = dict(zip(key_list, values_list))
            list_batch_orders.append(result_list)

        parameters = {
            "batchOrders": json.dumps(list_batch_orders),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_multiple_market_futures(self,
                                     data_list: list[list[str]],
                                     time_stamp: str,
                                     recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить множественный ордер MARKER

        Полный url:
        "https://fapi.binance.com/fapi/v1/batchOrders"

        Вес запроса:
        5

        Параметры:
        - data_list="batchOrders" (list[list[str, ...], ...]): список сделок в строковом формате
        ("[{"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "positionSide": "BOTH",
            "type": "LIMIT", "newClientOrderId": "232", "workingType": "CONTRACT_PRICE",
            "priceProtect": "FALSE", "newOrderRespType": "RESULT"},
           {"symbol": "BTCUSDT", "side": "BUY", "quantity": "1.0", "price": "45596", "positionSide": "BOTH",
            "type": "MARKET", "timeInForce": "GTC", "newClientOrderId": "232112", "workingType": "CONTRACT_PRICE",
            "priceProtect": "FALSE", "newOrderRespType": "RESULT"}, ...]")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - "recvWindow"=recv_window (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Максимально можно сделать запрос на 5 ордеров
        - Все данные в списках заполняются заглавными буквами
        - порядок записи данных в data_list: ["symbol", "side", "quantity", "positionSide", "type", "newClientOrderId",
                                              "workingType", "priceProtect", "newOrderRespType"]
        - возможные варианты записи data_list:  [[<"ADAUSDT">, <"BUY", "SELL">, <"14.0">, <"BOTH", "LONG", "SHORT">,
                                                  <"MARKER">, <"2312">, <"CONTRACT_PRICE", "MARK_PRICE">,
                                                  <"FALSE", "TRUE">, <"ACK", "RESULT", "FULL">], ...]

        Ответ:
        [
           {
              "orderId": 31424464263,
              "symbol": "ADAUSDT",
              "status": "FILLED",
              "clientOrderId": "74133",
              "price": "0",
              "avgPrice": "0.38030",
              "origQty": "14",
              "executedQty": "14",
              "cumQty": "14",
              "cumQuote": "5.32420",
              "timeInForce": "GTC",
              "type": "MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "MARKET",
              "updateTime": 1682114212682
           },
           {
              "orderId": 31424464264,
              "symbol": "ADAUSDT",
              "status": "FILLED",
              "clientOrderId": "76171",
              "price": "0",
              "avgPrice": "0.38030",
              "origQty": "15",
              "executedQty": "15",
              "cumQty": "15",
              "cumQuote": "5.70450",
              "timeInForce": "GTC",
              "type": "MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "MARKET",
              "updateTime": 1682114212682
           },
           {
              "orderId": 31424464265,
              "symbol": "ADAUSDT",
              "status": "FILLED",
              "clientOrderId": "74342",
              "price": "0",
              "avgPrice": "0.38030",
              "origQty": "16",
              "executedQty": "16",
              "cumQty": "16",
              "cumQuote": "6.08480",
              "timeInForce": "GTC",
              "type": "MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "MARKET",
              "updateTime": 1682114212682
           },
           {
              "orderId": 31424464266,
              "symbol": "ADAUSDT",
              "status": "FILLED",
              "clientOrderId": "98485",
              "price": "0",
              "avgPrice": "0.38030",
              "origQty": "17",
              "executedQty": "17",
              "cumQty": "17",
              "cumQuote": "6.46510",
              "timeInForce": "GTC",
              "type": "MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "MARKET",
              "updateTime": 1682114212682
           },
           {
              "orderId": 31424464267,
              "symbol": "ADAUSDT",
              "status": "FILLED",
              "clientOrderId": "56364",
              "price": "0",
              "avgPrice": "0.38030",
              "origQty": "18",
              "executedQty": "18",
              "cumQty": "18",
              "cumQuote": "6.84540",
              "timeInForce": "GTC",
              "type": "MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "MARKET",
              "updateTime": 1682114212682
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/batchOrders"

        list_batch_orders = list()

        key_list = ["symbol", "side", "quantity", "positionSide", "type", "newClientOrderId", "workingType",
                    "priceProtect", "newOrderRespType"]

        for count, values_list in enumerate(data_list):
            result_list = dict(zip(key_list, values_list))
            list_batch_orders.append(result_list)

        parameters = {
            "batchOrders": json.dumps(list_batch_orders),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_multiple_profit_limit_futures(self,
                                           data_list: list[list[str]],
                                           time_stamp: str,
                                           recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить множественный ордер TAKE_PROFIT

        Полный url:
        "https://fapi.binance.com/fapi/v1/batchOrders"

        Вес запроса:
        5

        Параметры:
        - data_list="batchOrders" (list[list[str, ...], ...]): список сделок в строковом формате
        ("[{"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "price": "0.3896", "stopPrice": "0.4890",
            "positionSide": "BOTH", "type": "TAKE_PROFIT", "timeInForce": "GTC", "newClientOrderId": "232",
            "workingType": "CONTRACT_PRICE", "priceProtect": "FALSE", "newOrderRespType": "RESULT"},
           {"symbol": "BTCUSDT", "side": "BUY", "quantity": "1.0", "price": "45596", "stopPrice": "0.4890",
            "positionSide": "BOTH", "type": "MARKET", "timeInForce": "GTC", "newClientOrderId": "232112",
            "workingType": "CONTRACT_PRICE", "priceProtect": "FALSE", "newOrderRespType": "RESULT"}, ...]")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Максимально можно сделать запрос на 5 ордеров
        - Все данные в списках заполняются заглавными буквами
        - порядок записи данных в data_list: ["symbol", "side", "quantity", "price", "stopPrice", "positionSide",
                                              "type", "timeInForce", "newClientOrderId", "workingType",
                                              "priceProtect", "newOrderRespType"]
        - возможные варианты записи data_list:  [[<"ADAUSDT">, <"BUY", "SELL">, <"14.0">, <"0.3896">,
                                                  <"0.4890">, <"BOTH", "LONG", "SHORT">, <"TAKE_PROFIT">,
                                                  <"GTC", "IOC", "FOK", "GTD", "GTX">, <"2312">,
                                                  <"CONTRACT_PRICE", "MARK_PRICE">, <"FALSE", "TRUE">,
                                                  <"ACK", "RESULT", "FULL">], ...]

        Ответ:
        [
           {
              "orderId": 31424574628,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "10997",
              "price": "0.25960",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.28900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT",
              "updateTime": 1682114551241
           },
           {
              "orderId": 31424574629,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "87542",
              "price": "0.25960",
              "avgPrice": "0.00000",
              "origQty": "32",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.28900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT",
              "updateTime": 1682114551241
           },
           {
              "orderId": 31424574631,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "31299",
              "price": "0.25960",
              "avgPrice": "0.00000",
              "origQty": "16",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.28900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT",
              "updateTime": 1682114551241
           },
           {
              "orderId": 31424574630,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "11140",
              "price": "0.25960",
              "avgPrice": "0.00000",
              "origQty": "17",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.28900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT",
              "updateTime": 1682114551241
           },
           {
              "orderId": 31424574632,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "93867",
              "price": "0.25960",
              "avgPrice": "0.00000",
              "origQty": "20",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.28900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT",
              "updateTime": 1682114551241
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/batchOrders"

        list_batch_orders = list()

        key_list = ["symbol", "side", "quantity", "price", "stopPrice", "positionSide", "type", "timeInForce",
                    "newClientOrderId", "workingType", "priceProtect", "newOrderRespType"]

        for count, values_list in enumerate(data_list):
            result_list = dict(zip(key_list, values_list))
            list_batch_orders.append(result_list)

        parameters = {
            "batchOrders": json.dumps(list_batch_orders),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_multiple_profit_market_futures(self,
                                            data_list: list[list[str]],
                                            time_stamp: str,
                                            recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить множественный ордер TAKE_PROFIT_MARKET

        Полный url:
        "https://fapi.binance.com/fapi/v1/batchOrders"

        Вес запроса:
        5

        Параметры:
        - data_list="batchOrders" (list[list[str, ...], ...]): список сделок в строковом формате
        ("[{"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "stopPrice": "0.4890", "positionSide": "BOTH",
            "type": "TAKE_PROFIT_MARKET", "timeInForce": "GTC", "reduceOnly": "FALSE", "newClientOrderId": "232",
            "closePosition": "FALSE", "workingType": "CONTRACT_PRICE", "priceProtect": "FALSE",
            "newOrderRespType": "RESULT"},
        {"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "stopPrice": "0.4890", "positionSide": "BOTH",
            "type": "TAKE_PROFIT_MARKET", "timeInForce": "GTC", "reduceOnly": "FALSE", "newClientOrderId": "232",
            "closePosition": "FALSE", "workingType": "CONTRACT_PRICE", "priceProtect": "FALSE",
            "newOrderRespType": "RESULT"}, ...]")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Максимально можно сделать запрос на 5 ордеров
        - Все данные в списках заполняются заглавными буквами
        - порядок записи данных в data_list: ["symbol", "side", "quantity", "stopPrice", "positionSide", "type",
                                              "timeInForce", "reduceOnly", "newClientOrderId", "closePosition",
                                              "workingType", "priceProtect", "newOrderRespType"]
        - возможные варианты записи data_list:  [[<"ADAUSDT">, <"BUY", "SELL">, <"14.0">, <"0.4890">,
                                                  <"BOTH", "LONG", "SHORT">, <"TAKE_PROFIT_MARKET">,
                                                  <"GTC", "IOC", "FOK", "GTD", "GTX">, <"FALSE", "TRUE">,
                                                  <"2312">, <"FALSE", "TRUE">, <"CONTRACT_PRICE", "MARK_PRICE">
                                                   <"FALSE", "TRUE">, <"ACK", "RESULT", "FULL">], ...]

        Ответ:
        [
           {
              "orderId": 31424671606,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "84441",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.30900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT_MARKET",
              "updateTime": 1682114897270
           },
           {
              "orderId": 31424671609,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "27289",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "32",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.30900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT_MARKET",
              "updateTime": 1682114897270
           },
           {
              "orderId": 31424671607,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "13931",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "16",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.30900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT_MARKET",
              "updateTime": 1682114897270
           },
           {
              "orderId": 31424671608,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "62458",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "17",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.30900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT_MARKET",
              "updateTime": 1682114897270
           },
           {
              "orderId": 31424671610,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "85969",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "20",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TAKE_PROFIT_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.30900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TAKE_PROFIT_MARKET",
              "updateTime": 1682114897270
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/batchOrders"

        list_batch_orders = list()

        key_list = ["symbol", "side", "quantity", "stopPrice", "positionSide", "type", "timeInForce", "reduceOnly",
                    "newClientOrderId", "closePosition", "workingType", "priceProtect", "newOrderRespType"]

        for count, values_list in enumerate(data_list):
            result_list = dict(zip(key_list, values_list))
            list_batch_orders.append(result_list)

        parameters = {
            "batchOrders": json.dumps(list_batch_orders),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_multiple_stop_limit_futures(self,
                                         data_list: list[list[str]],
                                         time_stamp: str,
                                         recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить множественный ордер STOP

        Полный url:
        "https://fapi.binance.com/fapi/v1/batchOrders"

        Вес запроса:
        5

        Параметры:
        - data_list="batchOrders" (list[list[str, ...], ...]): список сделок в строковом формате
        ("[{"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "price": "0.3896", "stopPrice": "0.4890",
            "positionSide": "BOTH", "type": "STOP", "timeInForce": "GTC", "newClientOrderId": "232",
            "workingType": "CONTRACT_PRICE", "priceProtect": "FALSE", "newOrderRespType": "RESULT"},
           {"symbol": "BTCUSDT", "side": "BUY", "quantity": "1.0", "price": "45596", stopPrice": "0.4890",
            "positionSide": "BOTH", "type": "MARKET", "timeInForce": "GTC", "newClientOrderId": "232112",
            "workingType": "CONTRACT_PRICE", "priceProtect": "FALSE", "newOrderRespType": "RESULT"}, ...]")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Максимально можно сделать запрос на 5 ордеров
        - Все данные в списках заполняются заглавными буквами
        - порядок записи данных в data_list: ["symbol", "side", "quantity", "price", "stopPrice", "positionSide",
                                              "type", "timeInForce", "newClientOrderId", "workingType",
                                              "priceProtect", "newOrderRespType"]
        - возможные варианты записи data_list:  [[<"ADAUSDT">, <"BUY", "SELL">, <"14.0">, <"0.3896">, <"0.4890">,
                                                  <"BOTH", "LONG", "SHORT">, <"STOP">,
                                                  <"GTC", "IOC", "FOK", "GTD", "GTX">, <"2312">,
                                                  <"CONTRACT_PRICE", "MARK_PRICE">, <"FALSE", "TRUE">,
                                                  <"ACK", "RESULT", "FULL">], ...]

        Ответ:
        [
           {
              "orderId": 31424518687,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "59119",
              "price": "0.38960",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP",
              "updateTime": 1682114391378
           },
           {
              "orderId": 31424518689,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "87323",
              "price": "0.37960",
              "avgPrice": "0.00000",
              "origQty": "32",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP",
              "updateTime": 1682114391378
           },
           {
              "orderId": 31424518686,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "41246",
              "price": "0.36960",
              "avgPrice": "0.00000",
              "origQty": "16",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP",
              "updateTime": 1682114391378
           },
           {
              "orderId": 31424518690,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "44910",
              "price": "0.35960",
              "avgPrice": "0.00000",
              "origQty": "17",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP",
              "updateTime": 1682114391378
           },
           {
              "orderId": 31424518688,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "52487",
              "price": "0.34960",
              "avgPrice": "0.00000",
              "origQty": "20",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP",
              "updateTime": 1682114391378
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/batchOrders"

        list_batch_orders = list()

        key_list = ["symbol", "side", "quantity", "price", "stopPrice", "positionSide", "type", "timeInForce",
                    "newClientOrderId", "workingType", "priceProtect", "newOrderRespType"]

        for count, values_list in enumerate(data_list):
            result_list = dict(zip(key_list, values_list))
            list_batch_orders.append(result_list)

        parameters = {
            "batchOrders": json.dumps(list_batch_orders),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_multiple_stop_market_futures(self,
                                          data_list: list[list[str]],
                                          time_stamp: str,
                                          recv_window: str = "5000") -> dict:
        """
        Запрос:
        Разместить множественный ордер STOP_MARKET

        Полный url:
        "https://fapi.binance.com/fapi/v1/batchOrders"

        Вес запроса:
        5

        Параметры:
        - data_list="batchOrders" (list[list[str, ...], ...]): список сделок в строковом формате
        ("[{"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "stopPrice": "0.4890", "positionSide": "BOTH",
            "type": "STOP_MARKET", "timeInForce": "GTC", "reduceOnly": "FALSE", "newClientOrderId": "232",
            "closePosition": "FALSE", "workingType": "CONTRACT_PRICE", "priceProtect": "FALSE",
            "newOrderRespType": "RESULT"},
           {"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "stopPrice": "0.4890", "positionSide": "BOTH",
            "type": "STOP_MARKET", "timeInForce": "GTC", "reduceOnly": "FALSE", "newClientOrderId": "232",
            "closePosition": "FALSE", "workingType": "CONTRACT_PRICE", "priceProtect": "FALSE",
            "newOrderRespType": "RESULT"}, ...]")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Максимально можно сделать запрос на 5 ордеров
        - Все данные в списках заполняются заглавными буквами
        - порядок записи данных в data_list: ["symbol", "side", "quantity", "stopPrice", "positionSide", "type",
                                              "timeInForce", "reduceOnly", "newClientOrderId", "closePosition",
                                              "workingType", "priceProtect", "newOrderRespType"]
        - возможные варианты записи data_list:  [[<"ADAUSDT">, <"BUY", "SELL">, <"14.0">, <"0.4890">,
                                                  <"BOTH", "LONG", "SHORT">, <"STOP_MARKET">,
                                                  <"GTC", "IOC", "FOK", "GTD", "GTX">, <"FALSE", "TRUE">, <"2312">,
                                                  <"FALSE", "TRUE">, <"CONTRACT_PRICE", "MARK_PRICE">,
                                                  <"FALSE", "TRUE">, <"ACK", "RESULT", "FULL">], ...]

        Ответ:
        [
           {
              "orderId": 31424620475,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "24774",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP_MARKET",
              "updateTime": 1682114705072
           },
           {
              "orderId": 31424620472,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "70464",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "32",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP_MARKET",
              "updateTime": 1682114705072
           },
           {
              "orderId": 31424620473,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "61786",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "16",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP_MARKET",
              "updateTime": 1682114705072
           },
           {
              "orderId": 31424620476,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "64302",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "17",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP_MARKET",
              "updateTime": 1682114705072
           },
           {
              "orderId": 31424620474,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "59728",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "20",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.48900",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "STOP_MARKET",
              "updateTime": 1682114705072
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/batchOrders"

        list_batch_orders = list()

        key_list = ["symbol", "side", "quantity", "stopPrice", "positionSide", "type", "timeInForce", "reduceOnly",
                    "newClientOrderId", "closePosition", "workingType", "priceProtect", "newOrderRespType"]

        for count, values_list in enumerate(data_list):
            result_list = dict(zip(key_list, values_list))
            list_batch_orders.append(result_list)

        parameters = {
            "batchOrders": json.dumps(list_batch_orders),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def post_multiple_trailing_stop_market_futures(self,
                                                   data_list: list[list[str]],
                                                   time_stamp: str,
                                                   recv_window: str = "5000") -> dict[str, Any] | dict[str, Any]:
        """
        Запрос:
        Разместить множественный ордер TRAILING_STOP_MARKET

        Полный url:
        "https://fapi.binance.com/fapi/v1/batchOrders"

        Вес запроса:
        5

        Параметры:
        - data_list="batchOrders" (list[list[str, ...], ...]): список сделок в строковом формате
        ("[{"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "activationPrice": "0.4450", "callbackRate": "1.0",
            "positionSide": "BOTH", "type": "TRAILING_STOP_MARKET", "timeInForce": "GTC", "newClientOrderId": "232",
            "workingType": "CONTRACT_PRICE", "newOrderRespType": "RESULT"},
           {"symbol": "ADAUSDT", "side": "BUY","quantity": "14.0", "activationPrice": "0.4450", "callbackRate": "1.0",
            "positionSide": "BOTH", "type": "TRAILING_STOP_MARKET", "timeInForce": "GTC", "newClientOrderId": "232",
            "workingType": "CONTRACT_PRICE", "newOrderRespType": "RESULT"}, ...]")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Максимально можно сделать запрос на 5 ордеров
        - Все данные в списках заполняются заглавными буквами
        - порядок записи данных в data_list: ["symbol", "side", "quantity", "activationPrice", "callbackRate",
                                              "positionSide", "type", "timeInForce", "newClientOrderId",
                                              "workingType", "newOrderRespType"]
        - возможные варианты записи data_list:  [[<"ADAUSDT">, <"BUY", "SELL">, <"14.0">, <"0.4450"> ,
                                                  <"0.1", "0.2", "0.3", ..., "5.0"> , <"BOTH", "LONG", "SHORT">,
                                                  <"TRAILING_STOP_MARKET">, <"GTC", "IOC", "FOK", "GTD", "GTX">,
                                                  <"2312">, <"CONTRACT_PRICE", "MARK_PRICE">,
                                                  <"ACK", "RESULT", "FULL">], ...]

        Ответ:
        [
           {
              "orderId": 31424714051,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "43160",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "cumQty": "0",
              "activatePrice": "0.30900",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TRAILING_STOP_MARKET",
              "updateTime": 1682115046384
           },
           {
              "orderId": 31424714049,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "34698",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "cumQty": "0",
              "activatePrice": "0.30800",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TRAILING_STOP_MARKET",
              "updateTime": 1682115046384
           },
           {
              "orderId": 31424714048,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "8144",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "cumQty": "0",
              "activatePrice": "0.30700",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TRAILING_STOP_MARKET",
              "updateTime": 1682115046384
           },
           {
              "orderId": 31424714047,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "28876",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "cumQty": "0",
              "activatePrice": "0.30600",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TRAILING_STOP_MARKET",
              "updateTime": 1682115046384
           },
           {
              "orderId": 31424714050,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "73655",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "cumQty": "0",
              "activatePrice": "0.30500",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TRAILING_STOP_MARKET",
              "updateTime": 1682115046384
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/batchOrders"

        list_batch_orders = list()

        key_list = ["symbol", "side", "quantity", "activationPrice", "callbackRate", "positionSide", "type",
                    "timeInForce", "newClientOrderId", "workingType", "newOrderRespType"]

        for count, values_list in enumerate(data_list):
            result_list = dict(zip(key_list, values_list))
            list_batch_orders.append(result_list)

        parameters = {
            "batchOrders": json.dumps(list_batch_orders),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def put_multiple_limit_futures(self,
                                   data_list: list[list[str]],
                                   time_stamp: str,
                                   recv_window: str = "5000") -> dict:
        """
        Запрос:
        Обновить несколько ордеров LIMIT

        Полный url:
        "https://fapi.binance.com/fapi/v1/batchOrders"

        Вес запроса:
        5

        Параметры:
        - data_list="batchOrders" (list[list[str, ...], ...]): список изменяемых ордеров в строковом формате
        ("[{"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "price": "0.3896",
            "orderId": "159756485", "origClientOrderId": "12854"},
           {"symbol": "ADAUSDT", "side": "BUY", "quantity": "14.0", "price": "0.3896",
            "orderId": "45698521", "origClientOrderId": "75854"}, ...]")
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - порядок записи данных в data_list: ["symbol", "side", "quantity", "price", "orderId", "origClientOrderId"]
        - возможные варианты записи data_list:  [[<"ADAUSDT">, <"BUY", "SELL">,
                                                  <"14.0">, <"0.3896">, <"15651651">, <"45874">], ...]
        - Один заказ может быть изменен не более 10000 раз

        Ответ:
        [
           {
              "orderId": 32717797178,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "74707",
              "price": "0.31000",
              "avgPrice": "0.00000",
              "origQty": "68",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "LIMIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,
              "origType": "LIMIT",
              "updateTime": 1686134330079
           },
           {
              "orderId": 32717797177,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "14019",
              "price": "0.30500",
              "avgPrice": "0.00000",
              "origQty": "136",
              "executedQty": "0",
              "cumQty": "0",
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "LIMIT",
              "reduceOnly": false,
              "closePosition": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0",
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,
              "origType": "LIMIT",
              "updateTime": 1686134330079
           }
        ]

        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/batchOrders"

        list_batch_orders = list()

        key_list = ["symbol", "side", "quantity", "price", "orderId", "origClientOrderId"]

        for count, values_list in enumerate(data_list):
            result_list = dict(zip(key_list, values_list))
            list_batch_orders.append(result_list)

        parameters = {
            "batchOrders": json.dumps(list_batch_orders),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.put(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def delete_multiple_order_id_futures(self,
                                         symbol: str,
                                         time_stamp: str,
                                         order_id_list: list[str] = (),
                                         orig_client_order_id_list: list[str] = (),
                                         recv_window: str = "5000") -> dict:
        """
        Запрос:
        Закрыть несколько ордеров по идентификатору

        Полный url:
        "https://fapi.binance.com/fapi/v1/batchOrders"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - order_id_list="orderIdList" list(str): самозаполняющимся идентификатор для каждой сделки (["567834287", ...])
        - orig_client_order_id_list="origClientOrderIdList" list(str): идентификатор сделки  (["567887", ...])
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Максимально можно передать 10 идентификаторов
        - Закрывает ордера, не открытые позиции!!!
        - Необходимо обязательно отправить либо order_id, либо orig_client_order_id
        - order_id является самозаполняющимся для каждого конкретного символа

        Ответ:
        [
           {
              "clientOrderId": "72017",
              "cumQty": "0",
              "cumQuote": "0",
              "executedQty": "0",
              "orderId": 31425437277,
              "origQty": "14",
              "price": "0",
              "reduceOnly": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "status": "CANCELED",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "symbol": "ADAUSDT",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "updateTime": 1682117738301,
              "avgPrice": "0.00000",
              "workingType": "CONTRACT_PRICE",
              "origType": "TRAILING_STOP_MARKET",
              "activatePrice": "0.30900",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "closePosition": false,   (if Close-All)
              "priceProtect": false   (if conditional order trigger is protected)
           },
           {
              "clientOrderId": "78581",
              "cumQty": "0",
              "cumQuote": "0",
              "executedQty": "0",
              "orderId": 31425437280,
              "origQty": "14",
              "price": "0",
              "reduceOnly": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "status": "CANCELED",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "symbol": "ADAUSDT",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "updateTime": 1682117738301,
              "avgPrice": "0.00000",
              "workingType": "CONTRACT_PRICE",
              "origType": "TRAILING_STOP_MARKET",
              "activatePrice": "0.30800",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "closePosition": false,   (if Close-All)
              "priceProtect": false   (if conditional order trigger is protected)
           },
           {
              "clientOrderId": "39333",
              "cumQty": "0",
              "cumQuote": "0",
              "executedQty": "0",
              "orderId": 31425437278,
              "origQty": "14",
              "price": "0",
              "reduceOnly": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "status": "CANCELED",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "symbol": "ADAUSDT",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "updateTime": 1682117738301,
              "avgPrice": "0.00000",
              "workingType": "CONTRACT_PRICE",
              "origType": "TRAILING_STOP_MARKET",
              "activatePrice": "0.30700",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "closePosition": false,   (if Close-All)
              "priceProtect": false   (if conditional order trigger is protected)
           },
           {
              "clientOrderId": "74115",
              "cumQty": "0",
              "cumQuote": "0",
              "executedQty": "0",
              "orderId": 31425437279,
              "origQty": "14",
              "price": "0",
              "reduceOnly": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "status": "CANCELED",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "symbol": "ADAUSDT",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "updateTime": 1682117738301,
              "avgPrice": "0.00000",
              "workingType": "CONTRACT_PRICE",
              "origType": "TRAILING_STOP_MARKET",
              "activatePrice": "0.30600",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "closePosition": false,   (if Close-All)
              "priceProtect": false   (if conditional order trigger is protected)
           },
           {
              "clientOrderId": "95436",
              "cumQty": "0",
              "cumQuote": "0",
              "executedQty": "0",
              "orderId": 31425437276,
              "origQty": "14",
              "price": "0",
              "reduceOnly": false,
              "side": "BUY",
              "positionSide": "BOTH",
              "status": "CANCELED",
              "stopPrice": "0",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "symbol": "ADAUSDT",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "updateTime": 1682117738301,
              "avgPrice": "0.00000",
              "workingType": "CONTRACT_PRICE",
              "origType": "TRAILING_STOP_MARKET",
              "activatePrice": "0.30500",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "closePosition": false,   (if Close-All)
              "priceProtect": false   (if conditional order trigger is protected)
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/batchOrders"
        parameters = {
            "symbol": symbol.upper(),
            "orderIdList": json.dumps(order_id_list).replace(" ", ""),
            "origClientOrderIdList": json.dumps(orig_client_order_id_list).replace(" ", ""),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.delete(url=complete_request, params=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def delete_multiple_order_symbol_futures(self,
                                             symbol: str,
                                             time_stamp: str,
                                             recv_window: str = "5000") -> dict:
        """
        Запрос:
        Закрыть несколько ордеров по символу

        Полный url:
        "https://fapi.binance.com/fapi/v1/allOpenOrders"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Закрывает ордера, не открытые позиции!!!


        Ответ:
        {
           "code": 200,
           "msg": "The operation of cancel all open order is done."
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/allOpenOrders"
        parameters = {
            "symbol": symbol.upper(),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.delete(url=complete_request, params=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def delete_multiple_orders_time_futures(self,
                                            symbol: str,
                                            countdown_time: str,
                                            time_stamp: str,
                                            recv_window: str = "5000") -> dict:
        """
        Запрос:
        Закрыть все ордера по символу через заданное время

        Полный url:
        "https://fapi.binance.com/fapi/v1/countdownCancelAll"

        Вес запроса:
        0

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - countdown_time="countdownTime" (str): количество миллисекунд до закрытия ордеров ("54000", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - countdown_time задается в миллисекундах
        - Закрывает ордера, не открытые позиции!!!

        Ответ:
        {
           "symbol": "ADAUSDT",
           "countdownTime": "20000"
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/countdownCancelAll"
        parameters = {
            "symbol": symbol.upper(),
            "countdownTime": countdown_time,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

        complete_request = self.base_url + end_point
        complete_parameters = parameters
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url=complete_request, data=complete_parameters, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def get_current_position_symbol_futures(self,
                                            symbol: str,
                                            time_stamp: str,
                                            recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить информацию о текущей позиции по символу

        Полный url:
        "https://fapi.binance.com/fapi/v2/positionRisk"

        Вес запроса:
        5

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Пожалуйста, используйте с потоком пользовательских данных ACCOUNT_UPDATE,
          чтобы получать данные своевременно и точно.

        Ответ:
        - Для режима односторонней-позиции:

        [
           {
              "symbol": "ADAUSDT",
              "positionAmt": "-14",
              "entryPrice": "0.3842",
              "markPrice": "0.38440335",
              "unRealizedProfit": "-0.00284690",
              "liquidationPrice": "0.57337452",
              "leverage": "2",
              "maxNotionalValue": "30000000",
              "marginType": "isolated",
              "isolatedMargin": "2.68573256",
              "isAutoAddMargin": "false",
              "positionSide": "BOTH",
              "notional": "-5.38164690",
              "isolatedWallet": "2.68857946",
              "updateTime": 1682279427514
           }
        ]

        - Для режима хедж-позиции:

        [
           {
              "symbol": "ADAUSDT",
              "positionAmt": "0",
              "entryPrice": "0.0",
              "markPrice": "0.38270000",
              "unRealizedProfit": "0.00000000",
              "liquidationPrice": "0",
              "leverage": "2",
              "maxNotionalValue": "30000000",
              "marginType": "isolated",
              "isolatedMargin": "0.00000000",
              "isAutoAddMargin": "false",
              "positionSide": "LONG",
              "notional": "0",
              "isolatedWallet": "0",
              "updateTime": 0
           },
           {
              "symbol": "ADAUSDT",
              "positionAmt": "-14",
              "entryPrice": "0.3823",
              "markPrice": "0.38270000",
              "unRealizedProfit": "-0.00560000",
              "liquidationPrice": "0.57054436",
              "leverage": "2",
              "maxNotionalValue": "30000000",
              "marginType": "isolated",
              "isolatedMargin": "2.66975912",
              "isAutoAddMargin": "false",
              "positionSide": "SHORT",
              "notional": "-5.35780000",
              "isolatedWallet": "2.67535912",
              "updateTime": 1682280093556
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v2/positionRisk"
        parameters = {
            "symbol": symbol.upper(),
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_open_order_id_futures(self,
                                  symbol: str,
                                  time_stamp: str,
                                  order_id: str = "",
                                  orig_client_order_id: str = "",
                                  recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить информацию об открытом ордере по идентификатору

        Полный url:
        "https://fapi.binance.com/fapi/v1/openOrder"

        Вес запроса:
        1

        Параметры:
        - "symbol"=symbol (str): актив ("BTCUSDT", ...)
        - "timestamp"=time_stamp (str): время отправки запроса ("1681501516492", ...)
        - "orderId"=order_id (str): самозаполняющимся идентификатор для каждой сделки ("567834287", ...)
        - "origClientOrderId"=orig_client_order_id (str): идентификатор сделки  ("567887", ...)
        - "recvWindow"=recv_window (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Необходимо обязательно отправить либо order_id, либо orig_client_order_id
        - order_id является самозаполняющимся для каждого конкретного символа
        - Если запрошенный заказ был выполнен или отменен, будет возвращено сообщение об ошибке «Order does not exist»
        - Эти заказы не будут найдены:
            - статус заказа CANCELED
            - статус заказа CANCELED EXPIRED
            - ордер не имеет заполненной сделки
            - прошло больше 3-х дней с момента исполнения ордера

        Ответ:
        {
           "orderId": 31449177351,
           "symbol": "ADAUSDT",
           "status": "NEW",
           "clientOrderId": "51475",
           "price": "0",
           "avgPrice": "0",
           "origQty": "14",
           "executedQty": "0",
           "activatePrice": "0.30970",   (в ответе только если ордер TRAILING_STOP_MARKET)
           "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "TRAILING_STOP_MARKET",
           "reduceOnly": false,
           "closePosition": false,   (if Close-All)
           "side": "BUY",
           "positionSide": "BOTH",
           "stopPrice": "0.39915",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "TRAILING_STOP_MARKET",
           "time": 1682190400946,   (время создания ордера)
           "updateTime": 1682190400946   (последние время взаимодействия с ордером)
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/openOrder"
        parameters = {
            "symbol": symbol.upper(),
            "orderId": order_id,
            "origClientOrderId": orig_client_order_id,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_open_orders_all_futures(self,
                                    time_stamp: str,
                                    symbol: str = "",
                                    recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить информацию о всех открытых ордерах

        Полный url:
        "https://fapi.binance.com/fapi/v1/openOrders"

        Вес запроса:
        1 с указанным символом, 40 без указанного символа

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492". ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Если запрошенный заказ был выполнен или отменен, будет возвращено сообщение об ошибке «Order does not exist»
        - Эти заказы не будут найдены:
            - статус заказа CANCELED
            - статус заказа CANCELED EXPIRED
            - ордер не имеет заполненной сделки
            - прошло больше 3-х дней с момента исполнения ордера

        Ответ:
        [
           {
              "orderId": 31449177351,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "51475",
              "price": "0",
              "avgPrice": "0",
              "origQty": "14",
              "executedQty": "0",
              "activatePrice": "0.30970",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,   (if Close-All)
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.39915",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TRAILING_STOP_MARKET",
              "time": 1682190400946,   (время создания ордера)
              "updateTime": 1682190400946   (последние время взаимодействия с ордером)
           },
           {
              "orderId": 31449046574,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "1113",
              "price": "0",
              "avgPrice": "0",
              "origQty": "14",
              "executedQty": "0",
              "activatePrice": "0.30970",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,   (if Close-All)
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.39945",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TRAILING_STOP_MARKET",
              "time": 1682190044181,   (время создания ордера)
              "updateTime": 1682190044181   (последние время взаимодействия с ордером)
           }
        ]
        """

        end_point = "/fapi/v1/openOrders"
        parameters = {
            "timestamp": time_stamp,
            "symbol": symbol.upper(),
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_orders_all_futures(self,
                               symbol: str,
                               time_stamp: str,
                               order_id: str = "",
                               start_time: str = "",
                               end_time: str = "",
                               limit: str = "500",
                               recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить информацию о всех ордерах аккаунта

        Полный url:
        "https://fapi.binance.com/fapi/v1/allOrders"

        Вес запроса:
        5

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - order_id="orderId" (str): самозаполняющимся идентификатор для каждой сделки ("567834287", ...)
        - start_time="startTime" (str): время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - limit="limit" (str): какое количество ордеров вывести ("5", ..., "1000")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - order_id является самозаполняющимся для каждого конкретного символа
        - Если установлен "orderId", он выведет ордера позже этого "orderId" включительно.
          В противном случае будут возвращены самые последние заказы.
        - Период между "startTime" и  "endTime" должен быть меньше 7 дней (по умолчанию последние 7 дней).

        Ответ:
        [
           {
              "orderId": 31449046574,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "1113",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "activatePrice": "0.30970",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,   (if Close-All)
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.39945",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TRAILING_STOP_MARKET",
              "time": 1682190044181,   (время создания ордера)
              "updateTime": 1682190044181   (последние время взаимодействия с ордером)
           },
           {
              "orderId": 31449177351,
              "symbol": "ADAUSDT",
              "status": "NEW",
              "clientOrderId": "51475",
              "price": "0",
              "avgPrice": "0.00000",
              "origQty": "14",
              "executedQty": "0",
              "activatePrice": "0.30970",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
              "cumQuote": "0",
              "timeInForce": "GTC",
              "type": "TRAILING_STOP_MARKET",
              "reduceOnly": false,
              "closePosition": false,   (if Close-All)
              "side": "BUY",
              "positionSide": "BOTH",
              "stopPrice": "0.39915",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
              "workingType": "CONTRACT_PRICE",
              "priceProtect": false,   (if conditional order trigger is protected)
              "origType": "TRAILING_STOP_MARKET",
              "time": 1682190400946,   (время создания ордера)
              "updateTime": 1682190400946   (последние время взаимодействия с ордером)
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/allOrders"
        parameters = {
            "symbol": symbol.upper(),
            "orderId": order_id,
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_order_id_futures(self,
                             symbol: str,
                             time_stamp: str,
                             order_id: str = "",
                             orig_client_order_id: str = "",
                             recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить информацию об ордере

        Полный url:
        "https://fapi.binance.com/fapi/v1/order"

        Вес запроса:
        1

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - order_id="orderId" (str): самозаполняющимся идентификатор для каждой сделки ("567834287", ...)
        - orig_client_order_id="origClientOrderId" (str): идентификатор сделки  ("567887", ...)
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - Необходимо обязательно отправить либо order_id, либо orig_client_order_id
        - order_id является самозаполняющимся для каждого конкретного символа

        Ответ:
        {
           "orderId": 31424895264,
           "symbol": "ADAUSDT",
           "status": "NEW",
           "clientOrderId": "92067",
           "price": "0",
           "avgPrice": "0.00000",
           "origQty": "14",
           "executedQty": "0",
           "activatePrice": "0.30970",   (в ответе только если ордер TRAILING_STOP_MARKET)
           "priceRate": "1.0",   (в ответе только если ордер TRAILING_STOP_MARKET)
           "cumQuote": "0",
           "timeInForce": "GTC",
           "type": "TRAILING_STOP_MARKET",
           "reduceOnly": false,
           "closePosition": false,   (if Close-All)
           "side": "BUY",
           "positionSide": "BOTH",
           "stopPrice": "0.38450",   (пожалуйста, игнорируйте, если тип ордера TRAILING_STOP_MARKET)
           "workingType": "CONTRACT_PRICE",
           "priceProtect": false,   (if conditional order trigger is protected)
           "origType": "TRAILING_STOP_MARKET",
           "time": 1682115684694,   (время создания ордера)
           "updateTime": 1682115684694   (последние время взаимодействия с ордером)
        }
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/order"
        parameters = {
            "symbol": symbol.upper(),
            "orderId": order_id,
            "origClientOrderId": orig_client_order_id,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    def get_trades_futures(self,
                           symbol: str,
                           time_stamp: str,
                           order_id: str = "",
                           start_time: str = "",
                           end_time: str = "",
                           from_id: str = "",
                           limit: str = "500",
                           recv_window: str = "5000") -> dict:
        """
        Запрос:
        Получить информацию о сделках

        Полный url:
        "https://fapi.binance.com/fapi/v1/userTrades"

        Вес запроса:
        5

        Параметры:
        - symbol="symbol" (str): актив ("BTCUSDT", ...)
        - time_stamp="timestamp" (str): время отправки запроса ("1681501516492", ...)
        - order_id="orderId" (str): самозаполняющимся идентификатор для каждой сделки ("567834287", ...)
        - start_time="startTime" (str): время начала отбора ("1681505080619", ...)
        - end_time="endTime" (str): время окончания отбора ("1681505034619", ...)
        - from_id="fromId" (str): ... ("567834287", ...)
        - limit="limit" (str): какое количество ордеров вывести ("5", ..., "1000")
        - recv_window="recvWindow" (str): количество миллисекунд, в течение которых запрос действителен
                                                                                                ("1000", ..., "70000")

        Комментарии:
        - "orderId" является самозаполняющимся для каждого конкретного символа
        - "fromId" является "id" в ответе.
        - Если использовать "fromId" то будут выводиться сделки от "fromId" включительно
        - Если "startTime" и "endTime" не отправлены, будут возвращены данные за последние 7 дней.
        - Период между "startTime" и  "endTime" должен быть меньше 7 дней (по умолчанию последние 7 дней).
        - Параметр "fromId" нельзя отправлять с "startTime" или "endTime".

        Ответ:
        [
           {
              "symbol": "ADAUSDT",
              "id": 910559362,
              "orderId": 31479414461,
              "side": "SELL",
              "price": "0.38400",
              "qty": "14",
              "realizedPnl": "0",
              "marginAsset": "USDT",
              "quoteQty": "5.37600",
              "commission": "0.00215039",
              "commissionAsset": "USDT",
              "time": 1682283094999,
              "positionSide": "BOTH",
              "buyer": false,
              "maker": false
           },
           {
              "symbol": "ADAUSDT",
              "id": 910565858,
              "orderId": 31480052851,
              "side": "SELL",
              "price": "0.38390",
              "qty": "14",
              "realizedPnl": "0",
              "marginAsset": "USDT",
              "quoteQty": "5.37460",
              "commission": "0.00214984",
              "commissionAsset": "USDT",
              "time": 1682285029579,
              "positionSide": "BOTH",
              "buyer": false,
              "maker": false
           }
        ]
        """

        # -------------------------------------------------------------------------
        end_point = "/fapi/v1/userTrades"
        parameters = {
            "symbol": symbol.upper(),
            "orderId": order_id,
            "startTime": start_time,
            "endTime": end_time,
            "fromId": from_id,
            "limit": limit,
            "timestamp": time_stamp,
            "recvWindow": recv_window
        }
        query_string = urlencode(parameters)
        parameters["signature"] = hmac.new(key=self.secret_key.encode(),
                                           msg=query_string.encode(),
                                           digestmod=hashlib.sha256).hexdigest()
        # -------------------------------------------------------------------------

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

    async def get_stream_best_price_quantity_all_futures(self,
                                                         list_data: list,
                                                         method: str = "SUBSCRIBE",
                                                         my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим лучшей цены и количества всех символов

        Полный url:
        "wss://fstream.binance.com/ws!bookTicker"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e":"bookTicker",   (тип события)
            "u":400900217,   (идентификатор обновления книги заказов)
            "s":"BNBUSDT",   (символ)
            "b":"25.35190000",   (лучшая цена bid)
            "B":"31.21000000",   (лучшая ставка bid)
            "a":"25.36520000",   (лучшая цена ask)
            "A":"40.66000000"   (лучшая ставка ask)
            "T": 1568014460891,   (время транзакции)
            "E": 1568014460893,   (время события)
        }
        """

        # ----------------------------------------------
        streams = ["!bookTicker"]
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
                            print("Стрим лучшей цены и количества всех символов запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим лучшей цены и количества всех символов разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим лучшей цены и количества всех символов разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_best_price_quantity_symbol_futures(self,
                                                            list_data: list,
                                                            symbol: list[list[str]],
                                                            method: str = "SUBSCRIBE",
                                                            my_id: int = randint(1, 100)) -> None:

        """
        Запрос:
        Стрим лучшей цены и количества по символу


        Полный url:
        "wss://fstream.binance.com/ws{symbol}@bookTicker"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e":"bookTicker",   (тип события)
            "u":400900217,   (идентификатор обновления книги заказов)
            "s":"BNBUSDT",   (символ)
            "b":"25.35190000",   (лучшая цена bid)
            "B":"31.21000000",   (лучшая ставка bid)
            "a":"25.36520000",   (лучшая цена ask)
            "A":"40.66000000"   (лучшая ставка ask)
            "T": 1568014460891,   (время транзакции)
            "E": 1568014460893,   (время события)
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
                            print("Стрим лучшей цены и количества по символу запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим лучшей цены и количества по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим лучшей цены и количества по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_candles_futures(self,
                                         list_data: list,
                                         symbol_interval: list[list[str, str], ...],
                                         method: str = "SUBSCRIBE",
                                         my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим свечей

        Полный url:
        "wss://fstream.binance.com/ws{symbol}@kline_{interval}"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol_interval (list[list[str, str], ...]): список данных по стриму -
                                                        символ_интервал ([["btcusdt", "1m"], ["bnbusdt", "5m"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - symbol_interval вариант заполнения: [["btcusdt" или "bnbusdt" ..., "1m", "3m", "5m", "15m", "30m", "1h", "2h",
                                                                    "4h", "6h", 8h, "12h", "1d", "3d", "1w", "1M"], ...]
        - symbol_interval значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e":"continuous_kline",   (тип события)
            "E":1607443058651,   (время события)
            "ps":"BTCUSDT",   (пара)
            "ct":"PERPETUAL"   (тип контракта)
            "k":{
                    "t":1607443020000,   (время начала свечи)
                    "T":1607443079999,   (время завершения свечи)
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
                            print("Стрим свечей запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим свечей разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим свечей разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_candles_contract_futures(self,
                                                  list_data: list,
                                                  symbol_contract_interval: list[list[str, str, str], ...],
                                                  method: str = "SUBSCRIBE",
                                                  my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим свечей по контракту

        Полный url:
        "wss://fstream.binance.com/ws{symbol}_{contract}@continuousKline_{interval}"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol_contract_interval (list[list[str, str, str], ...]): список данных по стриму -
                символ_контракт_интервал ([["btcusdt", "perpetual", "1m"], ["bnbusdt", "current_quarter", "5m"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - symbol_contract_interval вариант заполнения: [["btcusdt" или "bnbusdt" ...,
                                            "perpetual" или "current_quarter" или "next_quarter",
                        "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", 8h, "12h", "1d", "3d", "1w", "1M"], ...]
        - symbol_contract_interval значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e":"continuous_kline",   (тип события)
            "E":1607443058651,   (время события)
            "ps":"BTCUSDT",   (пара)
            "ct":"PERPETUAL"   (тип контракта)
            "k":{
                    "t":1607443020000,   (время начала свечи)
                    "T":1607443079999,   (время завершения свечи)
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
        streams = [f"{data[0].lower()}_{data[1]}@continuousKline_{data[2]}" for data in symbol_contract_interval]
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
                            print("Стрим свечей по контракту запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим свечей по контракту разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим свечей по контракту разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_composite_index_futures(self,
                                                 list_data: list,
                                                 composite_index: list[list[str], ...],
                                                 method: str = "SUBSCRIBE",
                                                 my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим стакана ордеров составного индекса

        Полный url:
        "wss://fstream.binance.com/ws{composite_index}@compositeIndex"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - composite_index (list[list[str], ...]): список составных индексов ([["defiusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - composite_index значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e":"compositeIndex",   (тип события)
            "E":1602310596000,   (время события)
            "s":"DEFIUSDT",   (символ)
            "p":"554.41604065",   (цена)
            "C":"baseAsset",
            "c":[   (состав)
                {
                    "b":"BAL",   (базовый актив)
                    "q":"USDT",   (актив котировки)
                    "w":"1.04884844",   (вес в количестве)
                    "W":"0.01457800",   (вес в процентах)
                    "i":"24.33521021"   (цена индекса)
                },
                {
                    "b":"BAND",
                    "q":"USDT" ,
                    "w":"3.53782729",
                    "W":"0.03935200",
                    "i":"7.26420084"
                }
            ]
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@compositeIndex" for data in composite_index]
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
                            print("Стрим стакана ордеров составного индекса запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим стакана ордеров составного индекса разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим стакана ордеров составного индекса разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_contract_info_futures(self,
                                               list_data: list,
                                               method: str = "SUBSCRIBE",
                                               my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        ...

        Полный url:
        "wss://fstream.binance.com/ws!contractInfo"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e":"contractInfo",   (тип события)
            "E":1669356423908,   (время события)
            "s":"IOTAUSDT",   (символ)
            "ps":"IOTAUSDT",   (пара)
            "ct":"PERPETUAL",   (тип контракта)
            "dt":4133404800000,   (дата и время доставки)
            "ot":1569398400000,   (onboard date time)
            "cs":"TRADING",   (статус контракта)
            "bks":[
                {
                    "bs":1,   (Notional bracket)
                    "bnf":0,   (Floor notional of this bracket)
                    "bnc":5000,   (Cap notional of this bracket)
                    "mmr":0.01,   (Maintenance ratio for this bracket)
                    "cf":0,   (Auxiliary number for quick calculation)
                    "mi":21,   (минимальное кредитное плечо для этой группы)
                    "ma":50   (максимальное кредитное плечо для этой группы)
                },
                {
                    "bs":2,
                    "bnf":5000,
                    "bnc":25000,
                    "mmr":0.025,
                    "cf":75,
                    "mi":11,
                    "ma":20
                }
            ]
        }
        """

        # ----------------------------------------------
        streams = ["!contractInfo"]
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
                            print("... запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("... разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("... разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_info_day_all_futures(self,
                                              list_data: list,
                                              method: str = "SUBSCRIBE",
                                              my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по информации о всех символах за 24 часа

        Полный url:
        "wss://fstream.binance.com/ws!ticker@arr"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
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
              "c": "0.0025",  (последняя цена)
              "Q": "10",   (последнее количество)
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
                            print("Стрим по информации о всех символах за 24 часа запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим по информации о всех символах за 24 часа разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим по информации о всех символах за 24 часа разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_info_day_symbol_futures(self,
                                                 list_data: list,
                                                 symbol: list[list[str], ...],
                                                 method: str = "SUBSCRIBE",
                                                 my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по информации об определенном символе за 24 часа

        Полный url:
        "wss://fstream.binance.com/ws{symbol}@ticker"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
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
            "c": "0.0025",  (последняя цена)
            "Q": "10",   (последнее количество)
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
                            print("Стрим по информации об определенном символе за 24 часа запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим по информации об определенном символе за 24 часа разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим по информации об определенном символе за 24 часа разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_liquidated_orders_all_futures(self,
                                                       list_data: list,
                                                       method: str = "SUBSCRIBE",
                                                       my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим ликвидированных ордеров по всем символам

        Полный url:
        "wss://fstream.binance.com/ws!forceOrder@arr"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e":"forceOrder",   (тип события)
            "E":1568014460893,   (время события)
            "o":{
                "s":"BTCUSDT",   (символ)
                "S":"SELL",   (сторона)
                "o":"LIMIT",   (тип ордера)
                "f":"IOC",   (Time in Force)
                "q":"0.014",   (количество)
                "p":"9910",   (цена)
                "ap":"9910",   (средняя цена)
                "X":"FILLED",   (статус ордера)
                "l":"0.014",   (Order Last Filled Quantity)
                "z":"0.014",   (Order Filled Accumulated Quantity)
                "T":1568014460893,   (время исполнения ордера)
            }
        }
        """

        # ----------------------------------------------
        streams = ["!forceOrder@arr"]
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
                            print("Стрим ликвидированных ордеров по всем символам запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим ликвидированных ордеров по всем символам разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим ликвидированных ордеров по всем символам разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_liquidated_orders_symbol_futures(self,
                                                          list_data: list,
                                                          symbol: list[list[str], ...],
                                                          method: str = "SUBSCRIBE",
                                                          my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим ликвидированных ордеров по символу

        Полный url:
        "wss://fstream.binance.com/ws{symbol}@forceOrder"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e":"forceOrder",   (тип события)
            "E":1568014460893,   (время события)
            "o":{
                "s":"BTCUSDT",   (символ)
                "S":"SELL",   (сторона)
                "o":"LIMIT",   (тип ордера)
                "f":"IOC",   (Time in Force)
                "q":"0.014",   (количество)
                "p":"9910",   (цена)
                "ap":"9910",   (средняя цена)
                "X":"FILLED",   (статус ордера)
                "l":"0.014",   (Order Last Filled Quantity)
                "z":"0.014",   (Order Filled Accumulated Quantity)
                "T":1568014460893,   (время исполнения ордера)
            }
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@forceOrder" for data in symbol]
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
                            print("Стрим ликвидированных ордеров по символу запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим ликвидированных ордеров по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим ликвидированных ордеров по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_mark_price_funding_rate_all_futures(self,
                                                             list_data: list,
                                                             speed: str = "",
                                                             method: str = "SUBSCRIBE",
                                                             my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим цены маркировки (mark price) и ставки финансирования всех символов

        Полный url:
        "wss://fstream.binance.com/ws!markPrice@arr{speed}"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - speed (str): скорость стрима ("", "@1s"),
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - speed возможные варианты ["" - 3сек., "@1s" - 1сек.]
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        [
            {
                "e": "markPriceUpdate",   (тип события)
                "E": 1562305380000,   (время события)
                "s": "BTCUSDT",   (символ)
                "p": "11794.15000000",   (цена маркировки)
                "i": "11784.62659091",   (цена индекса)
                "P": "11784.25641265",   (предполагаемая цена, полезна только в последний час перед началом расчета)
                "r": "0.00038167",   (ставка финансирования)
                "T": 1562306400000   (время следующего финансирования)
            }
        ]
        """

        # ----------------------------------------------
        streams = [f"!markPrice@arr{speed}"]
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
                            print("Стрим цены маркировки (mark price) и ставки финансирования всех символов запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим цены маркировки (mark price) и ставки финансирования всех символов разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим цены маркировки (mark price) и ставки финансирования всех символов разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_mark_price_funding_rate_symbol_futures(self,
                                                                list_data: list,
                                                                symbol: list[list[str], ...],
                                                                speed: str = "",
                                                                method: str = "SUBSCRIBE",
                                                                my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим цены маркировки (mark price) и ставки финансирования по символу

        Полный url:
        "wss://fstream.binance.com/ws{symbol}@markPrice{speed}"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - speed (str): скорость стрима ("", "@1s"),
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - speed возможные варианты ["" - 3сек., "@1s" - 1сек.]
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e": "markPriceUpdate",   (тип события)
            "E": 1562305380000,   (время события)
            "s": "BTCUSDT",   (символ)
            "p": "11794.15000000",   (цена маркировки)
            "i": "11784.62659091",   (цена индекса)
            "P": "11784.25641265",   (предполагаемая цена, полезна только в последний час перед началом расчета)
            "r": "0.00038167",   (ставка финансирования)
            "T": 1562306400000   (время следующего финансирования)
        }
        """

        # ----------------------------------------------
        streams = [f"{data[0].lower()}@markPrice{speed}" for data in symbol]
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
                            print("Стрим цены маркировки (mark price) и ставки финансирования по символу запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим цены маркировки (mark price) и ставки финансирования по символу разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим цены маркировки (mark price) и ставки финансирования по символу разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_min_info_day_all_futures(self,
                                                  list_data: list,
                                                  method: str = "SUBSCRIBE",
                                                  my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по минимальной информации о всех символах за 24 часа

        Полный url:
        "wss://fstream.binance.com/ws!miniTicker@arr"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
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
                            print("Стрим по минимальной информации за 24 часа всех символов запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим по минимальной информации за 24 часа всех символов разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим по минимальной информации за 24 часа всех символов разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_min_info_day_symbol_futures(self,
                                                     list_data: list,
                                                     symbol: list[list[str], ...],
                                                     method: str = "SUBSCRIBE",
                                                     my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим по минимальной информации об определенном символе за 24 часа

        Полный url:
        "wss://fstream.binance.com/ws{symbol}@miniTicker"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
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
                            print(list_data)
                        else:
                            print("Стрим по минимальной информации об определенном символе за 24 часа запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print(
                    "Стрим по минимальной информации об определенном символе за 24 часа разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print(
                    "Стрим по минимальной информации об определенном символе за 24 часа разрыв соединения. "
                    "Восстанавливаем.\n"
                    "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_order_book_futures(self,
                                            list_data: list,
                                            symbol_quantity_speed: list[list[str, str, str]],
                                            method: str = "SUBSCRIBE",
                                            my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим стакана ордеров

        Полный url:
        "wss://fstream.binance.com/ws{symbol}@depth{quantity}@{speed}ms"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol_quantity_speed (list[list[str, str, str], ...]): список данных по стриму -
                       актив_глубина стакана_скорость стрима ([["btcusdt", "10", "100"], ["bnbusdt", "5", "250"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - symbol_quantity_speed вариант заполнения: [["btcusdt" или "bnbusdt" и т.д.,
                                                      "5" или "10" или "20",
                                                      "100" или "250" или "500"], ...]
        - symbol_quantity_speed значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e": "depthUpdate",   (тип события)
            "E": 1571889248277,   (время события)
            "T": 1571889248276,   (время запроса)
            "s": "BTCUSDT",   (символ)
            "U": 390497796,   (Идентификатор первого обновления в событии)
            "u": 390497878,   (Окончательный идентификатор обновления в событии)
            "pu": 390497794,   (Final update Id in last stream(ie `u` in last stream))
            "b": [   (bids)
                    [
                        "7403.89",   (цена)
                        "0.002"   (количество)
                    ],
                    [
                        "7403.90",
                        "3.906"
                    ],
                    [
                        "7404.00",
                        "1.428"
                    ],
                    [
                        "7404.85",
                        "5.239"
                    ],
                    [
                        "7405.43",
                        "2.562"
                    ]
                ],
            "a": [   (asks)
                    [
                        "7405.96",   (цена)
                        "3.340"   (количество)
                    ],
                    [
                        "7406.63",
                        "4.525"
                    ],
                    [
                        "7407.08",
                        "2.475"
                    ],
                    [
                        "7407.15",
                        "4.800"
                    ],
                    [
                        "7407.20",
                        "0.175"
                    ]
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
                            print("Стрим стакана ордеров запушен")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим стакана ордеров разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим стакана ордеров разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_order_book_difference_futures(self,
                                                       list_data: list,
                                                       symbol_speed: list[list[str, str]],
                                                       method: str = "SUBSCRIBE",
                                                       my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        ...

        Полный url:
        "wss://fstream.binance.com/ws{symbol}@depth@{speed}ms"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol_speed (list[list[str, str], ...]): список данных по стриму -
                                                актив_скорость стрима ([["btcusdt", "100"], ["bnbusdt", "250"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - symbol_speed вариант заполнения: [["btcusdt" или "bnbusdt" ...,  "100" или "250" или "500"], ...]
        - symbol_speed значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        {
            "e": "depthUpdate",   (тип события)
            "E": 1571889248277,   (время события)
            "T": 1571889248276,   (время запроса)
            "s": "BTCUSDT",   (символ)
            "U": 390497796,   (Идентификатор первого обновления в событии)
            "u": 390497878,   (Окончательный идентификатор обновления в событии)
            "pu": 390497794,   (Final update Id in last stream(ie `u` in last stream))
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
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            list_data.clear()
                            list_data.append(result)
                        else:
                            print("... запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("... разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("... разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_trades_tape_futures(self,
                                             list_data: list,
                                             symbol: list[list[str]],
                                             method: str = "SUBSCRIBE",
                                             my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим ленты сделок по символу

        Полный url:
        "wss://fstream.binance.com/ws{symbol}@aggTrade"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
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
                            print("Стрим ленты сделок по символу запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим ленты сделок по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим ленты сделок по символу разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    async def get_stream_asset_index_in_multi_assets(self,
                                                     list_data: list,
                                                     method: str = "SUBSCRIBE",
                                                     symbol: list[list[str]] = None,
                                                     my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим индексов активов в режиме мультиактива

        Полный url:
        "wss://fstream.binance.com/ws!assetIndex@arrOR" (для всех активов)
        или
        "wss://fstream.binance.com/ws{assetSymbol}@assetIndex" (для определенных активов)

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - symbol (list[list[str], ...]): список символов ([["btcusdt"], ["bnbusdt"], ...])
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - symbol вариант заполнения: [["btcusdt"], ...]
        - symbol значения должны быть строчными
        - method расшифровка ["SUBSCRIBE": подключить стрим, "UNSUBSCRIBE": отключить стрим,
                              "LIST_SUBSCRIPTIONS": информация о стриме, "SET_PROPERTY": ..., "GET_PROPERTY": ...]

        Ответ:
        [
            {
                "e":"assetIndexUpdate",
                "E":1686749230000,
                "s":"ADAUSD",    (asset index symbol)
                "i":"0.27462452",    (index price)
                "b":"0.10000000",    (bid buffer)
                "a":"0.10000000",    (ask buffer)
                "B":"0.24716207",    (bid rate)
                "A":"0.30208698",    (ask rate)
                "q":"0.05000000",    (auto exchange bid buffer)
                "g":"0.05000000",    (auto exchange ask buffer)
                "Q":"0.26089330",    (auto exchange bid rate)
                "G":"0.28835575"     (auto exchange ask rate)
            },
            {
                "e":"assetIndexUpdate",
                "E":1686749230000,
                "s":"USDTUSD",
                "i":"0.99987691",
                "b":"0.00010000",
                "a":"0.00010000",
                "B":"0.99977692",
                "A":"0.99997689",
                "q":"0.00010000",
                "g":"0.00010000",
                "Q":"0.99977692",
                "G":"0.99997689"
            }
        ]
        """

        # ----------------------------------------------
        if symbol:
            streams = [f"{data[0].lower()}@assetIndex" for data in symbol]
        else:
            streams = [f"!assetIndex@arrOR"]
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
                            print("Стрим индексов активов в режиме мультиактива запущен.")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим индексов активов в режиме мультиактива разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим индексов активов в режиме мультиактива разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    def start_user_data_stream_futures(self) -> dict:
        """
        Запрос:
        Запустить стрим по данным пользователя

        Полный url:
        "https://fapi.binance.com/fapi/v1/listenKey"

        Вес запроса:
        1

        Параметры:
        None

        Комментарии:
        None

        Ответ:
        {
           "listenKey": "N6Ogns4WQsQdYZ1JfzvqMIQLbx1Q9RKHMbl9vmEOgm4M0kUDxXdbtSejs0fruDsw"
        }
        """

        # -------------------------------------------
        end_point = "/fapi/v1/listenKey"
        # -------------------------------------------

        complete_request = self.base_url + end_point
        headers = {
            "X-MBX-APIKEY": self.api_key
        }
        response = requests.post(url=complete_request, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    async def connect_user_data_streams_futures(self,
                                                dict_data: dict,
                                                listen_key: str,
                                                method: str = "SUBSCRIBE",
                                                my_id: int = randint(1, 100)) -> None:
        """
        Запрос:
        Стрим для получения данных пользователя

        Полный url:
       "wss://fstream.binance.com/ws{listenKey}"

        Параметры:
        - list_data (list): аргумент через который будут передаваться данные стрима ([])
        - listenKey (str): ... ("LHW0SdJy0FuOISIN5MBDGDV0V2s2WjPSaKdpCLh5yQ31EH97OiNwI6tnhlidndAoe")
        - method (str): метод стрима ("SUBSCRIBE", "UNSUBSCRIBE")
        - my_id (int): идентификатор стрима (1, ..., 100)

        Комментарии:
        - listenKey можно получить по запросу через url "https://fapi.binance.com/fapi/v1/listenKey"

        Ответ:
        {
           "listenKey": "xVAUfwyLHjbiReNjOC1Xy0OU88UPzFke7LEjc2AmYi8GPIApGSdu492wzKkXrhQW"
        }
        """

        while True:
            try:
                async with websockets.connect(self.base_url_stream) as websocket:
                    subscribe_request = {
                        "method": method,
                        "params": [listen_key],
                        "id": my_id,
                    }
                    await websocket.send(json.dumps(subscribe_request))

                    while True:
                        result = json.loads(await websocket.recv())
                        if "id" not in result:
                            dict_data[result["e"].lower()] = result
                        else:
                            print("Стрим для получения данных пользователя запущен")
            except websockets.exceptions.ConnectionClosedError:
                print("Стрим для получения данных пользователя разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: websockets.exceptions.ConnectionClosedError.")
                await asyncio.sleep(10)
            except socket.gaierror:
                print("Стрим для получения данных пользователя разрыв соединения. Восстанавливаем.\n"
                      "Ошибка: socket.gaierror.")
                await asyncio.sleep(10)

    def keepalive_user_data_stream_futures(self) -> dict:

        """
        Запрос:
        Обновить стрим по данным пользователя

        Полный url:
        "https://fapi.binance.com/fapi/v1/listenKey"

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
        end_point = "/fapi/v1/listenKey"
        # -------------------------------------------

        complete_request = self.base_url + end_point
        headers = {
            "X-MBX-APIKEY": self.api_key
        }
        response = requests.put(url=complete_request, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }

    def delete_user_data_stream_futures(self) -> dict:
        """
        Запрос:
        Закрыть стрим по данным пользователя

        Полный url:
        "https://fapi.binance.com/fapi/v1/listenKey"

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
        end_point = "/fapi/v1/listenKey"
        # -------------------------------------------

        complete_request = self.base_url + end_point
        headers = {
            "X-MBX-APIKEY": self.api_key
        }
        response = requests.delete(url=complete_request, headers=headers)
        result = json.loads(response.text)

        return {
            "status_code": response.status_code,
            "result": result,
            "headers": response.headers
        }
