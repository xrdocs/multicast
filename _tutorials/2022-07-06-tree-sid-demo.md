---
published: true
date: '2022-07-06 16:40 +0300'
title: Tree-SID Demo
author: LAMPROS GKAVOGIANNIS
excerpt: This will be a Tree-SID demo using Cisco NCS5500 routers
tags:
  - iosxr
  - cisco
  - NCS5500
  - Tree-SID
position: hidden
---
## Tree-SID Demo

This tutorial describes the process of a Tree-SID demo which was implemented on 6 NCS5500 devices. It consists the topology, the outputs and the relevant configurations on all the routers.

### Overview

IGP Segment Routing is configured to establish unicast connectivity between root, mid and leaf nodes.
The MVPN BGP session is established between root and leaf nodes for:
- PE auto discovery.
- P-Tunnel signaling and.
- C-multicast route signaling.

PCE learns the topology via IGP or BGP-LS.
PCE has PCEP sessions with root, mid and leaf nodes.
Tree-SID labels are allocated from the segment routing local block.

There are two MVPNs configured:
1. MVPN VRF RED - P2MP transport with IGP metric and affinity constraint which corresponds to red links (color 10)
2. MVPN VRF BLUE - P2MP transport with IGP metric and affinity constraint which corresponds to blue links (color 20)

Note: Both VPNs have associated "default" and "data" MDTs

### Topology

The following drawing shows the connections between the routers, the IPs and the affinity links (red, blue). The source is the R1 and the receivers are R5 and R6.

![]({{site.baseurl}}/images/Tree-SID%20demo%201.1.png)

This drawing includes all the interfaces between the routers.

![]({{site.baseurl}}/images/Tree-SID%20demo%201.2.png)

### Router Configurations

#### ROOT - R1

```
vrf red
 address-family ipv4 unicast
  import route-target
   2:10
  !
  export route-target
   2:10
  !
 !
 address-family ipv4 multicast
 !
!
vrf blue
 address-family ipv4 unicast
  import route-target
   1:10
  !
  export route-target
   1:10
  !
 !
 address-family ipv4 multicast
 !
!
vrf vpn1
 address-family ipv4 unicast
  import route-target
   1:11
  !
  export route-target
   1:21
  !
 !
!
interface Loopback0
 ipv4 address 1.1.1.1 255.255.255.255
!
interface TenGigE0/0/0/8
 ipv4 address 11.1.3.1 255.255.255.0
 lldp
 !
!
interface TenGigE0/0/0/9
 ipv4 address 10.1.3.1 255.255.255.0
 lldp
 !
!
interface TenGigE0/0/0/12
 ipv4 address 10.1.4.1 255.255.255.0
 lldp
 !
!
interface TenGigE0/0/0/13
 ipv4 address 11.1.4.1 255.255.255.0
 lldp
 !
!
interface BVI1
 vrf blue
 ipv4 address 10.10.8.1 255.255.255.0
!
interface BVI2
 vrf red
 ipv4 address 10.10.9.1 255.255.255.0
!
route-policy treeSID
  set core-tree sr-p2mp
end-policy
!
route-policy treesid
  set on-demand-color 20
end-policy
!
route-policy pass-all
  pass
end-policy
!
route-policy treesid-color-10
  set on-demand-color 10
end-policy
!
router isis 1
 net 49.0001.0000.0000.0001.00
 distribute link-state
 address-family ipv4 unicast
  metric-style wide
  mpls traffic-eng level-2-only
  mpls traffic-eng router-id Loopback0
  router-id 1.1.1.1
  segment-routing mpls
 !
 interface Loopback0
  passive
  address-family ipv4 unicast
   prefix-sid absolute 16001
  !
 !
 interface TenGigE0/0/0/8
  circuit-type level-2-only
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
   metric 10
  !
 !
 interface TenGigE0/0/0/9
  circuit-type level-2-only
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
   metric 10
  !
 !
 interface TenGigE0/0/0/12
  circuit-type level-2-only
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
   metric 10
  !
 !
 interface TenGigE0/0/0/13
  circuit-type level-2-only
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
   metric 10
  !
 !
!
router bgp 1
 bgp router-id 1.1.1.1
 bgp graceful-restart
 address-family ipv4 unicast
  redistribute connected
 !
 address-family vpnv4 unicast
 !
 address-family ipv4 mvpn
 !
 neighbor 1.1.1.5
  remote-as 1
  update-source Loopback0
  address-family ipv4 unicast
  !
  address-family vpnv4 unicast
  !
  address-family ipv4 mvpn
   route-policy pass-all in
   route-policy pass-all out
  !
 !
 neighbor 1.1.1.6
  remote-as 1
  update-source Loopback0
  address-family ipv4 unicast
  !
  address-family vpnv4 unicast
  !
  address-family ipv4 mvpn
   route-policy pass-all in
   route-policy pass-all out
  !
 !
 neighbor 10.10.11.2
  remote-as 1
  address-family ipv4 unicast
  !
 !
 neighbor 10.10.12.3
  remote-as 1
  address-family ipv4 unicast
  !
 !
 vrf red
  rd 2:20
  address-family ipv4 unicast
   redistribute connected
  !
  address-family ipv4 mvpn
  !
 !
 vrf blue
  rd 1:20
  address-family ipv4 unicast
   redistribute connected
  !
  address-family ipv4 mvpn
  !
 !
!
l2vpn
 bridge group bg
  bridge-domain red
   interface TenGigE0/0/0/10.2
   !
   routed interface BVI2
   !
  !
  bridge-domain blue
   interface TenGigE0/0/0/10.1
   !
   routed interface BVI1
   !
  !
 !
!
multicast-routing
 address-family ipv4
  mdt source Loopback0
  interface all enable
  mdt static segment-routing
 !
 vrf red
  address-family ipv4
   interface all enable
   bgp auto-discovery segment-routing
   !
   mdt default segment-routing mpls color 10
   mdt data segment-routing mpls 1 color 10 threshold 0
  !
 !
 vrf blue
  address-family ipv4
   interface all enable
   bgp auto-discovery segment-routing
   !
   mdt default segment-routing mpls color 20
   mdt data segment-routing mpls 1 color 20 threshold 0
  !
 !
vrf vpn1
  address-family ipv4
   interface all enable
   mdt static segment-routing
  !
 !
!
segment-routing
 global-block 16000 23999
 local-block 15000 15999
 traffic-eng
  interface TenGigE0/0/0/8
   affinity
    name RED
   !
   metric 11
  !
  interface TenGigE0/0/0/9
   affinity
    name RED
   !
   metric 11
  !
  interface TenGigE0/0/0/12
   affinity
    name BLUE
   !
   metric 11
  !
  interface TenGigE0/0/0/13
   affinity
    name BLUE
   !
   metric 11
  !
  on-demand color 10
   dynamic
    metric
     type igp
    !
    affinity
     include-any
      name RED
     !
    !
   !
  !
  on-demand color 20
   dynamic
    metric
     type igp
    !
    affinity
     include-any
      name BLUE
     !
    !
   !
  !
  affinity-map
   name RED bit-position 23
   name BLUE bit-position 24
  !
  pcc
   pce address ipv4 1.1.1.2
    precedence 100
   !
  !
 !
!
router pim
 address-family ipv4
  sr-p2mp-policy p2mp-te-global
   static-group 233.1.4.1 inc-mask 0.0.0.1 count 5 11.1.1.135
  !
  sr-p2mp-policy p2mp-igp-global
   static-group 232.1.4.1 inc-mask 0.0.0.1 count 5 11.1.1.135
  !
 !
 vrf red
  address-family ipv4
   rpf topology route-policy treeSID
   mdt c-multicast-routing bgp
   !
  !
 !
 vrf blue
  address-family ipv4
   rpf topology route-policy treeSID
   mdt c-multicast-routing bgp
   !
  !
 !
 vrf vpn1
  address-family ipv4
   sr-p2mp-policy p2mp-igp-red-vpn1
    static-group 232.1.2.1 11.1.2.100
   !
   sr-p2mp-policy p2mp-igp-blue-vpn1
    static-group 233.1.2.1 11.1.2.100
   !
  !
 !
performance-measurement
 interface TenGigE0/0/0/8
  delay-measurement
   advertise-delay 12
  !
 !
 interface TenGigE0/0/0/9
  delay-measurement
   advertise-delay 12
  !
 !
 interface TenGigE0/0/0/12
  delay-measurement
   advertise-delay 12
  !
 !
 interface TenGigE0/0/0/13
  delay-measurement
   advertise-delay 12
  !
 !
!
```


