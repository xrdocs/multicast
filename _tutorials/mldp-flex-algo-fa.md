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

- Based on over 15 years of IP Multicast expertise, experience, and innovation using Cisco IOS Software
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
3. Opaque: Determines the kind of Multicast service (e.g. default MDT, partitioned MDT, data MDT). P routers do not interpret this value

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

In a scenario that LDP is not needed because of SR MPLS, unicast LDP will be off but LDP will be turned on only for Multicast.
