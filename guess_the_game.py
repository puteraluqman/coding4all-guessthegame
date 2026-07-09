"""
Guess the Game - a Python guessing game for the Coding for All challenge.

Author: Putera Muhammad Luqmanul Hakim
School: Sekolah Kebangsaan Seksyen 10 Kota Damansara

Disclaimer: This program was created for educational and competition purposes
as part of the "Coding for All" Python Coding Challenge by Penang Science
Cluster. All game titles referenced in this program are the trademarks and
property of their respective owners and are used here only as guessing-game
content; no ownership or affiliation is claimed.
"""

import random

GAMES = {
    "Minecraft": [
        "You can mine resources and craft tools.",
        "There's a Creeper that explodes near you.",
        "The world is made entirely of blocks you can place and destroy.",
        "Steve and Alex are the default player skins in this sandbox game.",
        "This game was created by Markus 'Notch' Persson and released in 2011.",
    ],
    "Among Us": [
        "You complete tasks aboard a spaceship.",
        "One or more players are secretly working against the crew.",
        "Players can call an emergency meeting to vote someone out.",
        "Small bean-shaped astronauts try to find the 'impostor' before they kill everyone.",
        "This game exploded in popularity in 2020 thanks to livestreamers.",
    ],
    "Fortnite": [
        "100 players parachute onto an island.",
        "You can build walls and ramps out of materials you collect.",
        "The playing area shrinks as a storm closes in.",
        "The last player or team standing wins this battle royale.",
        "Its dance emotes, like the 'Floss', became a real-world pop culture trend.",
    ],
    "Roblox": [
        "It's actually a platform full of games made by other players.",
        "You can create your own experiences using a scripting language called Lua.",
        "Your character is made of blocky, customizable avatars.",
        "Its in-game currency is called Robux.",
        "This platform launched in 2006 and lets anyone build their own games.",
    ],
    "Tetris": [
        "Falling shapes must be arranged without leaving gaps.",
        "Clearing a full row makes it disappear.",
        "The pieces are made of four squares each, called tetrominoes.",
        "This classic puzzle game was created in the Soviet Union in 1984.",
        "Its creator, Alexey Pajitnov, named it after tennis and the Greek word for four.",
    ],
    "Pac-Man": [
        "You move through a maze eating small dots.",
        "Four ghosts are chasing you.",
        "Eating a big flashing dot lets you eat the ghosts for a short time.",
        "The main character is a yellow circle known for its chomping sound.",
        "This 1980 arcade classic was originally called 'Puck-Man' in Japan.",
    ],
    "Chess": [
        "Two players take turns moving pieces on an 8x8 board.",
        "The most powerful piece is the queen.",
        "The goal is to checkmate the opposing king.",
        "This ancient strategy game uses pieces like pawns, knights, and bishops.",
        "World championships have been held for this game since the 1800s.",
    ],
    "Flappy Bird": [
        "You tap the screen to keep a bird flying.",
        "You must avoid green pipes.",
        "One touch on an obstacle ends the game instantly.",
        "This notoriously hard mobile game was pulled from app stores by its creator in 2014.",
        "Its creator, Dong Nguyen, said the game was 'too addictive' and removed it.",
    ],
    "Grand Theft Auto V": [
        "You can steal cars and evade the police in an open world.",
        "The game is set in the fictional state of San Andreas.",
        "You control three different playable characters throughout the story.",
        "Online multiplayer heists let you rob banks with friends.",
        "Developed by Rockstar Games, it's one of the best-selling entertainment products ever.",
    ],
    "Call of Duty": [
        "You battle through fast-paced first-person shootouts.",
        "Popular multiplayer modes include Team Deathmatch and Search and Destroy.",
        "Its battle royale spin-off is called Warzone.",
        "Campaign missions often follow modern or historical military conflicts.",
        "Published by Activision, this franchise gets a new title almost every year.",
    ],
    "League of Legends": [
        "Two teams of five battle to destroy the enemy base.",
        "Players choose a unique hero called a 'champion' before each match.",
        "Towers, minions, and jungle monsters populate the battlefield.",
        "It's one of the most-watched esports games in the world.",
        "This MOBA is developed by Riot Games and is often shortened to 'LoL'.",
    ],
    "Brawl Stars": [
        "You control a character with a unique attack and special ability in fast 3-minute matches.",
        "Game modes include Gem Grab, Brawl Ball, and Knockout.",
        "Collecting gems and holding them until a countdown ends wins one popular mode.",
        "This game was developed by the same Finnish studio behind a village-building strategy game.",
        "Its spiky-haired blonde mascot, Shelly, appears throughout its promotional art.",
    ],
    "Genshin Impact": [
        "You explore an open world as a Traveler searching for a lost sibling.",
        "Characters can be summoned through a gacha system using in-game currency.",
        "Elemental powers like Fire, Water, and Electro combine for special reactions.",
        "Gliding across the map with a magical glider is a core traversal mechanic.",
        "This free-to-play action RPG is developed by HoYoverse, set in the world of Teyvat.",
    ],
    "Super Mario Bros": [
        "A mustached plumber runs and jumps across colorful platform levels.",
        "Stomping on enemies like Goombas defeats them.",
        "Grabbing a mushroom makes your character grow bigger.",
        "The goal of each level is often to reach a flagpole.",
        "This character's princess, Peach, is regularly kidnapped by a villain named Bowser.",
    ],
    "The Legend of Zelda": [
        "You explore a fantasy kingdom solving puzzles and dungeons.",
        "A magical, ageless hero named Link is usually the playable character.",
        "The Triforce is a sacred relic central to the story.",
        "Princess Zelda often needs rescuing from the villain Ganon.",
        "This long-running Nintendo franchise inspired countless action-adventure games.",
    ],
    "Mario Kart": [
        "You race go-karts across colorful, obstacle-filled tracks.",
        "Item boxes give you things like shells and bananas to use against rivals.",
        "A blue shell homes in on whoever is in first place.",
        "Familiar characters like Mario, Luigi, and Bowser are playable racers.",
        "This Nintendo racing spin-off is a staple of party gaming nights.",
    ],
    "Candy Crush Saga": [
        "You swap colorful pieces to make matches of three or more.",
        "Special combos are created by matching four or five pieces in a row.",
        "Each level has a limited number of moves or time to reach the goal.",
        "Striped candies and wrapped candies help clear the board.",
        "This match-three mobile puzzle game was developed by King and has thousands of levels.",
    ],
    "Subway Surfers": [
        "You dash down train tracks, dodging oncoming trains.",
        "A grumpy inspector and his dog chase you the whole time.",
        "Swiping lets you jump, roll, and switch lanes to avoid obstacles.",
        "Collecting coins lets you unlock new characters and hoverboards.",
        "This endless runner features graffiti-loving teens escaping the law.",
    ],
    "Clash of Clans": [
        "You build and defend a village using gold, elixir, and dark elixir.",
        "Training troops like Barbarians and Archers lets you attack other players' bases.",
        "Joining a Clan lets you donate troops and battle in Clan Wars.",
        "Upgrading your Town Hall unlocks new buildings and defenses.",
        "This mobile strategy game was developed by Supercell and became a global phenomenon.",
    ],
    "Mobile Legends": [
        "Two teams of five battle across three lanes to destroy the enemy base.",
        "Players pick a unique Hero with special roles like Tank, Marksman, or Assassin.",
        "Farming jungle creeps and lanes helps you gain gold and experience.",
        "Destroying turrets clears the path toward the enemy's core.",
        "This mobile MOBA is especially popular in Southeast Asia and is made by Moonton.",
    ],
}

MAX_GUESSES = len(next(iter(GAMES.values())))  # one guess per clue available
QUESTIONS_PER_ROUND = 5


# Randomly pick QUESTIONS_PER_ROUND distinct games from GAMES for a round.
def choose_round_games():
    try:
        return random.sample(list(GAMES.keys()), QUESTIONS_PER_ROUND)
    except ValueError as error:
        raise ValueError(
            f"Not enough games in GAMES ({len(GAMES)}) to fill a round of "
            f"{QUESTIONS_PER_ROUND} questions."
        ) from error


# Reveal clues one at a time for secret_game and return the percentage mark earned.
def play_question(secret_game):
    clues = GAMES[secret_game]
    attempts_used = 0

    print("\nI'm thinking of a game. Try to guess it from the clues!")

    while attempts_used < MAX_GUESSES:
        print(f"\nClue {attempts_used + 1}: {clues[attempts_used]}")
        guess = input("Your guess: ").strip()
        attempts_used += 1

        if guess.lower() == secret_game.lower():
            mark = round((MAX_GUESSES - attempts_used + 1) / MAX_GUESSES * 100)
            print(f"\nCorrect! The game was '{secret_game}'.")
            print(f"You guessed it in {attempts_used} attempt(s). Mark: {mark}%")
            return mark

        remaining = MAX_GUESSES - attempts_used
        if remaining > 0:
            print(f"Not quite. {remaining} clue(s) left.")

    print(f"\nOut of guesses! The game was '{secret_game}'.")
    return 0


# Run one round of QUESTIONS_PER_ROUND questions and print the overall mark.
def play_round():
    round_games = choose_round_games()
    total_mark = 0

    print(f"\n=== New Round: {QUESTIONS_PER_ROUND} games to guess! ===")

    for question_number, secret_game in enumerate(round_games, start=1):
        print(f"\n--- Question {question_number} of {QUESTIONS_PER_ROUND} ---")
        total_mark += play_question(secret_game)

    average_mark = round(total_mark / QUESTIONS_PER_ROUND)
    print(f"\n=== Round complete! Your overall mark: {average_mark}% ===")


# Entry point: greet the player and keep playing rounds until they quit.
def main():
    print("=== Guess the Game ===")
    try:
        while True:
            play_round()
            again = input("\nPlay another round? (y/n): ").strip().lower()
            if again != "y":
                print("Thanks for playing!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGame interrupted. Thanks for playing!")
    except ValueError as error:
        print(f"\nSetup error: {error}")


if __name__ == "__main__":
    main()
