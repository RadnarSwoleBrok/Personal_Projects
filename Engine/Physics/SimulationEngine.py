from Gravity_Simulator.Engine.Display.PyGameEngine import Engine

class SimulationEngine(Engine):
    def __init__(self, config: dict):
        self.config = config
        super().__init__(config['Window']['Title'], (0,0,0), config['Window']['Width'], config['Window']['Height'], 60)

    def update(self):
        super().update_velocity()
        super().update()

    def paint(self):
        super().paint()

