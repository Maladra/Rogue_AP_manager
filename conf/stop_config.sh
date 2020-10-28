# Unlock wifi device
rfkill block wlan ## OK

# Permet le forward
echo 0 > /proc/sys/net/ipv4/ip_forward ## OK

# Set ip to interface
ip addr del 192.168.1.1/24 dev wlx78d294c227c2 ## OK


# Forward
iptables -A FORWARD -i wlx78d294c227c2 -o enp0s31f6 -j ACCEPT
## Forward
iptables -A FORWARD -i enp0s31f6 -o wlx78d294c227c2 -m state --state ESTABLISHED,RELATED -j ACCEPT
## Same public IP than host
iptables -t nat -A POSTROUTING -o enp0s31f6 -j MASQUERADE