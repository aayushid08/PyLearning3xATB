# Walk me IN dIR
import os

for root, dir, files in os.walk("C:/Users/intel/PycharmProjects/PyLearning3xATB/Ex_03072024"):
    print(f"Current Dir {root}")
    print(f"Sub Dir Dir {dir}")
    print(f"files Dir Dir {files}")
    print(len(files))