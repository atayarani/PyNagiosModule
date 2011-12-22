#!/usr/bin/env python
from os.path import basename
from re import match
from socket import gethostbyname
from sys import argv
from time import strftime

class Nagios(object):

    def __init__(self,filename):
        self.config_path="/cfengine/etc/nagios/configs/autogen/"
        self.file=open(self.config_path+filename,'w')
        self.warning=("#\n"
                    "# PLEASE DO NOT MODIFY THE CONTENTS OF THIS FILE."
                    "  This file is auto-generated\n"
                    "# by the `%s` script.\n" 
                    "#\n"
                    "# Last generated: %s\n" 
                    "#\n\n"
                    % (basename(argv[0]),strftime("%m/%d/%Y %T")))

    def host(self,use='generic-host',host_name='',address='',alias='',
        name='',register='',hostgroups='',contact_groups='',
        notification_interval='',notification_period='',
        contacts='',notifications_enabled='',notification_options='',parent='',
        max_check_attempts=''):

        info_list=['define host{','\tuse\t\t\t%s' % (use)]

        if host_name != '':
            info_list.append('\thost_name\t\t%s' % host_name)
        if address != '':
            info_list.append('\taddress\t\t\t%s' % address)
        if alias != '':
            info_list.append('\talias\t\t\t%s' % alias)
        if hostgroups!= '':
            info_list.append('\thostgroups\t\t%s' % hostgroups)
        if register != '':
            info_list.append('\tregister\t\t%s' % register)
        if parent != '':
            info_list.append('\tparent\t\t\t%s' % parent)
        if name != '':
            info_list.append('\tname\t\t\t%s' % name)
        if notification_period != '':
            info_list.append("\tnotification_period\t%s" % notification_period)
        if contact_groups != '':
            info_list.append("\tcontact_groups\t\t%s" % contact_groups)
        if contacts != '':
            info_list.append("\tcontacts\t\t\t\t%s" % contacts)
        if notification_interval != '':
            info_list.append('\tnotification_interval\t\t%s'
                               % notification_interval)
        if notifications_enabled != '':
            info_list.append('\tnotifications_enabled\t\t%s'
                                % notifications_enabled)
        if notification_options != '':
            info_list.append('\tnotification_options\t\t%s'
                                % notification_options)
        if max_check_attempts != '':
            info_list.append('\tmax_check_attempts\t%s'
                                % max_check_attempts)

        info_list.append('\t}\n')
        return '\n'.join(info_list)

    def hostgroup(self,hostgroup_name='',members='',alias=''):
        info_list=['define hostgroup{']

        if hostgroup_name != '':
            info_list.append('\thostgroup_name\t\t%s' % hostgroup_name)
        if alias != '':
            info_list.append('\talias\t\t\t%s' % alias)
        if members != '':
            info_list.append('\tmembers\t\t\t%s' % members)

        info_list.append('\t}\n')
        return '\n'.join(info_list)

    def hostescalation(self,hostgroup_name='',host_name='',
        service_description='', escalation_options='',
        contact_groups='', first_notification='',
        last_notification='',contacts=''):
        info_list=['define serviceescalation{']

        if hostgroup_name != '':
            info_list.append('\thostgroup_name\t\t\t%s'
                              % hostgroup_name)
        if host_name != '':
            info_list.append('\thost_name\t\t%s' % host_name)
        if escalation_options != '':
            info_list.append('\tescalation_options\t%s' % escalation_options)
        if contact_groups != '':
            info_list.append('\tcontact_groups\t\t\t%s' % contact_groups)

        if contacts != '':
            info_list.append("\tcontacts\t\t\t\t%s" % contacts)
        if first_notification != '':
            info_list.append('\tfirst_notification\t%s'
                                % first_notification)
        if last_notification != '':
            info_list.append('\tlast_notification\t%s'
                                % last_notification)

        info_list.append('\t}\n')
        return '\n'.join(info_list)



    def getIP(self,_hostname):
        '''Retrieve IP of supplied argument'''
        _ip=gethostbyname(_hostname)
        return _ip if __name__!="__main__" else (_ip,_hostname)

    def servicegroup(self,name='',alias='',members='',servicegroup_members=''):
        info_list['define servicegroup{']

        if servicegroup_name != '':
            info_list.append('\tservicegroup_name\t\t\t%s' % servicegroup_name)
        if members != '':
            info_list.append('\tmembers\t\t\t%s' % members)
        if servicegroup_members != '':
            info_list.append('\tservicegroup_members\t\t\t%s'
                                % servicegroup_members)

        info_list.append('\t}\n')
        return '\n'.join(info_list)

    def services(self,use='generic',name='',hostgroup_name='',register='',
                 notification_period='',contacts='',contact_groups='',
                 notification_interval='',notifications_enabled='',
                 notification_options='',service_description='',host_name='',
                 check_command=''):
                 info_list=['define service{','\tuse\t\t\t%s' % (use)]
                 
                 if hostgroup_name != '':
                     info_list.append('\thostgroup_name\t\t%s'
                                         % hostgroup_name)
                 if register != '':
                     info_list.append('\tregister\t\t%s' % register)
                 if name != '':
                     info_list.append('\tname\t\t\t%s' % name)
                 if notification_period != '':
                     info_list.append("\tnotification_period\t%s"
                                         % notification_period)
                 if contact_groups != '':
                     info_list.append("\tcontact_groups\t\t%s"
                                         % contact_groups)
                 if contacts != '':
                     info_list.append("\tcontacts\t\t\t\t%s"
                                         % contacts)
                 if notification_interval != '':
                     info_list.append('\tnotification_interval\t\t%s'
                                        % notification_interval)
                 if notifications_enabled != '':
                     info_list.append('\tnotifications_enabled\t\t%s'
                                        % notifications_enabled) 
                 if notification_options != '':
                     info_list.append('\tnotification_options\t%s'
                                        % notification_options)
                 if check_command != '':
                     info_list.append('\tcheck_command\t\t%s'
                                        % check_command)

                 if service_description != '':
                     info_list.append('\tservice_description\t%s'
                                        % service_description)
                 if host_name != '':
                     info_list.append('\thost_name\t\t%s' % host_name)

                 info_list.append('\t}\n')
                 return '\n'.join(info_list)

    def serviceescalations(self,hostgroup_name='',host_name='',
                            service_description='', escalation_options='',
                            contact_groups='', first_notification='',
                            last_notification=''):
                 info_list=['define serviceescalation{']
        
                 if hostgroup_name != '':
                     info_list.append('\thostgroup_name\t\t\t%s'
                                         % hostgroup_name)
                 if host_name != '':
                     info_list.append('\thost_name\t\t%s' % host_name)
                 if service_description != '':
                     info_list.append('\tservice_description\t%s'
                                        % service_description)
                 if escalation_options != '':
                     info_list.append('\tescalation_options\t%s'
                                        % escalation_options)
                 if contact_groups != '':
                     info_list.append('\tcontact_groups\t\t\t%s'
                                         % contact_groups)
                 if first_notification != '':
                     info_list.append('\tfirst_notification\t%s'
                                         % first_notification)
                 if last_notification != '':
                     info_list.append('\tlast_notification\t%s'
                                         % last_notification)

                 info_list.append('\t}\n')
                 return '\n'.join(info_list)

    def contact(self,use='',contact_name='',alias='',email='',
                 host_notifications_enabled='',
                 service_notifications_enabled=''):
        info_list=['define contact{']

        if use != '':
            info_list.append('\tuse\t\t\t\t%s' % use)
        if contact_name != '':
            info_list.append('\tcontact_name\t\t\t%s' % contact_name)
        if alias != '':
            info_list.append('\talias\t\t\t\t%s' % alias)
        if email != '':
            info_list.append('\temail\t\t\t\t%s' % email)
        if host_notifications_enabled != '':
            info_list.append('\thost_notifications_enabled\t%s' %
            host_notifications_enabled)
        if service_notifications_enabled != '':
            info_list.append('\tservice_notifications_enabled\t%s' % 
            service_notifications_enabled)

        info_list.append('\t}\n')
        return '\n'.join(info_list)

    def contactgroup(self,contactgroup_name='',alias='',members='',
                     contactgroup_members=''):
        info_list=['define contactgroup{']

        if contactgroup_name != '':
            info_list.append('\tcontactgroup_name\t%s' % contactgroup_name)
        if alias != '':
            info_list.append('\talias\t\t\t%s' % alias)
        if members != '':
            info_list.append('\tmembers\t\t\t%s' % members)
        if contactgroup_members != '':
            info_list.append('\tcontactgroup_members\t%s' % contactgroup_members)

        info_list.append('\t}\n')
        return '\n'.join(info_list)

if __name__=="__main__":
    for arg in argv[1:]:
        rv=Nagios().getIP(arg)
        print rv
