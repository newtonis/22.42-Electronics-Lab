clc;
f = 10:0.1:1e6;
w=2*pi*f;
R=50e6
C=10.4e-9
w0=(4.950e6)*2*pi
Lz=1/(( C )*w0^2)
w0cuad=w0*w0;
L = 1/(w0cuad*C);
% D = 1/Q = R/X  p
% para 26Hz  D = 0.015 = R / (1/(2*pi*26*(Ca26))) ca26=10.4nf

ZC= 1./(C*1i.*w);
H =1i.*w*L + ((R.*ZC)./(R+ZC));
semilogx(f,rad2deg(angle(H)));
hold on

G= G*1e-6;
C1=C1*1e-9;
Freq  = 1000*Freq;
YCMED=2*1i*pi.*Freq.*C1;
YRMED=G;
YTOT = YCMED+YRMED
%semilogx(Freq,abs(1./YTOT));
semilogx(Freq,rad2deg(angle(1./YTOT)));

grid on
xlabel('Frecuencia(Hz)')
ylabel('Fase(°)')
title('Fase de Z')
legend('Teórico','Práctico');
set(gcf,'PaperOrientation','landscape');
print('Rta_frec_phase_Z','-dpdf','-fillpage');


