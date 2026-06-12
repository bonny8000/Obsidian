---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.76
---

# How should RBA be measured by a real robot in changing elevator conditions?

## Short Answer
A real robot should measure RBA dynamically using onboard sensors: depth sensors or LiDAR to estimate available floor space inside the elevator door zone, combined with a people-count estimate from camera or weight sensor. The robot computes available entry space minus estimated body footprint of current passengers. This real-time calculation should feed into a boarding decision model that also factors in total crowding level, consistent with the NAVER LABS research findings.

## Evidence
- [[concepts/robotics-spatial/robot-boarding-area|Robot Boarding Area]] — "RBA is not enough by itself; total crowding also affects acceptance. Robots should sometimes give up boarding and wait, especially when the elevator feels crowded. RBA can be used as an input to socially aware robot decision-making."
- [[concepts/robotics-spatial/socially-aware-navigation|Socially Aware Navigation]] — "Crowding and human acceptance are planning variables. Waiting can be the better UX choice even when a route is physically possible."
- [[sources/naverlabs-blog-10034251|NAVER LABS: Robot Elevator Boarding Acceptance]] — "People judge robot boarding acceptability using both crowding level and whether a practical entry space remains available."
- [[concepts/robotics-spatial/human-robot-interaction|Human-Robot Interaction]] — "Shared building infrastructure creates recurring HRI situations such as elevators. Human acceptance can be modeled and tested."

## Follow-up Sources Needed
- The underlying ACM CHI 2026 paper cited in the NAVER LABS blog for specific measurement method details and sensor configurations.
