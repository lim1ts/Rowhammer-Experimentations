#!/bin/bash

file=${1--}
total=0
useful=0
while IFS=, read stat agg1addr agg2addr vicaddr bit flipto; do
	let "total+=1"
	if [ "$bit" -ge 12 -a "$bit" -lt 31 ]; then 
		echo "$stat,$agg1addr,$agg2addr,$vicaddr,$bit,$flipto"
		let "useful+=1"
	fi
done < <(cat -- "$file")
echo "Total lines: $total"
echo "Total useful: $useful"
percentage=$(($useful * 100 / $total))
echo "Percentage = $percentage %"
