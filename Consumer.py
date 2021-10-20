class Consumer:
    def __init__(self, wtp, delta):
        self.wtp = wtp
        self.delta = delta
        self.traded = False

    def update_wtp(self):
        if not self.traded:
            self.wtp *= (1 + self.delta)
        #else:
            #self.wtp *= 0.8
