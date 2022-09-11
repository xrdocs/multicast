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
## IP Multicast Evolution

The purpose of the following blog is to give an insight on Business Multicast Service. We will explain how Multicast is currently deployed and how we propose to evolve these deployments in the future. Multicast is a technology used by many Service Providers (SP) but is very limited to Unicast in terms of deployments and evolution. _Cisco currently has customers who are using different flavours of Multicast and it is expected to keep supporting all of them_. However, we believe that Multicast should shift to new technology requirements and adapt to the upcoming evolution of IP Multicast.

## Multicast in the SP world

SPs are split into 3 main categories:
1. Media Streaming.
2. Business Multicast VPN.
3. Financial Streaming.

However, all of them have common Multicast goals such as:
- Deliver data to multiple locations.
- Optimize bandwidth utilisation by replicating data in the IP network.
- Assure the fair distribution of data across multiple sites (receivers, leaves) at the same time.

Our task here is to list these categories and propose solutions based on the current and future requirements.

## Media Streaming

_The Media Streaming customers are CNBC, Sky, BT Broadcast, Bell Broadcast, Verizon, Swisscom, Pixar, ESPN, Disney and more._



## asda

Multicast is a technology which Service Providers (SP) use to deploy
Service Providers (SP) use multicast to deliver 3 main deployments:
1. Media Streaming
2. Business Multicast VPN
3. Financial Streaming

The purpose of this blog is to give an idea of how Business Multicast Service is evolving.

Service Providers (SP) have two main Business use cases when it comes to delivering Multicast:
1. IPTV or Broadcast TV
	This service addresses the consumer market 
2. Multicast VPN (mVPN) for business customers
	This service addresses enterprise business customers
    
Broadcast TV use case:
Today: Most of the deployments are P2MP RSVP-TE + mVPN. The Tree has to be completed manually for disjointness and Live-Live scenarios.
Short term future: In 2021 we introduced a Software Defined Network (SDN) based solution made of PCE + Tree-SID + mVPN. The Tree can be automatically created by the Path Computation Element (PCE) for disjointness and Live-Live scenarios.
CDN overlay: Cisco will be shiting to a newer long term plan with CDN overlay. Replication will be done at the CDN layer and less on the network. Customers are consuming unicast TV with VoD, Replay, Netflix, Youtube are some examples. The encoding adaptation could be done at the SDN layer. Smart TV apps will replace setup boxes. New plan will be quicker and easier to deploy and develop.

Hardware trends
New NPUs are optimized to increase forwarding performance and speed for unicast with lower packet per second cost and lower power consumption and heat. They will not be optimized to replicate multicast traffic compare to the older generations.
The new equipment are limited to ingress NPU only which means no ingress and egress replication.

Business Multicast VPN.
Service providers are not looking into replacing mVPN service. SPs have lots of small mVPN trees and fewer large mVPN trees. It is also clear that mVPN traffic does not increase much while unicast bandwidth continues to double every 18-24 months.
Today: Vast majority of customers have Rosen mVPN (profile 0) and mLDP mVPN (profile 14) deployments. Cisco will keep on supporting these profiles.
Evolution: Segment Routing and Flex-Algo are IPv6!

[Screenshot 2022-09-11 at 11.56.24.jpg]({{site.baseurl}}/images/Screenshot 2022-09-11 at 11.56.24.jpg)


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
    4. Many are moving to Tree-SID + mVPN -> the computation of disjoing tree is automatic (thanks 		  to SR-PCE)
    5. COE (CrossWork Optimization Engine) and CNC (CrossWork Ip Network Controller) will add lots 		  of value to the Tree-SID + mVPN solution, as the customer could now visualize 2 trees and 	   prove their disjointness

What enterprise & financial are saying:
	1. Wants to deploy disjoint live-live trees
    2. Trees are dynamic and states are changing often
    3. Looking at mLDP + FA + mVPN
    4. Adding some constraint on topology and network design
    5. Better suit for dynamic environment compared to Tree-SID
    

