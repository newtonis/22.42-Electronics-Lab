ratio = squeeze(ratio);
semilogx(frec,ratio,'color','blue');
xlabel('Frecuencia [Hz]');
ylabel('Modulo [dB]');
% set(gcf,'PaperOrientation','landscape');
%print('bode_PB_Fase','-dpdf','-fillpage');