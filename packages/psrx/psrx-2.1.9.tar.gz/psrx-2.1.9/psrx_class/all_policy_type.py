import re
import ipaddress
from termcolor import colored
from colorama import init, Fore
import _configurations_
import all_address_type
import save_excel_def

# Initialize colorama
init()
policy_description = 'Policy Pushed through Netconf'

include_app = [
    'junos-icmp-all',
    ]


def make_new_address(address,ip,dev=None,file_content=None):
    to = ' to '
    if ip.find(to) != -1:
        send_address=f'address\t{address}\t\t{ip.split(to)[0]}\t{ip.split(to)[1]}' 
    else:
        send_address=f'address\t{address}\t\t{ip}' 
        
    list_of_list = all_address_type.address_address_set(dev,send_address,file_content=file_content)
    

    if len(list_of_list[0]) > 0:         
        return list_of_list[0]
      
    if len(list_of_list[1]) > 0:         
        print(yellow('!!!!!!!! Wrong Input, Please try again !!!!!!!!'))
        return 'try again'
        
    if len(list_of_list[2]) > 0:  
        print(yellow('!!!!!!!! Invalid Range, Please try again !!!!!!!!'))       
        return 'try again'
        
    if len(list_of_list[3]) > 0: 
        print(yellow('!!!!!!!! Invalid Address, Please try again !!!!!!!!'))        
        return 'try again'
        
    if len(list_of_list[5]) > 0:     
        print(yellow('!!!!!!!! Duplicated Input, Please try again !!!!!!!!'))
        return 'try again'
            
    if len(list_of_list[6]) > 0:     
        print(yellow('!!!!!!!! Already Excisted, Please try again !!!!!!!!'))
        return 'try again'   
            
    if len(list_of_list[7]) > 0:    
        print(yellow('!!!!!!!! The IP Already Excisted In Configuration, Please try again !!!!!!!!')) 
        return 'try again'
    
    if len(list_of_list[8]) > 0:     
        print(yellow('!!!!!!!! The Same IP You Paste Twice, Please try again !!!!!!!!'))
        return 'try again'
        
        
def find_address_caseSensitve(address,dev=None,file_content=None):
    if dev != None:
        all_set = _configurations_.retrive_configurations('all' ,address, dev=dev)
    if file_content != None:
        all_set = _configurations_.retrive_configurations('all' ,address, file_content=file_content)
    
    for line in all_set:
        match = re.match(r'set security address-book global address (.*?) (.*?)$',line)
        if match:
            configure_address_name = re.match(r'set security address-book global address (.*?) (.*?)$',line).group(1)
            configure_address_ip = re.match(r'set security address-book global address (.*?) (.*?)$',line).group(2)
            if is_valid_ipv4(configure_address_ip):
                if address.lower() == configure_address_name.lower():
                    return [configure_address_name,configure_address_ip]
                else:
                    return 'address not found'
    


def get_address_ip(address,dev=None,file_content=None):
    if dev != None:
        retuen_match_in_list_set = _configurations_.retrive_configurations('Tcloud_policy_address-set' , address, dev=dev)
        retuen_match_in_list = _configurations_.retrive_configurations('Tcloud_policy_address' , address, dev=dev)
    if file_content != None:
        retuen_match_in_list_set = _configurations_.retrive_configurations('Tcloud_policy_address-set' , address, file_content=file_content)
        retuen_match_in_list = _configurations_.retrive_configurations('Tcloud_policy_address' , address, file_content=file_content)
    address = re.sub(r'\x1b\[[0-9;]+m\x1b\[[0-9;]+m|\x1b\[[0-9;]+m', '', address)
    if len(retuen_match_in_list_set)== 0 : # not found as address set 
        if len(retuen_match_in_list) == 0 :# not found as address
            return 'address not found'
        else: # found as address
            match1 = re.search(r'address (.*?) (.*?)$',retuen_match_in_list[-1])
            if 'range-address' in match1.group(2):
                match1 = re.search(r' range-address (.*?) to (.*?)$',retuen_match_in_list[-1])
                return match1.group(1)
            else:
                ip = ip_without_prefix(match1.group(2))
                return ip
            
    else:#found as address set 
        add = re.search('address (.*?)$',retuen_match_in_list_set[-1]).group(1)
        if dev != None:
            retuen_match_in_list = _configurations_.retrive_configurations('Tcloud_policy_address' , add, dev=dev)
        if file_content != None:
            retuen_match_in_list = _configurations_.retrive_configurations('Tcloud_policy_address' , add, file_content=file_content)
        if len(retuen_match_in_list) == 0 :# not found as address
            return 'address not found'
        else: # found as address
            match1 = re.search(r'address (.*) (.*?)$',retuen_match_in_list[-1])
            if match1:
                if 'range-address' in match1.group(2):
                    match1 = re.search(r'address {} range-address (.*?) to (.*?)$'.format(address),retuen_match_in_list[0])
                    return match1.group(1)
                else:
                    ip = ip_without_prefix(match1.group(2))
                    return ip
            else:
                return 'address not found'
        
        
        
def get_zone_name(ip,dev=None,file_content=None): 
    if dev != None:
        retuen_match_in_list_route = _configurations_.retrive_configurations('all' ,ip, dev=dev)
    if file_content != None:
        retuen_match_in_list_route = _configurations_.retrive_configurations('all' ,ip, file_content=file_content)
    
    specific_range = []
    
    vlan_name = ''
    
    the_matched_commands = []

    r_specific_range = []
    
    r_the_matched_commands = []
    while True:
        for each_ip in retuen_match_in_list_route:
            match_unit_address = re.match(r'set interfaces (.*?) unit (.*?) family inet address (.*?)$',each_ip)
            if match_unit_address:
                interface_IP = re.match(r'set interfaces (.*?) unit (.*?) family inet address (.*?)$',each_ip).group(3)
                if is_ip_in_range(ip,interface_IP):
                    specific_range.append(interface_IP)
                    the_matched_commands.append(each_ip)
            else:
                match_route_address_ = re.match(r'set routing-options static route (.*?) next-hop (.*?)$',each_ip)
                if match_route_address_:
                    route_IP_ = re.match(r'set routing-options static route (.*?) next-hop (.*?)$',each_ip).group(1)
                    if is_ip_in_range(ip,route_IP_):
                        r_specific_range.append(route_IP_)
                        r_the_matched_commands.append(each_ip)
                        
        else:
            if len(specific_range) >= len(r_specific_range):
                break
            elif len(r_specific_range) > len(specific_range):
                ip_index = most_specific_range(ip,r_specific_range)
                for x in r_the_matched_commands:
                    ipz = re.match(r'set routing-options static route {} next-hop (.*?)$'.format(ip_index),x)
                    if ipz:
                        ip = re.match(r'set routing-options static route {} next-hop (.*?)$'.format(ip_index),x).group(1)
                        specific_range = []
                        r_specific_range = []



    command_index = most_specific_range(ip,specific_range)
    
    for x in the_matched_commands:
        ipc = re.match(r'set interfaces (.*?) unit (.*?) family inet address {}$'.format(command_index),x)
        if ipc :
            interface = re.match(r'set interfaces (.*?) unit (.*?) family inet address {}$'.format(command_index),x).group(1)
            unit = re.match(r'set interfaces (.*?) unit (.*?) family inet address {}$'.format(command_index),x).group(2)
            vlan_name = f'{interface}.{unit}'   
    
    for each_interface in retuen_match_in_list_route:
        match_interface = re.match(r'set security zones security-zone (.*?) interfaces {}$'.format(vlan_name),each_interface)
        if match_interface:
            interface_zone = re.match(r'set security zones security-zone (.*?) interfaces {}$'.format(vlan_name),each_interface).group(1)
            return interface_zone
                

def get_configured_policy(file_content=None):
    data = save_excel_def.save_excel(type_='policy',file_content=file_content, file_name='no name',onlyData='data')
    return data

def print_same_context_same_ruleName(old_rule_name,src_zone,dst_zone,three_values,new_rule_name,src_address,dst_address,app_Group):
    n = '\n'
    a = ' & '
    j = ', '
    e = ''
    z = 'zone-type'
    New_Src = 'New Src. Add'
    New_Dst = 'New Dst. Add'
    New_Service= 'New Service'

    print(yellow('!!!!!!!!! WARNING Duplicated Rule!!!!!!!!!'))
    print(g('▼▼▼▼▼▼▼▼▼▼▼▼ [')+b(new_rule_name)+g('] similar to an Existing rule called [')+b(old_rule_name)+g('].'))
    print(f' ►► Zone Type   : {b(z)}')
    print(f' ►► From Zone   : {b(src_zone)}')
    print(f' ►► To Zone     : {b(dst_zone)}')
    print(f' ►► Rule Name   : {b(old_rule_name)} ►► {b(new_rule_name)}')
    print(f' ►► Existing Src. Add    : {j.join([b(x) if x in src_address else x for x in three_values[0] if x != e])} ')
    print(f' ►► {g(New_Src)}         : {j.join([b(x) if x in three_values[0] else x for x in src_address if x != e])} ')
    print(f' ►► Existing Dst. Add    : {j.join([b(x) if x in dst_address else x for x in three_values[1] if x != e])} ')
    print(f' ►► {g(New_Dst)}         : {j.join([b(x) if x in three_values[1] else x for x in dst_address if x != e])} ')
    print(f' ►► Existing Service     : {j.join([b(x) if x in app_Group else x for x in three_values[2] if x != e])} ')
    print(f' ►► {g(New_Service)}          : {j.join([b(x) if x in three_values[2] else x for x in app_Group if x != e])} ')
    print('▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲ End Of the rule ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲')

def print_rule(old_rule,rule_name,Sources,Destinations,Services):
    n = '\n'
    a = ' & '
    j = ', '
    e = ''
    
    New_Src = 'New Src. Add'
    New_Dst = 'New Dst. Add'
    New_Service= 'New Service'

    print(yellow('!!!!!!!!! WARNING Duplicated Rule Name !!!!!!!!!'))
    print(g('▼▼▼▼▼▼▼▼▼▼▼▼ [')+m(rule_name)+g('] similar to an Existing rule called [')+m(old_rule[3])+g('].'))
    print(f' ►► Zone Type   : {old_rule[0].replace(n,a)}')
    print(f' ►► From Zone   : {old_rule[1]}')
    print(f' ►► To Zone     : {old_rule[2]}')
    print(f' ►► Rule Name   : {b(old_rule[3])} ►► {b(rule_name)}')
    print('--------------------------:------------------------------------------------------')
    print(f' ►► Existing Src. Add    : {j.join([b(x) if x in Sources else x for x in old_rule[4].split(n) if x != e])} ')
    print(f' ►► {g(New_Src)}         : {j.join([b(x) if x in old_rule[4].split(n) else x for x in Sources if x != e])} ')
    print('--------------------------------------------------------------------------------')
    print(f' ►► Existing Dst. Add    : {j.join([b(x) if x in Destinations else x for x in old_rule[5].split(n) if x != e])} ')
    print(f' ►► {g(New_Dst)}         : {j.join([b(x) if x in old_rule[5].split(n) else x for x in Destinations if x != e])} ')
    print('--------------------------:------------------------------------------------------')
    print(f' ►► Existing Service     : {j.join([b(x) if x in Services else x for x in old_rule[6].split(n) if x != e])} ')
    print(f' ►► {g(New_Service)}          : {j.join([b(x) if x in old_rule[6].split(n) else x for x in Services if x != e])} ')
    print('--------------------------:------------------------------------------------------')
    print(f' ►► Dyn. App    : {old_rule[7]}')
    print(f' ►► Url. Cat    : {old_rule[8]}')
    print(f' ►► Action      : {j.join([x for x in old_rule[9].split(n) if x != e])}')
    print(f' ►► App. Serv   : {old_rule[10]}')
    print(f' ►► Log         : {old_rule[11]}')
    print('▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲ End Of the rule ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲')



def  get_app(each_app, dev = None, file_content = None):
    if dev != None:
        retuen_match_set = _configurations_.retrive_configurations('Tcloud_policy_app-set' , each_app,is_exist = 'yes', dev=dev)
        retuen_match = _configurations_.retrive_configurations('Tcloud_policy_app' , each_app,is_exist = 'yes', dev=dev)
    if file_content != None:
        retuen_match_set = _configurations_.retrive_configurations('Tcloud_policy_app-set' , each_app,is_exist = 'yes', file_content=file_content)
        retuen_match = _configurations_.retrive_configurations('Tcloud_policy_app' , each_app,is_exist = 'yes', file_content=file_content)

    if retuen_match == True or retuen_match_set == True:
        return True
    else:
        return False

def check_for_valid_app_format(each_app): # [True,protocol,port]

    parts = each_app.split('_')
    port = parts[1].split('-')
    if len(port) == 1 and port[0].isdigit():
        return [True,parts[0],parts[1]]
        
    elif len(port) == 2 and port[0].isdigit() and port[1].isdigit():
        return [True,parts[0],parts[1]]
    else:
        return [False,False,False]

    
def create_new_app(protocol,port): #['app',['command1','command2']] or [False,False]
    app = f'{protocol.upper()}_{port}'
    command=[
        f'set applications application {m(app)} protocol {m(protocol.lower())}',
        f'set applications application {m(app)} destination-port {m(port)}',
    ]
    return [app,command]

def return_application(Services,dev=None,file_content=None):
    ser_com_LIST = []
    for each_app in Services:
        app = get_app(each_app, dev = dev, file_content = file_content)
        if app or each_app in include_app: #if app found
            ser_com_LIST.append([each_app,''])
            
        else: # if app not found
            # each_app = TCP_443 or TCP_123-233 or ser_group
            print(g('This Application [')+m(each_app)+g('] Not Found.Do you want to create it.'))
            user_agrees = input('type ['+yellow('y')+'] to continue : ')
            if user_agrees.lower() == 'y':
                after_check = check_for_valid_app_format(each_app) # [True,protocol,port]
                if after_check[0]:
                    protocol = after_check[1]
                    port = after_check[2]
                    created_app = create_new_app(protocol,port) #['app',['command1','command2']] or [False,False]
                    ser_com_LIST.append(created_app)
                else:
                   print(g('You can not make application-set in this section. This Application will be skipped'))
                   ser_com_LIST.append([False,False]) 
            else:
                print(g('This Application will be skipped'))
                ser_com_LIST.append([False,False])
    return  ser_com_LIST             

def return_zones(addresses,dev=None,file_content=None): 
    # return #[[address,zone,[command]],[False,False,False]]   # command may == ''  
    add_zon_com_LIST = []
    
    for count,each_source in enumerate(addresses):
        flag = True
        while True:
            ip = get_address_ip(each_source,dev=dev,file_content=file_content) # the ip of the given address
            if ip != 'address not found': # if ip found
                zone_name = get_zone_name(ip,dev=dev,file_content=file_content)
                add_zon_com_LIST.append([each_source,zone_name,''])
                break
            else:# if ip not found
                
                # try find somthing similar
                found_address = find_address_caseSensitve(each_source,dev=dev,file_content=file_content)
                
                #not fount but found similr
                if found_address != 'address not found' and found_address !=None:
                    print(g('This address [')+m(each_source)+g('] Not Found.Did you mean [')+m(found_address[0])+g('] with IP [')+m(found_address[1])+g('].'))
                    user_agrees = input('type ['+yellow('y')+'] to continue : ')
                    if user_agrees.lower() == 'y':
                        addresses[count] = found_address[0]
                        each_source = found_address[0]
                        continue
                    else:
                        # if you not want to select the old try make new one
                        print(g('Do you want to create this Address  [') +  m(each_source) + g('].'))
                        user_agrees = input('type ['+yellow('y')+'] to continue : ')
                        if user_agrees.lower() == 'y':
                            while flag:
                                user_input = input(g('Enter [') + m(each_source) + g('] Ip or Range : '))
                                commands = make_new_address(each_source,user_input,dev=dev,file_content=file_content)
                                if commands != 'try again':
                                    ip = get_address_ip(each_source,dev=dev,file_content=commands) # the ip of the given address
                                    if ip != 'address not found': # if ip found
                                        zone_name = get_zone_name(ip,dev=dev,file_content=file_content)
                                        add_zon_com_LIST.append([each_source,zone_name,commands])
                                        flag = False
                            break
                                        
                            
                        else:
                            add_zon_com_LIST.append([False,False,False])
                            break
                            
                else:# not found at all
                    print(g('This address [')+m(each_source)+g('] Not Found.Do you want to create it.'))
                    user_agrees = input('type ['+yellow('y')+'] to continue : ')
                    if user_agrees.lower() == 'y':
                        while flag:
                            user_input = input(g('Enter [') + m(each_source) + g('] Ip or Range : '))
                            commands = make_new_address(each_source,user_input,dev=dev,file_content=file_content)
                            if commands != 'try again':
                                color_address = f'\x1b[1m\x1b[35m{each_source}\x1b[0m' 
                                ip = get_address_ip(color_address,dev=dev,file_content=commands) # the ip of the given address
                                if ip != 'address not found': # if ip found
                                    zone_name = get_zone_name(ip,dev=dev,file_content=file_content)
                                    add_zon_com_LIST.append([each_source,zone_name,commands])
                                    flag = False
                        break
                                    
                        
                    else:
                        add_zon_com_LIST.append([False,False,False])
                        break
                            
                            
    return  add_zon_com_LIST                       

def commands_zonesGroup(Address_Zones,Address_Zones_Group):
    commands=[]
    for x in Address_Zones:
        if x != [False,False,False]:
            if x[2] != '' and x[2] != False:
                commands.append(x[2])
            for index,each_group in enumerate(Address_Zones_Group):
                if x[1] in each_group :
                    if not(x[0] in each_group[1]):
                        Address_Zones_Group[index][1].append(x[0])
                        break
            else:
                Address_Zones_Group.append([x[1],[x[0]]])
    commands.append('')
    return [commands,Address_Zones_Group]

def commands_appGroup(applications):#[['app',['command1','command2']],[False,False]]  # command may == '' 
    app=[]
    commands=[]
    for x in applications:
        if x != [False,False]:
            if x[1] != '' and x[1] != False:
                for cmd in x[1]:
                    commands.append(cmd)

            if x[0] != '' and x[0] != False:
                app.append(x[0])
    commands.append('')
    return [commands,app]

def True_if_idp(dev=None, file_content = None):
    if dev != None:
        return _configurations_.retrive_configurations('Tcloud_idp' , 'line',is_exist = 'yes', dev=dev)
    if file_content != None:
        return _configurations_.retrive_configurations('Tcloud_idp' , 'line',is_exist = 'yes', file_content=file_content)

def same_context_same_ruleName(rule_name=None,context=None,src_address=None,dst_address=None,dev=None, file_content = None):
    if dev != None:
        all_set = _configurations_.retrive_configurations('all' ,'address', dev=dev)
    if file_content != None:
        all_set = _configurations_.retrive_configurations('all' ,'address', file_content=file_content)
    matched_lines = []
    for line in all_set:
        if f'set security policies {context} policy {rule_name} ' in line:
            matched_lines.append(line)
    return matched_lines

def same_context_same_adresses(rule_name=None,context=None,src_address=None,dst_address=None,dev=None, file_content = None):
    if dev != None:
        all_set = _configurations_.retrive_configurations('all' ,'address', dev=dev)
    if file_content != None:
        all_set = _configurations_.retrive_configurations('all' ,'address', file_content=file_content)
    
    matched_lines = []
    policy_name= []
    match_policy_context = []
    matched_policy_name = []

    for line in all_set:
        match_me = re.match(r'set security policies {} policy (.*?) '.format(context),line)
        if match_me:
            ruleName = match_me.group(1)
            policy_name.append(ruleName)
            for index,x in enumerate(match_policy_context):
                if x[0]== policy_name:
                    if not(line in match_policy_context[index][1]):
                        match_policy_context[index][1].append(line)
            else:
                match_policy_context.append([policy_name,[line]])

    for each_policy in match_policy_context:
        for add in src_address:
            if not(f'set security policies {context} policy {each_policy[0]} source-address {add}' in each_policy[1]):
                break
        else:
            if not(each_policy[0] in matched_policy_name):
                matched_policy_name.append(each_policy[0])

    for each_policy in match_policy_context:
        for add in dst_address:
            if not(f'set security policies {context} policy {each_policy[0]} destination-address {add}' in each_policy[1]):
                break
        else:
            if not(each_policy[0] in matched_policy_name):
                matched_policy_name.append(each_policy[0])        

    for x in match_policy_context:
            if x[0] in matched_policy_name:
                matched_lines.append(x)

    return matched_lines

def get_values_from_commands(lines):
    src=[]
    dst=[]
    ser=[]
    for each_line in lines:
        if re.match(r'(.*?) source-address (.*?)$',each_line):
            src.append(re.match(r'(.*?) source-address (.*?)$',each_line).group(2))
        if re.match(r'(.*?) destination-address (.*?)$',each_line):
            dst.append(re.match(r'(.*?) destination-address (.*?)$',each_line).group(2))
        if re.match(r'(.*?) application (.*?)$',each_line):
            ser.append(re.match(r'(.*?) application (.*?)$',each_line).group(2))
    return [src,dst,ser]

def print_same_zone_error(rule_name,each_src,each_dst,src_address,dst_address,in_,not_):
    print('----------------------------This rule had been skipped----------------------------')
    print(f'This Rule : {m(rule_name)} must be in {in_} Not in {not_} because both zones in {in_}')
    print(f'Source Zone : {m(each_src)}')
    print(f'Destination Zone : {m(each_dst)}')
    print(f'Source Adress : {yellow(src_address)}')
    print(f'Destination Adress : {yellow(dst_address)}')
    print('----------------------------This rule had been skipped----------------------------')

def policy_maker(rule_name,Src_Zon_Group,Dst_Zon_Group,app_Group,dev=None ,file_content=None):
#[[zone1,[add1,add2]],[zone2,[add3,add4]]]
#[[zone3,[add5,add6]],[zone4,[add7,add8]],[zone5,[add9,add10]]]
#['app1','app2','app3'],
    commands=[]
    for each_src in Src_Zon_Group:
        for each_dst in Dst_Zon_Group:
            context = f'from-zone {each_src[0]} to-zone {each_dst[0]}'
            src_address = [src for src in each_src[1]]
            dst_address = [dst for dst in each_dst[1]]
            
            #['set sec..','set sec..','set sec..']
            check_Context_RuleName = same_context_same_ruleName(rule_name=rule_name,context=context,dev=dev, file_content = file_content)

            if len(check_Context_RuleName) > 0 :
                three_values = get_values_from_commands(check_Context_RuleName)
                print_same_context_same_ruleName(rule_name,each_src[0],each_dst[0],three_values,rule_name,src_address,dst_address,app_Group)
            
            #[[policyName,['set sec..','set sec..','set sec..']],[policyName,['set sec..','set sec..','set sec..']]]
            check_Context_address = same_context_same_adresses(context=context,src_address=src_address,dst_address=dst_address,dev=dev, file_content = file_content)

            if len(check_Context_address) > 0 :
                for x in check_Context_address:
                    thre_values = get_values_from_commands(x[1]) 
                    print_same_context_same_ruleName(x[0],each_src[0],each_dst[0],thre_values,rule_name,src_address,dst_address,app_Group)
            
            if each_src[0] == each_dst[0] =='Outside_to_DCFW':
                print_same_zone_error(rule_name,each_src[0],each_dst[0],src_address,dst_address,'DFW','PFW')
                break

            if each_src[0] == each_dst[0] =='Management_Platform_FW':
                print_same_zone_error(rule_name,each_src[0],each_dst[0],src_address,dst_address,'PFW','DFW')
                break
            
            if each_src[0] == each_dst[0] =='DC_FW_to_ACI_North-South':
                 each_src[0] = each_dst[0] = 'DC_FW_to_ACI_East-West'
            
            for src_add in each_src[1]:
                commands.append(f'set security policies from-zone {m(each_src[0])} to-zone {m(each_dst[0])} policy {m(rule_name)} match source-address {m(src_add)}')

            for dst_add in each_dst[1]:
                commands.append(f'set security policies from-zone {m(each_src[0])} to-zone {m(each_dst[0])} policy {m(rule_name)} match destination-address {m(dst_add)}')

            for app in app_Group:
                commands.append(f'set security policies from-zone {m(each_src[0])} to-zone {m(each_dst[0])} policy {m(rule_name)} match application {m(app)}')

            if True_if_idp(dev=dev ,file_content=file_content):
                commands.append(f'set security policies from-zone {m(each_src[0])} to-zone {m(each_dst[0])} policy {m(rule_name)} match dynamic-application ' + m('any'))
                commands.append(f'set security policies from-zone {m(each_src[0])} to-zone {m(each_dst[0])} policy {m(rule_name)} match url-category '+ c('none'))
                commands.append(f'set security policies from-zone {m(each_src[0])} to-zone {m(each_dst[0])} policy {m(rule_name)} then permit application-services idp-policy Recommended')
            else:
                commands.append(f'set security policies from-zone {m(each_src[0])} to-zone {m(each_dst[0])} policy {m(rule_name)} then ' + c('permit'))
            commands.append(f'set security policies from-zone {m(each_src[0])} to-zone {m(each_dst[0])} policy {m(rule_name)} then log ' + c('session-close'))
            commands.append(f'set security policies from-zone {m(each_src[0])} to-zone {m(each_dst[0])} policy {m(rule_name)} then ' + c('count'))
    commands.append('')
    return commands

def policy_set(pasted_from_cli, dev=None, file_content = None):
    
    skipped_rules = []
    final_commands=[]
    for each_line in pasted_from_cli:
    
        rule_name = each_line[3]
        Sources = values_after(each_line,'Src') #Sources = [Sources1,Sources2,Sources3]
        Destinations = values_after(each_line,'Dst')#Destinations = [Destinations1,Destinations2,Destinations3]
        Services = values_after(each_line,'Ser')#Services = [Services1,Services2,Services3]
        Source_Zones = []
        Source_Zones_Group = []
        Destination_Zones = []
        Destination_Zones_Group = []
        applications = []
        app_Group = []
        
        print(g(' ►► Working with [') + m(rule_name) + g(']....'))
        all_policies = get_configured_policy(file_content=file_content)
        for each_rule in all_policies:
            if rule_name.lower() == each_rule[3].strip().lower():
                print_rule(each_rule,rule_name,Sources,Destinations,Services)
                user_input = input(' ►► Press [' + yellow('c') + '] to continue or any key to skip : ').lower()
                if user_input != 'c':
                    skipped_rules.append(each_line)
                    break
        else:
            Source_Zones = return_zones(Sources,dev=dev,file_content=file_content)#[[address,zone,[command]],[False,False,False]]   # command may == ''  
            obj1 = commands_zonesGroup(Source_Zones,Source_Zones_Group)#[[['command'],''],[['zone',[address,address']]]]
            for y in obj1[0]:#[['command'],'']
                for x in y:
                    if x != '':
                        final_commands.append(x)
            Source_Zones_Group = obj1[1] #[[zone1,[add1,add2]],[zone2,[add3,add4]]]

            Destination_Zones = return_zones(Destinations,dev=dev,file_content=file_content)#[[address,zone,[command]],[False,False,False]]   # command may == ''  
            obj4 = commands_zonesGroup(Destination_Zones,Destination_Zones_Group)#[[['command'],''],[['zone',[address,address']]]]
            for y in obj4[0]:
                for x in y:
                    if x != '':
                        final_commands.append(x)
            Destination_Zones_Group = obj4[1] #[[zone1,[add1,add2]],[zone2,[add3,add4]]]
            
            applications = return_application(Services,dev=dev,file_content=file_content) #[['app',['command1','command2']],[False,False]]  # command may == '' 
            obj2 = commands_appGroup(applications)#[ ,['app1','app2','app3']]
            for x in obj2[0]:
                if x != '':
                    final_commands.append(x)
            app_Group = obj2[1] #['app1','app2','app3'],

            obj3 = policy_maker(rule_name,Source_Zones_Group,Destination_Zones_Group,app_Group,dev=dev ,file_content=file_content)
            for x in obj3:
                if x != '':
                    final_commands.append(x)
               
            

    return [final_commands,policy_description]

def valid_ports(port):

    # Split the port by hyphen and check the parts
    parts = port.split('-')
    if len(parts) == 1 and parts[0].isdigit():
        return True
        
    elif len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        return True
    else:
        return False

def network_ip(ip_str,invalid_line):
    
    try:
    
        ip_network = ipaddress.IPv4Network(ip_str, strict=False)
        
        # Extract the IPv4 address without the subnet
        ipv4_address = ip_network.network_address
        return ipv4_address
        
    except Exception as e:
        wrong_inputs = f"Error: Invalid characters in the IPv4 address: \b{invalid_line} no action had taken."
        return ['error',wrong_inputs]
        
        
def ip_without_prefix(ip_str):
        if ip_str.find('/') != -1 :
            ipv4_prefix = ip_str.split('/')[0]
            return ipv4_prefix
            
      
def is_ip_in_range(ip, ip_prefix):
    try:
        # Parse the IP address and prefix into IPv4Network objects
        network = ipaddress.IPv4Network(ip_prefix, strict=False)
        ip_address = ipaddress.IPv4Address(ip)

        # Check if the IP address is within the range of the IP prefix
        if ip_address in network:
            return True
        else:
            return False
    except (ipaddress.AddressValueError, ValueError):
        return False
        
def most_specific_range(ip, ip_ranges):
    most_specific_match = None
    longest_prefix_length = -1

    ip = ipaddress.IPv4Address(ip)

    for ip_range in ip_ranges:
        try:
            network = ipaddress.IPv4Network(ip_range, strict=False)
            if ip in network and network.prefixlen > longest_prefix_length:
                most_specific_match = ip_range  # Store the actual IP range
                longest_prefix_length = network.prefixlen
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError):
            pass

    return most_specific_match


    
def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False
        
def values_after(mylist,after_value):
    # Initialize variables
    found_values_between = []
    if after_value == 'Src': search_range = 5
    if after_value == 'Dst': search_range = 10
    if after_value == 'Ser': search_range = 15
    
    for index in range(search_range,search_range + 5):
        try:
            if mylist[index] != "":found_values_between.append(mylist[index])
        except:
            pass
    return found_values_between


def m(word):
    styled_text = colored(word, "magenta")
    return styled_text
def c(word):
    styled_text = colored(word, "cyan")
    return styled_text
def b(word):
    styled_text = colored(word, "blue")
    return styled_text
def yellow(word):
    styled_text = colored(word, "yellow")
    return styled_text
def g(word):
    styled_text = colored(word, "green")
    return styled_text