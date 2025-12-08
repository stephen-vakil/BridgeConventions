# Inverted Minors
General approach:  
- Opener bids a minor.  
- Responder has no 4 card major but 4+/5+ cards in the opener's minor and 11+ points
- Goal is to explore No Trump by figuring out which suits are stopped, or short-circuit to the minor if No Trump isn't viable
- Once inverted minor is bid, the working assumption is that both minors are stopped unless someone bids the other minor

# Inverted Minor - Clubs #
```mermaid
graph TD

%% Definitions
    OpenMinor["1♣️ opened"]
    InvertedMinor["2♣️"]
%% Bidding flow
    OpenMinor -->|"No 4 card major, 5+ ♣️ and 10+ HCP"| InvertedMinor
    OpenMinor -->|4 card major| Bid4cardMajor[Bid 4 card major]

    InvertedMinor -->|❤️ stopper but not ♠️| Inverted2H[2 ❤️]
    InvertedMinor -->|♠️ stopper but not ❤️| Inverted2S[2 ♠️]
    InvertedMinor -->|♠️ and ❤️ stopper, medium hand| Inverted2NT[2NT]
    InvertedMinor -->|♠️ and ❤️ stopper, maximum hand| Inverted3NT[3NT]
    InvertedMinor -->|Concerned about ♦️| InvertedOtherMinor["2♦️"]

    InvertedOtherMinor -->|♦️ + ❤️ stopper, no ♠️ stopper| InvertedOtherMinor2H[2 ❤️]
    InvertedOtherMinor -->|♦️ + ♠️ stopper, no ❤️ stopper| InvertedOtherMinor2S[2 ♠️]
    InvertedOtherMinor -->|♦️ + ❤️ + ♠️ stopped| InvertedOtherMinor2N[2/3NT]
    InvertedOtherMinor -->|No ♦️ stopper| InvertedOtherMinorNoOtherMinor[3♣️]
```
# Inverted Minor - Diamonds #
```mermaid
graph TD

%% Definitions
    OpenMinor["1♦️ opened"]
    InvertedMinor["2♦️"]
%% Bidding flow
    OpenMinor -->|"No 4 card major, 4+ ♦️ and 10+ HCP"| InvertedMinor
    OpenMinor -->|4 card major| Bid4cardMajor[Bid 4 card major]

    InvertedMinor -->|❤️ stopper but not ♠️| Inverted2H[2 ❤️]
    InvertedMinor -->|♠️ stopper but not ❤️| Inverted2S[2 ♠️]
    InvertedMinor -->|♠️ and ❤️ stopper, medium hand| Inverted2NT[2NT]
    InvertedMinor -->|♠️ and ❤️ stopper, maximum hand| Inverted3NT[3NT]
    InvertedMinor -->|♠️ and ❤️ stopper,Concerned about ♣️| InvertedOtherMinor["3♣️"]

    InvertedOtherMinor -->|♦️ + ❤️ + ♠️ stopped| InvertedOtherMinor2N[3NT]
    InvertedOtherMinor -->|No ♦️ stopper| InvertedOtherMinorNoOtherMinor[3♦️]
```


# Sample Hands (TO DO)
**♠️**
**❤️**
**♦️**
**♣️**
