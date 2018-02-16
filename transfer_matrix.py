class SolenoidTransferMatrix(object):
    """
    SolenoidTransferMatrix represents a transfer matrix to transport particles 
    from one point to another in s, assuming a solenoidal transport element.
    """
    def __init__(self, z_in, z_out, reference_momentum):
        """
        Transfer matrix transports particles from z_in to z_out, with
        reference_momentum representing the reference momentum of the matrix
        """
        raise NotImplementedError("Not implemented")

    def transport_phase_space_vector(self, phase_space_vector):
        """
        Transport a phase space vector from z_in to z_out

        Returns a new phase space vector
 
        Throws an exception if phase_space_vector z is not consistent with z_in
        """
        raise NotImplementedError("Not implemented")

    def calculate_transfer_matrix(self):
        """
        Calculate the transfer matrix

        Looks up the field on axis; calculates the infinitesimal transfer
        matrix; uses the infinitesimal transfer matrix to generate the full
        transfer matrix from z_in to z_out. Stores the calculated transfer matrix
        internally.
        """
        raise NotImplementedError("Not implemented")
