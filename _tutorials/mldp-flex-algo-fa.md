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
## What is Multicast Label Distribution Protocol (mLDP)

MLDP is an extension to LDP used to facilitate the transportation of multicast messages in an MPLS network. MLDP supports P2MP and MP2MP label-switched paths (LSPs). With MLDP, you can use the same encapsulation method as with the unicast messages, which reduces the complexity of the network. MLDP is a true pull-model implementation in that the PE closest to the receiver is the device to initiate the LSP.

### Benefits

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

### LDP Label Mapping Message

Before we move to the mLDP examples we need to understand what a LDP message is like.





### mLDP signaling and packet forwarding - P2MP Tree

![mLDP + FA_image_1.1.jpg]({{site.baseurl}}/images/mLDP + FA_image_1.1.jpg)

In the above P2MP scenario there are 2 receivers, PE3 and PE2. The Label Mapping(LM) starts from the receivers. P3 initiaties the LM with P node and moves to the root(PE1). 

PE2, PE3: receivers
Label mapping starts from the receiver.
- P3 does the LM with P and goes to the root
- Opaque data can carry any identifier, that identifies the tree uniquely, can be (S, G) with some VRF info
- the Opaque data in PE2 is creating the branch to P and establishes the P2MP tree
- the traffic flows similarly to PIM

MP2MP Tree
differences: 
- Receivers have MP2MP variable
- traffic flows from Root to all the leaves
- leaves can send traffic towards the Root

In mLDP scenario, in P2MP Tree Root is ingress PE, in MP2MP Tree, Root is any P or PE

If you have SR MPLS, you do not need LDP anymore, how will mLDP work?
- only for Multicast LDP will be turned on
- for unicast LDP will be turned off

### mLDP signaling and packet forwarding - MP2MP Tree

![mLDP + FA_image_2.1.jpg]({{site.baseurl}}/images/mLDP + FA_image_2.1.jpg)

test
