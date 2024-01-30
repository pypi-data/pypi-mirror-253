from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import CommitError
from jnpr.junos.exception import RpcError


def open_session(dev_list):
    try:
        dev = Device(host=dev_list[0], user=dev_list[1], password=dev_list[2]) # start Net conf
        print (">Opening session in progress....")
        dev.open() # open connention
        print ("Session opened succesfully.\n")
        return dev
    except ConnectError as err: 
        print ("Cannot connect to device: {0}".format(err))
        print(">Press any key to retry...")
        input()
        return 'retry'
            
def lock_configuration(cu,dev_list):
    print (">Locking the configuration in progress....")
    try:
        cu.lock()
        print ("Configuration locked succesfully.\n")
    except LockError as err:
        print ("Unable to lock configuration: {0}".format(err))
        print("Press any key to retry...")
        input()
        open_session(dev_list)
        
def commit_check(cu):
    try:
        #Commit check the loaded configuration
        print (">Commit check the loaded configuration in progress......")
        cu.commit_check(timeout=60)
        print ("Commit check ended succesfully with no errors.\n")
        print("Press any key to commit...")
        input()
    except CommitError as err:
        # try rollback
        try:
            print ("Error: Commit check the loaded configuration: {0}".format(err))
            print("Press any key to rollback...")
            input()
            print (">Rolling back the configuration [rollback 0]....")
            cu.rollback(rb_id=0)
            print ("Committing the configuration after rollback 0")
            cu.commit()
            print ("Committing the configuration after rollback 0 succesfully.")
            return
        except RpcError as err:
            print ("Unable to roll back configuration changes: {0}".format(err))
            print("Press any key to continue...")
            input()
            return
        except CommitError as err:
            print ("Error: Unable to commit configuration: {0}".format(err))
            print("Press any key to continue...")
            input()
            return


def commit(cu,Configuration_Description = ''):
    try:
        #Committing the configuration......
        print (">Committing the configuration......")
        cu.commit(comment=Configuration_Description, timeout=300)
        print ("Committing the configuration succesfully.\n")
    except CommitError as err:
        print ("Unable to commit configuration: {0}".format(err))
        
        
def unlock_close(cu, dev):
    try:
        print (">Unlocking the configuration....")
        cu.unlock()
        print ("Configuration Unlocked.\n")
    except UnlockError as err:
        print ("Unable to unlock configuration: {0}".format(err))

def unlock(cu):
    try:
        print (">Unlocking the configuration....")
        cu.unlock()
        print ("Configuration Unlocked.\n")
    except UnlockError as err:
        print ("Unable to unlock configuration: {0}".format(err))
  
def session_close(dev):
    # End the NETCONF session and close the connection
    dev.close()
    print ("Session Closed.")