from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError


     
def load_configurations(cu,config_set):
    try:    
        command_err=''
        #load configuration changes
        print (">Loading configuration in progress...")
        
        for command in config_set.splitlines():
            command_err = command
            cu.load(command, format='set')
            
        print('********************* The Changes in Configuration*********************')
        #print the candidate configuration on screen
        cu.pdiff()
        
        print (">Configuration loaded succesfully\n")
        print("Press any key to continue...")
        input()
    except (ConfigLoadError, CommitError) as err:
        print ('Error at: ' ,command_err)
        print ("Unable to load configuration changes:\n{0}".format(err))
        print("Press any key to continue...")
        input()
        
def load_list_set_configurations(cu,config_set):
    try:    
        command_err=''
        #load configuration changes
        
        print (">Loading configuration in progress...")
        
        for command in config_set:
            command_err = command
            cu.load(command, format='set')
            
        print('********************* The Changes in Configuration*********************')
        
        #print the candidate configuration on screen
        cu.pdiff()
        
        print (">Configuration loaded succesfully\n")
        print("Press any key to continue...")
        input()
    except (ConfigLoadError, CommitError) as err:
        print ('Error at: ' ,command_err)
        print ("Unable to load configuration changes:\n{0}".format(err))
        print("Press any key to continue...")
        input()
        