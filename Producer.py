class Producer:
    def __init__(self, wta, delta, is_delta):
        self.wta = wta
        self.delta = delta
        self.traded = False
        self.consecutive_trades = 0
        self.prices = []
        self.surplus = []
        self.price_group = ""
        self.delta_scale = is_delta

    def update_wta(self):
        if not self.traded:
            if self.delta_scale:
                self.wta *= (1 - self.delta)
            else:
                self.wta -= 10
        #elif self.consecutive_trades >= 3:
            #self.wta += 2
