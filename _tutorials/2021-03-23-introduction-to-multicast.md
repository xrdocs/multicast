---
published: true
date: '2021-03-23 14:46 +0200'
title: Multicast
author: Lampros Gkavogiannis
excerpt: Introduction to NCS5500 Multicast
position: hidden
---
## Introduction to Multicast on NCS-5500

This introduction will be the start of a new series in the NCS-5500 xrdocs family called “Introduction to Multicast on NCS-5500". NCS5500 is an important member of Cisco’s portfolio like ASR 9000 and 8000, however is not as heavily represented as ASR 9000. This series is an opportunity to learn more about NCS5500 and decide which platform is more suitable to your needs. It will focus mostly on multicast and will try to cover the most popular features on this. unveil strengths and weaknesses and compare the capabilities of NCS-5500 to the rest of CIsco’s portfolio. 

### Introduction to packet replication

This is the first blog spot of the new series and will cover the most important part, which is how is multicast replicated. In the following link https://xrdocs.io/ncs5500/tutorials/ncs5500-qos-part-1-understanding-packet-buffering/ you can find information about packet buffering and how is unicast traffic scheduled on ncs5500.

#### NCS 5500 System Architecture

Multicast replication is a two-stage process. The process starts in the fabric to send a copy to the NPUs which are interested in the flow and then each NPU performs the second level of replication to interfaces interested in receiving the traffic. There is not ingress replication in the current version of the platform. Multicast packets are transmitted and replicated without egress scheduler approval which is opposite to unicast traffic. Even if you are using a single chipset system, the packets will still be split in cells. If the packet is going out of the same interface, it will always go with the form of a cell internally.

#### Multicast packet ingress pipeline processing 

****Control plane:**** The packets are punted to the line card CPU and are passed to different processes. It is checked if an MCID (Multicast ID) already exists and if it does not a new one is created. If one already exists it is updated with the new multicast pairs. Two tables are created, MCID mapping table which is a 128 bitmap mask where Ones represent NPUs who received a join and expect a copy of the packet from fabric and MCID-DB which associates ports where a replication is expected. 

****Data plane:**** Multicast packet is received on ingress interface and there are two places where packets are stored, L3 packets go to LPM* and L2 packets go to iTCAM. We receive the packet, we have a lookup on the forwarding block of the ingress pipeline that will perform a resolution inside the FEC, and it will point to a MCID and then the packet will be sent to the fabric and will be split in cells. 

![Screenshot 2021-03-23 at 15.35.55.png]({{site.baseurl}}/images/Screenshot 2021-03-23 at 15.35.55.png)
