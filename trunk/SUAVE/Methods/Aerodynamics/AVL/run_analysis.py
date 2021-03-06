## @ingroup Methods-Aerodynamics-AVL
#run_analysis.py
# 
# Created:  Oct 2014, T. Momose
# Modified: Jan 2016, E. Botero
#           Jul 2017, M. Clarke

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import os
from SUAVE.Methods.Aerodynamics.AVL.read_results import read_results
from SUAVE.Methods.Aerodynamics.AVL.purge_files  import purge_files
from SUAVE.Core import redirect

## @ingroup Methods-Aerodynamics-AVL
def run_analysis(avl_object):
    """ This calls the AVL executable and runs an analysis

    Assumptions:
        None
        
    Source:
        None

    Inputs:
        avl_object - passed into the  call_avl function  
        
    Outputs:
        results

    Properties Used:
        N/A
    """    
    
    call_avl(avl_object)
    results = read_results(avl_object)

    return results


def call_avl(avl_object):
    """ This function calls the AVL executable and executes analyses

    Assumptions:
        None
        
    Source:
        None

    Inputs:
        avl_object

    Outputs:
        exit_status

    Properties Used:
        N/A
    """    
    
    import sys
    import time
    import subprocess

    log_file = avl_object.settings.filenames.log_filename
    err_file = avl_object.settings.filenames.err_filename
    if isinstance(log_file,str):
        purge_files(log_file)
    if isinstance(err_file,str):
        purge_files(err_file)
    avl_call = avl_object.settings.filenames.avl_bin_name
    geometry = avl_object.settings.filenames.features
    in_deck  = avl_object.current_status.deck_file

    with redirect.output(log_file,err_file):

        ctime = time.ctime() # Current date and time stamp
        sys.stdout.write("Log File of System stdout from AVL Run \n{}\n\n".format(ctime))
        sys.stderr.write("Log File of System stderr from AVL Run \n{}\n\n".format(ctime))

        with open(in_deck,'r') as commands:
            avl_run = subprocess.Popen([avl_call,geometry],stdout=sys.stdout,stderr=sys.stderr,stdin=subprocess.PIPE)
            for line in commands:
                avl_run.stdin.write(line)
        avl_run.wait()

        exit_status = avl_run.returncode
        ctime = time.ctime()
        sys.stdout.write("\nProcess finished: {0}\nExit status: {1}\n".format(ctime,exit_status))
        sys.stderr.write("\nProcess finished: {0}\nExit status: {1}\n".format(ctime,exit_status))        

    return exit_status

