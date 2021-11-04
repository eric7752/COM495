class Consumer:
    def __init__(self, wtp, delta):
        self.wtp = wtp
        self.delta = delta
        self.traded = False
        self.consecutive_trades = 0

    def update_wtp(self):
        if not self.traded:
            #self.wtp *= (1 + self.delta)
            self.wtp += 10
        #elif self.consecutive_trades >= 3:
            #self.wtp -= 2
