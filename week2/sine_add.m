clc
clear all
close all
t=0:0.01:1
F1=4
F2=2
x1=sin(0.2*pi*F1*t)
x2=sin(0.5*pi*F2*t)
c=x1+x2
plot(c)