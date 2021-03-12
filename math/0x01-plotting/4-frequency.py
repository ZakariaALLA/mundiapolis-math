#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Numbers of Students")
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.hist(student_grades, bins, edgecolor='black')
plt.xticks(np.arange(0, 110, 10))
plt.show()