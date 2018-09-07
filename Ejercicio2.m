
syms s;
R=120;
C=10e-9;
L=1000e-6;
%s=tf('s');
H= 1/(1+s*C*R + s^2 * L * C);
step=H/s;
K=ilaplace(step);
w0=1/(L*C)^(1/2);
p =  [L * C, C*R, 1];
sita = alpha / w0;

wpico = w0*(1-2*sita^2)^1/2;

x =roots (p);
Habs= abs(1/(1+1i*wpico*C*R + (1i*wpico)^2 * L * C));
alpha=R/(2*L);
sita = alpha / w0;
Q= 1/ (2*sita);

value =  20 * log10(0.2);


