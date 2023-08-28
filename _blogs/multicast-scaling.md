---
published: true
date: '2023-08-28 09:38 +0300'
title: Multicast Scaling
author: Lampros Gkavogiannis
excerpt: >-
  The following blog focus on the scaling of Multicast and the nuts and bolts
  around it.
tags:
  - iosxr
  - Multicast
position: hidden
---
{% include toc icon="table" title="Multicast Scaling" %}

# Multicast Scaling

## Introduction

Many thanks to [Anuj Budhiraja](https://www.linkedin.com/in/anuj-budhiraja/), Cisco Technical Lead Engineer, for his help writting this blog!
{: .notice--info}

We have talked about Multicast before, how the technology works and the level of its complexity but we have not mentioned the way Multicast scales. In almost every interaction we have _with customers or account teams_ we get questions such as:

1. What is the scale?
2. How many Trees can i create?
3. How does the scale vary from platform to platform?
4. How do you sum all these different counters (Labels, VRFs, etc.)?

This blog will try to answer the above questions as detailed as possible and will bring to the surface how things work in regards to Multicast within IOS-XR software running on Cisco platforms.

## MPLS Overview

In order to start talking about the scaling, we need to establish some basic knowledge regarding Multiprotocol Label Switching (MPLS).

MPLS is a networking routing technology that offers the ability to forward traffic based on labels, hence the name, instead of network addresses. These labels are defining the final destination of the packet and makes it much easier and more scalable for the SPs to send those packets. The labels are stored in L2.

MPLS is a transport protocol and provides the benefit of bridging different sites together (full mesh). Furthermore, offers the allocation of different labels such as ToS or DSCP to the external networks and enhances the ability to support QoS and traffic prioritization.

_benefits:
1. interface independence
2. bridge different sites together, full mesh
3. one to many
4. QoS
5. transport
6. assign labels to packets such as TOS, DSCP and are translated into MPLS Labels by SP_

## Multicast Scaling - MPLS Transport

In the following image we can see a simple design with all types of Nodes within a MPLS Transport network.

From MPLS Transport perspective we have 4 types of Nodes:
1. Root Node: R1, it is the Source Node
2. Transit/ Mid Node: R2, R3, pure Transit Nodes, no MVPN config.
3. Bud Node: R5, R6, mix of Mid/ Transit/ Leaf, can be directly connected to the Receivers
4. Leaf Node: R4, directly connected to the Receivers

![multicast scaling 1.3.1.jpg]({{site.baseurl}}/images/multicast scaling 1.3.1.jpg)

Previously we [discussed](https://xrdocs.io/multicast/blogs/multicast-distribution-trees-mdts/) about MVPN and at Cisco we have a huge variety of MVPN Profiles supported on our platforms. There is difference between each Profile when it comes to scaling, but in this blog we will mostly focus on Profile 14, because it is well known and massively deployed.
{: .notice--info}

For all the above Nodes there are different scale numbers that are being allocated for Profile 14. Let us define what scale numbers we get on each Node.

**1. Root Node:**
The Ingress traffic comes from the customer network to the service provider network and we have 3 scale numbers:
	1. The amount of (S, G).
    2. The amount of the Label Trees (MDTs).
    3. The amount of VRFs.
On the Egress Interface we get:
	1. The amount of replications per Label Tree.
    
**2. Transit/ Mid Node:**
On the Igress Interface we get:
	1. The amount of the Label Trees (MDTs).
On the Egress Interface we get:
	1. The amount of replications per Label Tree.
    
**3. Bud Node:**
On the Ingress Interface we get:
	1. The amount of the Label Trees (MDTs).
On the Egress Interface we get:
	1. The amount of replications per Label Tree per (S, G).
    2. The aggregate number of replications.

**4. Leaf Node:**
On the Ingress Interface we get:
	1. The amount of the Label Trees (MDTs).
On the Egress Interface we get:
	1. The amount of replications per Label Tree per (S, G).
    2. The aggregate number of replications.

![multicast scaling 1.3.2.jpg]({{site.baseurl}}/images/multicast scaling 1.3.2.jpg)

## Resource Allocation - Example

We will list a set of steps to understand the allocation of resources to each part of the network according to the image below.

![multicast scaling 1.4.1.jpg]({{site.baseurl}}/images/multicast scaling 1.4.1.jpg)

1. R1 acts as a receiver and sends an IGMP Join towards PE1.
2. PE1 will leverage IGMP Sync to sync with PE2.
3. PE1 sends a Join in MVPN context of BGP Route Type 7 for this (S, G) to PE4.
	- PE4 is behind a Dual Homed Peer.
4. PE4 will allocate a MDT for this (S, G).
	- It consumes a Label Resource.
5. PE4 will use BGP Auto Discovery Route Type 3 to send to all Ps.
	- P-1 receives it and learns which Tree to join.
6. PE1 will join this this Data MDT for this (S, G).
	- It consumes a Label Resource.
7. The Join will reach P-1 and P-1 joins the MLDP Tree.
	- It consumes a Label Resource.
8. P-1 sends the Join to P-2 and P-2 joins the MLDP Tree.
	- It consumes a Label Resource.
    - The Tree is complete.
9. Despite the fact we created 1 Data MDT, 4 Label Resources were consumed.
	- The purpose of the Label Resource allocation varies on each node.

# Redesign Options - Recommendations

So far we discussed how the Resources are allocated, but we understand that sometimes scaling can become an issue. There are networks that change over the time and the designs are getting replaced by new ones with updated requirements and we want to be able to comply to them as much as possible. There are situations that a platform upgrade can happen and will suffice for the new changes but there also situations that the platform has to remain the same but a redesign might be required in order to adapt to the new scaling. On the second part of the blog, we will cover some these extra options that IOS-XR can provide to us.

## Route Policy Based S-PMSI

Going back to this [blog](https://xrdocs.io/multicast/blogs/multicast-distribution-trees-mdts/), we mentioned what Data MDT is and how/ when it can be used. Now, we will discuss about a policy that can be applied to a Data MDT.

The policy is called Based S-PMSI and it is an enhanced route policy to map multicast sources and/ or groups to a named Data MDT. It is developed to determnistically control multicast flow mapping to Data MDT Trees and we assign names instead of numbers because they can become more descriptive.
We can take a look on how the configuration for this policy looks in following image.

<div class="highlighter-rouge">
<pre class="highlight">
<code>
route-policy data-mdt
	if destination in (232.0.0.0/24 1e 32) then
    	<mark>set data-mdt Red-Group-1</mark>
        pass
    endif
end-policy
</code>
</pre>
</div>





- transport specific attributes (e.g., mLDP FEC) of a named Data MDT assigned automatically
- named Data MDT created when matches the route-policy and needs to be transitioned to Data MDT
- we can create a route policy and based on the route policy matching constraints we can put all the interested flows which we want to collect on one single Data MDT, so it can deterministically controll all the Multicast Flows and map it to a single Data MDT Tree
- the functionality is also known as Named Data MDT
- named Data MDT is removed when last flow using it is moved off the Data MDT Tree
- example criteria






