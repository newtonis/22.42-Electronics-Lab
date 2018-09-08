
s=tf('s');
R=304000;
L=0.0097;
C=10e-12; %el chabon de labo dijo que tiraramos entre 10 y 100 pf
Z1 = R+ s*L;
Z2 = 1/(s*C);
Z= (Z1*Z2)/(Z1+Z2);
bode(Z);
f = 1:1:10e6;
X= 2*pi.*f*L - 1./(2*pi.*f*C);
semilogx(f,X),