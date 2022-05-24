import numpy as np

from Gravity_Simulator.Engine.Physics.SimulationEngine import SimulationEngine
from Gravity_Simulator.resources.Objects import Planet
import yaml


def main():
    with open('configs/config.yaml') as file:
        config = yaml.safe_load(file)

        Sun = Planet(np.array(eval(config['Planet_Positions']['Sun'])),
                     np.array(eval(config['Planet_Velocities']['Sun'])), int(config['Planet_Masses']['Sun']),
                     float(config['Planet_Radii']['Sun']),
                     eval(config['Planet_Colors']['Sun']),
                     config['Constants']['Universal_Scale'],
                     isSun=True)

        Venus = Planet(np.array(eval(config['Planet_Positions']['Venus'])),
                     np.array(eval(config['Planet_Velocities']['Venus'])), int(config['Planet_Masses']['Venus']),
                     float(config['Planet_Radii']['Venus']),
                     eval(config['Planet_Colors']['Venus']),
                     config['Constants']['Universal_Scale'])

        Mercury = Planet(np.array(eval(config['Planet_Positions']['Mercury'])),
                     np.array(eval(config['Planet_Velocities']['Mercury'])), int(config['Planet_Masses']['Mercury']),
                     float(config['Planet_Radii']['Mercury']),
                     eval(config['Planet_Colors']['Mercury']),
                     config['Constants']['Universal_Scale'])

        Earth = Planet(np.array(eval(config['Planet_Positions']['Earth'])),
                    np.array(eval(config['Planet_Velocities']['Earth'])), int(config['Planet_Masses']['Earth']),
                    float(config['Planet_Radii']['Earth']),
                    eval(config['Planet_Colors']['Earth']),
                    config['Constants']['Universal_Scale'])


        simulation = SimulationEngine(config)
        simulation.add_object(Sun)
        simulation.add_object(Venus)
        simulation.add_object(Mercury)
        simulation.add_object(Earth)
        simulation.run()

if __name__ == '__main__':
    main()


