"""
MODULES
"""

# For text prettifying
import textwrap

width = 88

separator = "-" * width

"""
ITEMS
"""


class Items:
    """
    Class to make each item in the game world
    """

    def __init__(self, print_name, location, init_descript, take_descript):
        """
        :param print_name: Human-readable name (can be multi word)
        :param location: Current location of item
        :param init_descript: Prints when item is in a room
        :param take_descript: Prints when player takes item
        """
        self.print_name = print_name
        self.location = location
        self.init_descript = init_descript
        self.take_descript = take_descript

    def get_print_name(self):
        return self.print_name

    def get_init_descript(self):
        return self.init_descript

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def get_take_descript(self):
        return self.take_descript


t_item = Items(  # something about deleting this breaks the function for capturing the item from player input, so I'm leaving it in
    "test item",
    "t_room_2",
    "a mystery widget glints in the ash",
    "you got friend crow to take it for you",
)
tooth = Items(
    "wolf's tooth",
    "edge",
    "The ivory edge of a predator's TOOTH glints under the shed needles of pines.",
    [
        "The scent of its owner is long gone, but pushing aside the decaying leaves to reveal it still makes you nervous.",
        "The crow flutters down, curious as to what you found.",
        "'Crrrr tooth great gift,' it says. It plucks it easily from the ground and then deposits it into the bag.",
    ],
)
skull = Items(
    "deer skull",
    "bank",
    "The jagged edges of a SKULL are visible just off the path.",
    [
        "Death needn't require a danger lurk nearby, but any reminder of it makes you nervous. The crow hops over.",
        "'Seven tines, seven stars, seven gifts!' it says with glee.",
        "It's still too large for the bag, so, with reluctance and apologies, you place a hoof between the dead stag's eyes and press.",
        "It shatters easily, the sudden sound causing you to dance backwards. The crow isn't perturbed; it grabs the the now-separated crown and adds it to the bag.",
    ],
)
stone = Items(
    "carnelian",
    "river",
    "Beyond the shifting barrier of the water, a red STONE stands apart.",
    [
        "You call the crow over, but it seems to ignore you as it continues playing in water. You snort, thinking it no different from an impudent foal, but your heart feels heavy at the comparison.",
        "Once you've finished your quest, once things are set right again, you'll never complain about the energy and wonder of the young again.",
        "The crow finally joins you, and you point to the stone with your muzzle. It studies it for a moment before fishing it out with its beak.",
        "'Blood frozen into rock,' it says. The words aren't skewed despite its mouth full of stone, which ticks your anxiety ever-higher.",
    ],
)
nugget = Items(
    "gold nugget",
    "bend",
    "The glint of GOLD sparkles amongst the gravel.",
    [
        "You paw at the spot, shifting pebbles as they shift underhoof, leaving you at the sensation of nearly falling. The nugget is small, but it excites the crow like you've haven't seen before.",
        "'Crrrr shiny! Shiny good! Great, even!' It picks up the nodule and hesitates, as if considering something. It then grumbles before tucking it into the bag.",
        "You step away, but you can hear the crow poking around the gravel some more.",
    ],
)
egg = Items(
    "plover egg",
    "delta",
    "Amongst the reeds lies a nest with a single EGG.",
    [
        "You turn away from the nest and look elsewhere for a suitable gift, but the crow hops onto your withers and tugs at your mane.",
        "'Gift!' it says, half statement, half order. You tell it you're still looking for one, but it tugs you again. 'Egg!'",
        "You decline; the crow responds with 'Some die, some live. Bug, bird, grass, all same, crrrr.'",
        "You want to argue, but the journey has tired you, and you're unsure of the answer yourself. Don't the plants you eat have parents, children that will miss them? Do you curse the lion for doing what she must to feed her cubs? You would do the same, if you were born with teeth sharp instead of flat.",
        "You step towards the egg and ask the crow to get it, who is more than happy to oblige.",
    ],
)
shell = Items(
    "conch shell",
    "pools",
    "The sunset hues from within a SHELL stand out amongst the pools.",
    [
        "You carefully find your footing as you get closer to the shell. It's large and looks heavy, so you might need to help lift it. You move closer but are blocked by a storm of black.",
        "'Careful! Careful,' the crow squawks. You ask why, but it doesn't answer. It grabs a few small rocks and flings it at the shell, ducking low as if to see if anything would come out.",
        "After several minutes, the crow seems satisfied. You ask it again, and it laughs. 'Sometimes crab, sometimes snail! Kill fast, if not careful.'",
        "You don't know what sort of beast a crab is, but it couldn't be large if it could hide in the shell. How a snail could kill someone, especially an animal as large as yourself, is a possibility you'd never worried about before, but shall do so forevermore.",
        "You help the crow add it to the now-hefty bag of gifts.",
    ],
)
fossil = Items(
    "fossilized footprint",
    "fjord",
    "Amongst the rocks is one bearing a frozen FOOTPRINT.",
    [
        "You get a closer look and see it's similar to the crow's, with three pointed toes. But they're thick, with claws that could easily slice you from throat to tail.",
        "The crow hops over and can stand within the borders of it comfortably. You ask what possibly could have made it.",
        "'Cousin?' it offers. 'Big crows, big teeth, bones find sometimes.' You ask it where while your ears swivel for danger. A predator this big would have a hard time hiding, but the fjord was narrow with little room to run.",
        "The crow tilts its head back and forth in thought. 'Mountain, river sometimes. But bones old, turn to stone, they're all gone maybe.'",
        "You want to say that it's impossible for something to be gone forever, but only because you want it to be true. Either a predator like this could still exist, or your kind risks disappearing from the world altogether.",
        "The crow helps you pry it lose, but you have to carry it with your mouth, but your journey is almost at an end, so you'll not need to travel far.",
    ],
)

item_lookup = {
    """
	Converts player input into item instance
	"""
    "t_item": t_item,
    "test_item": t_item,
    "tooth": tooth,
    "skull": skull,
    "stone": stone,
    "red": stone,
    "gold": nugget,
    "egg": egg,
    "shell": shell,
    "footprint": fossil,
    "foot": fossil,
    "fossil": fossil,
}

"""
ROOMS
"""
# room dict template
"""
	"name" : { # num in planning docs
		"print_name": "",
        # directions: connected room (if any, else fail), move descript
		"north": ["",""],
		"south": ["",""],
		"east": ["",""],
		"west": ["",""],
		"init_descript": "",
		"item": ""
	},
"""

rooms = {
    # TEST ROOMS
    """
	Key each room, which is sub dict with:
    	printed name,
        cardinal directions (list for connected room + descript during move),
        descript for room per turn,
        item
	"""
    "t_room_1": {  # same thing with these two test rooms. Something about deleting them makes the init_descript lookup fail for the start of turn function. So I'm keeping it in (despite the rooms being inaccessible to the player)
        "north": ["fail", "north fail descript"],
        "south": ["fail", "south fail descript"],
        "east": ["t_room_2", "you go east to t room 2 and see stuff"],
        "west": ["fail", "west fail descript"],
        "init_descript": "you are currently in room 1 its to the west of the volcano and closer to the fjord",
        "item": "",
    },
    "t_room_2": {
        "north": ["fail", "north fail 2"],
        "south": ["fail", "south fail 2"],
        "east": ["fail", " east fail 2"],
        "west": ["t_room_1", "you go west to t room 1 and see other stuff"],
        "init_descript": "you are currently in room 2 its east of the volcano and closer to the tidepools",
        "item": "",
    },
    #
    "valley": {  # room0
        "print_name": "the valley",
        "north": [
            "edge",
            "You pick your way along the familiar path NORTH toward the end of the valley. The hills and mountains on either side soon give way to the darkness of the forest's edge.",
        ],
        "south": [
            "fail",
            "You turn your head SOUTH to see the narrow path between the mountains. Between the cats who blend into the stone with their spotted coats and the treacherous footing, nothing good will happen if you tread there.",
        ],
        "east": [
            "fail",
            "The mountains to the EAST protect you from any predators who travel alongside the river on its other side. They can only reach your herd through the narrow entrance to the NORTH.",
        ],
        "west": [
            "fail",
            "The mountains to the WEST protect you from the unknown. You've spoken to birds who have said they've come from the lands where the sun finally rests, but their stories about endless water are too fantastical to believe.",
        ],
        "init_descript": [
            "The valley is the home of your herd and always has been. But, as the seasons turn, the grass dies, as do you, one by one. It's your home, safe, but clearly no longer. If the crow is right, your only hopes to save them is to journey beyond.",
            "You know the path out is to the NORTH towards the glacier towering in the distance.",
        ],
        "item": "",
    },
    "edge": {  # room1
        "print_name": "the forest's edge",
        "north": [
            "fail",
            "The forest continues to the NORTH. The distance between the trees is just wide enough for you to fit, but the trunks are too many to give you the space to flee. You take one last, long look before deciding not to go that way.",
        ],
        "south": [
            "valley",
            [
                "You retread your hoofsteps SOUTH to the valley. Your sisters lift their heads as the wind carries your scent to them. The crow lands on your withers, the tips of its claws pricking into your hide.",
                "'Crrr no gifts in valley,' it says. 'Journey far, but go back after.'",
                "You know the crow is right; you won't be able to complete your quest--or save the others--if you linger here.",
            ],
        ],
        "east": [
            "bank",
            "The natural path EAST between the trees continues as the sound of water grows. You follow the sound to a natural in the woods, dark trunks framing your view of the other side of the river.",
        ],
        "west": [
            "fail",
            [
                "The forest continues to the WEST. You take a hesitant step toward it, but freeze when you hear a branch snap. The sound is as sharp and sudden as teeth to your throat.",
                "'Crrr no mean to scare.'",
                "You look up to see the crow perched in one of the trees, a branch in its beak. While it's a blessing that there's more ways a predator can give itself away, the anxiety would surely kill you first.",
            ],
        ],
        "init_descript": "The branches lean overhead, darkening your view of the sky. This is not a place for creatures like yourself, only those too small and too nimble to be of any interest to the wolves and lions. You can see a natural path between the trees heading EAST, as well as the path back to your valley to the SOUTH.",
        "item": tooth,
    },
    "bank": {  # room2
        "print_name": "the river bank",
        "north": [
            "fail",
            "The forest stretches further NORTH, but you can see the frigid base of the glacier between the trees. There's no room for you to run, so going in that direction wouldn't be wise.",
        ],
        "south": [
            "fail",
            "The mountains that protect your valley are to the SOUTH. Your hooves are singular and muscles withered, so traversing them is not an option.",
        ],
        "east": [
            "river",
            [
                "You step cautiously toward the river, looking up and down its edge for any predators who might be waiting. Trees block your line of sight, so you take another step.",
                "The ground gives way underhoof and you fall, dirt and roots following you into the water. You quickly get back onto your feet, heart hammering.",
                "Nothing was attracted by the noise, and the only thing that seems to be wounded is your pride.",
            ],
        ],
        "west": [
            "edge",
            "You take the path back into the forest, your ears searching for anything that might be lurking beyond sight. But the only other being here is the crow, so you should be safe for now.",
        ],
        "init_descript": "The ground slopes EAST down towards the river, a thing that had once been mighty, but now does little more than remind you of what's once been. The air is quiet, although your ears stay sharp if something had followed you on the path WEST.",
        "item": skull,
    },
    "river": {  # room3
        "print_name": "the river",
        "north": [
            "bend",
            [
                "You walk within the shallow water, expecting it to rise as you move towards the glacier, but it doesn't grow in strength.",
                "Instead you see the river has curled in on itself, like a dying snake, feeding most of its waters into the dead end.",
            ],
        ],
        "south": [
            "delta",
            "As you follow the river SOUTH, the gravel of its bottom shifts into mud. You move onto land to continue following it, but that, too, soon turns soft and sinking.",
        ],
        "east": [
            "cave",
            "A natural trail takes you out of the water and onto stone and the mouth of the cave.",
        ],
        "west": [
            "bank",
            "Carefully, you find new footholds to get back up and onto dry land.",
        ],
        "init_descript": [
            "The river is still cool, despite its shallowness. It's perfect for the crow, it seems, who starts splashing in the water.",
            "The river's source is to the NORTH, while it continues to flow SOUTH. To the EAST is the bank by the forest, and the bank to the WEST has the mouth of a dark cave.",
        ],
        "item": stone,
    },
    "bend": {  # room4
        "print_name": "the river bend",
        "north": [
            "fail",
            [
                "The wall of ice extends far to the NORTH. You ask the crow how far away the other side is.",
                "It only laughs. 'Forever! And ever and ever.' You're unsure how that's even possible, but, as it always feeds the river and doesn't disappear like the snow on the mountains, it must be true.",
            ],
        ],
        "south": [
            "river",
            "You follow the water back SOUTH, its chill sinking into your fetlocks.",
        ],
        "east": [
            "fail",
            "Tall cliffs stretch above the river to the EAST. You scan their base to find a trail where you could climb up, but don't see any such way.",
        ],
        "west": [
            "fail",
            [
                "A waterfall to the WEST is the source of the river. You have to flex your head all the way back to see where it starts; it's so high that the wind blows off some of the water into a fine mist.",
                "The waters there are much stronger, so you decide not to go in that direction.",
            ],
        ],
        "init_descript": [
            "The glacier looms over you at the bend of the river. Slivers of mountains ground down by the wall of ice coat the banks and ground underhoof.",
            "The river flows SOUTH from where you came.",
        ],
        "item": nugget,
    },
    "cave": {  # room5
        "print_name": "the cave",
        "north": ["fail", ""],
        "south": ["fail", ""],
        "east": ["fail", ""],
        "west": ["fail", ""],
        "init_descript": "",
        "item": "",
    },
    "delta": {  # room6
        "print_name": "the river delta",
        "north": [
            "river",
            "You follow the river back NORTH. It grows in strength with each step, imperceptible each moment, but chewing into your flagging energy all the same.",
        ],
        "south": [
            "pools",
            "As you travel SOUTH, a shape in the distance becomes clearer through the haze. There's a mountain rising from the ocean, its flanks coated with fire. It's far enough away that it poses you no harm, but the sight of danger so grand leaves you anxious all the same.",
        ],
        "east": [
            "fail",
            "The cliffs to the EAST stop sharply at the ocean's edge. You can swim, but you know you don't have the strength to travel far, so you decide that way would be too dangerous to go.",
        ],
        "west": [
            "fail",
            "To the WEST are the same mountains that help shield your valley. Your loved ones are on the other side, a reminder of the importance of your quest and your success.",
        ],
        "init_descript": [
            "The river expands as it reaches the sea, splitting into countless, shallow branches. Plants have taken root in the soft earth, which cleanly hold the prints of any animal that has trodden by.",
            "The ocean can be seen SOUTH underneath a reddened sky. The river can be followed back NORTH towards its source.",
        ],
        "item": egg,
    },
    "pools": {  # room7
        "print_name": "the tide pools",
        "north": [
            "delta",
            "The unsteady rocks beneath your hooves shift into the more familiar mud as you go back NORTH to the delta.",
        ],
        "south": [
            "fail",
            [
                "The sea stretches endlessly to the SOUTH. You ask the crow about the mountain and its fires.",
                "'Crrr burn long time,' it says. You ask how that's possible, as fires always die out when it runs out of fuel to burn. It pecks at the ground. 'Fire from inside,' it explains. 'Under.'",
                "You've seen and learned many strange things on your journey, and this is just another. You're unsure if anyone would believe you if you said that there was an endless fire burning beneath them. But, as long as the ground separated them from the danger, as long as they were safe, you would find a way to live with that knowledge.",
            ],
        ],
        "east": [
            "fail",
            "The ocean moves with an energy you've only seen in the grandest storms, the most desperate predators. It crashes into the rocks again and again as if desperate to pull the land into itself and under its control.",
        ],
        "west": [
            "fjord",
            [
                "The soft sand underhoof is a welcome change from the jagged rocks. But, even here, things feel wrong: the sand is black and burnt trees and bones litter the beach. You expect to see a predator, something that could have picked the bodies so thoroughly clean, but there's no life you can see. Even the strange creatures in the tidepools would have been a welcome sight.",
                "The beach curves into a narrow canyon, water trickling between the rocks below.",
            ],
        ],
        "init_descript": [
            "Where the land meets the sea isn't a clear line; sharp, bare rocks hold pockets of water with strange plants wriggling within them. What you thought was a stone slowly creeps towards a translucent flower. What you thought was a slug makes no movements as you trod by.",
            "Strangest of all is the mountain of fire far in the distance. Curls of clouds rise from the water where the fire meets it, and the sky is reddest near its flaming peak.",
            "The pools peter out and the ground flattens out again to the WEST. You can also go back up river to the NORTH.",
        ],
        "item": shell,
    },
    "fjord": {  # room8
        "print_name": "the fjord",
        "north": [
            "fail",
            [
                "Your pace quickens as you feel home approach, but the crow lands on your neck and squawks.",
                "'Not yet!' it says. 'Gifts!'",
                "You're annoyed, but you know you need to collect enough gifts before you're allowed to return home.",
            ],
        ],
        "south": [
            "fail",
            "The ocean quietly laps at the sand to the SOUTH. Perhaps at one time it could reach the fjord; perhaps it, too, is weaker than it once was.",
        ],
        "east": [
            "pools",
            "You carefully turn around and retrace your steps back to the beach. Your pace quickens as you walk past the charred remains of both trees and animals.",
        ],
        "west": [
            "fail",
            "Your eyes trace up the fjord's EAST wall. You're unsure if your eyes are playing tricks on you, but you swear you can spot the shells of creatures, not unlike what you saw in the tidepools, suspended within the rocks.",
        ],
        "init_descript": [
            "The walls of the fjord are high, leaving a single ribbon of sky above you. It leads NORTH, back to your home and, hopefully, the end of your journey.",
            "The way out of the fjord curves back to the EAST.",
        ],
        "item": fossil,
    },
}

direction_synonyms = {"n": "north", "s": "south", "e": "east", "w": "west"}

"""
CHARACTERS
"""


class Character:
    """
    Class for character objects, such as player
    """

    def __init__(self, location: str, inventory: list):
        """
        :param location: starting room in game world
        :param inventory: starting character inventory (default empty)
        """
        self.location = location
        self.inventory = inventory
        self.inventory_count = 0

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_inventory(self, inventory):
        self.inventory.append(inventory)
        self.inventory_count = len(self.inventory)

    def get_inventory(self):
        return self.inventory

    def get_inventory_count(self):
        return self.inventory_count


player = Character("valley", [])

"""
PROMPT MANAGEMENT
"""


class Parsed_Prompt:
    """
    Prompt object, allowing to be updated by various functions/loops
    """

    def __init__(self, prompt: str):
        """
        :param raw_prompt: Capture input from player
        :param prompt: Parsed prompt (list)
        :param prompt_len: How many "words" in prompt
        """
        self.raw_prompt = prompt
        self.prompt = []
        self.prompt_len: 0  # type: ignore

    def set_prompt(self, prompt):
        self.raw_prompt = prompt
        self.prompt = self.raw_prompt.split(" ")
        self.prompt_len = len(self.prompt)

    def get_prompt(self, index):
        return self.prompt[index]

    def get_prompt_len(self):
        return self.prompt_len


player_prompt = Parsed_Prompt("")

"""
FUNCTIONS
"""

"""
SYSTEM
"""


def text_wrapper(text):
    """
    Takes variable-length flavor text and prints it with text wrap. A string is formatted into a single paragraph, so lists print multiple paragraphs.
    """
    if type(text) is list:
        for elements in text:
            print(textwrap.fill(elements, width=width) + "\n")
    else:
        print(textwrap.fill(text, width=width) + "\n")


"""
VERBS
"""


def move(direction):
    """
    Takes noun from prompt, checks room dict, prints movement descript, updates player location (if possible)
    """
    if direction in ["n", "s", "e", "w"]:
        direction = direction_synonyms[direction]
    text_wrapper(rooms[player.get_location()][direction][1])
    if rooms[player.get_location()][direction][0] != "fail":
        player.set_location(rooms[player.get_location()][direction][0])


def take(noun):
    """
    Takes noun from prompt, looks up str noun for matching item instance
            if noun is valid item: set local item variable, checks item's location and sets item location/player inventory with new item (or error if already in inventory or item is in different room)
                else if noun is not valid item: print error message
    """
    if noun in item_lookup:
        item = item_lookup[noun]
        if item.get_location == "inventory":
            print("You've already collected that!\n")
        elif (
            item is rooms[player.get_location()]["item"]
            and player.get_location() == item.get_location()
        ):
            item.set_location("inventory")
            player.set_inventory(noun)
            rooms[player.get_location()]["item"] = ""
            text_wrapper(item.get_take_descript())
        else:
            print(f"You can't see a {noun} to pick up.")
    else:
        print("The crow doesn't know what you want it to get.")


"""
GAME FUNCTIONS
"""


def parsing(
    prompt,
):
    """
    Takes input captured in next_prompt() and breaks into verb (player action) and noun (target of action). Checks verb for synonym matches and passes through noun if the verb is an available action.

    After the verb function runs, it checks for win/loss conditions and runs the proper actions to end the game. Otherwise it asks for the next prompt and goes again.
    """
    player_prompt.set_prompt(prompt)
    verb = player_prompt.get_prompt(0).lower()
    noun = ""
    if player_prompt.get_prompt_len() > 1:
        noun = player_prompt.get_prompt(1).lower()
        if noun in ["the", "a", "an"]:
            noun = player_prompt.get_prompt(2).lower()
    if verb in ["move", "go"] and noun in [
        "north",
        "south",
        "east",
        "west",
        "n",
        "s",
        "e",
        "w",
    ]:
        move(noun)
    elif verb in ["move", "go"]:
        print("That's not a valid direction for movement.")
    elif verb in ["take", "t", "get", "g", "collect"]:
        take(noun)
    else:
        text_wrapper("The crow doesn't know what it is you'd like to do.")
    # end condition checks
    if player.get_location() == "cave":
        bad_end_1()
    elif player.get_inventory_count() == 7:
        true_end()
    next_prompt()


# prompt()
def next_prompt():
    """
    Inits start of new turn by printing current location, inventory, and prompt for next input. Sends captured str to be parsed.
    """
    inventory_message: str = ""
    print(separator)
    # Room description + item description (if any)
    text_wrapper(rooms[player.get_location()]["init_descript"])
    if rooms[player.get_location()]["item"] != "":
        text_wrapper(rooms[player.get_location()]["item"].get_init_descript())
    # Player status message
    if len(player.get_inventory()) == 0:
        inventory_message = ". Your inventory is empty."
    else:
        inventory_message = (
            ", and your inventory is " + ", ".join(player.get_inventory()) + "."
        )
    text_wrapper(
        f"Your current location is {rooms[player.get_location()]['print_name']}{inventory_message}"
    )
    # Prompt input
    prompt = str(input("↦ What's your next move?\n")).lower()
    print(separator)
    parsing(prompt)


"""
GAME LOGIC
"""

# Intro
intro_text = [
    "You've lived many seasons, more than you have stripes on your legs, so the cycle of give and take of the world is a familiar one. The bad will soon fade into the good, you'd tell the others, the expectant mothers, their worried wives. Nothing is forever.",
    "But the bad seasons have grown more frequent, the reprieves more rare. When the first foal was born with a coat white as snow, eyes pale as the moon, it was seen as a portent of change. Even after it died a few days later, it had to be a sign.",
    "After the third foal in a row suffered the same fate, it was recognized the curse it was. Perhaps it was a kindness, with the thinning of the grass, the weakening of the river, the reddening of the sky. The world you once knew was dying an ignoble death.",
    "Still, your youngest daughter is due any day. She still holds hope that the world will turn green and new again. You look to the stars, lurking above the herd bedding down for the night. The seven familiar dapple of the great horse constellation is still there, despite everything.",
    "A sudden streak of color slashes through the night sky. The bright red rolls down the neck of the great horse, its back, flaring out into a lustrous tail. The sight of something so far and vast grips you in fear, so you don't notice the creeping shadow until it speaks.",
    "'Crrr pretty, yes?'",
    "You snort and dance backwards to see a crow standing before you. 'Horse come to fox's wedding,' it says. 'But get gifts first. Seven good. Back morning, yes?' It flies off before you can ask what it means."
    "You awaken the next day to see the the crow impatiently staring at you. 'Seven stars, seven gifts,' it reminds you. It pokes the the thing it's standing on, hides and furs from different animals, scarred together into an unliving mass. 'Fox give gift back,' it adds.",
    "This is another portent, surely, and you hope it to be a good one. You tell the crow you'll accept the invitation and find the gifts for fox.",
    "",
    "Your journey will require you to GO to different places to look for suitable gifts, which the crow has helpfully volunteered itself to GET for you. If you look carefully enough, you should be able to see the paths and items of interest.",
]


# Bad end

bad_end_1_text = [
    "It'd been many years since you've seen them, but you know cave lions like to haunt places like this. The heavy cave air doesn't carry the weight of blood, though, or bones, or the spice of their pale hides.",
    "Instead there's a scent you don't recognize, a heat in the darkness that both welcomes and warns. The crow lands at the mouth of the cave and stands on its toes to get a better look in, but it doesn't follow you.",
    "It's not long until you step deeper than the sunlight can reach. It's not longer still until the sound of something is ahead.",
    "You freeze, hoping it's simply your fear, but it's been a long time since the world's been forgiving. A massive, shaggy shape approaches, looming above your eyesight.",
    "You let your fear take rein as you wheel around and rush towards the light. The walls of the cave scrape at your sides and the uneven floor jabs into the bottoms of your hooves, but still you run.",
    "The thing behind you speeds up before suddenly stopping. You've only an instant to wonder why, as the ground is suddenly gone beneath you. The realization that you've run past the river bank hits you the same time your forehoof touches the ground.",
    "You might have made the jump if you were younger, if you had known it was coming. But all of your weight comes down on a single, slender leg, and it shatters like a sheet of ice.",
    "The predator takes its time to reach you, but the crow lands within your eyesight first. 'Crrrr bad fall,' it says, as if you didn't already know that. 'Bear look hungry, hope he shares.'",
    "You demand to know why it hadn't warned you, and it shrugs. 'Hungry, too. And thanks for gifts, maybe bear come instead?' It then calls out to the bear, in the voice of growls and rumbles spoken by the things of teeth and claws.",
    "The bear responds, but you don't understand. Whatever it said, it's clearly in no rush, as it takes its time enjoying the 'gift' you so kindly brought to it.",
]


def bad_end_1():
    text_wrapper(bad_end_1_text)
    print(separator)
    any_key = str(input("Thank you for playing. Press enter to exit the program."))  # noqa: F841
    quit()


# Regular end

# runs only if player isn't in "expected" last room
true_end_not_fjord = [
    "The crow hops up and down excitedly. 'Seven! Seven gifts! Let's go go go! Fjord!'",
    "You retrace your steps back to the fjord and head NORTH, to your home and the end of the journey.",
]
# runs if player is in "expected" last room
true_end_fjord = [
    "The crow hops up and down excitedly. 'Seven! Seven gifts! Must go see fox!'"
]

true_end_text = [
    "The fjord slopes upward, forcing you to push harder with your hind legs. This journey has been a long one, but it'll soon be over. You'll be back home, with your family, and the world will go back to the way it once was.",
    "Exhaustion seeps between your bones, but you press onwards, ascending until you feel like you're within the clouds themselves. The crow darts ahead as the path finally flattens out and you take a moment to catch your breath.",
    "The wind shifts, carrying scents that make you freeze. You look ahead to see a series of predators, and they all turn to look at you. There's the saber-tooth, the cheetah, the lion, the wolf, the condor. There's another that you don't recognize. It walks on two legs like the crow, but with a straight back. It has no fur of its own but is draped in the hides of others.",
    "A coyote trots up to you, but stops before the crow, who puts down its bag. You place the fossil on the ground and watch the canine nervously.",
    "'I'm so glad you could join us,' the coyote says. 'Fox said how you promised you'd bring us the best gift of all.' At this, the crow's feathers puffed out in pride.",
    "'Yes, yes! Come see!'",
    "You expect the crow to open the bag, but it doesn't, nor does it gesture at the fossil. Instead you feel the teeth of truth start to wrap around your neck.",
    "You take a step backwards, muscles tightening. What's the meaning of this, you ask, what about fox giving a gift in return?",
    "'Crrr won't need to worry anymore, yes? No horse will.'",
    "The fox appears, a shadow of white-tipped red, of bone, of fire. He nuzzles against the coyote. 'An entire valley, all to ourselves! How can we thank you, crow?'",
    "The crow tilts its head back and forth in thought. 'Crrr trip very long, very hungry. Eat now?'",
    "The other predators are now shifting, well-fed muscles sliding under glossy coats. Your knees nearly buckle in fear. You glance NORTH, to your home, to safety, to the SOUTH, away from your family.",
    "Somehow, you make your choice. Your legs carry you as swiftly as they can, but your bones are old, your muscles tired. Even a single predator could take you down in this state, but an entire party sinks into you and pulls you down, down, and soon you're unable to worry or fear ever again.",
]


def true_end():
    if player.get_location() == "fjord":
        text_wrapper(true_end_fjord)
    else:
        text_wrapper(true_end_not_fjord)
    text_wrapper(true_end_text)
    print(separator)
    any_key = str(input("Thank you for playing. Press enter to exit the program."))  # noqa: F841
    quit()


"""
GAME START
"""
any_key = str(
    input(
        "Please fullscreen your terminal for the best experience. Press enter to start.\n"
    )
)
print(separator)
text_wrapper(intro_text)
player.set_location("valley")
next_prompt()
