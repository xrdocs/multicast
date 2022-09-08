---
published: true
date: '2022-09-08 11:50 +0300'
title: Future of Multicast
author: Lampros Gkavogiannis
excerpt: The following blog gives insight of Cisco's position to Multicast future
tags:
  - iosxr
  - cisco
  - Multicast
  - Future
  - Innovation
position: hidden
---
## Multicast Future

There are multiple customer use-cases and some of them are:
1. Multi-media streaming use-case
2. Financial streaming use-case
3. Multicast VPN services to business customers use-case
4. Live-live distribution with disjointness
5. Other type of constraints

Suggested solutions
- If there is no need for TE but mVPN is needed:
	1. IR (Ingress Replication) + mVPN for small VPNs:
    	In IR packets are replicated by ingress PE and send unicast packets over the core to the 		 destination PEs.
    2. mLDP + mVPN for large mVPN.
    3. IR and mLDP could be deployed together within the same network. It is transparent to the 		end-user and easy to switch from one to another.
    4. Solid solution has been proved to work well with SR-MPLS unicast.

- Need for TE in another working tree, computation with constraints (disjointness or other)
	1. mLDP + FA + mVPN:
    	- Preferred solution when mVPN are dynamic (lots of state changes)
        - Limited to some topology (double plane design required, no ring topology)
    2. Tree-SID + mVPN:
    	- Preferred solution when mVPN are almost static
        - Allow the customer to optimize multicast trees and simplify operation with a SDN 		  			controller
        
 What are the classical SPs are saying (ATT Business, BT Global, Orange Business Services, ...:
 - Multicast VPN is not the most growing business area, but can NOT be dropped/ deprecate, must  	carry on newer networks and newer hardware.
 - IR + mVPN and mLDP + mVPN are still preferred choice
 	1. It does not require newer investment (team education, operational tools, ...)
    2. Has been proved to work for years
    3. Works well with SR-MPLS
    4. Required enablement on newer platforms (i.e. 8000)
    
 What broadcast SPs are saying (NBC, Sky, ...):
 	1. They want to deploy disjoint live-live trees
    2. Trees are fairly statics
    3. Use to deploy RSVP-TE to address it -> the computation of disjoint trees is made manually 		and it is painful
    4. 

