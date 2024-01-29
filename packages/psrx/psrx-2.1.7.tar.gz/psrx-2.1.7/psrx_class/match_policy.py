from psrx_class import save_excel_def

def get_configured_policy(file_content=None):
    data = save_excel_def.save_excel(type_='policy',file_content=file_content, file_name='no name',onlyData='data')
    return data


#['zone-based', 'Management_Platform_FW', 'DC_FW_to_ACI_North-South',
#  'AV_UTL_DNS_Access1',
#  'Avamar_Vault\nAvamar_Vault_ADM\n',
#  'DNS\n', 'TCP_53\nUDP_53\njunos-icmp-all\n',
#  'any\n', 'none\n', 'permit\ncount\n', 'idp-policy Recommended', 'session-close']

def get_all_policies(dev=None,file_content=None):
    all_policies = get_configured_policy(file_content=file_content)
    add = {
        'Avamar_Vault':'192'
    }

    source = input('Source : ')
    destination = input('Destination : ')
    app = input('Application : ')

    