
s= tf ('s');
R=120;
C=10*10^-9;
L=1000*10^-6;

h1= (s*C*R)/(s^2*L*C+s*R*C+1);
h2= (s^2*L*C+1)/(s^2*L*C+s*R*C+1);
h3= (s^2*L*C)/(s^2*L*C+s*R*C+1);

% step1=h1/s;
% step2=h2/s;
% step3=h3/s;

plot (freq, pha)
hold on
% opt = stepDataOptions('InputOffset',0,'StepAmplitude', 0.5);
% step(h3,opt,'r')

% %bode 
% w=logspace(-1,6,5000);
% [mag, phase] = bode(h3,w);
% mag = squeeze (mag);
% phase = squeeze (phase);
% % for i=1:length(phase)
% %     if phase(i)<0
% %         phase(i)=phase(i)+180;
% %     end
% % end
% %phase
% semilogx ( w./(2*pi), phase);
% 
% %mag
% %semilogx( w./(2*pi), 20*log10(mag));
% 
% 
% grid on
%  %title ('Bode diagram - Magnitude')
% %itle ('Bode diagram - Phase')
% xlabel ('Frequecy (Hz)')
% %ylabel ('Magnitude (dB)')
% ylabel ('Phase(degrees)')

legend ('práctico' , 'teórico')
grid on
