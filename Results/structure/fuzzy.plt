set terminal X11
set termoption enhanced
set encoding utf8
set xlabel "Number of parameters" font ", 16"
set ylabel "Mean square error" font ", 16"
set grid
unset key #font ", 18"
set tics font ", 18"
unset logscale x 
#set xrange [0.000000e+00:5.000000e+00]
unset logscale y 
#set yrange [5.000000e+01:2.000000e+03]
#set xtics 1
#set x2tics 1
#set ytics 1
#set y2tics 1
set format y "%g"
set format x "%g"
set macro
name = "fuzzy"
set title name font ", 24"
plot '../3_smart_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#FF0000" title "3s layer", \
'../3_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#0000FF" title "3 layer", \
'../4_smart_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#FF7700" title "4s layer", \
'../4_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#0077FF" title "4 layer", \
'../5_smart_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#FFFF00" title "5s layer", \
'../5_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#00FFFF" title "5 layer"
set terminal push
set terminal postscript eps color
set out name.'.eps'
replot
set term pop
replot
