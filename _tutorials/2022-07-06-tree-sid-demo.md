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

