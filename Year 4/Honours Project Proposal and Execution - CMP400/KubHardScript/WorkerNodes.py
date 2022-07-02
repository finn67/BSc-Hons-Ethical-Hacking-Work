from kubernetes import client, config
from termcolor import colored
import array
import subprocess
import yaml

import os
cmds = "/etc/systemd/system/kubelet.service.d/10-kubeadm.conf", "/var/lib/kubelet/config.yaml"
array.test = []
pas = ""
test1 = "authorization-mode"

def permissions():
    # array.stdout = []
    print("------------------------------------------------")
    print("Ensuring specification file/dirs permissions are set correctly i.e 700/644")
    print("------------------------------------------------")
    for cmd in cmds:
        PodPermissions = subprocess.run(["stat", "-c", "%a", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True)
        output = (PodPermissions.stdout)

        # output = ''.join(filter(str.isdigit, output))
        test = (int(output))
        print(cmd)

        if test >= 644:
            pas = "pass"
            print(colored(pas, 'green'))

        elif test <= 643:
            pas = "fail"
            print(colored(pas, 'red'))
            for cmd in cmds:
                PodPermissions = subprocess.run(["chmod", "644", cmd], stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE, text=True)
                # PodPermissions = (int(PodPermissions.stdout))
                # print(PodPermissions)





def fileOwnership():
    print("------------------------------------------------")
    print("Ensuring that the API server pod specification file ownership is set to root:root.")
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










def main():
    permissions()
    fileOwnership()





if __name__ == '__main__':
    main()