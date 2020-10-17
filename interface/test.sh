echo "hello world"

screen -d -m -S airodump_session airodump-ng wlan0mon

echo "baba"
sleep 2
i="0"
while [ $i -lt 5 ]
do
    echo "refresh file"
    screen -p 0 -S airodump_session -X /home/julien/Bureau/RogueAP/hardcopy
    sleep 2 
    input='/home/julien/Bureau/RogueAP/hardcopy.0'
    
    while IFS= read -r line
    do
        echo "$line"
    done < "$input"

    rm ./hardcopy.0
    sleep 20
    i=$[$i+1]
done
screen -p 0 -S airodump_session -X quit