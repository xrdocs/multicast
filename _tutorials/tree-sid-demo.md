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

All the routers are running the following IOS-XR releases:
R1 - 7.4.2
R2 - 7.5.1
R3 - 7.5.1
R4 - 7.5.2
R5 - 7.5.1
R6 - 7.3.2

The base release is 7.3.1 +. Anything above that can support this demo

### Router Configurations

[ROOT-R1](https://github.com/lambros90/xrdocs/blob/main/tree-sid-demo/root-R1.txt)

It is important to notice the Tree-SID policies, the segment routing and the colour affinities.

```
...
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
 ...
!
```

[PCE-R2](https://github.com/lambros90/xrdocs/blob/main/tree-sid-demo/PCE-R2.txt)

```
segment-routing
  traffic-eng
   p2mp
    endpoint-set leaf-R6
     ipv4 1.1.1.6
    !
    endpoint-set leaf-R5-R6
     ipv4 1.1.1.5
     ipv4 1.1.1.6
    !
    label-range min 15400 max 15600
    policy p2mp-te-global
     source ipv4 1.1.1.1
     color 101 endpoint-set leaf-R5-R6
     treesid mpls 15101
     candidate-paths
      preference 100
       dynamic
        metric
         type te
        !
       !
      !
     !
    !
    policy p2mp-igp-global
     source ipv4 1.1.1.1
     color 100 endpoint-set leaf-R5-R6
     treesid mpls 15100
     candidate-paths
      preference 100
       dynamic
        metric
         type igp
        !
       !
      !
     !
    !
    policy p2mp-delay-global
     source ipv4 1.1.1.1
     color 102 endpoint-set leaf-R5-R6
     treesid mpls 15102
     candidate-paths
      preference 100
       dynamic
        metric
         type latency
        !
       !
      !
     !
    !
    policy p2mp-igp-red-vpn1
     source ipv4 1.1.1.1
     color 200 endpoint-set leaf-R5-R6
     treesid mpls 15200
     candidate-paths
      constraints
       affinity
        include-any
         RED
        !
       !
      !
      preference 100
       dynamic
        metric
         type igp
        !
       !
      !
     !
    !
    policy p2mp-igp-blue-vpn1
     source ipv4 1.1.1.1
     color 201 endpoint-set leaf-R5-R6
     treesid mpls 15201
     candidate-paths
      constraints
       affinity
        include-any
         BLUE
        !
       !
      !
      preference 100
       dynamic
        metric
         type igp
        !
       !
      !
     !
    !
   !
   affinity bit-map
    RED 23
    BLUE 24
   !
  !
 !
!
...
```
[MID-node-R3](https://github.com/lambros90/xrdocs/blob/main/tree-sid-demo/MID-node-R3.txt)

[MID-node-R4](https://github.com/lambros90/xrdocs/blob/main/tree-sid-demo/MID-node-R4.txt)

[LEAF-R5](https://github.com/lambros90/xrdocs/blob/main/tree-sid-demo/LEAF-R5.txt)

[LEAF-R6](https://github.com/lambros90/xrdocs/blob/main/tree-sid-demo/LEAF-R6.txt)




