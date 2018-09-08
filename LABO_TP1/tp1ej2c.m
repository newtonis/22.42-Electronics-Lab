 hold off
s=tf('s');
 h=(s*7.05*10^-6)/((s*7.05*10^-6)+1)
 g= 1/((s*7.05*10^-6)+1)
 bode(h)
 hold on
 bode(g)
 grid on