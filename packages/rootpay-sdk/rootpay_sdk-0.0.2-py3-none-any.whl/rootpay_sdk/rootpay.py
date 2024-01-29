import httpx


class Payment:
    def __init__(self, session_id: str, api_key: str):
        """

        :param session_id: инициализация класса под конкретный платеж
        :param api_key: апи ключ рутпэй
        """
        self.session_id = session_id
        self.api_key = api_key
        self.pay_data = {
            'api_token': self.api_key,
            'session_id': self.session_id
        }
        self.payment_url = "https://root-pay.app/api/get_payment_info"
        self.link = "https://root-pay.app/"+session_id

    async def is_paid(self) -> bool:
        """
        :return: возвращает bool в котором False - инвойс не оплачен, True - оплачен
        """
        async with httpx.AsyncClient() as client:
            result = await client.post(self.payment_url, data=self.pay_data)
        if result.status_code != 200:
            raise ConnectError(result.text)
        result = result.json()

        if 'error' in result:
            raise ChechPayExcept(result['error'])

        elif len(result['payments']) == 0:
            raise Exception("Payment not exist")

        if result['payments'][0]['status'] == 'paid':
            return True

        return False

    async def get_amount(self) -> float:
        """

        :return: возвращает сумму текущего инстанса платежа
        """
        async with httpx.AsyncClient() as client:
            result = await client.post(self.payment_url, data=self.pay_data)
        if result.status_code != 200:
            raise ConnectError(result.text)
        result = result.json()

        if 'error' in result:
            raise ChechPayExcept(result['error'])

        elif len(result['payments']) == 0:
            raise Exception("Payment not exist")

        return result['payments'][0]['amount']


class RootPayApi:
    def __init__(self, api_key: str):
        """

        :param api_key: получает апи ключ для инициализации класса
        """
        self.API_KEY = api_key
        self.base_url = "https://root-pay.app/api/"
        self.simple_data = {
            'api_token': self.API_KEY
        }
        self.methods = ['usdt', 'card', 'sbp', 'qiwi']

    async def get_active_methods(self) -> list:
        """

        :return: возвращает активные методы получения платежей
        """
        method_url = self.base_url + "methods_pay"
        answer = []

        async with httpx.AsyncClient() as client:
            result = await client.post(method_url, data=self.simple_data)
        if result.status_code != 200:
            raise ConnectError(result.text)
        result = result.json()

        if 'error' in result:
            raise AuthError(result['error'])

        for i in result["methods"]:
            if i['enable']:
                answer.append(i['name'])
        return answer

    async def balance(self) -> float:
        """
        :return: возвращает баланс кассы
        """
        method_url = self.base_url + "balance"

        async with httpx.AsyncClient() as client:
            result = await client.post(method_url, data=self.simple_data)
        if result.status_code != 200:
            raise ConnectError(result.text)
        result = result.json()

        if 'error' in result:
            raise AuthError(result['error'])

        return result['balance']

    async def get_payments(self, limit: int = 10) -> list:
        """

        :param limit: лимит количества операций для выгрузки (по умолчанию 10)
        :return: возвращает список платежей с указанным лимитом
        """
        method_url = self.base_url + "get_payments"
        temp = self.simple_data
        if limit != 10 and limit > 0:
            temp['limit'] = limit
        async with httpx.AsyncClient() as client:
            result = await client.post(method_url, data=temp)
        if result.status_code != 200:
            raise ConnectError(result.text)
        result = result.json()

        if 'error' in result:
            raise AuthError(result['error'])

        return result['payments']

    '''Почему-то всегда True'''
    async def create_payoff(self, method: str, wallet: str) -> bool:
        """
        :param method: платежная система кошелька вывода: usdt, card, sbp, qiwi
        :param wallet: реквизиты кошелька получения
        :return: возвращает удачный или нет вывод. По непонятным мне обстоятельствам всегда True
        """
        if method.lower() not in self.methods:
            raise MetodError("Invalid method name")
        method_url = self.base_url + "create_payoff"
        temp = self.simple_data
        temp['method'] = method.lower()
        temp['wallet'] = wallet

        async with httpx.AsyncClient() as client:
            result = await client.post(method_url, data=temp)
        if result.status_code != 200:
            raise ConnectError(result.text)
        result = result.json()

        if 'error' in result:
            raise AuthError(result['error'])

        return result['status']

    async def create_pay_link(self,
                              method: str,
                              amount: int,
                              subtitle: str = None,
                              comment: str = None) -> Payment:
        """
        :param method: метод оплаты (можно получить в функции get_active_methods)
        :param amount: целочисленная сумма оплаты
        :param subtitle: описание платежа, видит покупатель. Не обязательный параметр
        :param comment: дополнительная информация, любая полезная вам нагрузка. Например: Telegram userid покупателя. Не обязательный параметр
        :return: возвращает инстанс класса Payment
        """

        method = method.upper()
        temp = self.simple_data
        available = await self.get_active_methods()
        if method not in available:
            raise MetodError("Invalid method name")
        method_url = self.base_url + "create_payment"
        temp['method'] = method
        temp['amount'] = amount
        if subtitle is not None:
            temp['subtitle'] = subtitle
        if comment is not None:
            temp['comment'] = comment

        async with httpx.AsyncClient() as client:
            result = await client.post(method_url, data=temp)
        result = result.json()

        if 'error' in result:
            raise PayCreateErr(result['error'])
        return Payment(result['session_id'], self.API_KEY)


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