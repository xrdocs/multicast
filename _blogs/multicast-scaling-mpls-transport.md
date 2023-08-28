---
published: true
date: '2023-08-28 09:38 +0300'
title: Multicast Scaling - MPLS Transport
author: Lampros Gkavogiannis
excerpt: >-
  The following blog focus on the scaling of Multicast and the nuts and bolts
  around it.
tags:
  - iosxr
  - Multicast
position: hidden
---
{% include toc icon="table" title="Multicast Distribution Trees - MDTs" %}

# Introduction

We have talked about Multicast before, how the technology works and the level of its complexity but we have not mentioned the way Multicast scales. In almost every interaction we have _with customers or account teams_ we get questions such as:
1. What is the scale?
2. How many Trees can i create?
3. How does the scale vary from platform to platform?
4. How do you sum all these different counters (Labels, VRFs, etc.)?
This blog will try to answer the above questions as detailed as possible and will bring to the surface how things work in regards to Multicast within IOS-XR software running on Cisco platforms.

## MPLS Overview

In order to start talking about the scaling, we need to establish some basic knowledge regarding Multiprotocol Label Switching (MPLS).

MPLS is a networking routing technology that offers the ability to forward traffic based on "labels", hence the name, instead of network addresses. These "labels" are defining the final destination of the packet and makes it much easier for the SPs to send those packets. The labels are stored in L2.

benefits:
1. interface independence
2. bridge different sites together, full mesh
3. one to many
4. QoS
5. transport
6. assign labels to packets such as TOS, DSCP and are translated into MPLS Labels by SP
