while read line; do
    if [ -z "$line" ]; then
        break
    fi
    echo "$line" | cut -c3
done
