''' This is a configuarion class from mega flask tutorial iii
'''
import probgen.generators as gens
class Config:
    """docstring for Config.
    usage:
        from config import Config
    """
    generators = gens.config['base']

    print("Config class got",generators)
