import sys, os

installed_dirs = ['asemd', 'cnsmd', 'lasermd', 'Services', 'Utils']

installed_files_in_asemd = ('asemd.cat', 'asemd.dll', 'asemd.inf', 'asemd64.dll')

installed_files_in_cnsmd = ('cnsmd.cat', 'cnsmd.dll', 'cnsmd.inf', 'cnsmd64.dll')

installed_files_in_lasermd = ('lasermd.cat', 'lasermd.dll', 'lasermd.inf', 'lasermd64.dll')

installed_files_in_services = ('aseVCServiceB.exe', 'aseVCServiceSC.exe')

installed_files_in_utils = ('JaCarta BioTool.exe')


def test_installed_dirs():
    
    dirs= os.listdir('C:\\Program Files (x86)\\JaCarta\\JC-Client')
    print(dirs)
    print(installed_dirs)
   
   # if dirs == installed_dirs:

    #    print('OK')
    # else:
      #  print('Error list dirs')"""


             
