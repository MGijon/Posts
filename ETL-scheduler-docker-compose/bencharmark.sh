#!/bin/bash

# Check if a filename was provided as the first argument
if [ -z "$1" ]; then
    echo "Error: No output filename provided."
    echo "Usage: ./benchmark.sh <output_filename.csv>"
    exit 1
fi

OUTPUT_FILE="$1"
INTERVAL=5 
DURATION=300 

# Create the header in the new file
echo "Timestamp,Container,CPU_Perc,Mem_Usage,Mem_Perc" > "$OUTPUT_FILE"

echo "Starting benchmark for $DURATION seconds. Saving to: $OUTPUT_FILE"

for ((i=0; i<$DURATION; i+=$INTERVAL)); do
    # Capture current docker stats
    # We use --format to get clean data for your CSV/Medium charts
    docker stats --no-stream --format "{{.Name}},{{.CPUPerc}},{{.MemUsage}},{{.MemPerc}}" > temp_stats.txt
    
    TIMESTAMP=$(date +%H:%M:%S)
    
    # Prepend timestamp to each line and append to our output file
    while read -r line; do
        echo "$TIMESTAMP,$line" >> "$OUTPUT_FILE"
    done < temp_stats.txt
    
    rm temp_stats.txt
    sleep $INTERVAL
done

echo "Benchmark complete! Data saved to $OUTPUT_FILE"

