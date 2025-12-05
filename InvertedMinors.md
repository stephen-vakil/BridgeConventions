# Inverted Minors
General approach:  
- Opener bids a minor.  
- Responder has no 4 card major but 4+ cards in the opener's minor and 11+ points
- Goal is to explore No Trump by figuring out which suits are stopped, or short-circuit to the minor if No Trump isn't viable
- Once inverted minor is bid, the working assumption is that both minors are stopped unless someone bids the other minor

```mermaid
graph TD
    A[Minor] -->|"No 4 card major, 4+(D) or 5(C) in the minor and 10+"| InvertedMinor[2 of the minor]
    A[Minor] -->|4 card major| Bid4cardMajor[Bid 4 card major]

    InvertedMinor -->|Hearts stopper but not spades| Inverted2H[2 hearts]
    InvertedMinor -->|Spades stopper but not hearts| Inverted2S[2 spades]
    InvertedMinor -->|Hearts and Spades stopper, medium hand| Inverted2NT[2NT]
    InvertedMinor -->|Hearts and Spades stopper, maximum hand| Inverted3NT[3NT]
    InvertedMinor -->|Concerned about other minor| InvertedOtherMinor["2(D) or 3(C) of other minor"]

    InvertedOtherMinor -->|Other minor stopper + Hearts stopper, no spades stopper| InvertedOtherMinor2H[2/3 hearts]
    InvertedOtherMinor -->|Other minor stopper + Spades stopper, no hearts stopper| InvertedOtherMinor2S[2/3 spades]
    InvertedOtherMinor -->|Other minor stopper + Spades and hearts stopped| InvertedOtherMinor2N[2/3NT]
    InvertedOtherMinor -->|No stopper in other minor| InvertedOtherMinorNoOtherMinor[3/4 of opener's minor]
```

# Sample Hands (TO DO)
♦️❤️♠️♣️
