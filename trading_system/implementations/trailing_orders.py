from trading_system.api.factory import ApiClientFactory
from trading_system.systems.executor import SystemExecutor
from trading_system.systems.trailing_orders.system import TrailingOrders


class TrailingOrderImpl(object):
    def __init__(self, client_type):
        client = ApiClientFactory().make_client(client_type)
        self.system = TrailingOrders(client)

    def run(self):
        executor = SystemExecutor(self.system, interval=3)
        executor.execute()

if __name__ == '__main__':
    TrailingOrderImpl(ApiClientFactory.BITFINEX).run()
