import libs

class Level1(libs.Level):
    def __init__(self) :
        super().__init__()
        self.barrier_pos= [(200,400),(300,400)]
        self.ball_pos = (300,650)

class Level2(libs.Level):
    def __init__(self):
        super().__init__()
        self.barrier_pos = [(200,400),(300,500),(400,500)]
        self.ball_pos = (300,650)
