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