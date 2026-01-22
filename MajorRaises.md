# Major Raises

## General Approach
- Use Bergen to show invitational 4 card support
- Use Splinter to show game-forcing 4 card support with a singleton or void.  Usually the singleton or void is not an honor.
- Use Jacoby 2NT to show game-forcing **or better** 4 card support
- Use Drury with a passed hand to show 3+ card support and at least a minimum hand

## When to choose splinter or Jacoby 2NT
- A splinter usually is limited in point range to less-than-slam.  It puts your partner in control of deciding how high.
- Because your honors are usually not in the splinter suit, partner could potentially explore slam if there's a good fit in other suits and they don't have many HCP in the splinter suit.
- Jacoby 2NT can be slam-worthy.  It puts you in control of deciding how high.

```mermaid

graph TD
    A[Start] -->B1[A - Opener in 1st or 2nd seat opens a major]
    A[Start] -->3rdseat[B - Opener in 3rd or 4th seat opens a major]

    B1 -->|With 4 card support, 13+ HCP, and no void or singleton| Jacoby[Jacoby 2NT]:::alerted
    B1 -->|With 4 card support, 13+ total points including distribution, and a singleton or void| Splinter[Splinter]:::alerted
    B1 -->|With 4 card support and 12- points| Bergen[Bergen]

    Bergen -->|With 10-12 points| D1[3 Club Bergen raise]:::alerted
    Bergen -->|With 7-9 points| D2[3 Diamond Bergen raise]:::alerted
    Bergen -->|With 4-6 points| D3[2 of the major Bergen raise]
    Bergen -->|With 0-3 points| D4[3 of the major Bergen raise]:::alerted

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