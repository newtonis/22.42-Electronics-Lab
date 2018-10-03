clc;
f = 10:0.1:1e6;
w = 2*pi.*f;
L = 0;
Rl = 0;
C = 0.14e-9;
R = 50e6;
ZC= 1./(C*1i.*w);
H = Rl + 1i.*w*L + ((R.*ZC)./(R+ZC));
semilogx(f,abs(H));
hold on
G= G*1e-6;
C1=C1*1e-9;

Freq  = 1000*Freq;
C1= C1*1e-9;
YCMED=2*1i*pi.*Freq.*C1;
YRMED=G;
YTOT = YCMED+YRMED
semilogx(Freq,abs(1./YTOT));
