## sh_t

another word puzzle game (under heavy development)

#### get the code

    git clone https://github.com/philshem/sh_t.git

#### run the code

    cd sh_t
    git pull
    python3 sh_t.py 

The `git pull` step is optional, but because the code is under heavy development, I suggest it.

#### play sh_t

Each word has exactly one partner word that is one letter off. It is your job to guess the letter to find the other valid word. The letter to guess is capitalized (e.g. `Buzz` becomes `Fuzz`, and `aShy` to `aChy`).

    HOW TO PLAY:
            Make the only other valid word by guessing the capital letter.
                    Example: couNt becomes couRt
            Type a letter and hit ENTER to play your turn.
            Incorrect guesses :  -1 points, but keep trying!
            Correct guesses :  5 points
            Hint ENTER to skip a word :  -3 points
            Type !h ,and ENTER to get a hint:  -3 points
                    (Hints are randomly shuffled)
            Type !q and ENTER to quit

To change the default scoring, edit `params.py`
