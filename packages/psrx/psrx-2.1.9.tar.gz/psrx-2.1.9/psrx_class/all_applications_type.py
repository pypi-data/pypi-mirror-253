import _configurations_
from termcolor import colored
application_description = 'Application Pushed through Netconf'





excelude_applications = [
    'application_group',
    'application-group',
    'application group',
    ''
    ]
    
def application_applications_set(dev, input_any_applications_to_configure, file_content = None): #dev, input_any_applications_to_configure

    invalid_application_set = []
    
    valid_application_count = 0 
    
    commands=[]
    
    already_existed=[]
    
    duplicated_in_commands = []
    lines = input_any_applications_to_configure.strip().split('\n')
    
     # [[each line.split], [each line.split], [each line.split]]
    result = [line.split('\t') for line in lines]

    for each_line1 in result:
    
# if >>  For application only >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        if len(each_line1) == 6 and each_line1[5] != '':
        
            # if desctription has space between it's word replace it with _
            each_line = [element.strip().replace('\t','').replace('\xa0','').replace(' ', '_').replace('&', 'And').replace('(','').replace(')','').replace('\r','') for element in each_line1]

 #==================== For Application Only ==================================================================================================
            
            valid_Src_Port = valid_ports(each_line[4])
            valid_Dst_Port = valid_ports(each_line[5])
            if dev != None:
                retuen_match_in_list = _configurations_.retrive_configurations('application' , each_line[1], dev=dev)
            if file_content != None:
                retuen_match_in_list = _configurations_.retrive_configurations('application' , each_line[1], file_content=file_content)
                    
            if each_line[2] == '' and valid_Dst_Port: # ['Application', name, '', prtocol , any, port ]
                if not(valid_Src_Port): # if source port not exist
                    if not(f'set applications application {each_line[1]} protocol {each_line[3].lower()}' in commands):
                        if len(retuen_match_in_list) == 0:    
                            commands.append(f'set applications application {m(each_line[1])} protocol {yellow(each_line[3].lower())}')
                            commands.append(f'set applications application {m(each_line[1])} destination-port {yellow(each_line[5])}')
                            valid_application_count +=1
                            continue
                        else:
                            already_existed.append(f'The application [{m(each_line[1])}] Already existed. No action had taken.')
                            continue
                    else:
                        duplicated_in_commands.append(f'The application [{m(each_line[1])}] Is duplicated and done once. No action had taken.')
                        continue
                
                if valid_Src_Port: # if source port exist  
                    if not(f'set applications application {each_line[1]} protocol {each_line[3].lower()}' in commands):
                        if len(retuen_match_in_list) == 0:    
                            commands.append(f'set applications application {m(each_line[1])} protocol {yellow(each_line[3].lower())}')
                            commands.append(f'set applications application {m(each_line[1])} source-port {yellow(each_line[4])}')
                            commands.append(f'set applications application {m(each_line[1])} destination-port {yellow(each_line[5])}')
                            valid_application_count +=1
                            continue
                        else:
                            already_existed.append(f'The application [{m(each_line[1])}] Already existed. No action had taken.')
                            continue
                    else:
                        duplicated_in_commands.append(f'The application [{m(each_line[1])}] Is duplicated and done once. No action had taken.')
                        continue
            elif each_line[2] == '' and not(valid_Dst_Port):
                
                invalid_application_set.append(f' You enter invalid destination-port [{yellow(each_line[5])}] in the application name[{m(each_line[1])}]. no action had taken.')
                continue   
               
           
            if each_line[2] != '' and valid_Dst_Port: # ['Application', name, description, prtocol , any, port ] 
                if not(valid_Src_Port): # if source port not exist
                    if not(f'set applications application {each_line[1]} description {each_line[2]} protocol {each_line[3].lower()}' in commands):
                        if len(retuen_match_in_list) == 0:    
                            commands.append(f'set applications application {m(each_line[1])} description {yellow(each_line[2])} protocol {yellow(each_line[3].lower())}')
                            commands.append(f'set applications application {m(each_line[1])} description {yellow(each_line[2])} destination-port {yellow(each_line[5])}')
                            valid_application_count +=1
                            continue
                        else:
                            already_existed.append(f'The application [{m(each_line[1])}] Already existed. No action had taken.')
                            continue
                    else:
                        duplicated_in_commands.append(f'The application [{m(each_line[1])}] Is duplicated and done once. No action had taken.')
                        continue
                    
                if valid_Src_Port: # if source port exist
                    if not(f'set applications application {each_line[1]} description {each_line[2]} protocol {each_line[3].lower()}' in commands):
                        if len(retuen_match_in_list) == 0:    
                            commands.append(f'set applications application {m(each_line[1])} description {yellow(each_line[2])} protocol {yellow(each_line[3].lower())}')
                            commands.append(f'set applications application {m(each_line[1])} description {yellow(each_line[2])} source-port {yellow(each_line[4])}')
                            commands.append(f'set applications application {m(each_line[1])} description {yellow(each_line[2])} destination-port {yellow(each_line[5])}')
                            valid_application_count +=1
                            continue
                        else:
                            already_existed.append(f'The application [{m(each_line[1])} ] Already existed. No action had taken.')
                            continue
                    else:
                        duplicated_in_commands.append(f'The application [{m(each_line[1])}] Is duplicated and done once. No action had taken.')
                        continue
            elif each_line[2] != '' and not(valid_Dst_Port):
                invalid_application_set.append(f' You enter invalid destination-port [{yellow(each_line[5])}] in the application name[{m(each_line[1])}]. no action had taken.')
                continue          
            
                    
  # if >>  For application group >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.  
  
        #inilaize each_line1 add more elements '' if have less than 4
        if len(each_line1) < 6:
            for more_element in range(6 - len(each_line1)):
                each_line1.append('')
                
        each_line = [element.strip().replace('\t','').replace('\xa0','').replace(' ', '_').replace('&', 'And').replace('(','').replace(')','').replace('\r','') for element in each_line1]
        
        if len(each_line) == 6 and each_line[5] == '':
            
            # send column 2 value to retrived data > return true or false
            if dev != None:
                is_excist_application = _configurations_.retrive_configurations('application' , each_line[1], is_exist= 'yes', dev = dev)
                retuen_match_in_list = _configurations_.retrive_configurations('application-set' , [each_line[0],each_line[1]], is_exist= 'yes', dev=dev)
            if file_content != None:
                
                is_excist_application = _configurations_.retrive_configurations('application' , each_line[1], is_exist= 'yes', file_content=file_content)
                
                retuen_match_in_list = _configurations_.retrive_configurations('application-set' , [each_line[0],each_line[1]], file_content=file_content)
                #retuen_match_in_list return a list that contain [logical app match , normal match] or [normal match ] or []
            if is_excist_application and not(each_line[0].lower() in [s.lower() for s in excelude_applications]):   # ['address-set', address, '', ''] 

                if not(each_line[0].lower() in [s.lower() for s in excelude_applications]):   # ['address-set', address, '', ''] 

                    if not(f'set applications application-set {each_line[0]} application {each_line[1]}' in commands):
                    
                        if len(retuen_match_in_list) == 0:

                            commands.append(f'set applications application-set {c(each_line[0])} application {m(each_line[1])}')
                            valid_application_count +=1
                            continue
                            
                        else:
                        
                            already_existed.append(f'The application [{m(each_line[1])}] Already existed in application-set called [ {c(each_line[0])} ]. No action had taken.')
                            continue
                            
                    else:
                    
                        duplicated_in_commands.append(f'The application [{m(each_line[1])}] Is duplicated and done once. No action had taken.')
                        continue
            else:
            
                invalid_application_set.append(f'The application [{m(each_line[1])}] Not exist. So you can not add it to application-set [ {c(each_line[0])} ]. No action had taken.')
                continue
                
                
    return [commands, invalid_application_set, application_description,valid_application_count,duplicated_in_commands,already_existed]

def valid_ports(port):

    # Split the port by hyphen and check the parts
    parts = port.split('-')
    if len(parts) == 1 and parts[0].isdigit():
        return True
        
    elif len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        return True
    else:
        return False

def m(word):
    styled_text = colored(word, "magenta", attrs=["bold"])
    return styled_text
def c(word):
    styled_text = colored(word, "cyan", attrs=["bold"])
    return styled_text
def b(word):
    styled_text = colored(word, "blue", attrs=["bold"])
    return styled_text
def yellow(word):
    styled_text = colored(word, "yellow", attrs=["bold"])
    return styled_text
def g(word):
    styled_text = colored(word, "green", attrs=["bold"])
    return styled_text