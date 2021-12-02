class Consumer:
    def __init__(self, wtp, delta, is_delta):
        self.wtp = wtp
        self.delta = delta
        self.traded = False
        self.consecutive_trades = 0
        self.prices = []
        self.surplus = []
        self.delta_scale = is_delta

    def update_wtp(self):
        if not self.traded:
            if self.delta_scale:
                self.wtp *= (1 + self.delta)
            else:
                self.wtp += 10
