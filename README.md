# WEC-Weyburn

WEC 2021 Programming Competition

# Prompt

It is your task to design a system for you and your siblings to play the modified chess game found in the <Rules> section despite the fact that you live far away from each other.

## Rules

All rules are described as variations on the traditional game and it is assumed that competitors are vaguely familiar with the game.

There are seven game pieces each with their own movement and attacking functions:

### Pawns

    - These start by filling the front row of the players side of the board
    - They may move one to three spaces forward but immediately jump to the left or right of an enemy encountered in said line This means they may only “take” a piece if there is two enemy pieces adjacent to each other and ahead of them
    - One to four of the pawns are replaced as explained in the vanguard section

### Bishops

    - Move and placed as normal

### Rooks

    - Move and placed as normal

### Knight

    - Move as a normal game’s queen except they can only reach between 2 and 4 (inclusive) squares away
    - Jumping is preserved

### Queen

    - Must wait 5 turns between moves - may change this to balance as you see fit
    - In the scenario where there is additional queens, the counter resets after the last friendly queen moves
        -- Eg. Queen Moves, Queen Moves, Queen Moves, Five turn wait before FIRST queen may move again
    - They may move to and attack any square on their side of the board which a series of straight lines can bring them to. (Anywhere, unless they are boxed in)

### King

    - Moves and should be protected as normal

### Vanguards

    - May move in an L of any size which is fully clear (except the final square)
    - At the beginning of the game the player is given two vanguards + those as defined below and can replace any of their pawns in the front row with them.
    - If this is not implemented in your design or the player does not choose positions it defaults to the outermost square biasing to the kingside in the event there is an odd number

- The game board can be any even amount from 8x8 to 16x16 squares (10x10,12x12…)
  -- For every increase in width beyond 8 (10,12,14,16), additional pieces are added as described below:
  -- At 10, each player receives two more knights, on the outside of the existing ones as well as two additional pawns in the front row
  -- At 12, each player receives two more bishops, on the outside of the existing ones as well as one vanguard and one pawn to place in the front row
  -- At 14, each player receives two more rooks, on the outside of the existing ones as well as two additional pawns in the front row
  -- At 16, each player receives two morel queens, on the outside of the existing queen/king pair as well as one vanguard/one pawn to place in the front row

- You may add any additional rules, game modes, or supporting infrastructure as you see fit to improve the deliverables. These will be counted towards your creativity/innovation points or your overall design points depending upon their nature.

# Additional Notes
- Made using Python