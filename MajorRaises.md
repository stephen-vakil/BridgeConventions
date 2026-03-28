# Major Raises

## General Approach
- A simple raise to 2M covers two hands: 3-card support with 6–10 points, or exactly 6 points with 4-card support
- Use Bergen (3♣ or 3♦) to show 4-card support in the 7–12 point range
- Use a preemptive 3M to show 4-card support with 0–5 points (alertable)
- Use Splinter to show game-forcing 4 card support with a singleton or void.  Usually the singleton or void is not an honor.
- Use Jacoby 2NT to show game-forcing **or better** 4 card support
- Use Drury with a passed hand to show 3+ card support and at least a minimum hand
- After a splinter bid, if opener has wasted honors in the short suit, opener usually will sign off in game

## When to choose splinter or Jacoby 2NT
- A splinter usually is limited in point range to less-than-slam.  It puts your partner in control of deciding how high.
- Because your honors are usually not in the splinter suit, partner could potentially explore slam if there's a good fit in other suits and they don't have many HCP in the splinter suit.
- Jacoby 2NT can be slam-worthy.  It puts you in control of deciding how high.

```mermaid

graph TD
    A[Start] -->B1[A - Opener in 1st or 2nd seat opens a major]
    A[Start] -->3rdseat[B - Opener in 3rd or 4th seat opens a major]

    B1 -->|"4-card support, 13+ HCP, no singleton/void"| Jacoby[Jacoby 2NT]:::alerted
    B1 -->|"4-card support, 13+ total points, with singleton or void"| Splinter[Splinter]:::alerted
    B1 -->|"3-card support 6-10pts, OR 4-card support exactly 6pts"| D3[2 of the major]
    B1 -->|"4-card support, 7-9 points"| D2[3♦ Bergen raise]:::alerted
    B1 -->|"4-card support, 10-12 points"| D1[3♣ Bergen raise]:::alerted
    B1 -->|"4-card support, 0-5 points"| D4[3 of the major]:::alerted

    3rdseat -->|Medium or more and 3+ card support| Drury[Drury]
    Drury -->|With 3 cards| E1[2 clubs]:::alerted
    Drury -->|With 4 cards and medium or more| E2[2 diamonds]:::alerted
    3rdseat -->|Minimum and 3 cards| E3[2 of Major]
    3rdseat -->|Minimum and 4 cards| E4[3 of Major]:::alerted
    3rdseat -->|Medium balanced hand| E5[2NT]

    classDef alerted fill:#FFC0CB,stroke:#ff0000,stroke-width:2px;
```

<div style="background-color: #FFC0CB; border: 1px solid #FF0000; padding: 1px; max-width: 50px; font-size: x-small">
  Alertable
</div>