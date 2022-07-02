from termcolor import colored
import array
import subprocess
import json

def etcd():

    with open('etcd.json', "w") as outfile:
        test = subprocess.run(["checkov", "--compact", "--quiet", "-o", "json", "-f", "/etc/kubernetes/manifests/etcd.yaml"], stdout=outfile, stderr=subprocess.PIPE,
                                    text=True)

    with open('etcd.json', 'r') as json_file:
        json_load = json.load(json_file)

    print("------------------------------------------------")
    print("etcd.yaml file")
    print("------------------------------------------------")
    passed = (json_load['summary']['passed'])
    failed = (json_load['summary']['failed'])

    print("Passed:")
    print(colored(passed, 'green'))
    print("Failed:")
    print(colored(failed, 'red'))
    print(colored("Full details and remadations can be found in kube-controller-manager.json", 'yellow'))







def main():
    etcd()

if __name__ == '__main__':
    main()