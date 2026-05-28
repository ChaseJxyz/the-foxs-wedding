# The Fox's Wedding

Made for SNHU's Introduction to Scripting python course, where I went extremely overboard. Parser-based interactive fiction that runs in your terminal.

## Story

You are an [ancient hors](https://en.wikipedia.org/wiki/Equus_scotti), and your world is dying. When searching for answers for how to save your family, a crow appears. It invites you to fox's wedding; if you bring gifts then, just maybe, you'll get something in return.

## How to run

Download the python file, open your shell of choice, and run it. Something like `python3 ./the-foxs-wedding.py`. You might need to add execute permissions. [This article](https://realpython.com/run-python-scripts/) goes over how to run python script files.

## How to play

At the start of each turn, you type what you want to do and hit enter. 

* Move/go north/south/east/west
* Take/get/collect [item]

You can also use the classical shorthands of n/s/e/w/t/g. But, if you're new to this kind of game, don't worry about it.

You need to move through various "rooms" and collect items. What you can take and where you can move are in the text, so you do need to read it and think for a second. But be careful: danger still exists in this world.

This is designed to be played in one sitting, so there are no saves. If you read everything, it should take maybe 10-15 minutes.

## Under the hood

Items are objects from an object class, which allows the getting/setting of its location, and printing of its intial description and the flavor text of taking it. Rooms are dictionaries (because it's what the course required...), with keys for their print name, what rooms they're connected to and the flavor text for moving in that direction, the description of the room itself, and what item it contains.

Since the plan is to turn this into a standalone engine at some point in the future, there's also a character class, with the play character being the only such object in this. This does mean that future NPCs would be able to have their own inventories and can move around to other rooms. The prompt is also a class where it's its own object, mostly so it can have properties like length and splitting it up into a list.

All outputted text goes into a wrapper that prints text that "wraps" nicely. The default width value is 88.

Prompts are broken up into a list that's "verb, noun". e.g. the player `take tooth` or `move north`. Verbs have synonym dictionaries, and once the parser determines what verb the player is doing, it then uses the noun to determine what it should do. An item that is already in the player's inventory will say that it's already in the inventory, and moving in a direction that is not conencted to another room has a custom error text explaining why the player character can't move in that direction. Words like the/a/an are ignored (so `take tooth` and `take the tooth` are functionally equal)

As the player is a horse, they can't pick anything up themselves, so a helpful crow does the item management for them. It's also a helpful excuse as to why the player can't do many other things one would expect in a parser-based IF (because I did not have the time to program in more).

There's two endings: a "bad" end that happens if a player enters a specific room, and the "good" end if the player collects all of the items. These are checked for after the noun gets verbed. If the game isn't over, the player's inventory gets printed out, as well as the description of the current room and the text to ask for the next prompt. The rest of the game logic is just printing the intro/ending texts at the right points, plus a "Thanks for playing!" and a program exit. If the player doesn't pick up the last item in the last room, the text is slightly different, as they "walk back" to the final room. 

I was SUPPOSED to use a while loop to check if the game should keep going but lol. I also didn't need to print out any flavor text, just "you are in this room this is your inventory this item is in the room." I took a bootcamp last year on how to make parser-based IFs with Inform7, so it was drilled into me that you NEED custom error text, you NEED descriptions, you NEED this and that. 

## Story details

I've been horsepilled for awhile now. The set up is very similar to a (still unsold) story of mine about a pleistocence horse and her world ending. But this time! You get to do something about it. This is some sort of fantasy setting that isn't *actually* North America (there were no vocalnos off the coast of wherever the horses were) but pretty much is.

The concept of "the fox's wedding" is a Japanese one, yes, but I liked the concept and having it to be coyote, so the ending being the way it did would make sense to the player. It would be less of a surprise if they reached the bad ending first. And, yeah, it's a bummer ending. No spirit or wish would be enough to undo the end of an ice age, but now the MC doesn't have to worry about things!

## Future stuff

I do want to turn this "engine" into a stand alone thing, so that you could just make a "story file" and focus on only that (and as little game logic as possible.) Part of that would be adding more features, like looking at scenary, getting hints, a better synonym system. And this story would be updated with the new features to test them out.

Honestly the scenery/synonym system *is* functional it's just that I would have needed to write so. many. things. And I did not have the time to do that on top of my SANS course work and everything else. So it'll be a minute before this will be updated and/or the engine comes out. This has been ready to be "published" for awhile now...but so many other things got in the way.

## And if you're a fellow SNHU student...

Don't copy my work. You're not gonna learn everything if you just copy/paste what I did. You're also not supposed to know what classes are lol I only do because I kept asking my roommate how best to do things and she told me to look up classes. Honestly I got, like, 90% of the course requirements done by week 1 just because I wanted to see what I could do and I was having so much fun. Which is why this ended up being so extra, I had so much time to just keep working on it. Don't be me.

But also don't be afraid to do more than the course reqs because they are just such a low bar to pass. At least think about how you can format/prettify your output.
