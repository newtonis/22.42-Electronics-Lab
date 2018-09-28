
%syms s;
R=120;
%R=632.4555;
C=10e-9;
L=1000e-6;
s = tf ('s');
%H = 1/(1+s*C*R + (s^2) * L * C);
H= (s*C*R)/(s^2*L*C+s*R*C+1);

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
%opt = stepDataOptions('InputOffset',-0.25,'StepAmplitude',0.5);


 plot (second1, Volt1)
 hold on
%step(H,opt,'r')
step (H)






