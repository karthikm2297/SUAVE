## @ingroup Components-Wings
# Segment.py
# 
# Created:  Sep 2016, E. Botero
# Modified: Jul 2017, M. Clarke

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Components import Component, Lofted_Body, Mass_Properties
from SUAVE.Components.Wings.Control_Surface import Control_Surface 
# ------------------------------------------------------------ 
#  Wing Segments
# ------------------------------------------------------------

## @ingroup Components-Wings
class Segment(Lofted_Body.Segment):
    def __defaults__(self):
        """This sets the default for wing segments in SUAVE.

        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        N/A
        """         
        self.tag = 'segment'
        self.percent_span_location = 0.0
        self.twist                 = 0.0
        self.root_chord_percent    = 0.0
        self.dihedral_outboard     = 0.0
        self.sweeps                = Data()
        self.sweeps.quarter_chord  = 0.0
        self.sweeps.leading_edge   = 0.0
        self.Airfoil               = Data()
        self.control_surfaces      = Data()  
        
    def append_airfoil(self,airfoil):
        """ Adds an airfoil to the segment

        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        N/A
        """  
        # assert database type
        if not isinstance(airfoil,Data):
            raise Exception, 'input component must be of type Data()'

        # store data
        self.Airfoil.append(airfoil)

        return    

## @ingroup Components-Wings
class SegmentContainer(Lofted_Body.Segment.Container):
    """ Container for wing segment
    
    Assumptions:
    None

    Source:
    N/A

    Inputs:
    None

    Outputs:
    None

    Properties Used:
    N/A
    """     
    
    pass