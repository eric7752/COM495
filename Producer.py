class Producer:
    def __init__(self, wta, delta):
        self.wta = wta
        self.delta = delta
        self.traded = False
        self.consecutive_trades = 0
        self.prices = []
        self.surplus = []
        self.price_group = 0

    def update_wta(self):
        if not self.traded:
            #self.wta *= (1 - self.delta)
            self.wta -= 10
        #elif self.consecutive_trades >= 3:
            #self.wta += 2
