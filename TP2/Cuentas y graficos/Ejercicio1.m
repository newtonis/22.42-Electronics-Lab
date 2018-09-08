f = 1:1:10e6;
s=i*2*f;
R=304000;
%L=0.0097; // tengo que fijarme bien los valores
L=1000e-6;
C=100e-12; %el chabon de labo dijo que tiraramos entre 10 y 100 pf
Z1 = R+ s*L;
Z2 = 1./(s*C);
Z= (Z1.*Z2)./(Z1+Z2);
IM = imag(Z);
RE= real(Z);
semilogx(f,RE)
grid
