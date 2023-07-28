import matplotlib.pyplot as p

avg_marks = [30,20,25,15,10]
subjects = ["Mathematics", "Physics", "English", "Chemistry", "Biology"]
p.pie(avg_marks,labels=subjects)
p.show()
