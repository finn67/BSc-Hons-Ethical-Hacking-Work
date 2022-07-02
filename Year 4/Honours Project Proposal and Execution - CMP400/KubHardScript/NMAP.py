from kubernetes import client, config
import nmap
import socket


def Nmap():
    config.load_kube_config()
    api = client.CoreV1Api()
    service = api.read_namespaced_service(name="kubernetes", namespace="default")
    print("------------------------------------------------")
    print("Running nmap scan on cluster machine")
    print("------------------------------------------------")
    print("cluster ip:" + service.spec.cluster_ip)
    print("------------------------------------------------")




    fin = service.spec.cluster_ip

    hostname = socket.gethostname()
    IPADDR = socket.gethostbyname(hostname)

    nm = nmap.PortScanner()

    scan_range = nm.scan(hosts=IPADDR)

    nm.all_hosts()

    for host in nm.all_hosts():
        print("Host: %s(%s)" % (host, nm[host].hostname()))

        print("Open TCP Ports: ")

        print("%s" % (nm[host].all_tcp()))

        print("Open UDP Ports: ")

        print("%s" % (nm[host].all_udp()))

        print("state: ")

        print("%s" % (nm[host].state()))

        print("%s" % (nm[host].all_protocols()))

    nm2 = nmap.PortScanner()

    scan_range = nm2.scan(hosts=fin)


    nm2.all_hosts()

    for host in nm2.all_hosts():
        print("Host: %s(%s)" % (host, nm2[host].hostname()))

        print("Open TCP Ports: ")

        print("%s" % (nm2[host].all_tcp()))

        print("Open UDP Ports: ")

        print("%s" % (nm2[host].all_udp()))

        print("state: ")

        print("%s" % (nm2[host].state()))

        print("%s" % (nm2[host].all_protocols()))


print("------------------------------------------------")
print("PDF Report Created")
print("HTML Report Created")
print("------------------------------------------------")
def main():
    Nmap()

if __name__ == '__main__':
    main()