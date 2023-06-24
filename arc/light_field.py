class LaserBeam(object):
    
    def __init__(self,
                 wavelength,
                 radius,
                 power,
                 polarization,
                 direction
                 ):
        
        self.wavelength = wavelength
        self.radius = radius
        self.power = power
        self.polarization = polarization
        self.direction = direction


class LightField(object):
    """
    Implement general calculations for complex light field formed
    by interfering Gaussian beams.
    
    """
    def __init__(self, beams: list[dict]) -> None:
        pass

    def getIntensity(self, x, y, z):
        pass

    def getPolarization(self, x, y, z):
        pass


