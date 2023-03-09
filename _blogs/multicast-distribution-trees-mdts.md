---
published: true
date: '2023-03-09 09:37 +0200'
title: Multicast Distribution Trees - MDTs
author: Lampros Gkavogiannis
excerpt: 'Description of MDTs (Default, Partitioned, Data)'
tags:
  - iosxr
  - cisco
  - multicast
position: hidden
---
## MVPN Overview

In this blog, we will cover mVPN (Multicast VPN) and the Multicast Distribution Trees (MDT). In Unicast VPN, once the transport underlay is set, any VPN instance or any VRF instance can use the exact same transport but in Multicast this is not the case.

The instances might be using different VPNs, Red or Blue. If these instances are using the same transport then the traffic designated to Red will be forwarded to Green, thus for each VPN instance we have to build a separate transport underlay. We can come up with an example based on the following snapshot.

### VPNs

We assume that we have 4 PEs (PE1, PE2, PE3, PE4) and only one of them has 1 subset VPN instance. For example PE1, PE3 and PE4 use a Green VPN, while PE2 uses a Red VPN. In this case, if we use a common transport underlay then there will be a mix of traffic. Red VPN will receiving traffic from Green and vice-versa. This is why we need to come up with a new transport underlay.

![mdt 1.1.jpg]({{site.baseurl}}/images/mdt 1.1.jpg)

### Underlay

The next step is to build a core plane (underlay) in the network. We need to use a core tree protocol such as PIM, mLDP, P2MP TE, Tree-SID or IR.

![mdt 1.2.jpg]({{site.baseurl}}/images/mdt 1.2.jpg)

### Overlay

To build the overlay we are adding the customer boxes and PE devices that are already aware of the above underlay. There are 2 common protocols to be used here, PIM or IGMP. If the switch is directly connected to the PE then we configure PIM between the CE and the PE. For the connectivity between the PEs we either use BGP Signaling or PIM Signaling. For mVPN profile 14 we use BGP Signaling.









