#!/usr/bin/env python
from re import match
from socket import gethostbyname
from sys import argv

class Nagios(object):

    def __init__(self,filename):
        self.config_path="/cfengine/etc/nagios/configs/autogen/"
        self.file=open(self.config_path+filename,'w')
        self.master_host_listing='/sysman/install/broad/master.host.listing'
        self.MHL=open(self.master_host_listing,'r')

    def host(self,use='generic-host',host_name='',address='',alias='',
        name='',register='',hostgroups='',contact_groups='',
        notification_interval='',notification_period='',
        contacts='',notifications_enabled='',notification_options=''):

        info_list=['define host{','\tuse\t\t\t\t%s' % (use)]

        if host_name != '':
            info_list.append('\thost_name\t\t\t%s' % host_name)
        if address != '':
            info_list.append('\taddress\t\t\t%s' % address)
        if alias != '':
            info_list.append('\talias\t\t\t%s' % alias)
        if hostgroups!= '':
            info_list.append('\thostgroups\t\t\t%s' % hostgroups)
        if register != '':
            info_list.append('\tregister\t\t%s' % register)
        if name != '':
            info_list.append('\tname\t\t\t%s\n' % name)
        if notification_period != '':
            info_list.append("\tnotification_period\t%s" % notification_period)
        if contact_groups != '':
            info_list.append("\tcontact_groups\t\t\t%s" % contact_groups)
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

        info_list.append('\t}\n')
        return '\n'.join(info_list)

    def hostgroup(self,hostgroup_name='',members=''):
        info_list=['define hostgroup{']

        if hostgroup_name != '':
            info_list.append('\thostgroup_name\t\t\t%s' % hostgroup_name)
        if members != '':
            info_list.append('\tmembers\t\t\t%s\n' % members)

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
            info_list.append('\tescalation_options\t%s\n' % escalation_options)
        if contact_groups != '':
            info_list.append('\tcontact_groups\t\t\t%s' % contact_groups)
        if contacts != '':
            info_list.append("\tcontacts\t\t\t\t%s" % contacts)
        if first_notification != '':
            info_list.append('\tfirst_notification\t%s\n'
                                % first_notification)
        if last_notification != '':
            info_list.append('\tlast_notification\t%s\n'
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
            info_list.append('\tmembers\t\t\t%s\n' % members)
        if servicegroup_members != '':
            info_list.append('\tservicegroup_members\t\t\t%s\n' 
                                % servicegroup_members)

        info_list.append('\t}\n')
        return '\n'.join(info_list)

    def services(self,use='generic',name='',hostgroup_name='',register='',
                 notification_period='',contacts='',contact_groups='',
                 notification_interval='',notifications_enabled='',
                 notification_options='',service_description='',host_name='',
                 check_command=''):
                 info_list=['define service{','\tuse\t\t\t\t%s' % (use)]
                 
                 if hostgroup_name != '':
                     info_list.append('\thostgroup_name\t\t\t%s' 
                                         % hostgroup_name)
                 if register != '':
                     info_list.append('\tregister\t\t%s' % register)
                 if name != '':
                     info_list.append('\tname\t\t\t%s\n' % name)
                 if notification_period != '':
                     info_list.append("\tnotification_period\t%s" 
                                         % notification_period)
                 if contact_groups != '':
                     info_list.append("\tcontact_groups\t\t\t%s"
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
                     info_list.append('\tnotification_options\t\t%s'
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
                     info_list.append('\tescalation_options\t%s\n'
                                        % escalation_options)
                 if contact_groups != '':
                     info_list.append('\tcontact_groups\t\t\t%s'
                                         % contact_groups)
                 if first_notification != '':
                     info_list.append('\tfirst_notification\t%s\n'
                                         % first_notification)
                 if last_notification != '':
                     info_list.append('\tlast_notification\t%s\n'
                                         % last_notification)

                 info_list.append('\t}\n')
                 return '\n'.join(info_list)

if __name__=="__main__":
    for arg in argv[1:]:
        rv=Nagios().getIP(arg)
        print rv
