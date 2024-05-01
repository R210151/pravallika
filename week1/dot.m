clc
clear all
close all
a=[7,1,2]
b=[1,3,5]
sum=0
for i=1:length(a)
  sum=sum+a(i).*b(i)
endfor
  disp(['dot product of two lists',num2str(sum)])