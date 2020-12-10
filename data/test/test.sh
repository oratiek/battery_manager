#!/bin/sh

# show the remaining battery percentage

cap=`ioreg -l | grep Capacity`
full=`echo $cap | sed -e "s/^.*MaxCapacity\" = \([0-9]*\).*/\1/"`
curr=`echo $cap | sed -e "s/^.*CurrentCapacity\" = \([0-9]*\).*/\1/"`
pct=`echo "scale=3; $curr / $full * 100" | bc`
echo -----
printf "%.1f%%\n" $pct