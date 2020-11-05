import cv2
import pandas
import os
import matplotlib.pyplot as plt
def funcion_calibracion():
  print('Introducir escala (mm/px)')
  escala=float(input())
  return escala

def transformacion(X,escala):
  return [x*escala for x in X]

