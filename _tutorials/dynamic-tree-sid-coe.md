---
published: true
date: '2022-10-03 11:31 +0300'
title: Dynamic Tree-SID + COE
author: Lampros Gkavogiannis
excerpt: Dynamic Tree-SID + COE
position: hidden
---
# A New Post

We already discussed about Tree-SID in previous tutorials. Today we want to show in action the integration of Dynamic Tree-SID with Crosswork Optimization Engine). The COE team has put effort and time to evolve Tree-SID into an automated and better user experience. We have the option to visualize Tree-SID topology, sessions, policies and more which supports the idea of having an automated Multicast solution. In the rest of the article we will go over screenshots from the COE dashboard and we will use them to visualize the configurations we have in the routers.

The topology that will be used is shown below.

_screenshot of topology_

node 5 is root

SR-PCE (xtc1) node 1?

Leaf Node (Node-4) Configuration

transit node 8, 7, 3?

all the nodes are xrv9k devices


## SR-PCE (xtc1) Configuration

The PCE holds PCEP sessions with all the routers in the topology. We can verify that by running the following command:

### Command:
```
show pce ipv4 peer
```

### Output:
```
PCE's peer database:
--------------------
Peer address: 198.19.1.1
  State: Up
  Capabilities: Stateful, Segment-Routing, Update, Instantiation, SRv6

Peer address: 198.19.1.3
  State: Up
  Capabilities: Stateful, Segment-Routing, Update, Instantiation, SRv6

Peer address: 198.19.1.4
  State: Up
  Capabilities: Stateful, Segment-Routing, Update, Instantiation, SRv6

Peer address: 198.19.1.5
  State: Up
  Capabilities: Stateful, Segment-Routing, Update, Instantiation, SRv6

Peer address: 198.19.1.7
  State: Up
  Capabilities: Stateful, Segment-Routing, Update, Instantiation, SRv6

Peer address: 198.19.1.8
  State: Up
  Capabilities: Stateful, Segment-Routing, Update, Instantiation, SRv6

Peer address: 198.19.1.99
  State: Up
  Capabilities: Stateful, Segment-Routing, Update, Instantiation

Peer address: 198.19.1.101
  State: Up
  Capabilities: Stateful, Update, Instantiation

Peer address: 198.19.1.103
  State: Up
  Capabilities: Stateful, Update, Instantiation

Peer address: 198.19.1.104
  State: Up
  Capabilities: Stateful, Update, Instantiation

Peer address: 198.19.1.105
  State: Up
  Capabilities: Stateful, Update, Instantiation

Peer address: 198.19.1.107
  State: Up
  Capabilities: Stateful, Update, Instantiation

Peer address: 198.19.1.108
  State: Up
  Capabilities: Stateful, Update, Instantiation

Peer address: 198.19.1.202
  State: TCP Pending
  Capabilities: Stateless
```
edit: remove the addresses not belonging in the topology

![Tree-SID + COE topology.jpg]({{site.baseurl}}/images/Tree-SID + COE topology.jpg)



```
router bgp 65000
 address-family ipv4 mvpn
 !
 neighbor-group AS65000-RRC-services-group
  address-family ipv4 mvpn
   route-reflector-client
 !
pce
 segment-routing
  traffic-eng
   p2mp
    label-range min 30000 max 31000
    fast-reroute lfa
    multipath-disable
```





# SR-PCE (xtc1) Configuration

router bgp 65000
 address-family ipv4 mvpn
 !
 neighbor-group AS65000-RRC-services-group
  address-family ipv4 mvpn
   route-reflector-client
 !
pce
 segment-routing
  traffic-eng
   p2mp
    label-range min 30000 max 31000
    fast-reroute lfa
    multipath-disable
    
# Root Node (Node-5) Configuration

vrf L3VPN_NM-MVPN-80
 address-family ipv4 unicast
  import route-target
   65000:80
  !
  export route-target
   65000:80
  !
!
router bgp 65000
 address-family ipv4 mvpn
 !
 neighbor-group RR-services-group
   address-family ipv4 mvpn
!
 vrf L3VPN_NM-MVPN-80
  rd 65000:80
  address-family ipv4 unicast
   redistribute connected
  !
  address-family ipv4 mvpn
  !
!