
class PhaseSpaceVector(object):
    """
    Phase space vector class represents a single particle at a point in space/time
    """
    def __init__(self, x, y, z, time, px, py, pz, energy):
        """
        Initialise the phase space vector
        """
        raise NotImplementedError("Not implemented")

    def get_numpy_representation(self):
        """
        Return the numpy representation of the phase space vector, which is a
        numpy array containing [x, px, y, py, time, energy]
        """
        raise NotImplementedError("Not implemented")

