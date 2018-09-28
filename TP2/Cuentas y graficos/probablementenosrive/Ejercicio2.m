% frec = [4.9
% 7
% 9
% 11
% 13
% 16
% 20
% 23
% 26
% 29
% 31
% 33
% 36
% 40
% 41
% 43
% 45
% 46
% 47
% 48
% 49
% 52
% 56
% 60
% 63
% 66
% 76
% 86
% 109
% 209
% 309
% 409
% 490
% 690
% 900];
% 
% frecc = 1000.*frec;
% 
% 
% magg = [0.1
% 0.2
% 0.3
% 0.4
% 0.5
% 0.8
% 1.3
% 1.7
% 2.2
% 2.8
% 3.3
% 3.8
% 4.6
% 5.9
% 6.2
% 6.8
% 7.3
% 7.5
% 7.6
% 7.7
% 7.8
% 7.4
% 6.1
% 4.3
% 2.9
% 1.6
% -2.4
% -5.5
% -11
% -24
% -31
% -36
% -39
% -43
% -46];
% 
% phase= [-2
% -4
% -5
% -6
% -7
% -8
% -10
% -13
% -15
% -19
% -22
% -24
% -30
% -40
% -43
% -50
% -58
% -65
% -69
% -75
% -79
% -95
% -114
% -126
% -135
% -140
% -153
% -160
% -170
% -178
% -178
% -178
% -179
% -179
% -179];
% [mag, pha, w] = bode(H);
% mag = squeeze (mag);
% pha = squeeze (pha);
% 
% semilogx ( w./(2*pi), pha);
% hold on
% semilogx(frecc, phase,'r');


%step=H/s;
%K=ilaplace(step);
% w0=1/((L*C)^(1/2));
% p =  [L * C, C*R, 1];
% ro=roots(p); 
% alpha=R/(2*L);
% sita = alpha / w0;
% wpico = w0*((1-2*((sita)^2))^(1/2));
% Q= 1/ (2*sita);
% 
% x =roots (p);
% Habs= abs(1/(1+1i*wpico*C*R + ((1i*wpico)^2) * L * C));
% value =  20 * log10(0.2);
% 
% 
% wpico = w0;
% Habs= abs(1/(1+1i*wpico*C*R + ((1i*wpico)^2) * L * C));

R=632.455532;
C=10e-9;
L=1000e-6;
s = tf ('s');
H = 1/( 1 + s*C*R + (s^2) * L * C);

alpha=R/(2*L);
w0=1/((L*C)^(1/2));
sita = alpha / w0;

wd = (w0^2 - alpha^2)^(1/2);
fd = wd/(2*pi)


ts = (log(1/(0.05*(1-sita^2)^(1/2))))/alpha

Mp = exp(-pi*sita/((1-sita^2)^(1/2)))

opt = stepDataOptions('InputOffset',-0.5,'StepAmplitude',1);
plot (second1, Volt1)
hold on
step(H,opt,'r')
grid on







