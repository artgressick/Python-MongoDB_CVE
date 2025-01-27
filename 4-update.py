from pymongo import MongoClient
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# ###########Global Variables############
#server = 'localhost'
#port = '27017'
#username = ''
#password = ''
database = 'nvd'

def main():

    #connection = MongoClient(server,authSource=database)
    #connection = MongoClient("mongodb://USERNAME:PASSWORD@cluster0-shard-00-00.ja3ud.gcp.mongodb.net:27017,cluster0-shard-00-01.ja3ud.gcp.mongodb.net:27017,cluster0-shard-00-02.ja3ud.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-jgyvvk-shard-0&authSource=admin&retryWrites=true&w=majority")
    connection = MongoClient("mongodb://localhost:27017/<dbname>")

    db = connection[database]
    collection = ''
    UpdateResult = ''
    file_name = input('Please enter collection year: ')
    collection = db['cve_'+file_name]
    cve_data = ''

#----- Vendor Cisco -----#
    print("Vendor: Cisco Systems");
#----- IOS Operating System - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'o:cisco:ios:'}}, {"$push": {'vendor':'[cisco]', 'os':'[ios]'}} )
    print("Updating Cisco IOS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:cisco:ios:'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_os':'[ios]'}} )
    print("Updating Cisco IOS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- NX-OS Operating System - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'o:cisco:nx-os:'}}, {"$push": {'vendor':'[cisco]', 'os':'[nx-os]'}} )
    print("Updating Cisco NX-OS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:cisco:nx-os:'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_os':'[nx-os]'}} )
    print("Updating Cisco NX-OS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- IOS_XE  Operating System - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'o:cisco:ios_xe:'}}, {"$push": {'vendor':'[cisco]', 'os':'[ios_xe]'}} )
    print("Updating Cisco IOS XE (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:cisco:ios_xe:'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_os':'[ios_xe]'}} )
    print("Updating Cisco IOS XE (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- IOS_XR  Operating System - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'o:cisco:ios_xr:'}}, {"$push": {'vendor':'[cisco]', 'os':'[ios_xr]'}} )
    print("Updating Cisco IOS XR (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:cisco:ios_xr:'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_os':'[ios_xr]'}} )
    print("Updating Cisco IOS XR (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Identity Service Engine - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':cisco:identity_'}}, {"$push": {'vendor':'[cisco]', 'application':'[cisco_ise]'}} )
    print("Updating Cisco ISE (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':cisco:identity_'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_application':'[cisco_ise]'}} )
    print("Updating Cisco ISE (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Cisco ASA/Firepower Firewall - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':cisco:asa'}}, {"$push": {'vendor':'[cisco]', 'hardware':'[cisco_fw]'}} )
    print("Updating Cisco ASA 2014 Firewall (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':cisco:asa'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_hardware':'[cisco_fw]'}} )
    print("Updating Cisco ASA 2014 Firewall (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':cisco:adaptive_security'}}, {"$push": {'vendor':'[cisco]', 'hardware':'[cisco_fw]'}} )
    print("Updating Cisco ASA Firewall (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':cisco:adaptive_security'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_hardware':'[cisco_fw]'}} )
    print("Updating Cisco ASA Firewall (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':cisco:firepower'}}, {"$push": {'vendor':'[cisco]', 'hardware':'[cisco_fw]'}} )
    print("Updating Cisco Firepower Firewall (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':cisco:firepower'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_hardware':'[cisco_fw]'}} )
    print("Updating Cisco Firepower Firewall (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Cisco Wifi - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':cisco:aironet'}}, {"$push": {'vendor':'[cisco]', 'hardware':'[cisco_wifi]'}} )
    print("Updating Cisco Wifi (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':cisco:aironet'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_hardware':'[cisco_wifi]'}} )
    print("Updating Cisco Wifi (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Cisco SD-WAN (Viptela) - Primary and Secondary
    updateResult = collection.update_many({ "$or": [{'product': {'$regex':':cisco:vedge'}}, {'product': {'$regex':':cisco:sd-wan'}} ]}, {"$push": {'vendor':'[cisco]', 'application':'[cisco_sdwan]'}} )
    print("Updating Cisco SD-WAN (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({ "$or": [{'products': {'$regex':':cisco:vedge'}}, {'products': {'$regex':':cisco:sd-wan'}} ]}, {"$push": {'sec_vendor':'[cisco]', 'sec_application':'[cisco_sdwan]'}} )
    print("Updating Cisco SD-WAN (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Cisco Webex - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':cisco:webex'}}, {"$push": {'vendor':'[cisco]', 'application':'[webex]'}} )
    print("Updating Cisco Webex (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':cisco:webex'}}, {"$push": {'sec_vendor':'[cisco]', 'sec_application':'[webex]'}} )
    print("Updating Cisco Webex (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Find All Cisco O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:cisco:'}}, {"$push": {'vendor':'[cisco]', 'os':'[cisco_os]'}} )
    print("Updating Cisco Operating Systems - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:cisco:'}}, {"$push": {'vendor':'[cisco]', 'application':'[cisco_app]'}} )
    print("Updating Cisco Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:cisco:'}}, {"$push": {'vendor':'[cisco]', 'hardware':'[cisco_hw]'}} )
    print("Updating Cisco Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#-----------------------------------------------------------------------------------------------------------------------------------------
#----- Vendor nVidia -----#
    print("Vendor: nVidia");
#----- Mellanox Operating System, ONYX, Skyway - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'o:nvidia:mlnx-os:'}}, {"$push": {'vendor':'[nvidia]', 'os':'[nvda-os]'}} )
    print("Updating nVidia OS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':'o:nvidia:mlnx-gw:'}}, {"$push": {'vendor':'[nvidia]', 'os':'[nvda-os]'}} )
    print("Updating nVidia OS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':'o:nvidia:nvda-os_xc:'}}, {"$push": {'vendor':'[nvidia]', 'os':'[nvda-os]'}} )
    print("Updating nVidia OS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':'o:nvidia:onyx:'}}, {"$push": {'vendor':'[nvidia]', 'os':'[nvda-os]'}} )
    print("Updating nVidia OS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':'o:nvidia:cumulus*'}}, {"$push": {'vendor':'[nvidia]', 'os':'[nvda-os]'}} )
    print("Updating nVidia OS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':'o:cumulusnetworks:'}}, {"$push": {'vendor':'[nvidia]', 'os':'[nvda-os]'}} )
    print("Updating nVidia OS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:nvidia:mlnx-os:'}}, {"$push": {'sec_vendor':'[nvidia]', 'sec_os':'[nvda-os]'}} )
    print("Updating nVidia OS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:nvidia:mlnx-gw:'}}, {"$push": {'sec_vendor':'[nvidia]', 'sec_os':'[nvda-os]'}} )
    print("Updating nVidia OS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:nvidia:nvda-os_xc:'}}, {"$push": {'sec_vendor':'[nvidia]', 'sec_os':'[nvda-os]'}} )
    print("Updating nVidia OS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:nvidia:onyx:'}}, {"$push": {'sec_vendor':'[nvidia]', 'sec_os':'[nvda-os]'}} )
    print("Updating nVidia OS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:nvidia:cumulus*'}}, {"$push": {'sec_vendor':'[nvidia]', 'sec_os':'[nvda-os]'}} )
    print("Updating nVidia OS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:cumulusnetworks:'}}, {"$push": {'sec_vendor':'[nvidia]', 'sec_os':'[nvda-os]'}} )
    print("Updating nVidia OS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Find All nVidia O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:nvidia:'}}, {"$push": {'vendor':'[nvidia]', 'os':'[nvidia_os]'}} )
    print("Updating nVidia Operating Systems - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:nvidia:'}}, {"$push": {'vendor':'[nvidia]', 'application':'[nvidia_app]'}} )
    print("Updating nVidia Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:nvidia:'}}, {"$push": {'vendor':'[nvidia]', 'hardware':'[nvidia_hw]'}} )
    print("Updating nVidia Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

#-----------------------------------------------------------------------------------------------------------------------------------------
#----- Vendor Juniper Networks -----#
    print("Vendor: Juniper Networks");
#----- JUNOS Operating System - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'o:juniper:junos:'}}, {"$push": {'vendor':'[juniper]', 'os':'[junos]'}} )
    print("Updating Juniper JunOS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':'o:juniper:junos_os_evolved:'}}, {"$push": {'vendor':'[juniper]', 'os':'[junos]'}} )
    print("Updating Juniper JunOS EVO (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:juniper:junos:'}}, {"$push": {'sec_vendor':'[juniper]', 'sec_os':'[junos]'}} )
    print("Updating Juniper JunOS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:juniper:junos_os_evolved:'}}, {"$push": {'sec_vendor':'[juniper]', 'sec_os':'[junos]'}} )
    print("Updating Juniper JunOS EVO (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Find All Juniper O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:juniper:'}}, {"$push": {'vendor':'[juniper]', 'os':'[juniper_os]'}} )
    print("Updating Juniper Operating Systems - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:juniper:'}}, {"$push": {'vendor':'[juniper]', 'application':'[juniper_app]'}} )
    print("Updating Juniper Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:juniper:'}}, {"$push": {'vendor':'[juniper]', 'hardware':'[juniper_hw]'}} )
    print("Updating Juniper Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#-----------------------------------------------------------------------------------------------------------------------------------------
#----- Vendor Arista Networks -----#
    print("Vendor: Arista Networks");
#----- EOS Operating System - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'o:arista:.*eos.*'}}, {"$push": {'vendor':'[arista]', 'os':'[eos]'}} )
    print("Updating Arista EOS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:arista:.*eos.*'}}, {"$push": {'sec_vendor':'[arista]', 'sec_os':'[eos]'}} )
    print("Updating Arista EOS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':'o:arista:extensible_operating_system'}}, {"$push": {'vendor':'[arista]', 'os':'[eos]'}} )
    print("Updating Arista EOS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:arista:extensible_operating_system'}}, {"$push": {'sec_vendor':'[arista]', 'sec_os':'[eos]'}} )
    print("Updating Arista EOS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- MOS Operating System - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'o:arista:metamako_operating_system'}}, {"$push": {'vendor':'[arista]', 'os':'[mos]'}} )
    print("Updating Arista MOS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:arista:metamako_operating_system'}}, {"$push": {'sec_vendor':'[arista]', 'sec_os':'[mos]'}} )
    print("Updating Arista MOS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':'o:arista:mos'}}, {"$push": {'vendor':'[arista]', 'os':'[mos]'}} )
    print("Updating Arista MOS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'o:arista:mos'}}, {"$push": {'sec_vendor':'[arista]', 'sec_os':'[mos]'}} )
    print("Updating Arista MOS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Mojo Wireless - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':mojo:'}}, {"$push": {'vendor':'[arista]', 'hardware':'[arista_wifi]'}} )
    print("Updating Arista Wifi (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':mojo:'}}, {"$push": {'sec_vendor':'[arista]', 'sec_hardware':'[arista_wifi]'}} )
    print("Updating Arista Wifi (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Find All Arista O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:arista:'}}, {"$push": {'vendor':'[arista]', 'os':'[arista_os]'}} )
    print("Updating Arista Operating Systems - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:arista:'}}, {"$push": {'vendor':'[arista]', 'application':'[arista_app]'}} )
    print("Updating Arista Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:arista:'}}, {"$push": {'vendor':'[arista]', 'hardware':'[arista_hw]'}} )
    print("Updating Arista Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#-----------------------------------------------------------------------------------------------------------------------------------------
#----- Vendor HP-Aruba Networks -----#
    print("Vendor: HP-Aruba Networks");
#----- ArubaOS Operating System - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':arubaos:'}}, {"$push": {'vendor':'[aruba]', 'os':'[arubaos]'}} )
    print("Updating ArubaOS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':arubaos:'}}, {"$push": {'sec_vendor':'[aruba]', 'sec_os':'[arubaos]'}} )
    print("Updating ArubaOS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':arubaos-cx:'}}, {"$push": {'vendor':'[aruba]', 'os':'[aruba-cx]'}} )
    print("Updating ArubaOS (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':arubaos-cx:'}}, {"$push": {'sec_vendor':'[aruba]', 'sec_os':'[aruba-cx]'}} )
    print("Updating ArubaOS (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Aruba Clearpass - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'arubanetworks:clearpass'}}, {"$push": {'vendor':'[aruba]', 'application':'[clearpass]'}} )
    print("Updating Aruba Clearpass (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'arubanetworks:clearpass'}}, {"$push": {'sec_vendor':'[aruba]', 'sec_application':'[clearpass]'}} )
    print("Updating Aruba Clearpass (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Aruba Wifi - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':'arubanetworks:airwave'}}, {"$push": {'vendor':'[aruba]', 'hardware':'[aruba_wifi]'}} )
    print("Updating Aruba Wifi (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'arubanetworks:airwave'}}, {"$push": {'sec_vendor':'[aruba]', 'sec_hardware':'[aruba_wifi]'}} )
    print("Updating Aruba Wifi (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':'arubanetworks:instant'}}, {"$push": {'vendor':'[aruba]', 'hardware':'[aruba_wifi]'}} )
    print("Updating Aruba Wifi (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':'arubanetworks:instant'}}, {"$push": {'sec_vendor':'[aruba]', 'sec_hardware':'[aruba_wifi]'}} )
    print("Updating Aruba Wifi (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- HPE/Silver Peak SD-WAN - Primary and Secondary
    updateResult = collection.update_many({ "$or": [{'product': {'$regex':':silver-peak:ecos'}}, {'product': {'$regex':':silver-peak:unity'}} ]}, {"$push": {'vendor':'[silverpeak]', 'application':'[silverpeak_sdwan]'}} )
    print("Updating HPE/Silver Peak (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({ "$or": [{'products': {'$regex':':silver-peak:ecos'}}, {'products': {'$regex':':silver-peak:unity'}} ]}, {"$push": {'sec_vendor':'[silverpeak]', 'sec_application':'[silverpeak_sdwan]'}} )
    print("Updating HPE/Silver Peak (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Find All Aruba O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:arubanetworks:'}}, {"$push": {'vendor':'[aruba]', 'os':'[aruba_os]'}} )
    print("Updating Aruba Operating Systems - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:arubanetworks:'}}, {"$push": {'vendor':'[aruba]', 'application':'[aruba_app]'}} )
    print("Updating Aruba Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:arubanetworks:'}}, {"$push": {'vendor':'[aruba]', 'hardware':'[aruba_hw]'}} )
    print("Updating Aruba Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#-----------------------------------------------------------------------------------------------------------------------------------------
#----- Vendor Extreme Networks (Brocade) -----#
    print("Vendor: Extreme-Brocade Networks");
#----- Netiron Operating System - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':brocade:vyatta'}}, {"$push": {'vendor':'[extreme]', 'os':'[netiron]'}} )
    print("Updating Vyette (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':brocade:vyatta'}}, {"$push": {'sec_vendor':'[extreme]', 'sec_os':'[netiron]'}} )
    print("Updating Vyette (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':brocade:netiron'}}, {"$push": {'vendor':'[extreme]', 'os':'[netiron]'}} )
    print("Updating Netiron (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':brocade:netiron'}}, {"$push": {'sec_vendor':'[extreme]', 'sec_os':'[netiron]'}} )
    print("Updating Netiron (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Extreme Wireless / Aerohive - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':extremenetworks:'}}, {"$push": {'vendor':'[extreme]', 'hardware':'[extreme_wifi]'}} )
    print("Updating Extreme Wifi (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':extremenetworks:'}}, {"$push": {'sec_vendor':'[extreme]', 'sec_hardware':'[extreme_wifi]'}} )
    print("Updating Extreme Wifi (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':aerohive:'}}, {"$push": {'vendor':'[extreme]', 'hardware':'[extreme_wifi]'}} )
    print("Updating Aerohive Wifi (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':aerohive:'}}, {"$push": {'sec_vendor':'[extreme]', 'sec_hardware':'[extreme_wifi'}} )
    print("Updating Aerohive Wifi (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Find All Extreme Networks O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:extremenetworks:'}}, {"$push": {'vendor':'[extreme]', 'os':'[extreme_os]'}} )
    print("Updating Extreme Operating Systems - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:extremenetworks:'}}, {"$push": {'vendor':'[extreme]', 'application':'[extreme_app]'}} )
    print("Updating Extreme Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:extremenetworks:'}}, {"$push": {'vendor':'[extreme]', 'hardware':'[extreme_hw]'}} )
    print("Updating Extreme Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#-----------------------------------------------------------------------------------------------------------------------------------------
#----- Vendor Forescout -----#
    print("Vendor: Forescout");
#----- Forescout Software - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':forescout:'}}, {"$push": {'vendor':'[forescout]', 'application':'[forescout]'}} )
    print("Updating Forescout (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':forescout:'}}, {"$push": {'sec_vendor':'[forescout]', 'sec_application':'[forescout]'}} )
    print("Updating Forescout (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- Find All Forescout O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:forescout:'}}, {"$push": {'vendor':'[forescout]', 'os':'[forescout_os]'}} )
    print("Updating Forescout OS - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:forescout:'}}, {"$push": {'vendor':'[forescout]', 'application':'[forescout_app]'}} )
    print("Updating Forescout Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:forescout:'}}, {"$push": {'vendor':'[forescout]', 'hardware':'[forescout_hw]'}} )
    print("Updating Forescout Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#-----------------------------------------------------------------------------------------------------------------------------------------
#----- Vendor Forinet -----#
    print("Vendor: Forinet");
#----- FortiNAC - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':fortinac:'}}, {"$push": {'vendor':'[fortinet]', 'application':'[fortinac]'}} )
    print("Updating Fortinac (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':fortinac:'}}, {"$push": {'sec_vendor':'[fortinet]', 'sec_application':'[fortinac]'}} )
    print("Updating Fortinac (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

#----- FortiGate - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':fortinet:fortios:'}}, {"$push": {'vendor':'[fortinet]', 'os':'[fortios]', 'hardware':'[fortinet_fw]'}} )
    print("Updating Fortinac (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':fortinet:fortios:'}}, {"$push": {'sec_vendor':'[fortinet]','sec_os':'[fortios]', 'sec_hardware':'[fortinet_fw]'}} )
    print("Updating Fortinac (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

#----- Vendor CheckPoint -----#
    print("Vendor: CheckPoint");
#----- CheckPoint - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':checkpoint:'}}, {"$push": {'vendor':'[checkpoint]', 'hardware':'[checkpoint_fw]'}} )
    print("Updating CheckPoint (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':checkpoint:'}}, {"$push": {'sec_vendor':'[checkpoint]', 'sec_hardware':'[checkpoint_fw]'}} )
    print("Updating CheckPoint (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

#----- Vendor PaloAlto -----#
    print("Vendor: PaloAlto");
#----- Palo Firewall - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':paloaltonetworks:pan-os:'}}, {"$push": {'vendor':'[palo_alto]', 'hardware':'[palo_fw]'}} )
    print("Updating Palo Firewall (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':paloaltonetworks:pan-os:'}}, {"$push": {'sec_vendor':'[palo_alto]', 'sec_hardware':'[palo_fw]'}} )
    print("Updating Palo Firewall (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#----- PaloAlto SD-WAN (CloudGenix) - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':paloaltonetworks:prisma'}}, {"$push": {'vendor':'[palo_alto]', 'application':'[palo_sdwan]'}} )
    print("Updating PaloAlto Prisma/Cloudgenix (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':paloaltonetworks:prisma'}}, {"$push": {'vendor':'[palo_alto]', 'sec_application':'[palo_sdwan]'}} )
    print("Updating PaloAlto Prisma/Cloudgenix (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);


#----- Vendor VMware -----#
    print("Vendor: VMware");
#----- VMware SD-WAN (Velocloud) - Primary and Secondary
    updateResult = collection.update_many({ "$or": [{'product': {'$regex':':vmware:velocloud'}}, {'product': {'$regex':':vmware:sd-wan'}} ]}, {"$push": {'vendor':'[vmware]', 'application':'[vmware_sdwan]'}} )
    print("Updating VMware SD-WAN (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({ "$or": [{'products': {'$regex':':vmware:velocloud'}}, {'products': {'$regex':':vmware:sd-wan'}} ]}, {"$push": {'vendor':'[vmware]', 'sec_application':'[vmware_sdwan]'}} )
    print("Updating VMware SD-WAN (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

#----- Vendor Citrix -----#
    print("Vendor: Citrix");
#----- Citrix SD-WAN - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':citrix:netscaler_sd-wan'}}, {"$push": {'vendor':'[citrix]', 'application':'[citrix_sdwan]'}} )
    print("Updating Citrix SD-WAN (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':citrix:netscaler_sd-wan'}}, {"$push": {'vendor':'[citrix]', 'sec_application':'[citrix_sdwan]'}} )
    print("Updating Citrix SD-WAN (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

#----- Vendor Zoom -----#
    print("Vendor: Zoom");
#----- Zoom Conferencing - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':zoom:zoom'}}, {"$push": {'vendor':'[zoom]', 'application':'[zoom]'}} )
    print("Updating Zoom (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':zoom:zoom'}}, {"$push": {'sec_vendor':'[zoom]', 'sec_application':'[zoom]'}} )
    print("Updating Zoom (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

#----- Vendor Microsoft -----#
    print("Vendor: Microsoft");
#----- Teams Conferencing - Primary and Secondary
    updateResult = collection.update_many({'product': {'$regex':':microsoft:teams'}}, {"$push": {'vendor':'[microsoft]', 'application':'[teams]'}} )
    print("Updating MS Teams (Primary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'products': {'$regex':':microsoft:teams'}}, {"$push": {'sec_vendor':'[microsoft]', 'sec_application':'[teams]'}} )
    print("Updating MS Teams (Secondary) - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

#----- Find All Microsoft O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:microsoft:'}}, {"$push": {'vendor':'[microsoft]', 'os':'[microsoft_os]'}} )
    print("Updating Microsoft Operating Systems - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:microsoft:'}}, {"$push": {'vendor':'[microsoft]', 'application':'[microsoft_app]'}} )
    print("Updating Microsoft Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:microsoft:'}}, {"$push": {'vendor':'[microsoft]', 'hardware':'[microsoft_hw]'}} )
    print("Updating Microsoft Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#-----------------------------------------------------------------------------------------------------------------------------------------
#----- Find All Apple O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:apple:'}}, {"$push": {'vendor':'[apple]', 'os':'[apple_os]'}} )
    print("Updating Apple Operating Systems - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:apple:'}}, {"$push": {'vendor':'[apple]', 'application':'[apple_app]'}} )
    print("Updating Apple Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:apple:'}}, {"$push": {'vendor':'[apple]', 'hardware':'[apple_hw]'}} )
    print("Updating Apple Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#-----------------------------------------------------------------------------------------------------------------------------------------
#----- Find All Huawei O:A:H products in Primary
    updateResult = collection.update_many({'product': {'$regex':':o:huawei:'}}, {"$push": {'vendor':'[huawei]', 'os':'[huawei_os]'}} )
    print("Updating Huawei Operating Systems - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':a:huawei:'}}, {"$push": {'vendor':'[huawei]', 'application':'[huawei_app]'}} )
    print("Updating Huawei Applications - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);

    updateResult = collection.update_many({'product': {'$regex':':h:huawei:'}}, {"$push": {'vendor':'[huawei]', 'hardware':'[huawei_hw]'}} )
    print("Updating Huawei Hardware - Matched: ", updateResult.matched_count, " Modified: ", updateResult.modified_count);
#-----------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    return_value = main()
