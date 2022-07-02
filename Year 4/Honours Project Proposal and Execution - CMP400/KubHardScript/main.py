from kubernetes import client, config
from termcolor import colored
import subprocess
import MasterNode
import ReportHTML
import Report
import WorkerNodes

import etcd
from NMAP import Nmap
from etcd import etcd
import sys
import subprocess
import pkg_resources

def info():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    print("------------------------------------------------")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    print("------------------------------------------------")
    print("Supported APIs (* is preferred version):")
    print("------------------------------------------------")
    print("%-40s %s" %
          ("core", ",".join(client.CoreApi().get_api_versions().versions)))
    for api in client.ApisApi().get_api_versions().groups:
        versions = []
        for v in api.versions:
            name = ""
            if v.version == api.preferred_version.version and len(
                    api.versions) > 1:
                name += "*"
            name += v.version
            versions.append(name)
        print("%-40s %s" % (api.name, ",".join(versions)))

def hardening():
    print("test")




def requirments():
    required = {'python-nmap', 'kubernetes', 'PyYAML', 'termcolor'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.PIPE)



def main():
    requirments()
    info()
    MasterNode.main()
    etcd()
    WorkerNodes.main()
    Nmap()
    ReportHTML
    Report



main();
