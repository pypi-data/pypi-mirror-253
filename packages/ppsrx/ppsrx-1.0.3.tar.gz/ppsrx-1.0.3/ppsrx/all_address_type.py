import re
import ipaddress
from termcolor import colored
import _configurations_

address_description = 'Address Pushed through Netconf'




excelude_address = [
    'address',
    'address-set',
    'address range',
    'address-range',
    'address group',
    'address-group',
    'address_group',
    ''
    ]



  
def address_address_set(dev, input_any_address_to_configure , file_content = None):
    invalid_range = []
    already_existed=[]
    invalid_address_set = []
    commands=[]
    already_existed=[]
    duplicated_in_commands = []
    duplicated_ip=[]
    duplicated_ip_in_commands = []
    wrong_inputs=[]
    
    lines = input_any_address_to_configure.strip().split('\n')
     # [[each line.split], [each line.split], [each line.split]]
    result = [line.split('\t') for line in lines]

    for each_line1 in result:
    
# if >>  For address and address-range >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        if len(each_line1) >= 4 and each_line1[3] != '':
            each_line = [element.replace(' ', '_').replace('&', 'And').replace('(', '').replace(')', '').replace('\r','').strip() for element in each_line1]

            # if no cloumn 5 add column 5 = ''
            if len(each_line) == 4:
                each_line.append('') 
            
            
            is_ip3 = network_ip(each_line[3], each_line)
            if isinstance(is_ip3, list):    
                if is_ip3[0] == 'error':
                    wrong_inputs.append(is_ip3[1])
                    continue
            if each_line[4] != '' :
                is_ip4 = network_ip(each_line[4], each_line)
                if isinstance(is_ip4, list):
                    if is_ip4[0] == 'error':
                        wrong_inputs.append(is_ip4[1])
                        continue
                
            
            
            # match4 is a prefix in column 5 in excel sheet and must to be 32
            match3 = ip_prefix(each_line[3])
            match4 = ip_prefix(each_line[4])
            
            # no_slash3 is ip with no prefix in column 4 in excel sheet 
            # no_slash4 is ip with no prefix in column 5 in excel sheet 
            no_slash3 = each_line[3].split('/')[0] if '/' in each_line[3] else each_line[3] 
            no_slash4 = each_line[4].split('/')[0] if '/' in each_line[4] else each_line[4]
            
            
            if not(each_line[3].find('/') != -1) and is_valid_ip(each_line[3]):
                each_line[3] = each_line[3] + '/32'

            if not(each_line[4].find('/') != -1) and is_valid_ip(each_line[4]):
                each_line[4] = each_line[4] + '/32'
 
            


            if dev != None:
                retuen_match_in_list = _configurations_.retrive_configurations('address' , each_line[1], dev=dev)
            if file_content != None:
                retuen_match_in_list = _configurations_.retrive_configurations('address' , each_line[1], file_content=file_content)
            #==================== For Address Only ==================================================================================================
            # each_line[3] is the value in column 4 in excel sheet 
            # each_line[4] is the value in column 5 in excel sheet
            if each_line[4] == '' or match4 == 32 or no_slash3 == no_slash4 :
                if dev != None:
                    matched_ip_list = _configurations_.retrive_configurations('address-ip' , each_line[3], dev=dev)
                if file_content != None:
                    matched_ip_list = _configurations_.retrive_configurations('address-ip' , each_line[3], file_content=file_content) 
                if each_line[2] != '' and  each_line[4] == '': # ['address', word, description, ip , '']
                    if not( f'set security address-book global description {each_line[2]} address {each_line[1]} {each_line[3]}' in commands):
                        if len(retuen_match_in_list) == 0:
                                if len(matched_ip_list) == 0 and not(f'set security address-book global description {each_line[2]} address {each_line[1]} {each_line[3]}' in commands):
                                    for comm in commands:
                                        if  re.search(r'security address-book global address .* {}'.format(each_line[3]),comm):
                                            words = comm.split()
                                            duplicated_ip_in_commands.append(yellow('► WARNING ► Duplicated IP [') + yellow(each_line[3])+yellow('] Found Under ▼▼ Paste your set commands ▼▼.With Name [') +m(words[5])+ yellow('].Still configured as valid and associated with name [') + m(each_line[1]) + yellow('].'))
                                    commands.append(f'set security address-book global description {b(each_line[2])} address {m(each_line[1])} {yellow(each_line[3])}')
                                    continue
                                else:
                                    commands.append(f'set security address-book global description {b(each_line[2])} address {m(each_line[1])} {yellow(each_line[3])}')
                                    duplicated_ip.append(yellow('► WARNING ► ') + 'Duplicated IP Found [' + yellow(each_line[3]) + '] This IP already existed and associated with different name.Still configured as valid and associated with name [' + m(each_line[1]) + '].')
                                    duplicated_with = yellow('► Duplicated With ► \n') + '\n'.join(matched_ip_list)
                                    duplicated_ip.append(duplicated_with)
                                    continue
                        else:
                            already_existed.append(f'The Address [ {m(each_line[1])} ] Already existed. No action had taken.')
                            continue
                    else:
                        duplicated_in_commands.append(f'The Address [ {m(each_line[1])} ] Is duplicated and done once. No action had taken.')
                        continue
                    
                elif each_line[2] != '' and  each_line[4] != '': # ['address', word, description, ip , ip/prefix]
                    if not(f'set security address-book global description {each_line[2]} address {each_line[1]} {each_line[4]}' in commands):
                        if len(retuen_match_in_list) == 0:    
                            if len(matched_ip_list) == 0 and not(f'set security address-book global description {each_line[2]} address {each_line[1]} {each_line[4]}' in commands):
                                for comm in commands:
                                        if  re.search(r'security address-book global address .* {}'.format(each_line[4]),comm):
                                            words = comm.split()
                                            duplicated_ip_in_commands.append(yellow('► WARNING ► ') + 'Duplicated IP [' + yellow(each_line[4])+ '] Found Under ▼▼ Paste your set commands ▼▼.With Name [' +m(words[5])+ '].Still configured as valid and associated with name [' + m(each_line[1]) + '].')
                                commands.append(f'set security address-book global description {b(each_line[2])} address {m(each_line[1])} {yellow(each_line[4])}')
                                continue
                            else:
                                commands.append(f'set security address-book global description {b(each_line[2])} address {m(each_line[1])} {yellow(each_line[4])}')
                                duplicated_ip.append(yellow('► WARNING ► ') + 'Duplicated IP Found [' + m(each_line[4]) + '] This IP already existed and associated with different name.Still configured as valid and associated with name [' + m(each_line[1]) + '].')
                                duplicated_with = yellow('► Duplicated With ► \n') + '\n'.join(matched_ip_list)
                                duplicated_ip.append(duplicated_with)
                                continue    
                        else:
                            already_existed.append(f'The Address [ {m(each_line[1])} ] Already existed. No action had taken.')
                            continue
                    else:
                        duplicated_in_commands.append(f'The Address [ {m(each_line[1])} ] Is duplicated and done once. No action had taken.')
                        continue
                        
                elif each_line[2] == '' and  each_line[4] == '': # ['address', word, '', ip , ''] 
                    if not(f'set security address-book global address {each_line[1]} {each_line[3]}' in commands):
                        if len(retuen_match_in_list) == 0:
                            if len(matched_ip_list) == 0 and not(f'set security address-book global address {each_line[1]} {each_line[3]}' in commands):
                                for comm in commands:
                                        if  re.search(r'security address-book global address .* {}'.format(each_line[3]),comm):
                                            words = comm.split()
                                            duplicated_ip_in_commands.append(yellow('► WARNING ► ') + 'Duplicated IP [' + yellow(each_line[3]) +  '] Found Under ▼▼ Paste your set commands ▼▼.With Name [' +m(words[5])+ '].Still configured as valid and associated with name [' + m(each_line[1]) + '].')
                                commands.append(f'set security address-book global address {m(each_line[1])} {yellow(each_line[3])}') 
                                continue
                            else:
                                commands.append(f'set security address-book global address {m(each_line[1])} {yellow(each_line[3])}') 
                                duplicated_ip.append(yellow('► WARNING ► ') + 'Duplicated IP Found [' + m(each_line[3]) + '] This IP already existed and associated with different name.Still configured as valid and associated with name [' + m(each_line[1]) + '].')
                                duplicated_with = yellow('► Duplicated With ► \n') + '\n'.join(matched_ip_list)
                                duplicated_ip.append(duplicated_with)
                                continue  
                        else:
                            already_existed.append(f'The Address [ {m(each_line[1])} ] Already existed. No action had taken.')
                            continue
                    else:
                        duplicated_in_commands.append(f'The Address [ {m(each_line[1])} ] Is duplicated and done once. No action had taken.')
                        continue
                    
                elif each_line[2] == '' and  each_line[4] != '': # ['address', word, '', ip , ip/prefix]
                    if not(f'set security address-book global address {each_line[1]} {each_line[4]}' in commands):
                        if len(retuen_match_in_list) == 0:  
                            if len(matched_ip_list) == 0 and not(f'set security address-book global address {each_line[1]} {each_line[4]}' in commands):
                                for comm in commands:
                                        if  re.search(r'security address-book global address .* {}'.format(each_line[4]),comm):
                                            words = comm.split()
                                            duplicated_ip_in_commands.append(yellow('► WARNING ► ') + 'Duplicated IP [' + yellow(each_line[4]) + '] Found Under ▼▼ Paste your set commands ▼▼.With Name [' + m(words[5]) + '].Still configured as valid and associated with name [' + m(each_line[1]) + '].')
                                commands.append(f'set security address-book global address {m(each_line[1])} {yellow(each_line[4])}')
                                continue
                            else:
                                commands.append(f'set security address-book global address {m(each_line[1])} {yellow(each_line[4])}')
                                duplicated_ip.append(yellow('► WARNING ► ') + 'Duplicated IP Found [' + m(each_line[4]) + '] This IP already existed and associated with different name.Still configured as valid and associated with name [' + m(each_line[1]) + '].')
                                duplicated_with = yellow('► Duplicated With ► \n') + '\n'.join(matched_ip_list)
                                duplicated_ip.append(duplicated_with)
                                continue  
                        else:
                            already_existed.append(f'The Address [ {m(each_line[1])} ] Already existed. No action had taken.')
                            continue
                    else:
                        duplicated_in_commands.append(f'The Address [ {m(each_line[1])} ] Is duplicated and done once. No action had taken.')
                        continue
                    
                        
                    
                 
                    
                        
                    
            #==================== For Address-range Only ==================================================================================================
            if len(each_line) >= 5 and each_line[4] != '':
                end_ip =network_ip(each_line[4], each_line)
                start_ip =network_ip(each_line[3], each_line)
                
                if end_ip == 'error': continue
                if start_ip == 'error': continue
                
                ip_range = int(end_ip) - int(start_ip)
                if dev != None:
                    matched_ip_list = _configurations_.retrive_configurations('address-range-ip' , [start_ip,end_ip], dev=dev)
                if file_content != None:
                    matched_ip_list = _configurations_.retrive_configurations('address-range-ip' , [start_ip,end_ip], file_content=file_content) 
                if ip_range > 0:
                    if each_line[2] != '': # ['address-set', word, description, ip, ip]
                        if not( f'set security address-book global address {each_line[1]} description {each_line[2]} range-address {start_ip} to {end_ip}' in commands):
                            if len(retuen_match_in_list) == 0:  
                                if len(matched_ip_list) == 0:
                                    for comm in commands:
                                        if  re.search(r'set security address-book global address .* range-address {} to {}'.format(start_ip,end_ip),comm):
                                            words = comm.split()
                                            duplicated_ip_in_commands.append(yellow('► WARNING ► ') + 'Duplicated Range-IP [' + yellow(start_ip) + g(' to ') + yellow(end_ip) + '] Found Under ▼▼ Paste your set commands ▼▼.With Name [' + m(words[5]) + '].Still configured as valid and associated with name [' + m(each_line[1]) + '].')
                                    commands.append(f'set security address-book global address {m(each_line[1])} description {b(each_line[2])} range-address {yellow(start_ip)} to {yellow(end_ip)}')
                                    continue
                                else:
                                    commands.append(f'set security address-book global address {m(each_line[1])} description {b(each_line[2])} range-address {yellow(start_ip)} to {yellow(end_ip)}')
                                    duplicated_ip.append(yellow('► WARNING ► ') + 'Duplicated Range-IP Found [' + yellow(start_ip) + g(' to ') + yellow(end_ip) + '] This IP already existed and associated with different name.Still configured as valid and associated with name [' +  m(each_line[1]) + '].')
                                    duplicated_with = yellow('► Duplicated With ► \n') + '\n'.join(matched_ip_list)
                                    duplicated_ip.append(duplicated_with)
                                    continue
                            else:
                                already_existed.append(f'The Address [{m(each_line[1])}] Already existed. No action had taken.')
                                continue
                        else:
                            duplicated_in_commands.append(f'The Address [{m(each_line[1])}] Is duplicated and done once. No action had taken.')
                            continue
                        
                    
                    elif each_line[2] == '': # ['address', word, '', ip , ip]
                        if not(f'set security address-book global address {each_line[1]} range-address {start_ip} to {end_ip}' in commands):
                            if len(retuen_match_in_list) == 0:
                                if len(matched_ip_list) == 0:
                                    for comm in commands:
                                        if  re.search(r'set security address-book global address .* range-address {} to {}'.format(start_ip,end_ip),comm):
                                            words = comm.split()
                                            duplicated_ip_in_commands.append(yellow('► WARNING ► ') + 'Duplicated Range-IP [' + yellow(start_ip) + g(' to ') + yellow(end_ip) + '] Found Under ▼▼ Paste your set commands ▼▼.With Name [' + m(words[5]) + '].Still configured as valid and associated with name [' + m(each_line[1]) + '].')
                                    commands.append(f'set security address-book global address {m(each_line[1])} range-address {yellow(start_ip)} to {yellow(end_ip)}')
                                    continue
                                else:
                                    commands.append(f'set security address-book global address {m(each_line[1])} description {b(each_line[2])} range-address {yellow(start_ip)} to {yellow(end_ip)}')
                                    duplicated_ip.append(yellow('► WARNING ► ') + 'Duplicated Range-IP Found [' + yellow(start_ip) + g(' to ') + yellow(end_ip) + '] This IP already existed and associated with different name.Still configured as valid and associated with name [' +  m(each_line[1]) + '].')
                                    duplicated_with = yellow('► Duplicated With ► \n') + '\n'.join(matched_ip_list)
                                    duplicated_ip.append(duplicated_with)
                                    continue
                            else:
                                already_existed.append(f'The Address [ {m(each_line[1])} ] Already existed. No action had taken.')
                                continue
                        else:
                            duplicated_in_commands.append(f'The Address [ {m(each_line[1])} ] Is duplicated and done once. No action had taken.')
                            continue    

                elif ip_range < 0:
                    invalid_range.append(yellow("Error: ") +  'Invalid IPv4 address Range: \b' + yellow(each_line[3]) + ' to ' + yellow(each_line[4]) + "no action had taken.")
                    continue
                    
  # if >>  For address and address-set >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.  
  
        #inilaize each_line1 add more elements '' if have less than 4
        if len(each_line1) < 4:
            for more_element in range(4 - len(each_line1)):
                each_line1.append('')
        
        each_line = [element.replace(' ', '_').replace('&', 'And').replace('(', '').replace(')', '').replace('\r','').strip() for element in each_line1]
        if each_line[3] == '':
            
            

            # send column 2 value to retrived data > return true or false
            
            if dev != None:
            
                is_excist_address = _configurations_.retrive_configurations( 'address', each_line[1], is_exist= 'yes', dev = dev)
                retuen_match_in_list = _configurations_.retrive_configurations('address-set' , [each_line[0],each_line[1]], is_exist= 'yes', dev=dev)
                
            if file_content != None:
                
                is_excist_address = _configurations_.retrive_configurations( 'address', each_line[1], is_exist= 'yes',file_content=file_content)
                retuen_match_in_list = _configurations_.retrive_configurations('address-set' , [each_line[0],each_line[1]], file_content=file_content)
 
            if is_excist_address and not(each_line[0].lower() in [s.lower() for s in excelude_address]):   # ['address-set', address, '', ''] 
                    if len(retuen_match_in_list) == 0:
                        if not(f'set security address-book global address-set {each_line[0]} address {each_line[1]}' in commands):
                            commands.append(f'set security address-book global address-set {m(each_line[0])} address {m(each_line[1])}')
                            continue
                        else:
                            duplicated_in_commands.append(f'The address [{m(each_line[1])}] Is duplicated and done once. No action had taken.')
                            continue
                    else:
                        already_existed.append(f'The address [{m(each_line[1])}] Already existed in address-set called [ {m(each_line[0])}]. No action had taken.')
                        continue    
            else:

                invalid_address_set.append(f'The address [{m(each_line[1])}] not exist. So you can not add it to address-set [{m(each_line[0])}]. No action had taken.')
                continue
                
    return [commands, wrong_inputs, invalid_range, invalid_address_set, address_description,duplicated_in_commands ,already_existed,duplicated_ip,duplicated_ip_in_commands]

def network_ip(ip_str,invalid_line):
    
    try:
    
        ip_network = ipaddress.IPv4Network(ip_str, strict=False)
        
        # Extract the IPv4 address without the subnet
        ipv4_address = ip_network.network_address
        return ipv4_address
        
    except Exception as e:
        wrong_inputs = yellow("Error: ") + 'Invalid characters in the IPv4 address: \b ' + ' | '.join([x for x in invalid_line if x !='']) + " no action had taken."
        return ['error',wrong_inputs]
        
        
def ip_prefix(ip_str):
        if ip_str.find('/') != -1 :
            ipv4_prefix = ip_str.split('/')[1]
            return ipv4_prefix
            
      

    
def is_valid_ip(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
        return True
    except ValueError:
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