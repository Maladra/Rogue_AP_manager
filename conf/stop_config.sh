ip_interface=192.168.1.1/20
ap_interface_name=wlx78d294c227c0
internet_interface=enp0s31f2


# Block wifi device
rfkill block wlan

# Remove forward
echo 0 > /proc/sys/net/ipv4/ip_forward

# Remove ip from interface
ip addr del $ip_interface dev $ap_interface_name


# Remomve Forward
iptables -D FORWARD -i $ap_interface_name -o $internet_interface -j ACCEPT
iptables -D FORWARD -i $internet_interface -o $ap_interface_name -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -t nat -D POSTROUTING -o $internet_interface -j MASQUERADE