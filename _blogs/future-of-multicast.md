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

Our task here is to list these categories and propose solutions based on the current and future industry requirements.

## Media Streaming

_The Media Streaming customers are CNBC, Sky, BT Broadcast, Bell Broadcast, Verizon, Swisscom, Pixar, ESPN, Disney and more._

Streaming media is all about traffic delivered and consumed in a continuous stream from a source to the receivers. The main goal is to deliver IPTV broadcast channels to all the presence points while maintaning zero disruption of services.

The main requirements are:
- Data delivery for Broadcast TV in different formats such as SD, HD, 4K, 8K.
- Creation of multiple leaves that are controlled by the operator and are always on.
- Protection of the above by deploying Disjoing trees and Live-Live traffic.


### Current Deployments

Today, most Media Streaming deployments are running RSVP-TE P2MP + mVPN. The Multicast tree is created **manually** for scenarios such as disjointness and Live-Live and there is not visualization. There is no real-time view of the tree as computation is distributed.

### Today's Cisco Suggestion

In Cisco, we believe that theere are better ways to deliver Media Streaming. We can get rid of manual tree creation and maintenance by deploying the Tree-SID technology which is a controller based approach to build a tree either static or dynamic. It is a product of Software Defined Networks (SDN) architecture and is a result of PCE + Tree-SID + mVPN where Tree-SID is a SR P2MP policy. Below you can find a list of sources for better understanding of Tree-SID.

[Tree-SID Article](https://xrdocs.io/multicast/tutorials/tree-sid/) and [Video](https://www.youtube.com/watch?v=q3VNOnw-bIE&t=1s&ab_channel=xrdocs)
[Tree-SID Demo](https://xrdocs.io/multicast/tutorials/tree-sid-demo/) and [Video](https://youtu.be/WhYCwysSDAQ)

### Media Streaming Future

The Industry is moving forward and it is our task to tag alone. The majority of traffic is Unicast, thus it is undeniable that it will grow faster than Multicast. The new NPU's are designed and optimized to increase the forwarding performance and speed while achieving lower per packet cost. There is also lower power consumption and heat generation. Therefore, these NPU's are not Multicast designed. In Addition, replication is happening at ingress NPU only and it is no longer splitted between ingress and egress. In summary we should expect similar replication performance on newer equipment compared to older without any large improvement anymore.

Cisco is currently working with the CNC (Crosswork Network Collector) and Crosswork Optimization Engine (COE) team to delivery the visualization of Tree-SID. As a result of NPU's evolution the replication will be happening at the Content Delivery Network (CDN) Layer. This will provide the following advantages and features:
- Smart TV apps consuming Unicast traffic will replace setup boxes which will reduce Operating Expenditure (OPEX) for SPs.
- There can be Network Functions Virtualization (NFV) as elastic mechanism to scale up during large broadcast events such as sports evemts, political events, etc...

The deployment of above innovation can be much faster to deploy with CDN in place than deploying common network solutions which makes it possible to compete with WEB and OTT competitors.
 
_na balw photos apo cnc dashboard_

## Business Multicast VPN

_The Business Multicast VPN customers are Orange Business Service, ATT IP Services, BT Global, Charter, Comcast, Deutsche Telekom, Vodafone and more._

## Financial Streaming

_The Financial Streaming customers are LSEG, Bloomberg, Pico, Morgan Stanley and more._

## asda

    
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
