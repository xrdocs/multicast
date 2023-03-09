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

![mdt 1.1.1.jpg]({{site.baseurl}}/images/mdt 1.1.1.jpg)

### Underlay

The next step is to build a core plane (underlay) in the network. We need to use a core tree protocol such as PIM, mLDP, P2MP TE, Tree-SID or IR.

![mdt 1.2.1.jpg]({{site.baseurl}}/images/mdt 1.2.1.jpg)

### Overlay

To build the overlay we are adding the customer boxes and PE devices that are already aware of the above underlay. There are 2 common protocols to be used here, PIM or IGMP. If the switch is directly connected to the PE then we configure PIM between the CE and the PE. For the connectivity between the PEs we either use BGP Signaling or PIM Signaling. For mVPN profile 14 we use BGP Signaling.

![mdt 1.3.2.jpg]({{site.baseurl}}/images/mdt 1.3.2.jpg)

## Core Tree Types

They are called MDT (Multicast Distribution Tree) or PMSI (Provider Multicast Service Interface, IETF naming). It can be build with any of the Transport core protocols depending on the profile used.

### Default MDT or Multi-Directional Inclusive PMSI (MI-PMSI)

All the PEs that belong in the same mVPN, are all connected together and bidirectional which means any traffic sent to a PE will be received by all the PEs. This MDT will always be present no matter if there is traffic or not.

- Connects all PEs
- Bidirectional
- Always present

![mdt 1.4.jpg]({{site.baseurl}}/images/mdt 1.4.jpg)

### Data MDT or Selective PMSI (S-PMSI)

There is a PE (PE1) which is the Source or the Root and it is connected to a subset of PEs (PE3 and PE4), thus traffic will be received by them only.

- Connects subset of PEs
- Unidirectional (operating in a single direction)
- On-Demand (config exists but it is triggered when parameters are met)

![mdt 1.5.jpg]({{site.baseurl}}/images/mdt 1.5.jpg)

### Partitioned MDT or Multidirectional Selective PMSI (MS-PMSI)

It is a combination of the previous two.

- Connects subset of PEs
- Uni- or Bidirectional
- On-Demand (a Join request will trigger the creation of the Tree)

![mdt 1.6.jpg]({{site.baseurl}}/images/mdt 1.6.jpg)

## Core Tree Type Construction - mLDP POV

### Default MDT

In the following Default MDT scenario we have 4 PEs, where PE1 is the Root and creates the MDT towards all 3 PEs. All the PEs act as the Root at once, trying to send the information to all PEs and all the PEs join that Tree. Thus we have a Full mesh of P2MP mLDP Trees.

![mdt 1.7.jpg]({{site.baseurl}}/images/mdt 1.7.jpg)








