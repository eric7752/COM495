class Producer:
    def __init__(self, wta, delta):
        self.wta = wta
        self.delta = delta
        self.traded = False

    def update_wta(self):
        if not self.traded:
            self.wta *= (1 - self.delta)
        #else:
            #self.wta *= 1.2