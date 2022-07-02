import json
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from reportlab.platypus import Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from time import time, ctime


json1 = "kube-scheduler.json", "kube-apiserver.json", "kube-controller-manager.json", "etcd.json"
t = time()
timeM = ctime(t)

style = ParagraphStyle(
    name='Normal',
    fontSize=20,
)
stylePassed = ParagraphStyle(
    name='Normal',
    fontSize=14,
    textColor=(HexColor('#038a27')),
    # leading=15,
    leftIndent=320,
)
styleFailed = ParagraphStyle(
    name='Normal',
    fontSize=14,
    textColor=(HexColor('#FF0000')),
    leftIndent=320,
)
stylePassedH = ParagraphStyle(
    name='Normal',
    fontSize=14,
    leftIndent=320,
)
styleFailedH = ParagraphStyle(
    name='Normal',
    fontSize=14,
    leftIndent=320,
)




style1 = ParagraphStyle(
    name='Normal',
    fontSize=40,
    leftIndent=25,
)

style2 = ParagraphStyle(
    name='Normal',
    fontSize=12,
    leftIndent=210,
)

style3 = ParagraphStyle(
    name='Normal',
    fontSize=17,
)

style4 = ParagraphStyle(
    name='Normal',
    fontSize=12,
    leading=15,
    spaceBefore=17,
    textColor=(HexColor('#038a27')),
)
style5 = ParagraphStyle(
    name='Normal',
    fontSize=11,
    leading=18,
    spaceBefore=17,
)

style6 = ParagraphStyle(
    name='Normal',
    fontSize=12,
    leading=15,
    spaceBefore=40,
    textColor=(HexColor('#e62727')),
)

styleSchedH = ParagraphStyle(
    name='Normal',
    fontSize=15,
    leftIndent=20,


)
styleSchedP = ParagraphStyle(
    name='Normal',
    fontSize=13,
    leftIndent=50,
    textColor=(HexColor('#038a27')),



)
styleSchedF = ParagraphStyle(
    name='Normal',
    fontSize=13,
    leftIndent=50,
    textColor=(HexColor('#FF0000')),



)



styles = getSampleStyleSheet()
story = []
story1 = []
story2 = []
story3 = []
story4 = []
story5 = []
story6 = []
story7 = []
story10 = []
story11 = []
story12 = []
story13 = []
story14 = []

passed = []
failed = []
sum2 = []
image = "kubernetes-horizontal-color.png"
image2 = "kube-apiserver.png"
image3 = "kube-scheduler.png"
image4 = "kube-controller-manager.png"
image5 = "etcd.png"

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

for j in json1:
    with open(json1[0], 'r') as json_file:
        json_load = json.load(json_file)

    sum1 = (json_load['summary'])

    sum2.append(sum1)






passedT = sum(passed)
failedT = sum(failed)

story.append(Paragraph("The Cluster Score is:", style))
story.append(Paragraph("Passed:", stylePassedH))
story.append(Paragraph(str(passedT), stylePassed))
story.append(Paragraph("Failed:", styleFailedH))
story.append(Paragraph(str(failedT), styleFailed))
story11.append(Image('Summary.png',  width=330, height=305))
# story10.append(Paragraph("kube-scheduler.YAML", styleSchedH))
# story10.append(Paragraph(str(passed[0]), styleSchedP))
# story10.append(Paragraph(str(failed[0]), styleSchedF))
# story10.append(Paragraph("kube-scheduler.YAML", styleSchedH))
# story10.append(Paragraph(str(passed[1]), styleSchedP))
# story10.append(Paragraph(str(failed[1]), styleSchedF))

t = time()
t2 = str(t)

c = Canvas('PDF_Report' + t2 + '.pdf')
c.setFont("Helvetica", 16)
c.drawString(100, 245, "kube-scheduler.YAML")
c.setFillColor(HexColor('#038a27'))
c.drawString(120, 227, str(passed[0]))
c.setFillColor(HexColor('#FF0000'))
c.drawString(200, 227, str(failed[0]))

c.setFillColor(HexColor('#000000'))

c.drawString(100, 200, "kube-apiserver.YAML")
c.setFillColor(HexColor('#038a27'))
c.drawString(120, 182, str(passed[1]))
c.setFillColor(HexColor('#FF0000'))
c.drawString(200, 182, str(failed[1]))

c.setFillColor(HexColor('#000000'))

c.drawString(100, 155, "kube-controller-manager.YAML")
c.setFillColor(HexColor('#038a27'))
c.drawString(120, 137, str(passed[2]))
c.setFillColor(HexColor('#FF0000'))
c.drawString(200, 137, str(failed[2]))

c.setFillColor(HexColor('#000000'))

c.drawString(100, 110, "etcd.YAML")
c.setFillColor(HexColor('#038a27'))
c.drawString(120, 92, str(passed[3]))
c.setFillColor(HexColor('#FF0000'))
c.drawString(200, 92, str(failed[3]))

c.setFillColor(HexColor('#038a27'))
c.drawString(370, 200, "Passed")
c.setFillColor(HexColor('#FF0000'))
c.drawString(370, 150, "Failed")
c.setFont("Courier", 10)
c.setFillColor(HexColor('#000000'))
c.drawCentredString(4 * inch, 0.2 * inch, timeM)

f = Frame(1 * inch, 9.4 * inch, 6 * inch, 1.5 * inch, showBoundary=1)
f1 = Frame(1 * inch, 4.2 * inch, 6 * inch, 5 * inch, showBoundary=1)
f3 = Frame(1 * inch, 0.5 * inch, 6 * inch, 3.5 * inch, showBoundary=1)


f.addFromList(story, c)
f.addFromList(story3, c)
f.addFromList(story4, c)
f1.addFromList(story1, c)
f3.addFromList(story2, c)
f1.addFromList(story6, c)
f3.addFromList(story5, c)
f1.addFromList(story7, c)
f1.addFromList(story11, c)
f3.addFromList(story10, c)
f3.addFromList(story12, c)



c.drawImage(image, 2.2 * inch, 11 * inch, width=230, height=45)

c.showPage()




f4 = Frame(1 * inch, 0.9 * inch, 6 * inch, 10 * inch, showBoundary=1)
f4.addFromList(story, c)
c.setFont("Helvetica", 23)
c.drawString(180, 740, "kube-scheduler.YAML")
c.drawImage(image, 2.2 * inch, 11 * inch, width=230, height=45)
c.drawImage(image3, 1.15 * inch, 6.1 * inch, width=400, height=275)


# c.setFillColor(HexColor('#000000'))



c.setFont("Helvetica", 18)
c.drawString(180, 420, "Passed")
c.setFillColor(HexColor('#038a27'))
c.drawString(200, 390, str(passed[0]))

c.setFillColor(HexColor('#000000'))
c.drawString(340, 420, "Failed")
c.setFillColor(HexColor('#000000'))
c.setFillColor(HexColor('#FF0000'))
c.drawString(357, 390, str(failed[0]))
c.setFillColor(HexColor('#000000'))
c.setFont("Helvetica", 11)
c.setFont("Courier", 10)
c.setFillColor(HexColor('#000000'))
c.drawCentredString(4 * inch, 0.2 * inch, timeM)

c.showPage()
c.setFont("Courier", 10)
c.setFillColor(HexColor('#000000'))
c.drawCentredString(4 * inch, 0.2 * inch, timeM)
f5 = Frame(1 * inch, 0.9 * inch, 6 * inch, 10 * inch, showBoundary=1)
f5.addFromList(story, c)
c.setFont("Helvetica", 23)
c.drawString(180, 740, "kube-apiserver.YAML")
c.drawImage(image, 2.2 * inch, 11 * inch, width=230, height=45)
c.drawImage(image2, 1.15 * inch, 6.1 * inch, width=400, height=275)


# c.setFillColor(HexColor('#000000'))



c.setFont("Helvetica", 18)
c.drawString(180, 420, "Passed")
c.setFillColor(HexColor('#038a27'))
c.drawString(200, 390, str(passed[1]))

c.setFillColor(HexColor('#000000'))
c.drawString(340, 420, "Failed")
c.setFillColor(HexColor('#000000'))
c.setFillColor(HexColor('#FF0000'))
c.drawString(357, 390, str(failed[1]))
c.setFillColor(HexColor('#000000'))
c.setFont("Helvetica", 11)







c.showPage()

c.setFont("Courier", 10)
c.setFillColor(HexColor('#000000'))
c.drawCentredString(4 * inch, 0.2 * inch, timeM)
f6 = Frame(1 * inch, 0.9 * inch, 6 * inch, 10 * inch, showBoundary=1)
f6.addFromList(story, c)
c.setFont("Helvetica", 23)
c.drawString(150, 740, "kube-controller-manager.YAML")
c.drawImage(image, 2.2 * inch, 11 * inch, width=230, height=45)
c.drawImage(image4, 1.15 * inch, 6.1 * inch, width=400, height=275)


# c.setFillColor(HexColor('#000000'))



c.setFont("Helvetica", 18)
c.drawString(180, 420, "Passed")
c.setFillColor(HexColor('#038a27'))
c.drawString(200, 390, str(passed[2]))

c.setFillColor(HexColor('#000000'))
c.drawString(340, 420, "Failed")
c.setFillColor(HexColor('#000000'))
c.setFillColor(HexColor('#FF0000'))
c.drawString(357, 390, str(failed[2]))
c.setFillColor(HexColor('#000000'))
c.setFont("Helvetica", 11)

c.showPage()
c.setFont("Courier", 10)
c.setFillColor(HexColor('#000000'))
c.drawCentredString(4 * inch, 0.2 * inch, timeM)
f7 = Frame(1 * inch, 0.9 * inch, 6 * inch, 10 * inch, showBoundary=1)
f7.addFromList(story, c)
c.setFont("Helvetica", 23)
c.drawString(230, 740, "etcd.YAML")
c.drawImage(image, 2.2 * inch, 11 * inch, width=230, height=45)
c.drawImage(image5, 1.15 * inch, 6.1 * inch, width=400, height=275)


# c.setFillColor(HexColor('#000000'))



c.setFont("Helvetica", 18)
c.drawString(180, 420, "Passed")
c.setFillColor(HexColor('#038a27'))
c.drawString(200, 390, str(passed[3]))

c.setFillColor(HexColor('#000000'))
c.drawString(340, 420, "Failed")
c.setFillColor(HexColor('#000000'))
c.setFillColor(HexColor('#FF0000'))
c.drawString(357, 390, str(failed[3]))
c.setFillColor(HexColor('#000000'))
c.setFont("Helvetica", 11)

c.setFillColor(HexColor('#038a27'))
c.setFontSize(12)
c.setFillColor(HexColor('#e62727'))
c.save()


