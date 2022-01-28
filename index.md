# Sid Allocation

**Mission statement**: a working group to self organize sid ranges for the benfit of users


|      SID Range      | Organization          | Note                                                                             |
| :-----------------: | :-------------------- | :------------------------------------------------------------------------------- |
|   1000000-1999999   | De Facto              | Reserved for Local Use - Put your custom rules in this range to avoid conflicts  |
|   2000000-2099999   | Emerging Threats      | ET Open                                                                          |
|   2100000-2103999   | Emerging Threats      | Forked Snort GPL Signatures (Originally sids 3464 and prior)                     |
|   2200000-2200999   | OISF                  | Suricata Decoder Events                                                          |
|   2210000-2210999   | OISF                  | Suricata Stream Events                                                           |
|   2220000-2299999   | OISF                  | Suricata Reserved                                                                |
|   2800000-2899999   | Emerging Threats      | Emerging Threats Pro Full Coverage Ruleset - ETProRules                          |
|   2400000-2400999   | Emerging Threats      | SpamHaus DROP List                                                               |
|   2402000-2402299   | Emerging Threats      | Dshield Top Attackers Rules                                                      |
|   2403300-2403499   | Emerging Threats      | CIArmy.com Top Attackers Rules - http://www.ciarmy.com#list                      |
|   2404000-2405999   | Emerging Threats      | Shadowserver.org Bot C&C List - BotCC                                            |
|   2404000-2405999   | Emerging Threats      | Shadowserver.org Bot C&C List Grouped by Port - BotCC                            |
|   2406000-2406999   | Emerging Threats      | Russian Business Network Known Nets - OBSOLETED - RussianBusinessNetwork         |
|   2408000-2408499   | Emerging Threats      | Russian Business Network Known Malvertisers - OBSOLETED - RussianBusinessNetwork |
|   2520000-2521999   | Emerging Threats      | Tor Exit Nodes List Updated Daily - TorRules                                     |
|   2522000-2524999   | Emerging Threats      | Tor Relay Nodes List (NOT Exit nodes) Updated Daily - TorRules                   |
|   2525000-2526999   | Emerging Threats      | 3CORESec Poor Reputation Updated Daily - 3CORESec                                |
|   2527000-2528999   | Emerging Threats      | Threatview.io High Confidence Cobalt Strike C2 Updated Daily - threatview_io     |
|   2610000-2619999   | TGI HUNT              | Hunting Ruleset                                                                  |
|   2620000-2629999   | 3CORESec NIDS         | Lateral Movement Ruleset                                                         |
|   5000000-5000213   | Etnetera a.s.         | Etnetera aggressive IP blacklist                                                 |
|   5000000-5000033   | MalSilo               | MalSilo DNS Rules                                                                |
|   5000034-5000122   | MalSilo               | MalSilo IP Rules                                                                 |
|   5000123-5000505   | MalSilo               | MalSilo URL Rules                                                                |
|   7724000-7726000   | 3CORESec NIDS         | Sinkholes Ruleset                                                                |
|  10000005-11999999  | Positive Technologies | Positive Technologies Attack Detection Team ruleset                              |
| 902200000-902204616 | Abuse.ch              | Abuse.ch SSL Blacklist                                                           |
| 906200000-906200096 | Abuse.ch              | Abuse.ch Suricata JA3 Fingerprint Ruleset                                        |


- [x] Add ranges from https://doc.emergingthreats.net/bin/view/Main/SidAllocation
- [x] add TGI range
- [x] add 3CORESec range
- [x] Add ranges from https://github.com/OISF/suricata-intel-index/blob/master/index.yaml
- [ ] add links to sources as [references](https://doc.emergingthreats.net/bin/view/Main/SidAllocation)
- [ ] draft - upper and lower bounds, org, reference




