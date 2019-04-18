#set term tikz
#set output 'anticorrel.tex'
set term qt
set key off
set xrange [-6:6]
set yrange [-6:6]

set xlabel '$v$'
set ylabel '$u$'
set title 'Correlated'

plot 'd2.dat' pt 3 lc rgb 'black'
