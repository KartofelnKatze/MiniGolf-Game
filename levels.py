import libs

class Level1(libs.Level):
    def __init__(self) :
        super().__init__()
        self.barrier_pos= [(200,400),(300,400)]

class Level2(libs.Level):
    def __init__(self):
        super().__init__()
        self.barrier_pos = [(200,400),(300,500),(400,500)]
