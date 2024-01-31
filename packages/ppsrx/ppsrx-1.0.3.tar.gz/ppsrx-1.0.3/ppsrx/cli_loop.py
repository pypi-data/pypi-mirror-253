from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
import re
import devices
import _configurations_
import save_excel_def
import _main_functions_
import match_policy
from jnpr.junos.utils.config import Config
from logger_config import setup_logging
import logging

# Call the setup_logging function from logger_config
setup_logging()

module_name = __name__.split('.')[-1]


class hierarchy: # A hierarchy for commands


    def Crossroad(self):
        # Define a hierarchy of commands using a nested completer.
        completer = NestedCompleter.from_nested_dict({
            'local': None,
            'netconf': None,
            'exit': None,
        })
        
        return completer

    def local(self):

        _Backups_files = devices.loacls_Backup()

        completer_local = NestedCompleter.from_nested_dict({})

        completer_local_dict = {}
        
        for item in _Backups_files:
            completer_local_dict[item] = None
        
        completer_local_dict['return'] = None
        
        completer_local = NestedCompleter.from_nested_dict(completer_local_dict)
        
        return completer_local


    def netconf(self):
        
        FW_name = []
        FW_info = []
        
        for key, value in devices.FWs.items():
            FW_name.append(key)
            FW_info.append(value)

        completer_netconf = NestedCompleter.from_nested_dict({})

        completer_netconf_dict = {}

        for item in FW_name:
            completer_netconf_dict[item] = None

        
        completer_netconf_dict['return'] = None
        
        completer_netconf = NestedCompleter.from_nested_dict(completer_netconf_dict)
        
        return completer_netconf
            
    def commands(self):   
        completer_netconf_fw = NestedCompleter.from_nested_dict({
            'push': {
            'policy': None,
            'full-set-commands': None,
            'address': None,
            'application': None,
            },
            'get': {
             'match-policies':None,
            },
            'show': {
            'address': {
            'ip': None,
            'zone': None,
            'interface': None,
            },
            'application': None,
            },
            'save-as-excel': {
            'all-configuration': {
            'select-node':None
            },
            'policies': None,
            'logical-policy': None,
            'address': None,
            'address-set': None,
            'application': None,
            'application-set': None,
            },
            'close-session': None,
        })
        
        return completer_netconf_fw
            
            
# Define a function to handle the user's input.

def select_multi_FW(ff):
    coms_obj = hierarchy()
    files_contents = []
    files_name = []
    try:
        files_content = devices.open_local_backup_file(ff)
    except Exception as e:
        print(f"Invalid command: {ff}")
        
    files_contents.append(files_content)
    files_name.append(ff)
    #choosing file name     
    while True:
        uf = prompt(' > ',completer=coms_obj.local()).strip()
        if re.match(uf,r'\s+$'):
                break
        elif re.match(uf,r'return$'):
                return 'return' 
                
        files_content = devices.open_local_backup_file(uf)
        
        if not(files_content in files_contents):
            files_contents.append(files_content)
            files_name.append(uf)
        else:
            print(f' !> {uf} Already added.')
            continue
        
    return [files_contents,files_name]
def netconf(mode):
    coms_obj = hierarchy()
    logging.debug(f' {module_name} This is a debug message in some_module')
    logging.info(f' {module_name} This is an info message in some_module')
    while True:
        
        if mode == 'netconf' :
            # Cridential as list for the selected device [option,'192.168.1.201','root','Password']
            cri = devices.netconf() 
            
            # open a connection with the device and start a NETCONF session
            if len(cri) == 4:
                cridential_as_list = [cri[1],cri[2],cri[3]]
                netconf_name = f'{cri[0]}@{cri[2]}'
            elif len(cri) == 3:
                cridential_as_list = cri
                netconf_name = cri[1]
            dev = _main_functions_.open_session(cridential_as_list)
            
            if dev == 'retry':continue
                        
            # make an object from configuration utility
            cu = Config(dev, mode='private')
            
            uf = prompt(f'CLI > {mode} > {netconf_name} >').strip()
                
        elif mode == 'local':
                
            #choosing file name
            uf = prompt(f'CLI > {mode} >', completer=coms_obj.local()).strip()

        if uf == 'return': return 'return' 
        
        #intialize session
        if uf != 'return':
        
 
            if mode == 'local':
                
                try:
                
                    file_content = devices.open_local_backup_file(uf)
                
                except Exception as e:
                    print(f"Invalid command: {uf}")
                    continue
            
        while True:

            #choosing commands
            u_c_f_n3 = prompt(f'CLI > {mode} > {uf} >', completer=coms_obj.commands()).strip()
            
            #push policy
            if re.match(r'push\s+policy$',u_c_f_n3):
                if mode == 'netconf' :
                    if _configurations_.load_policy(cu,dev): continue
                elif mode == 'local':
                    if _configurations_.load_policy(file_content=file_content): continue
                    continue
                    
            #push full-set-commands
            if re.match(r'push\s+full-set-commands$',u_c_f_n3):
                if mode == 'netconf':
                    if _configurations_.load_full_set_commands(cu): continue
                elif mode == 'local':
                    print('THIS COMMAND NOT CONFIGURED YET.')
                    continue
                
            #push address
            if re.match(r'push\s+address$',u_c_f_n3):
                if mode == 'netconf' :
                    if _configurations_.load_adresses(cu,dev): continue
                elif mode == 'local':
                    if _configurations_.load_adresses(file_content=file_content): continue
                    continue
                
            #push application
            if re.match(r'push\s+application$',u_c_f_n3):
                if mode == 'netconf' :
                    if _configurations_.load_application(cu,dev): continue
                elif mode == 'local':
                    if _configurations_.load_application(file_content=file_content): continue
                    continue

             #get match-policies
            if re.match(r'get\s+match-policies$',u_c_f_n3):
                if mode == 'netconf' :
                    if match_policy.get_all_policies(dev=dev): continue
                elif mode == 'local':
                    if match_policy.get_all_policies(file_content=file_content): continue
                    continue
                    
            #show address ip
            if re.match(r'show\s+address\s+ip$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    print('THIS COMMAND NOT CONFIGURED YET.')
                    continue
                    
            #show address zone
            if re.match(r'show\s+address\s+zone$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    print('THIS COMMAND NOT CONFIGURED YET.')
                    continue
                    
            #show address interface
            if re.match(r'show\s+address\s+interface$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    print('THIS COMMAND NOT CONFIGURED YET.')
                    continue
                    
            #show application
            if re.match(r'show\s+application$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    print('THIS COMMAND NOT CONFIGURED YET.')
                    continue
                    
            #save-as-excel all-configuration select-node
            if re.match(r'save-as-excel\s+all-configuration\s+select-node$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT AVILABLE FOR NETCONF TRY WITHOUT select-node ')
                elif mode == 'local':
                    print('THIS COMMAND NOT CONFIGURED YET.')
                    files_contents = select_multi_FW(uf)
                    # if files_contents != 'return':
                        # if save_excel_def.save_excel(type_='select-node',file_content=files_contents[0],file_name=files_contents[1]): continue
                        # continue
                    # else:
                        # continue
                    
            #save-as-excel all-configuration
            if re.match(r'save-as-excel\s+all-configuration$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    if save_excel_def.save_excel(type_='all-configuration',file_content=file_content,file_name=uf): continue
                    continue
            
            #save-as-excel policies
            if re.match(r'save-as-excel\s+policies$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    if save_excel_def.save_excel(type_='policy',file_content=file_content,file_name=uf): continue
                    continue
                    
            #save-as-excel policies
            if re.match(r'save-as-excel\s+logical-policy$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    if save_excel_def.save_excel(type_='logical_policy',file_content=file_content,file_name=uf): continue
                    continue
                    
            #save-as-excel address
            if re.match(r'save-as-excel\s+address$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    if save_excel_def.save_excel(type_='address',file_content=file_content,file_name=uf): continue
                    continue
                    
            #save-as-excel address-set
            if re.match(r'save-as-excel\s+address-set$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    if save_excel_def.save_excel(type_='address-set',file_content=file_content,file_name=uf): continue
                    continue
            
            #save-as-excel application
            if re.match(r'save-as-excel\s+application$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    if save_excel_def.save_excel(type_='application',file_content=file_content,file_name=uf): continue
                    continue
                    
            #save-as-excel application-set
            if re.match(r'save-as-excel\s+application-set$',u_c_f_n3):
                if mode == 'netconf' :
                    print('THIS COMMAND NOT CONFIGURED YET.')
                elif mode == 'local':
                    if save_excel_def.save_excel(type_='application-set',file_content=file_content,file_name=uf): continue
                    continue
                    
            #close-session
            if re.match(r'close-session$',u_c_f_n3):
                if mode == 'netconf' :
                    _main_functions_.session_close(dev)
                break

            else:
                print(f"Invalid command: {u_c_f_n3}")
    

def exiting():
    print("Exiting the CLI.")
    return 'exit'  # Exit the CLI loop    
    
def handle_input(text):

        if text.strip() == 'exit':
            return exiting()
        
        
        elif text.strip() == 'local':
            return netconf('local')
        
        
        elif text.strip() == 'netconf':
            return netconf('netconf')
            
        else:
           print(f"Invalid command: {text}")


    
def main_cli_loop():
    while True:
        main_com = hierarchy()
        
        user_input = prompt('CLI> ', completer=main_com.Crossroad())
        
        main_input = handle_input(user_input)
        if main_input == 'exit':
            break
        

    