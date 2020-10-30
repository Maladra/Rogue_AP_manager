#### EDIT ####
ip_interface=192.168.1.1/24
ap_interface_name=wlx78d294c227c2
internet_interface=enp0s31f6
##############

# Unlock wifi device
rfkill block wlan ## OK

# Permet le forward
echo 0 > /proc/sys/net/ipv4/ip_forward ## OK

# Set ip to interface
ip addr del $ip_interface dev $ap_interface_name ## OK


# Forward
iptables -D FORWARD -i $ap_interface_name -o $internet_interface -j ACCEPT
## Forward
iptables -D FORWARD -i $internet_interface -o $ap_interface_name -m state --state ESTABLISHED,RELATED -j ACCEPT
## Same public IP than host
iptables -t nat -D POSTROUTING -o $internet_interface -j MASQUERADE