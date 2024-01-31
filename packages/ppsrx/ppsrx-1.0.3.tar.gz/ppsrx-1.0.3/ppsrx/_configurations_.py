import load_full_set_configurations
import _main_functions_
import re
import all_applications_type
import all_policy_type
import all_address_type
from lxml import etree
import clipboard
from termcolor import colored


def load_policy(cu=None,dev=None,file_content=None):
    print('►►►►►►►►►►►►►►►►► MAKE SURE THE Policies IN THE CLIPBOARD ◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄')
    input('Press any key to continue...')
    print('▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼ Paste your set commands ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼')
    lines = clipboard.paste()

    
    get_set_commands = lines.strip().split('\n')   

    result = [line.replace('\r','').split('\t') for line in get_set_commands]
    for x in result:print(x)
    print(f'▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲           Count = {len(result)}           ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲')
    user_agrees = input('type y to continue : ')
    if user_agrees.lower() == 'y':
        
        #list_of_list = [commands, invalid_application_set, application_description,valid_application_count]

        list_of_list = all_policy_type.policy_set( result,dev=dev,file_content=file_content)
    else:
        return True
    
            
    if len(list_of_list[0]) > 0:
        print(g('▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼  ') + y('Valid Commands.') + g('  ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼'))
        for c in list_of_list[0]:
            print(c)
        print(g('▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲  ') + y('End of Valid Commands.') + g('  ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲'))
    
    
    if dev != None :
        pushing(cu,list_of_list[0],list_of_list[1])

    return True

def load_application(cu=None,dev=None,file_content=None):
    print('►►►►►►►►►►►►►►►►► MAKE SURE THE COMMANDS IN THE CLIPBOARD ◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄')
    input('Press any key to continue...')
    print('▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼ Paste your set commands ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼')
    lines = clipboard.paste()
    get_set_commands = lines.strip().split('\n')
    get_set_commands = [element.replace('\r', '').strip() for element in get_set_commands]
    for x in get_set_commands:print(x)
    print(f'▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲           Count = {len(get_set_commands)}           ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲')
    user_agrees = input('type y to continue : ')
    if user_agrees.lower() == 'y':
        
        #list_of_list = [commands, invalid_application_set, application_description,valid_application_count]
        list_of_list = all_applications_type.application_applications_set(dev, lines,file_content=file_content)
    else:
        return True
    if list_of_list[3] > 0:
        print(f'********************* Valid Application. Count : {list_of_list[3]} *********************')
        for c in list_of_list[0]:
            print(c)
            
    if len(list_of_list[1]) > 0: 
        print(f'********************* Invalid Application. Count : {len(list_of_list[1])} *********************')
        for c in list_of_list[1]:
            print(c)
            
    if len(list_of_list[4]) > 0:     
        print(f'********************* Duplicated Input. Count : {len(list_of_list[4])} *********************')
        for c in list_of_list[4]:
            print(c)
            
    if len(list_of_list[5]) > 0:     
        print(f'********************* Already Excisted. Count : {len(list_of_list[5])} *********************')
        for c in list_of_list[5]:
            print(c)
    
    
    if dev != None :
        pushing(cu,list_of_list[0],list_of_list[2])

    return True



def load_adresses(cu=None,dev=None,file_content=None):
    print('►►►►►►►►►►►►►►►►► MAKE SURE THE COMMANDS IN THE CLIPBOARD ◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄')
    input('Press any key to continue...')
    print('▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼ Paste your set commands ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼')
    lines = clipboard.paste()
    get_set_commands = lines.strip().split('\n')
    get_set_commands = [element.replace('\r', '').strip() for element in get_set_commands]
    for x in get_set_commands:print(x)
    print(f'▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲           Count = {len(get_set_commands)}           ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲')
    user_agrees = input('type y to continue : ')
    if user_agrees.lower() == 'y':
        #list_of_list = [commands, wrong_inputs, invalid_range, invalid_address_set, address_description]
        list_of_list = all_address_type.address_address_set(dev, lines,file_content)
    else:
        return True
    if len(list_of_list[0]) > 0:         
        print(f'********************* Valid Commands Count : {len(list_of_list[0])} *********************')
        for c in list_of_list[0]:
            print(c)
      
    if len(list_of_list[1]) > 0:         
        print(f'********************* Wrong Inputs Count : {len(list_of_list[1])} *********************')
        for c in list_of_list[1]:
            print(c)
        
    if len(list_of_list[2]) > 0:         
        print(f'********************* Invalid Range Count : {len(list_of_list[2])} *********************')
        for c in list_of_list[2]:
            print(c)
        
    if len(list_of_list[3]) > 0:         
        print(f'********************* Invalid Address Set Count : {len(list_of_list[3])} *********************')
        for c in list_of_list[3]:
            print(c)
        
    if len(list_of_list[5]) > 0:     
        print(f'********************* Duplicated Input. Count : {len(list_of_list[5])} *********************')
        for c in list_of_list[5]:
            print(c)
            
    if len(list_of_list[6]) > 0:     
        print(f'********************* Already Excisted. Count : {len(list_of_list[6])} *********************')
        for c in list_of_list[6]:
            print(c)    
            
    if len(list_of_list[7]) > 0:     
        print(f'********************* The IP Already Excisted In Configuration. Count : {int(len(list_of_list[7])/2)} *********************')
        for c in list_of_list[7]:
            print(c)
    
    if len(list_of_list[8]) > 0:     
        print(f'********************* The Same IP You Paste Twice. Count : {len(list_of_list[8])} *********************')
        for c in list_of_list[8]:
            print(c)
            
    if dev != None :
        pushing(cu,list_of_list[0],list_of_list[4])
    
    
    return True
        
        
    
    
        
    
    
                
                
                
def load_full_set_commands(cu):
        print('►►►►►►►►►►►►►►►►► MAKE SURE THE COMMANDS IN THE CLIPBOARD ◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄')
        input('Press any key to continue...')
        print('▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼ Paste your set commands ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼')
        lines = clipboard.paste()
        get_set_command = lines.strip().split('\n')
        get_set_commands = [element.replace('\r', '').strip() for element in get_set_command]
        for x in get_set_commands:print(x)
        print(f'▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲           Count = {len(get_set_commands)}           ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲')
        user_agrees = input('type y to continue : ')
        if user_agrees.lower() == 'y':
            load_full_set_configurations.load_list_set_configurations(cu,get_set_commands) #loading the conf
        else:
            return True
        
        _main_functions_.commit_check(cu)
        
        _main_functions_.commit(cu)
        
        return True


def pushing(cu, configuration_list, configuration_decription):
    user_agrees = input('type y to continue : ')
    if user_agrees.lower() != 'y':return True  
    
    load_full_set_configurations.load_list_set_configurations(cu,configuration_list)
    
    _main_functions_.commit_check(cu)
    
    _main_functions_.commit(cu,configuration_decription)
    
    
    
    
def retrive_configurations(type_, word_to_find, is_exist = 'return as list', file_content = None, dev = None):

    data_to_return = []
    
    tempelte_to_find = re.sub(r'\x1b\[[0-9;]+m\x1b\[[0-9;]+m|\x1b\[[0-9;]+m', '', retrive_tempeletes(type_,word_to_find)[0]) 
    
    filter_ = retrive_tempeletes(type_,word_to_find)[1]
    
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
    
        for x in file_content:
            each_line = re.sub(r'\x1b\[[0-9;]+m\x1b\[[0-9;]+m|\x1b\[[0-9;]+m', '', x)
            if re.search(tempelte_to_find, each_line):

                data_to_return.append(each_line)
            
        return data_to_return


def retrive_tempeletes(type_,word_to_find_):

    if type_ == 'address':
        pattern = r'security address-book global address {} '.format(word_to_find_)
        return [pattern,  'security/address-book']

    if type_ == 'address-set':
        pattern = r'security address-book global address-set {} address {}'.format(word_to_find_[0],word_to_find_[1])
        return [pattern,  'security/address-book']
    
    if type_ == 'address-ip': 
        pattern = r'security address-book global address .* {}'.format(word_to_find_)
        return [pattern,  'security/address-book']
        
    if type_ == 'address-range-ip':
        pattern = r'security address-book global address .* range-address {} to {}'.format(word_to_find_[0],word_to_find_[1])
        return [pattern,  'security/address-book']
    
    if type_ == 'Tcloud_policy_address-set':
        pattern = r'set security address-book global address-set {} address (.*?)$'.format(word_to_find_)
        return [pattern,  'security/address-book']
    
    if type_ == 'Tcloud_policy_address': 
        pattern = r'set security address-book global address {} (.*?)$'.format(word_to_find_)
        return [pattern,  'security/address-book']
    
    if type_ == 'Tcloud_policy_app-set':
        pattern = r'set applications application-set {} application (.*?)$'.format(word_to_find_)
        return [pattern,  'applications']
    
    if type_ == 'Tcloud_policy_app': 
        pattern = r'set applications application {} protocol (.*?)$'.format(word_to_find_)
        return [pattern,  'applications']
    
    if type_ == 'Tcloud_idp': 
        pattern = r'set system security-profile LSYS-Resoreses-Profile idp-policy IDP_Default$'
        return [pattern,  'system/idp']
    
    if type_ == 'all': 
        pattern = r'set'
        return [pattern,  'security']
            
    if type_ == 'application':
        pattern = r'application {} protocol '.format(word_to_find_)
        return [pattern, 'applications']
    
    if type_ == 'application-set':
        pattern = r'application-set {} application {}'.format(word_to_find_[0],word_to_find_[1])
        return [f'application-set {word_to_find_[0]} application {word_to_find_[1]}', 'applications']
    

  
    
def m(word):
    styled_text = colored(word, "magenta", attrs=["bold"])
    return styled_text
def c(word):
    styled_text = colored(word, "cyan", attrs=["bold"])
    return styled_text
def b(word):
    styled_text = colored(word, "blue", attrs=["bold"])
    return styled_text
def y(word):
    styled_text = colored(word, "yellow", attrs=["bold"])
    return styled_text
def g(word):
    styled_text = colored(word, "green", attrs=["bold"])
    return styled_text