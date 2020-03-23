#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import platform
import logging

prog_version = "%prog 0.91 - (c) ASTREL 2020"

script_basename = os.path.basename(__file__)

my_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(my_dir)

my_conf_dir = os.path.join(my_dir, "configurations")
if not os.path.isdir(my_conf_dir):
    os.mkdir(my_conf_dir)

script_shortname = script_basename

if ".py" in script_basename:
    if script_basename[-3:] == ".py":
        script_shortname = script_basename[:-3]

if ".exe" in script_basename:
    if script_basename[-4:] == ".exe":
        script_shortname = script_basename[:-4]

if platform.system() == "Windows":
    #logging_filename = os.path.join(os.environ["TEMP"], script_shortname+".log")
    logging_filename =  os.path.join("log", script_shortname+".log")
else:
    logging_filename = os.path.join("log", script_shortname+".log")

logging.basicConfig(level=logging.INFO)


def suivi_conf(ip, device_type):

    nagios_state = 3 # UNKNOWN
    nagios_text = ""
    
    if device_type == "fortigate":
        cmd_running = ["scp", "admin@"+ip+":sys_config", "configurations/"+ip+".cfg"]
        result_running = subprocess.call(cmd_running, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result_running != 0:
            nagios_state = 2 # CRITICAL
            nagios_text += "CRITICAL: cant get config by scp"
            get_config_ok = False
        else:
            nagios_state = 0 # OK
            nagios_text += "OK: configuration saved "
            get_config_ok = True
    else: # device_type == hp_procurve
        cmd_running = ["scp", "admin@"+ip+":cfg/running-config", "configurations/"+ip+".cfg"]
        result_running = subprocess.call(cmd_running, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result_running != 0:
            nagios_state = 2 # CRITICAL
            nagios_text += "CRITICAL: cant get config by scp"
            get_config_ok = False
        else: 
            nagios_state = 0 # OK
            nagios_text += "OK: configuration saved "
            get_config_ok = True
            
    if get_config_ok:        
        if device_type == "hp_procurve":
            cmd_startup = ["scp", "admin@"+ip+":cfg/startup-config", "configurations/"+ip+"-startup.cfg"]
            result_startup = subprocess.call(cmd_startup, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result_startup != 0: 
                nagios_state = 2 # CRITICAL
                nagios_text += "CRITICAL: cant get startup config by scp"
            
            cmd_diff = ["diff", "configurations/"+ip+".cfg", "configurations/"+ip+"-startup.cfg"]
            result_diff = subprocess.call(cmd_diff, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result_diff == 0:
                nagios_state = 0 # OK
                nagios_text += "OK: running-config==startup-config "
                os.remove("configurations/"+ip+"-startup.cfg")
            else:
                nagios_state = 1 # WARNING
                nagios_text += "WARN: running-config and startup-config are different "
        
        #diff exist ?
        
        cmd_git_exist = [ "git", "ls-files", "--error-unmatch", "configurations/"+ip+".cfg" ]
        result_git_exist = subprocess.call(cmd_git_exist, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result_git_exist != 0:
            cmd_git_add = ["git", "add", "configurations/"+ip+".cfg"]
            result_git_add = subprocess.call(cmd_git_add, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result_git_add != 0:
                nagios_text += "; WARN: couldnt add "+repr(cmd_git_add)+" "
                if nagios_state == 0:
                    nagios_state = 1 # WARNING
            else:
                cmd_initial_commit = ["git", "commit", "configurations/"+ip+".cfg", "-m", '"'+ip+' created"']
                result_initial_commit = subprocess.call(cmd_initial_commit, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if result_initial_commit != 0:
                    nagios_text += "; WARN: couldnt commit "+repr(cmd_initial_commit)+" "
                    if nagios_state == 0:
                        nagios_state = 1 # WARNING
        
        cmd_gitdiff = ['git', 'diff', '--exit-code', '--', 'configurations/'+ip+'.cfg']
        result_gitdiff = subprocess.call(cmd_gitdiff, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result_gitdiff != 0:
            cmd_commit = ["git", "commit", "configurations/"+ip+".cfg", "-m", '"'+ip+' changed"']
            result_commit = subprocess.call(cmd_commit, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result_commit != 0:
                nagios_text += "; WARN: couldnt commit "+repr(cmd_commit)+" "
                if nagios_state == 0:
                    nagios_state = 1 # WARNING
        
        # date de dernière modification
        cmd_date = ["git", "log", "-1", '--pretty="%ci"', "--", "configurations/"+ip+".cfg"]
        try:
            output = subprocess.check_output(cmd_date)
        except:
            if nagios_state == 0:
                nagios_state = 1
            nagios_text += "; WARN: cant get last change date"
        else:
            date = output.decode("utf-8").replace("\"", "").strip()
            nagios_text += "; configuration last modified "+date+" "
            
    #nagios_text += "; running-config and startup-config are stored in https://adm-rsx.morin-logistic.com (https://10.234.130.134)" 
    return (nagios_state,nagios_text)

if __name__=="__main__":

    import optparse
    parser = optparse.OptionParser(usage="usage: %prog [options] <ip_address> [ <device_type> ]", version=prog_version)

    parser.add_option("-d", "--debug", dest="debug", default=False, action="store_true", help="activate debug mode")
    parser.add_option("-p", "--port", dest="portnum", default=22, type="int", help="port number for ssh connexions (default: 22)")

    (options, args) = parser.parse_args()

    if len(args) == 0 :
        print ("\nI received the following args:"+repr(args)+"\n")
        parser.print_help()
        sys.exit(1)

    debug = options.debug

    ip = args[0]
        
    if len(args) >= 2:
        device_type = args[1].lower()
        if device_type not in [ "fortigate", "hp_procurve" ]:
            print("\nUnknown device type "+args[1].decode("utf-8")+".\n")
            sys.exit(2)
    else:
        device_type = "hp_procurve"

    (nagios_state, nagios_text) = suivi_conf(ip, device_type)


    
    print (nagios_text)
    
    sys.exit(nagios_state)
