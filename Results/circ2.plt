set terminal X11
set termoption enhanced
set encoding utf8
set xlabel "Number of parameters" font ", 16"
set ylabel "Mean square error" font ", 16"
set grid
set key font ", 18"
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
name = "circ2"
plot '2_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#0000FF" title "2 layer", \
'3_smart_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#FF0000" title "3s layer", \
'3_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#0000CC" title "3 layer", \
'4_smart_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#BB0000" title "4s layer", \
'4_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#000099" title "4 layer", \
'5_smart_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#770000" title "5s layer", \
'5_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#000066" title "5 layer", \
'6_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#000033" title "6 layer", \
'7_layer_runs/'.name.'.plt' using (($1+1)*1000):2 with lines lw 4 lt rgb "#000000" title "7 layer"
set terminal push
set terminal postscript eps color
set out name.'.eps'
replot
set term pop
replot
