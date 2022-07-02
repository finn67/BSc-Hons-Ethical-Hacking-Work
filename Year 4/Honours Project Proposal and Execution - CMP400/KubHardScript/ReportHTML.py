import json
import matplotlib.pyplot as plt
import numpy as np
import time
from time import time, ctime
json1 = "kube-scheduler.json", "kube-apiserver.json", "kube-controller-manager.json", "etcd.json"

def Summary():

    passed = []
    failed = []

    for j in json1:
        with open(j, 'r') as json_file:
            json_load = json.load(json_file)

        passedJ = (json_load['summary']['passed'])
        passed.append(passedJ)




    for j in json1:
        with open(j, 'r') as json_file:
            json_load = json.load(json_file)

        failedJ = (json_load['summary']['failed'])
        failed.append(failedJ)

    labels = ['Scheduler', 'Apiserver', 'Controller-Manager', 'etcd']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, passed, width, color="green", label='Passed')
    rects2 = ax.bar(x + width / 2, failed, width, color="red", label='Failed')

    ax.set_ylabel('Scores')
    ax.set_title('Scores of Kubernetes YAML files')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.savefig("Summary.png")

def sched():
    with open(json1[0], 'r') as json_file:
        json_load = json.load(json_file)
    y = []
    counterCapa = 0
    counterRootC = 0
    counterSeriveA = 0
    counterLimits = 0
    counterImage = 0
    counterTotal = 0
    MiscCalc = 0


    test = json_load["results"]["failed_checks"]

    for index in range(len(test)):
        for key, value in test[index].items():
                # print(value)
                # print(test)
                if key == "check_class":
                    # y = [value]
                    # print(y)
                    counterTotal = counterTotal + 1

                    if "Capabilities" in value:
                        counterCapa = counterCapa + 1

                    elif "RootContainers" in value:
                        counterRootC = counterRootC + 1

                    elif "Limits" in value:
                        counterLimits = counterLimits + 1

                    elif "Service" in value:
                        counterSeriveA = counterSeriveA + 1

                    elif "Image" in value:
                        counterImage = counterImage + 1


    Misc = counterCapa + counterRootC + counterSeriveA + counterImage + counterLimits
    MiscCalc = counterTotal - Misc
    CounterT = [counterCapa, counterRootC, counterSeriveA, counterImage, MiscCalc]
    labels = 'Capabilities', 'RootContainer', 'Limits', 'Service', 'Image'

    fig1, ax1 = plt.subplots()
    ax1.pie(CounterT, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Distribution of Failed Checks in kube-scheduler.yaml")
    plt.show()
    plt.savefig("kube-scheduler.png")


def API():
    with open(json1[1], 'r') as json_file:
        json_load = json.load(json_file)
    y = []
    counterServiceAcc = 0
    counterAuditLog = 0
    counterContainer = 0
    counterLimits = 0
    counterApi = 0
    counterTotal = 0
    MiscCalc = 0


    test = json_load["results"]["failed_checks"]

    for index in range(len(test)):
        for key, value in test[index].items():
                # print(value)
                if key == "check_class":
                    # y = [value]
                    # print(y)
                    counterTotal = counterTotal + 1
                    if "ServiceAccount" in value:
                        counterServiceAcc = counterServiceAcc + 1

                    elif "Container" in value:
                        counterContainer = counterContainer + 1

                    elif "AuditLog" in value:
                        counterAuditLog = counterAuditLog + 1

                    elif "Api" in value:
                        counterApi = counterApi + 1

                    elif "Limitis" in value:
                        counterLimits = counterLimits + 1



    Misc = counterApi + counterAuditLog + counterContainer + counterServiceAcc + counterLimits
    MiscCalc = counterTotal - Misc

    CounterT = [counterServiceAcc, counterAuditLog, counterContainer, counterApi, MiscCalc]

    labels = 'ServiceAccount', 'AuditLog', 'Container', 'API', 'Misc'

    fig1, ax1 = plt.subplots()
    ax1.pie(CounterT, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Distribution of Failed Checks in kube-apiserver.yaml")
    plt.show()
    plt.savefig("kube-apiserver.png")

def CM():
    with open(json1[2], 'r') as json_file:
        json_load = json.load(json_file)
    y = []
    counterCapa = 0
    counterRootC = 0
    counterSeriveA = 0
    counterLimits = 0
    counterImage = 0
    counterTotal = 0
    counterKCM = 0
    MiscCalc = 0


    test = json_load["results"]["failed_checks"]

    for index in range(len(test)):
        for key, value in test[index].items():
                # print(value)
                # print(test)
                if key == "check_class":
                    # y = [value]
                    # print(y)
                    counterTotal = counterTotal + 1

                    if "Capabilities" in value:
                        counterCapa = counterCapa + 1

                    elif "RootContainers" in value:
                        counterRootC = counterRootC + 1

                    elif "Limits" in value:
                        counterLimits = counterLimits + 1

                    elif "Service" in value:
                        counterSeriveA = counterSeriveA + 1

                    elif "Image" in value:
                        counterImage = counterImage + 1
                    elif "KubeControllerManager" in value:
                        counterKCM = counterKCM + 1




    Misc = counterCapa + counterRootC + counterSeriveA + counterImage + counterLimits + counterKCM
    MiscCalc = counterTotal - Misc

    CounterT = [counterCapa, counterRootC, counterSeriveA, counterImage, counterKCM, MiscCalc]
    labels = 'Capabilities', 'RootContainer', 'Service', 'Image', 'KCM', 'Misc'

    fig1, ax1 = plt.subplots()
    ax1.pie(CounterT, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Distribution of Failed Checks in kube-controller-manager.yaml")
    plt.show()
    plt.savefig("kube-controller-manager.png")

def etcd():
    with open(json1[3], 'r') as json_file:
        json_load = json.load(json_file)
    y = []
    counterCapa = 0
    counterRootC = 0
    counterSeriveA = 0
    counterLimits = 0
    counterImage = 0
    counterTotal = 0
    counterKCM = 0
    MiscCalc = 0


    test = json_load["results"]["failed_checks"]

    for index in range(len(test)):
        for key, value in test[index].items():
                # print(value)
                # print(test)
                if key == "check_class":
                    # y = [value]
                    # print(y)
                    counterTotal = counterTotal + 1

                    if "Capabilities" in value:
                        counterCapa = counterCapa + 1

                    elif "RootContainers" in value:
                        counterRootC = counterRootC + 1

                    elif "Limits" in value:
                        counterLimits = counterLimits + 1

                    elif "Service" in value:
                        counterSeriveA = counterSeriveA + 1

                    elif "Image" in value:
                        counterImage = counterImage + 1
                    elif "KubeControllerManager" in value:
                        counterKCM = counterKCM + 1




    Misc = counterCapa + counterRootC + counterSeriveA + counterImage + counterLimits
    MiscCalc = counterTotal - Misc


    CounterT = [counterCapa, counterRootC, counterSeriveA, counterImage, counterLimits, MiscCalc]
    labels = 'Capabilities', 'RootContainer', 'Service', 'Image', 'Limits','Misc'

    fig1, ax1 = plt.subplots()
    ax1.pie(CounterT, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Distribution of Failed Checks in etcd.yaml")
    plt.show()
    plt.savefig("etcd.png")



def html():
    passed = []
    failed = []

    for j in json1:
        with open(j, 'r') as json_file:
            json_load = json.load(json_file)

        passedJ = (json_load['summary']['passed'])
        passed.append(passedJ)
    for j in json1:
        with open(j, 'r') as json_file:
            json_load = json.load(json_file)

        failedJ = (json_load['summary']['failed'])
        failed.append(failedJ)

    passedT = sum(passed)
    failedT = sum(failed)



    # print(failedT)
    # print(passedT)
    t = time()
    timeM = ctime(t)
    text = f"""

   <!DOCTYPE html>
<html lang="en">
<head>
<title>CSS Template</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="HTML.css">
</head>
<body>

<header>
  <h2>Kubernetes Hardening Report</h2>
</header>
<img id = "sum" src="Summary.png" alt="Trulli" width="600" height="370">
<h4 id = "hedp">Passed:</h4>
    <p class = "passed1">{passedT}</p>
    <h4 id ="hedf">Failed:</h4>
    <p class = "failed1">{failedT}</p>
    </div>
<section>
  <nav>
    <img id = "kube-scheduler" src="kube-scheduler.png" alt="Trulli" width="374" height="300">
  </nav>
  
  <article>
    <h1 id = "Sched">kube-scheduler.yaml</h1>
    <h4>Passed:</h4>
    <p class = "passed">{passed[0]}</p>
    <h4>Failed:</h4>
    <p class = "failed">{failed[0]}</p>
    <p>The Kubernetes scheduler is a control plane process which assigns Pods to Nodes. The scheduler determines which Nodes are valid placements for each Pod in the scheduling queue according to constraints and available resources. The scheduler then ranks each valid Node and binds the Pod to a suitable Node</p>
  </article>
</section>

<section>
  <nav>
    <img id = "kube-scheduler" src="kube-apiserver.png" alt="Trulli" width="374" height="300">
  </nav>
  
  <article>
    <h1 id = "Sched">kube-apiserver.YAML</h1>
    <h4>Passed:</h4>
    <p class = "passed">{passed[1]}</p>
    <h4>Failed:</h4>
    <p class = "failed">{failed[1]}</p>
    <p>The Kubernetes API server validates and configures data for the api objects which include pods, services, replicationcontrollers, and others. The API Server services REST operations and provides the frontend to the cluster's shared state through which all other components interact.</p>
  </article>
</section>

<section>
  <nav>
    <img id = "kube-scheduler" src="kube-controller-manager.png" alt="Trulli" width="374" height="300">
  </nav>
  
  <article>
    <h1 id = "Sched">kube-controller-manager.YAML</h1>
    <h4>Passed:</h4>
    <p class = "passed">{passed[2]}</p>
    <h4>Failed:</h4>
    <p class = "failed">{failed[2]}</p>
    <p>The Kubernetes controller manager is a daemon that embeds the core control loops shipped with Kubernetes. In applications of robotics and automation, a control loop is a non-terminating loop that regulates the state of the system.</p>
  </article>
</section>

<section>
  <nav>
    <img id = "kube-scheduler" src="etcd.png" alt="Trulli" width="374" height="300">
  </nav>
  
  <article>
    <h1 id = "Sched">etcd.YAML</h1>
    <h4>Passed:</h4>
    <p class = "passed">{passed[3]}</p>
    <h4>Failed:</h4>
    <p class = "failed">{failed[3]}</p>
    <p>etcd is a consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.</p>
  </article>
</section>
<footer>
<p>{timeM}</p>
</footer>

</body>

</html>


    """


    strSec = str(t)
    strSec = 'HTML_Report' + strSec + ".HTML"

    file = open(strSec, "w")

    file.write(text)

    file.close()






def main():
    Summary()
    sched()
    API()
    CM()
    etcd()
    html()



main()