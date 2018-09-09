clear;
clc;
clear all;
close all;
k=1e3;
m=1e-3;
C=10e-12; %el chabon de labo dijo que tiraramos entre 10 y 100 pf
R=354.6;
L=0.956e-3;
f=1:10:1e7;
w=2*pi.*f;

%Cuentas a manopla
Z1= 1./(1i.*w*C);
Z2= R + 1i.*w*L;
Z= (Z1.*Z2)./(Z1+Z2);
RE= real(Z);
%RE= (R./((C.*w).^2))./ (R^2 + (L.*w - 1./(C.*w)).^2);
%IMAG= ((-R^2./(C.*w)) -(L.*w - (1./(C.*w))*(L/C)))./ (R^2 + (L.*w - 1./(C.*w)).^2);

filename = 'Ejercicio1.xlsx';
xlsread(filename);
sheet = 1;
xlRange = 'A2:E30';
mediciones = xlsread(filename,sheet,xlRange);
Freq = mediciones(:, 1) * k;
Lmed= mediciones(:,2)*m ;
Qmed = mediciones(:, 3);
Res= mediciones(:, 4);
Pha = mediciones(:, 5);
axis([10 1e6 0 inf]);
grid

React = Lmed*2*pi.*Freq;
semilogx(f,RE);
hold on;
semilogx(Freq,Res);
legend('Teorico','Práctico');