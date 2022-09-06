---
published: true
date: '2022-09-01 17:36 +0300'
title: mLDP + Flex-Algo (FA)
author: Lampros Gkavogiannis
excerpt: Brief tutorial on  mLDP + FA technology
position: hidden
tags:
  - iosxr
  - cisco
  - mLDP
  - FA
  - Multicast
---
# What is Multicast Label Distribution Protocol (mLDP)

mLDP is an extension to LDP used to facilitate the transportation of multicast messages in an MPLS network. mLDP supports P2MP and MP2MP label-switched paths (LSPs). With mLDP, you can use the same encapsulation method as with the unicast messages, which reduces the complexity of the network. mLDP is a true pull-model implementation in that the PE closest to the receiver is the device to initiate the LSP.

## Benefits

- Based on over 15 years of IP multicast expertise, experience, and innovation using Cisco IOS Software
- An innovative unified control and forwarding plane that allows service providers and enterprises to transit MVPN traffic using multipoint LSPs (P2MP and MP2MP)
- State aggregation to minimize core states
- MPLS capabilities, such as Fast Reroute, that can now be applied to multicast traffic
- Seamless support of migration from generic routing encapsulation (GRE) and IP Multicast VPNs
- No need to manage customer premise equipment, enable multicast routing in the core, or use link-state routing protocol extensions to support MLDP
- Minimal cost associated with meeting bandwidth requirements of applications such as high-definition video
- Based on industry standards
- It is a receiver driven tree building protocol like PIM
- mLDP uses the LDP Transport to exchange Label Mappings

## LDP Label Mapping Message

Before we move to the mLDP examples we need to understand what a LDP message is like.

![mLDP + FA_image_1.1.jpeg]({{site.baseurl}}/images/mLDP + FA_image_1.1.jpeg)

There is mLDP Label Binding and it is a FEC Type 0x100. The FEC element contains 3 things:
1. Type: Point-to-Multipoint (P2M) or Multipoint-to-Multipoint (MP2MP)
2. Root: There is only one Root identified by an IP address
3. Opaque: Determines the kind of multicast service (e.g. default MDT, partitioned MDT, data MDT). P routers do not interpret this value

The above 3 items uniquely identify the mLDP tree.

## mLDP signaling and packet forwarding - P2MP Tree

![mLDP + FA_image_1.1.jpg]({{site.baseurl}}/images/mLDP + FA_image_1.1.jpg)

In the above P2MP scenario there are 2 receivers, PE3 and PE2 and PE1 the root. The Label Mapping (LM) starts from the receiver. P3 initiaties the LM with P node and moves to the root (PE1).

The message contains the type P2MP, the root and the Opaque value. There is a local label exchange between PE and P to receive traffic on this tree. This creates a leg from PE3 to P to PE1 and when a new receiver comes, PE2 will do the similar Label Mapping and this Opaque value will remain same for the single given tree. P already has the information from the tree that was created and will simply add a branch to PE2 to join that tree. This is how the P2MP tree is created.

When traffic flows, it starts from the root downstream to the receivers which is reverse direction of the signaling and it is similar to the traditional use of PIM.

## mLDP signaling and packet forwarding - MP2MP Tree

![mLDP + FA_image_2.1.jpg]({{site.baseurl}}/images/mLDP + FA_image_2.1.jpg)

The MP2MP tree can support bidirectional traffic. It will flow from root to leaves and the opposite.

The leaf starts the signaling by sending the LM all the way to the root while the Opaque value remains the same. The main difference is the type in the LM which becomes MP2MP. However, in a MP2MP there will be Downstream LM starting from the root to the leaves and the Opaque values carries the tree identifier.

The Downstream traffic is going to flow to the reverse direction of the Upstream tree building flow but the leaves can send traffic Upstream to the root.

In the case of mLDP, the tree root for P2MP will be the ingress PE while for MP2MP tree the root is any P or PE.

In a scenario that LDP is not needed because of SR MPLS, unicast LDP will be off but LDP will be turned on only for multicast.

# Multicast LDP with transport differentiation using SR Flex-Algo

In this section mLDP with Traffic Engineering (TE) will be covered. So far it is known that mLDP works with basic IGP metrics but by using a different transport, SR Flex-Algo it can be enhanced to use custom constraints and metrics.

## SR Flex-Algo (FA)

SR FLex-Algo is a complement solution for SRTE that adds new Prefix-Segments with specific optimization objective and constraints such as:
- minimize igp-metric or delay or te-metric
- avoid SRLG or affinity

It makes it possible to define different constraints and segment the network in multiple parts which results in a network which is defined by different segments. Also it leverages SRTE benefits of simplicity and automation such as
- Automated sub-50msec FRR (TILFA)
- On-Demand Policy (ODN)
- Automated Steering (AS)

## FA + Unicast

FA gives the ability to segment the network into different planes.

In the following example there are 3 groups of nodes:
1.Nodes 0 and 9 participate to Algo0, Algo128 and Algo129
2.Nodes 1/2/3/4 participate to Algo0 and Algo128
3.Nodes 5/6/7/8 participate to Algo0 and Algo129

It provides a virtual segmentation of the network with 2 planes, one green and one red. Each node must advertise which FA it belongs to.

![mLDP + FA_image_1.2.jpeg]({{site.baseurl}}/images/mLDP + FA_image_1.2.jpeg)

### FA aware mLDP

Let's see how mLDP can work with FA. Originally mLDP is used to build the network tree. However, FA gives the option to create multiple trees by influencing the path computation by associating metrics and constraints within the same network. This is done to enable a new list of use cases. 

Some of the use cases:
1. Disjoint Trees (Dual plane)
	In the scenario of Disjoint Trees we can achieve segmentation of the traffic in the same network. We might want to avoid specific links, paths due to security reasons.
2. Live-Live
	We might have critical traffic that we want to carry it through different paths and leverage the Live-Live scenario. Later, We can define which path the traffic should follow.
3. Low latency routing
	We might want to achieve low latency routes for real-time, latency-sensitive activities.
    
All of the above use cases are possible by adding the flexible metrics and constraints.

In the following example we have 1 multicast source, 5 receivers and 2 planes, green and blue. There is the slicing of the traffic between the 2 different planes but we can see that the source is able to send traffic to both planes.

![mLDP + FA_image_2.2.jpg]({{site.baseurl}}/images/mLDP + FA_image_2.2.jpg)

Most of bgp mvpn discovery routers they do carry P-MSI tunnel attributes (PTA) and the FEC is carried in the PTA.

reminder: FEC is the opaque value that is being used to create the underlay tree.

we use another field which is called IPA field and it is the IGP algorithm field that carries the SR Flex Algo instance ID. that helps the egress PE to start building the underlay tree with appropriate fa underlay.

fa + cisco ios-xr
what is supported today:

mvpn profile 14 - partitioned MDT mLDP P2MP with BGP-AD and BGP c-mcast signaling

mVPNv4/ mVPNv6 overlay

Partitioned and data MDTs

Granular mapping of (C-S, C-G) to a Partitioned MDT/ DATA MDT bound to a FA instance

PIM ASM, SSM, IGMPv2 and IGMPv3 as customer access protocols

ECMP - A FA topology may have ECMP and therefore multicast flows are load balanced if multiple paths are available

### mLDP signaling with FA (How operation works)

In the follow example we have 2 vrfs, blue and purple. S1 is the source and R1, R2 the receivers for the blue vrf while S2 is the source and R3 the receiver for the purple vrf.

with respect to mVPN signaling routers 0 and 9 are the edge devices, P nodes. ALl the overlay signaling will happen between 0 and 9 and underlay tree will be built using the core network

there is a policy defined on router 0 for the given source with S1 that any request that is coming for (S, G) it has to go over Algo129 which is nothing but redplane. The member receive request could PIM Join, IGMP Join in case receivers are directly connected.

for mVPN signaling we look where the source is. the source is behind Router 0. So 9 sends Join overlay to 0 for this particular flow in vrf context.
Once Router 0 receives this particular overlay Join, is going to look at the policy, where exactly this traffic has to come from, where the underlay tree has to be created and it looks that this tree has to be created using FA129. So it is going to allocate a tree which we call partioned MDT or data MDT and it is going to signal back to 9 saying that if you want to build a tree you need to use Algo129 which is defined in the policy.
Router 9 starts building underlay multicast tree for this FEC we received from 0 and now this particular Join goes over your redplane and once the Join is received by the actual source vrf , traffic starts flowing through the redplane.

one thing that is really important to remember here, if there is any failure this failure will be taken care within the same plane. No matter what is happening between 5,6,7,8 it will never be linked to green plane. it will be contained within the single plane that you have defined in fa.

there are many use cases that you might want Live-Live scenario with same content but different flows. You might want to make sure that some flows are using the green or redplane



![mLDP + FA_image_1.3.jpg]({{site.baseurl}}/images/mLDP + FA_image_1.3.jpg)




