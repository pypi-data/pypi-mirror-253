import httpx


class Payment:
    def __init__(self, session_id: str, api_key: str):
        """

        :param session_id: инициализация класса под конкретный платеж
        :param api_key: апи ключ рутпэй
        """
        self.__session_id = session_id
        self.__api_key = api_key
        self.__pay_data = {
            'api_token': self.__api_key,
            'session_id': self.__session_id
        }
        self.__payment_url = "https://root-pay.app/api/get_payment_info"
        self.link = "https://root-pay.app/"+session_id
        self.__client = httpx.AsyncClient()

    async def __fetch_payment_info(self):
        """
        Сервисный класс для вэб запросов
        :return: ответ апи
        """
        result = await self.__client.post(self.__payment_url, data=self.__pay_data)
        if result.status_code != 200:
            raise ConnectError(result.text)
        result = result.json()

        if 'error' in result:
            raise ChechPayExcept(result['error'])

        elif len(result['payments']) == 0:
            raise Exception("Payment not exist")

        return result['payments'][0]

    async def is_paid(self) -> bool:
        """
        :return: возвращает bool в котором False - инвойс не оплачен, True - оплачен
        """
        payment_info = await self.__fetch_payment_info()
        return payment_info['status'] == 'paid'

    async def full_info(self) -> dict:
        """
        :return: полную информацию о платеже в формате:         {
            "amount": "1500",
            "created_at": "2023-02-28 19:36",
            "expired_at": "2023-02-28 19:57",
            "method": "CARD",
            "session_id": "puKHMyu4XxF5",
            "status": "paid",
            "total_amount": "1506.12"
        }
        """
        return await self.__fetch_payment_info()

    async def get_amount(self) -> float:
        """
        :return: возвращает сумму текущего инстанса платежа
        """
        payment_info = await self.__fetch_payment_info()
        return payment_info['amount']


class RootPayApi:
    def __init__(self, api_key: str):
        """
        :param api_key: получает апи ключ для инициализации класса
        """
        self.__API_KEY = api_key
        self.__base_url = "https://root-pay.app/api/"
        self.__simple_data = {
            'api_token': self.__API_KEY
        }
        self.__methods = ['USDT', 'CARD', 'SBP', 'QIWI']

    async def __request(self, endpoint: str, data: dict = None) -> dict:

        url = f"{self.__base_url}{endpoint}"
        data = data or self.__simple_data

        async with httpx.AsyncClient() as client:
            result = await client.post(url, data=data)
        if result.status_code != 200:
            raise ConnectError(result.text)
        result = result.json()

        if 'error' in result:
            raise AuthError(result['error'])

        return result

    async def get_active_methods(self) -> list:
        """
        :return: возвращает активные методы получения платежей
        """
        result = await self.__request("methods_pay")
        return [i['name'] for i in result["methods"] if i['enable']]

    async def balance(self) -> float:
        """
        :return: возвращает баланс кассы
        """
        result = await self.__request("balance")
        return result['balance']

    async def get_payments(self, limit: int = 10) -> list:
        """
        :param limit: лимит количества операций для выгрузки (по умолчанию 10)
        :return: возвращает список платежей с указанным лимитом
        """
        data = self.__simple_data.copy()
        if limit > 0 or limit != 10:
            data.update({'limit': limit})
        result = await self.__request("get_payments", data)
        return result['payments']

    '''Почему то всегда True'''
    async def create_payoff(self, method: str, wallet: str) -> bool:
        """
        :param method: платежная система кошелька вывода: usdt, card, sbp, qiwi
        :param wallet: реквизиты кошелька получения
        :return: возвращает удачный или нет вывод. По непонятным мне обстоятельствам всегда True
        """
        if method.upper() not in self.__methods:
            raise MetodError("Invalid method name")
        data = self.__simple_data.copy()
        data.update({'method': method.upper(), 'wallet': wallet})
        result = await self.__request("create_payoff", data)
        return result['status']

    async def create_pay_link(self, method: str,
                              amount: int,
                              subtitle: str = None,
                              comment: str = None) -> Payment:
        """
        :param method: метод оплаты (можно получить в функции get_active_methods)
        :param amount: целочисленная сумма оплаты
        :param subtitle: описание платежа, видит покупатель. Не обязательный параметр
        :param comment: дополнительная информация, любая полезная вам нагрузка. Например: Telegram userid покупателя.
        Не обязательный параметр
        :return: возвращает инстанс класса Payment
        """
        method = method.upper()
        available = await self.get_active_methods()
        if method not in available:
            raise MetodError("Invalid method name")
        data = self.__simple_data.copy()
        data.update({'method': method, 'amount': amount})
        if subtitle is not None:
            data.update({'subtitle': subtitle})
        if comment is not None:
            data.update({'comment': comment})
        result = await self.__request("create_payment", data)
        return Payment(result['session_id'], self.__API_KEY)


class ChechPayExcept(Exception):
    pass


class AuthError(Exception):
    pass


class MetodError(Exception):
    pass


class PayCreateErr(Exception):
    pass


class ConnectError(Exception):
    pass

