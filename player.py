
class Player:
    def __init__(self, mode, waves, spawn_rate, cash):
        #int value
        self.mode = mode
        #waves, spawn_rate, starting_cash
        self.waves = waves
        self.spawn_rate = spawn_rate
        self.cash = cash
        self.current_wave = 0

    def add_cash(self, cash_add):
        self.cash += cash_add
    def take_cash(self, cash_take):
        self.cash -= cash_take
    def next_wave(self):
        if self.wave + 1 < len(self.wave):
            self.curent_wave += 1