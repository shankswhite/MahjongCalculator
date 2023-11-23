# MahjongCalculator
A Score Calculator for Riichi Mahjong. It would be the best.
First Goal:
Apply discrete math to solve some questions of Mahjong Playing.
Easy:
1. Under what circumstances should we discard a tile from a set of two identical tiles? in other words, when the value of pairs is maximized?
2. How different 4-tile shapes are prioritized?

Hard:
1. Under what circumstances should we choose to discard tiles which let our hand further away from Ready, and to increase number of acceptable tiles?
2. Which round to discard Honor tiles is is considered to be a balance of defense and attack?


Some Consensus for Concepts:
1. Tiles' Name
<img width="635" alt="image" src="https://github.com/shankswhite/MahjongCalculator/assets/21222666/b5d1839d-208d-4a6c-a80e-8e5596961d68">
tiles' number 2 - 8: simples (tanyao)
tiles' number 1 or 9: terminals (yaochu)

<img width="601" alt="image" src="https://github.com/shankswhite/MahjongCalculator/assets/21222666/01af6d08-1cf5-409f-8bf2-e04f8f491c25">

2. Objectives
1) One of the major goals in playing mahjong is to win a hand.
2) Standard Hand
   To win a standard hand, we need to complete four groups (mentsu) and one head (atama;finalpair).
   There are three exceptions to this:
     chiitoitsu (Seven Pairs),
     kokushi musou (ThirteenOrphans),
     andnagashi mangan(All Terminals and Honors Discard) do not require four groups and one head.
4) Chow & Pung
   Groups can be classified into two kinds — run and set
   Chow is a set of three consecutive number tiles
   Pung is a set of three identical tiles: e.g., ———, $$$.
   Kong is a set of four identical tiles.
5) Ready & n-away
   We say a hand is ready (tenpai) when the hand can be complete with one more tile.
   <img width="647" alt="image" src="https://github.com/shankswhite/MahjongCalculator/assets/21222666/37591468-0dfc-41cd-a785-aa636b255cd6">
   We say a hand is 1-away from ready (1-shanten) when the hand can become ready with one more tile.
   <img width="625" alt="image" src="https://github.com/shankswhite/MahjongCalculator/assets/21222666/2fb040aa-1460-4a5f-9f65-918c5bde2a00">
   <img width="624" alt="image" src="https://github.com/shankswhite/MahjongCalculator/assets/21222666/4b177297-3453-4e9d-8581-c63df81760e1">

6)
   <img width="544" alt="image" src="https://github.com/shankswhite/MahjongCalculator/assets/21222666/33bab1f9-08e9-486a-8c66-9279aa457eef">





