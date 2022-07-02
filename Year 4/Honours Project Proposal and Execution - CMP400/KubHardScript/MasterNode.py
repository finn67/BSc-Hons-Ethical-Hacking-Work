from kubernetes import client, config
from termcolor import colored
import array
import subprocess
import json
import yaml
import os


cmds = "/etc/kubernetes/manifests/kube-apiserver.yaml", \
       "/etc/kubernetes/manifests/kube-controller-manager.yaml", \
       "/etc/kubernetes/manifests/etcd.yaml", "/etc/kubernetes/manifests/kube-scheduler.yaml", \
       "/etc/kubernetes/admin.conf","/etc/kubernetes/controller-manager.conf", \
       "/etc/kubernetes/pki/apiserver.crt", "/etc/kubernetes/pki/apiserver-etcd-client.crt", "/etc/kubernetes/pki/apiserver-kubelet-client.crt", "/etc/kubernetes/pki/ca.crt", "/etc/kubernetes/pki/front-proxy-ca.crt", "/etc/kubernetes/pki/front-proxy-client.crt"
cmdsEtcd = "/etc/kubernetes/pki/etcd"
array.test = []
pas = ""

def permissions():
    # array.stdout = []
    print("------------------------------------------------")
    print("Ensuring specification file/dirs permissions are set correctly i.e 700/644")
    print("------------------------------------------------")
    for cmd in cmds:
        PodPermissions = subprocess.run(["stat", "-c", "%a", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True)
        output = (int(PodPermissions.stdout))
        test = output
        print(cmd)

        if test >= 644:
            pas = "pass"
            print(colored(pas, 'green'))

        elif test <= 600:
            pas = "fail"
            print(colored(pas, 'red'))
            for cmd in cmds:
                PodPermissions = subprocess.run(["chmod", "644", cmd], stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE, text=True)
                # PodPermissions = (int(PodPermissions.stdout))
                # print(PodPermissions)

    etcd = subprocess.run(["stat", "-c", "%a", cmdsEtcd], stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE, text=True)
    output = int(etcd.stdout)
    print(cmdsEtcd)
    if output >= 700:
        pas = "pass"
        print(colored(pas, 'green'))

    elif output < 700:
        pas = "fail"
        print(colored(pas, 'red'))
        subprocess.run(["chmod", "700", cmdsEtcd], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, text=True)



def fileOwnership():
    print("------------------------------------------------")
    print("Ensuring that the specification file ownership is set to root:root.")
    print("------------------------------------------------")


    for cmd in cmds:
        PodfileOwner = subprocess.run(["stat", "-c", "%U:%G", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True)
        output = (str(PodfileOwner.stdout))
        output = output.strip()
        print(cmd)

        if output == "root:root":
            pas = "pass"
            print(colored(pas, 'green'))

        else:
            pas = "fail"
            print(colored(pas, 'red'))
            for cmd in cmds:
                PodPermissions = subprocess.run(["chown", "root:root", cmd], stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                # PodPermissions = (int(PodPermissions.stdout))
                # print(PodPermissions)

    etcd = subprocess.run(["stat", "-c", "%U:%G", cmdsEtcd], stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=True)
    output = etcd.stdout
    output = output.strip()
    print(cmdsEtcd)
    if output == "root:root":
        pas = "pass"
        print(colored(pas, 'green'))

    else:
        pas = "fail"
        print(colored(pas, 'red'))
        subprocess.run(["chown", "root:root", cmdsEtcd], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, text=True)





def ApiYaml():
    with open('kube-apiserver.json', "w") as outfile:
        test = subprocess.run(["checkov", "--compact", "--quiet", "-o", "json", "-f", "/etc/kubernetes/manifests/kube-apiserver.yaml"], stdout=outfile, stderr=subprocess.PIPE,
                                    text=True)

    with open('kube-apiserver.json', 'r') as json_file:
        json_load = json.load(json_file)

    print("------------------------------------------------")
    print("Running checks on the kube-apiserver.yaml file")
    print("------------------------------------------------")
    passed = (json_load['summary']['passed'])
    failed = (json_load['summary']['failed'])

    print("Passed:")
    print(colored(passed, 'green'))
    print("Failed:")
    print(colored(failed, 'red'))
    print(colored("Full details and remadations can be found in kube-apiserver.json", 'yellow'))

def KCMYaml():
    with open('kube-controller-manager.json', "w") as outfile:
        test = subprocess.run(["checkov", "--compact", "--quiet", "-o", "json", "-f", "/etc/kubernetes/manifests/kube-controller-manager.yaml"], stdout=outfile, stderr=subprocess.PIPE,
                                    text=True)

    with open('kube-controller-manager.json', 'r') as json_file:
        json_load = json.load(json_file)

    print("------------------------------------------------")
    print("Running checks on the kube-controller-manager.yaml file")
    print("------------------------------------------------")
    passed = (json_load['summary']['passed'])
    failed = (json_load['summary']['failed'])

    print("Passed:")
    print(colored(passed, 'green'))
    print("Failed:")
    print(colored(failed, 'red'))
    print(colored("Full details and remadations can be found in kube-controller-manager.json", 'yellow'))

def SchedYaml():

    with open('kube-scheduler.json', "w") as outfile:
        test = subprocess.run(["checkov", "--compact", "--quiet", "-o", "json", "-f", "/etc/kubernetes/manifests/kube-scheduler.yaml"], stdout=outfile, stderr=subprocess.PIPE,
                                    text=True)

    with open('kube-scheduler.json', 'r') as json_file:
        json_load = json.load(json_file)

    print("------------------------------------------------")
    print("Running checks on the kube-scheduler.yaml file")
    print("------------------------------------------------")
    passed = (json_load['summary']['passed'])
    failed = (json_load['summary']['failed'])

    print("Passed:")
    print(colored(passed, 'green'))
    print("Failed:")
    print(colored(failed, 'red'))
    print(colored("Full details and remadations can be found in kube-scheduler.json", 'yellow'))

def main():
    permissions()
    fileOwnership()
    ApiYaml()
    KCMYaml()
    SchedYaml()













if __name__ == '__main__':
    main()