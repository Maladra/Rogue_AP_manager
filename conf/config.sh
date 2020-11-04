ip_interface=192.168.1.1/20
ap_interface_name=wlx78d294c227c0
internet_interface=enp0s31f2

# Unlock wifi device
rfkill unblock wlan

# Permet le forward
echo 1 > /proc/sys/net/ipv4/ip_forward 

# Set ip to interface
ip addr add $ip_interface dev $ap_interface_name


# Forward
iptables -A FORWARD -i $ap_interface_name -o $internet_interface -j ACCEPT
## Forward
iptables -A FORWARD -i $internet_interface -o $ap_interface_name -m state --state ESTABLISHED,RELATED -j ACCEPT
## Same public IP than host
iptables -t nat -A POSTROUTING -o $internet_interface -j MASQUERADE