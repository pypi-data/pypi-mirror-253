from psrx_class import excel_output
from lxml import etree
import re

def policy_def(type_ = None , file_content=None ,dev=None,file_name=None, onlyData=None):
    returned =  retrive_configurations(type_ = type_ , file_content=file_content ,dev=dev)
    data_to_return = returned[0]
    columns_ = returned[1]
    rules = save_policy(data_to_return,type_)
    sheet_name_ = 'Policies'
    sheet_data1  = {
    'sheet_name': sheet_name_,
    'data': rules,
    'columns': columns_
    } 
    if onlyData == None:
        return sheet_data1
    else:
        return rules
def logical_policy_def(type_ = None , file_content=None ,dev=None,file_name=None):
    returned =  retrive_configurations(type_ = type_ , file_content=file_content ,dev=dev)
    data_to_return = returned[0]
    columns_ = returned[1]
    rules = save_policy(data_to_return,type_)
    sheet_name_ = 'Logical Policies'
    sheet_data1  = {
    'sheet_name': sheet_name_,
    'data': rules,
    'columns': columns_
    }    
    return sheet_data1
    
def address_def(type_ = None , file_content=None ,dev=None,file_name=None):
    returned =  retrive_configurations(type_ = type_ , file_content=file_content ,dev=dev)
    data_to_return = returned[0]
    columns_ = returned[1]
    rules = save_address(data_to_return,type_,file_name)
    sheet_name_ = 'Addresses_Book'
    sheet_data1  = {
    'sheet_name': sheet_name_,
    'data': rules,
    'columns': columns_
    }
    return sheet_data1
    
def address_set_def(type_ = None , file_content=None ,dev=None,file_name=None,x=None):
    rules = []
    if x != None:
        for filee in x:
            returned =  retrive_configurations(type_ = type_ , file_content=filee ,dev=dev)
            data_to_return = returned[0]
            columns_ = returned[1]
            rule = save_address_set(data_to_return,type_,file_name)
            rules.append(rule)
    else:
        returned =  retrive_configurations(type_ = type_ , file_content=file_content ,dev=dev)
        data_to_return = returned[0]
        columns_ = returned[1]
        rules = save_address_set(data_to_return,type_,file_name)
    sheet_name_ = 'Addresses_Groups'
    sheet_data1  = {
    'sheet_name': sheet_name_,
    'data': rules,
    'columns': columns_
    }     
    return sheet_data1
    
def application_def(type_ = None , file_content=None ,dev=None,file_name=None,x=None):
    rules = []
    if x != None:
        for filee in x:
            returned =  retrive_configurations(type_ = type_ , file_content=filee ,dev=dev)
            data_to_return = returned[0]
            columns_ = returned[1]
            rule = save_application(data_to_return,type_,file_name)
            rules.append(rule)
    else:
        returned =  retrive_configurations(type_ = type_ , file_content=file_content ,dev=dev)
        data_to_return = returned[0]
        columns_ = returned[1]
        rules = save_application(data_to_return,type_,file_name)
    sheet_name_ = 'Applications'
    sheet_data1  = {
    'sheet_name': sheet_name_,
    'data': rules,
    'columns': columns_
    } 
    return sheet_data1
    
def application_set_def(type_ = None , file_content=None ,dev=None,file_name=None,x=None):
    rules = []
    if x != None:
        for filee in x:
            returned =  retrive_configurations(type_ = type_ , file_content=filee ,dev=dev)
            data_to_return = returned[0]
            columns_ = returned[1]
            rule = save_application_set(data_to_return,type_,file_name)
            rules.append(rule)
    else:
        returned =  retrive_configurations(type_ = type_ , file_content=file_content ,dev=dev)
        data_to_return = returned[0]
        columns_ = returned[1]
        rules = save_application_set(data_to_return,type_,file_name)
    sheet_name_ = 'APP_Groups'
    sheet_data1  = {
    'sheet_name': sheet_name_,
    'data': rules,
    'columns': columns_
    }   
    return sheet_data1


def save_excel(type_=None,word_to_find=None,cu=None, dev=None, file_content=None,file_name=None,onlyData=None):
    
    
    if type_ == 'select-node':
        sheet_data_address = []
        empty = []
        # for x in file_content:
            # sheet_data1.append(policy_def(type_ = 'policy' , file_content=x ,dev=dev,file_name=file_name))
        # logical_policy = logical_policy_def(type_ = 'logical_policy' , file_content=file_content ,dev=dev,file_name=file_name,x='y')
        for x,y in zip(file_content,file_name):
            empty = address_def(type_ = 'address' , file_content=x ,dev=dev,file_name=y)
            sheet_data_address.append(empty)
            empty = []
        # address_set = address_set_def(type_ = 'address-set' , file_content=file_content ,dev=dev,file_name=file_name,x='y')
        # application = application_def(type_ = 'application' , file_content=file_content ,dev=dev,file_name=file_name,x='y')
        # application_set = application_set_def(type_ = 'application-set' , file_content=file_content ,dev=dev,file_name=file_name,x='y')
        # sheet_data1 = [policy]
        excel_output.extract_excel(sheet_data_address,file_name)
        
    if type_ == 'all-configuration':
        policy = policy_def(type_ = 'policy' , file_content=file_content ,dev=dev,file_name=file_name)
        logical_policy = logical_policy_def(type_ = 'logical_policy' , file_content=file_content ,dev=dev,file_name=file_name)
        address = address_def(type_ = 'address' , file_content=file_content ,dev=dev,file_name=file_name)
        address_set = address_set_def(type_ = 'address-set' , file_content=file_content ,dev=dev,file_name=file_name)
        application = application_def(type_ = 'application' , file_content=file_content ,dev=dev,file_name=file_name)
        application_set = application_set_def(type_ = 'application-set' , file_content=file_content ,dev=dev,file_name=file_name)
        sheet_data1 = [address,address_set,application,application_set,policy,logical_policy]
        excel_output.extract_excel(sheet_data1,file_name)
        
    if type_ == 'policy':
        sheet_data1 = policy_def(type_ = type_ , file_content=file_content ,dev=dev,onlyData=onlyData)
        if onlyData != None:
            return sheet_data1
        else:
            sheet_na = sheet_data1['sheet_name']
            name= f'{file_name} {sheet_na}'
            excel_output.extract_excel([sheet_data1],name)
        
    if type_ == 'logical_policy':
        sheet_data1 = logical_policy_def(type_ = type_ , file_content=file_content ,dev=dev)
        sheet_na = sheet_data1['sheet_name']
        name= f'{file_name} {sheet_na}'
        excel_output.extract_excel([sheet_data1],name)
        
    if type_ == 'address':
        sheet_data1 = address_def(type_ = type_ , file_content=file_content ,dev=dev,file_name=file_name)
        sheet_na = sheet_data1['sheet_name']
        name= f'{file_name} {sheet_na}'
        excel_output.extract_excel([sheet_data1],name)
        
    if type_ == 'address-set':
        sheet_data1 = address_set_def(type_ = type_ , file_content=file_content ,dev=dev,file_name=file_name)
        sheet_na = sheet_data1['sheet_name']
        name= f'{file_name} {sheet_na}'
        excel_output.extract_excel([sheet_data1],name)
    if type_ == 'application':
        sheet_data1 = application_def(type_ = type_ , file_content=file_content ,dev=dev,file_name=file_name)
        sheet_na = sheet_data1['sheet_name']
        name= f'{file_name} {sheet_na}'
        excel_output.extract_excel([sheet_data1],name)
    
    if type_ == 'application-set':
        sheet_data1 = application_set_def(type_ = type_ , file_content=file_content ,dev=dev,file_name=file_name)
        sheet_na = sheet_data1['sheet_name']
        name= f'{file_name} {sheet_na}'
        excel_output.extract_excel([sheet_data1],name)
    
    
    


  
def matchs(match_me, each_line):
    match_results = {
        'match_system_name': re.search(r' logical-systems\s+(.*?)\s+security policies ', each_line),
        'match_system': re.search(r' logical-systems (.*?) ', each_line),
        'match_global_zone': re.search(r' policies\s+(.*?)\s+policy ', each_line),
        'match_from_zone': re.search(r' from-zone\s+(.*?)\s+to-zone ', each_line),
        'match_to_zone': re.search(r' to-zone\s+(.*?)\s+policy ', each_line),
        'match_policy_name': re.search(r' policy\s+(.*?)\s+', each_line),
        'match_address_des': re.search(r' address (.*?) description (.*?)$', each_line),
        'match_address_name': re.search(r' address (.*?) ', each_line),
        'match_address_range_ip': re.search(r' address (.*?) range-address (.*?) to (.*?)$', each_line),
        'match_address_ip': re.search(r' address (.*?) (.*?)$', each_line),
        'match_dns_address': re.search(r'dns-name (.*?)$', each_line),
        'match_address_set_name': re.search(r' address-set (.*?) address (.*?)$', each_line),
        'match_address_set_set_name': re.search(r' address-set (.*?) address-set (.*?)$', each_line),
        'match_application': re.search(r' applications application (.*?) (.*?) (.*?)$', each_line),
        'match_application_set_name': re.search(r' applications application-set (.*?) application (.*?)$', each_line),
        
        }
    return match_results.get(match_me)





def application_set_type(data_to_return,type_,file_name):
    context = []
    for each_line in data_to_return:
        match_system = matchs('match_system',each_line)
        match_application_set_name = matchs('match_application_set_name', each_line)
        if match_system:
            context.append([match_application_set_name.group(1), match_application_set_name.group(2),match_system.group(1),file_name])
        else:
            context.append([match_application_set_name.group(1), match_application_set_name.group(2),'T-Cloud', file_name])  
    return context

def application_type(data_to_return,type_,file_name):
    context = []
    for each_line in data_to_return:
        match_system = matchs('match_system',each_line)
        match_application = matchs('match_application',each_line)
        while True:
            if match_system:
                match_system_var = match_system.group(1)
            else:
                match_system_var = 'T-Cloud'
               
            found_lists = [lst for lst in context if lst[1] == match_application.group(1) and lst[5] == match_system_var]
            if not(found_lists):
                context.append(['',match_application.group(1),'','','','',match_system_var,''])
                if match_system_var == 'T-Cloud':
                    context[-1][5] ='T-Cloud'
                    if not(file_name in context[-1][7]):
                        context[-1][7] = file_name
                else:
                    context[-1][5] = match_system_var
                    if not(file_name in context[-1][7]):
                        context[-1][7] =file_name
            else:
                if match_application.group(2) == 'description':
                    context[-1][2] =match_application.group(3)
                    break
                elif match_application.group(2) == 'protocol':
                    context[-1][3] =match_application.group(3)
                    break
                elif match_application.group(2) == 'source-port':
                    context[-1][4] =match_application.group(3)
                    break
                elif match_application.group(2) == 'destination-port':
                    if re.match(r'\d-\d', match_application.group(3)):
                        context[-1][0] = 'Application Range'
                    else:
                        context[-1][0] = 'Application'
                    context[-1][5] =match_application.group(3)
                    break
    return context
    
def address_set_type(data_to_return,type_,file_name):
    context = []
    for each_line in data_to_return:
        match_system = matchs('match_system',each_line)
        match_address_set_name = matchs('match_address_set_name', each_line)
        match_address_set_set_name = matchs('match_address_set_set_name', each_line)
        if match_system:
            if match_address_set_name:
                context.append(['address-set',match_address_set_name.group(1),'address', match_address_set_name.group(2),match_system.group(1),file_name])
                continue
            if match_address_set_set_name:
                context.append(['address-set',match_address_set_set_name.group(1),'address-set', match_address_set_set_name.group(2),match_system.group(1),file_name])
                continue
        else:
            if match_address_set_name:
                context.append(['address-set',match_address_set_name.group(1),'address',match_address_set_name.group(2), 'T-Cloud',file_name])
                continue
            if match_address_set_set_name:
                context.append(['address-set',match_address_set_set_name.group(1),'address-set',match_address_set_set_name.group(2), 'T-Cloud',file_name])
                continue
                
    return context
def address_type(data_to_return,type_,file_name):
    context = []
    for each_line in data_to_return:
        match_system = matchs('match_system',each_line)
        match_address_des = matchs('match_address_des',each_line)
        match_address_name = matchs('match_address_name', each_line)
        match_address_ip = matchs('match_address_ip', each_line)
        match_address_range_ip = matchs('match_address_range_ip', each_line)
        while True:
            if match_system:
                match_system_var = match_system.group(1)
            else:
                match_system_var = 'T-Cloud'
                
            found_lists = [lst for lst in context if lst[1] == match_address_name.group(1) and lst[5] == match_system_var]
            if not(found_lists):
                context.append(['',match_address_name.group(1),'','','',match_system_var,''])
                if match_system_var == 'T-Cloud':
                    context[-1][5] ='T-Cloud'
                    
                    if not(file_name in context[-1][6]):
                        context[-1][6] = file_name
                else:
                    context[-1][5] = match_system_var
                    if not(file_name in context[-1][6]):
                        context[-1][6] =file_name
            else:
                
                if match_address_des:
                    context[-1][2] =match_address_des.group(2)
                    break
                if match_address_ip:
                    if not('range-address' in match_address_ip.group(2)):
                        if 'dns-name ' in match_address_ip.group(2):
                            match_dns_address = matchs('match_dns_address', match_address_ip.group(2))
                            context[-1][0] = 'DNS Address'
                            context[-1][3] = match_dns_address.group(1)
                            break
                        context[-1][0] = 'Address'
                        context[-1][3] =match_address_ip.group(2)
                        break
                    elif 'range-address' in match_address_ip.group(2):
                        context[-1][0] = 'Address Range'
                        context[-1][3] =match_address_range_ip.group(2)
                        context[-1][4] =match_address_range_ip.group(3)
                        break   

    return context
    
def zone_type_normal_policy(data_to_return):
    context = []
    for each_line in data_to_return:
        match_global_zone = matchs('match_global_zone',each_line)
        match_from_zone = matchs('match_from_zone', each_line)
        match_to_zone = matchs('match_to_zone', each_line)
        match_policy_name = matchs('match_policy_name', each_line)
        if match_from_zone:
            if not(['zone-based',match_from_zone.group(1),match_to_zone.group(1),match_policy_name.group(1)] in context):
                context.append(['zone-based',match_from_zone.group(1),match_to_zone.group(1),match_policy_name.group(1)])
        elif match_global_zone:
            if not([match_global_zone.group(1),'-','-',match_policy_name.group(1)] in context):
                context.append([match_global_zone.group(1),'-','-',match_policy_name.group(1)])
    return context



def zone_type_logical_policy(data_to_return):
    context = []
    for each_line in data_to_return:
        match_system_name = matchs('match_system_name',each_line)
        match_global_zone = matchs('match_global_zone',each_line)
        match_from_zone = matchs('match_from_zone', each_line)
        match_to_zone = matchs('match_to_zone', each_line)
        match_policy_name = matchs('match_policy_name', each_line)
        if match_from_zone:
            if not([match_system_name.group(1),'zone-based',match_from_zone.group(1),match_to_zone.group(1),match_policy_name.group(1)] in context):
                context.append([match_system_name.group(1),'zone-based',match_from_zone.group(1),match_to_zone.group(1),match_policy_name.group(1)])
        elif match_global_zone:
            if not([match_system_name.group(1),match_global_zone.group(1),'-','-',match_policy_name.group(1)] in context):
                context.append([match_system_name.group(1),match_global_zone.group(1),'-','-',match_policy_name.group(1)])   
    return context


def policy_type(data_to_return,type_):
    if type_ == 'policy':
        context =  zone_type_normal_policy(data_to_return)
        return [context,0]
        
    if type_ == 'logical_policy':
        context =  zone_type_logical_policy(data_to_return)
        return [context,1]  

def append_policy(data_to_return,type_,context,t):

    for each_line in data_to_return:
        match_system_name = matchs('match_system_name',each_line)
        match_global_zone = matchs('match_global_zone',each_line)
        match_from_zone = matchs('match_from_zone', each_line)
        match_to_zone = matchs('match_to_zone', each_line)
        match_policy_name = matchs('match_policy_name', each_line)
        c = 0
        for each_list in context:

            if match_from_zone:
                if each_list[t] == 'zone-based' and each_list[t+1] == match_from_zone.group(1) and each_list[t+2] == match_to_zone.group(1) and each_list[t+3] == match_policy_name.group(1):
                    
                    if ' match source-address ' in each_line:
                    
                        src_address = re.search(r' match source-address\s+(.*?)$', each_line)
                        
                        context[c][t+4] += src_address.group(1) + '\n'
                        
                    
                    if ' match destination-address ' in each_line:
                        
                        dst_address = re.search(r' match destination-address\s+(.*?)$', each_line)
                        
                        context[c][t+5] += dst_address.group(1) + '\n'
                    
                    if ' match application ' in each_line:
                        
                        app = re.search(r' match application\s+(.*?)$', each_line)
                        
                        context[c][t+6] += app.group(1) + '\n'
                        
                    if ' match dynamic-application ' in each_line:
                        
                        dyn_app = re.search(r' match dynamic-application\s+(.*?)$', each_line)
                        
                        context[c][t+7] += dyn_app.group(1) + '\n'
                        
                    if ' match url-category ' in each_line:
                        
                        url = re.search(r' match url-category\s+(.*?)$', each_line)
                        
                        context[c][t+8] += url.group(1) + '\n'
               
                    if ' then' in each_line:
                        if ' then log' in each_line:
                        
                            log_ = re.search(r' then log\s+(.*?)$', each_line)
                            
                            context[c][t+11] = log_.group(1)
                        
                        else:
                            
                            after_then = re.search(r' then\s+(.*?)$', each_line)
                            
                            
                            if 'application-services' in after_then.group(1):
                            
                                act = re.search(r' then\s+(.*?)\s+application-services', each_line)
                                
                                context[c][t+9] = act.group(1) + '\n'
                                
                                app_services = re.search(r' application-services\s+(.*?)$', each_line)
                    
                                context[c][t+10] = app_services.group(1)
                            
                            else:
                            
                                act = re.search(r' then\s+(.*?)$', each_line)
                                
                                context[c][t+9] += act.group(1) + '\n'
            
            
            elif match_global_zone:
                if each_list[t+0] == match_global_zone.group(1) and each_list[t+3] == match_policy_name.group(1):
                    if ' match source-address ' in each_line:
                    
                        src_address = re.search(r' match source-address\s+(.*?)$', each_line)
                        
                        context[c][t+4] += src_address.group(1) + '\n'
                        
                    
                    if ' match destination-address ' in each_line:
                        
                        dst_address = re.search(r' match destination-address\s+(.*?)$', each_line)
                        
                        context[c][t+5] += dst_address.group(1) + '\n'
                    
                    if ' match application ' in each_line:
                        
                        app = re.search(r' match application\s+(.*?)$', each_line)
                        
                        context[c][t+6] += app.group(1) + '\n'
                        
                    if ' match dynamic-application ' in each_line:
                        
                        dyn_app = re.search(r' match dynamic-application\s+(.*?)$', each_line)
                        
                        context[c][t+7] += dyn_app.group(1) + '\n'
                        
                    if ' match url-category ' in each_line:
                        
                        url = re.search(r' match url-category\s+(.*?)$', each_line)
                        
                        context[c][t+8] += url.group(1) + '\n'
               
                    if ' then' in each_line:
                        if ' then log' in each_line:
                        
                            log_ = re.search(r' then log\s+(.*?)$', each_line)
                            
                            context[c][t+11] = log_.group(1)
                        
                        else:
                            
                            after_then = re.search(r' then\s+(.*?)$', each_line)
                            
                            
                            if 'application-services' in after_then.group(1):
                            
                                act = re.search(r' then\s+(.*?)\s+application-services', each_line)
                                
                                context[c][t+9] = act.group(1) + '\n'
                                
                                app_services = re.search(r' application-services\s+(.*?)$', each_line)
                    
                                context[c][t+10] = app_services.group(1)
                            
                            else:
                            
                                act = re.search(r' then\s+(.*?)$', each_line)
                                
                                context[c][t+9] += act.group(1) + '\n'
        
            c+=1
    return context




def save_policy(data_to_return,type_):
    
    returned_list = policy_type(data_to_return,type_)
    context = returned_list[0]
    t = returned_list[1]
    for x in context:
            for y in range(1,9):
                x.append('')
    
    return append_policy(data_to_return,type_,context,t)
    
def save_address(data_to_return,type_,file_name):    
    rules = address_type(data_to_return,type_,file_name)
    return rules
    
    
def save_address_set(data_to_return,type_,file_name):   
    rules = address_set_type(data_to_return,type_,file_name)
    return rules
def save_application(data_to_return,type_,file_name):
    rules = application_type(data_to_return,type_,file_name)
    return rules
def save_application_set(data_to_return,type_,file_name):   
    rules = application_set_type(data_to_return,type_,file_name)
    return rules
    
def retrive_configurations(type_ = None, word_to_find = None,is_exist = 'return as list', file_content = None, dev = None):

    data_to_return = []
    
    tempelte_to_find = retrive_tempeletes(type_,word_to_find)[0]
    
    filter_ = retrive_tempeletes(type_,word_to_find)[1]
    
    columns_ = retrive_tempeletes(type_,word_to_find)[2]
    
    if dev != None: # for netconf

        data = dev.rpc.get_config(options={'format':'set'},filter_xml=filter_)
        
        retrived__data = etree.tostring(data, encoding='unicode', pretty_print=True)
        
        retrived_data = [line.strip() for line in retrived__data.strip().split('\n')]
        
        retrived_data.pop()
        
        retrived_data.pop(0)
        file_content = retrived_data
        
    if is_exist == 'yes':
    
        for each_line in file_content:
        
            if re.search(tempelte_to_find, each_line): return True
            
        return False
        
    else:

        for each_line in file_content:
        
            if re.search(tempelte_to_find, each_line):
                
                data_to_return.append(each_line)
            
        return [data_to_return,columns_]

    
def retrive_tempeletes(type_,word_to_find_=None):

    if type_ == 'policy':
    
        match = r'set security policies '
        
        filter_ = 'security/policies'
        
        columns_ = ['Zone Type','From Zone','To Zone', 'Policy Name', 'Source Address', 'Destination Address' ,'Application','Dynamic Application','URL Category','Action','Application Services','Log']

        return [match,  filter_,columns_]
        
    if type_ == 'logical_policy':
    
        match = r'set logical-systems .* security policies '
        
        filter_ = 'security/policies'
        
        columns_ = ['System Name','Zone Type','From Zone','To Zone', 'Policy Name', 'Source Address', 'Destination Address' ,'Application','Dynamic Application','URL Category','Action','Application Services','Log']

        return [match,  filter_,columns_]    
    if type_ == 'address':
    
        match = r' security address-book global address '
        
        filter_ = 'security/address-book'
        
        columns_ = ['Type','Address Name', 'Address Description', 'Address Value', 'End Address Range' ,'Location', 'Model']

        return [match,  filter_,columns_] 
        
    if type_ == 'address-set':
    
        match = r' security address-book global address-set '
        
        filter_ = 'security/address-book'
        
        columns_ = ['Address Type','Group Name','Group Members','Address Type','Location', 'Model']

        return [match,  filter_,columns_] 
        
    if type_ == 'application':
    
        match = r' applications application '
        
        filter_ = 'applications'
        
        columns_ = ['Type','Service_Name','Service_Description','Service_Protocol', 'Service_Src-Port', 'Service_DST-Port', 'Location', 'Model']

        return [match,  filter_,columns_] 
        
    if type_ == 'application-set':
    
        match = r' applications application-set '
        
        filter_ = 'applications'
        
        columns_ = ['APP_Group_Name','APP_Group_Members','Location', 'Model']

        return [match,  filter_,columns_]         
    
    
 





