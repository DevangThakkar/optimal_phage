# !/bin/bash
for i in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
do
    for j in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
    do 
        # python alt_script.py $i $j
        # python alt_plot.py $i $j
        # python alt_plot_V2.py $i $j
        # python alt_points.py $i $j
        python alt_facetdata.py $i $j # use 0.2 0.4 0.6 0.8 1.0 for this command
    done
done