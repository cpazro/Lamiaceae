# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:
    default preferences.text_cps = 42

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room at truecenter

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "I tried to make a video game."
    show strawberry at center:
        xzoom 0.2 yzoom 0.2

    hide strawberry
    "I am too ambitious for my own good."

    hide strawberry

    show rose at truecenter with hide:
        xzoom 0.3 yzoom 0.3
    
    "This anxiety and attention disorder is making my life difficult, but it also gives meaning to it."
    "Drawing and video games are a big part of my life."
    show gingko at truecenter:
        xzoom 0.3 yzoom 0.3
    "Maybe I shouldn’t leave my current project like the foraging diary I had."
    show journal1 at center:
        xzoom 0.2 yzoom 0.2
    "Started but never finished. Left Behind."
    show journal2 at center:
        xzoom 0.2 yzoom 0.2
    "I must finish something."
    show journal3 at center:
        xzoom 0.2 yzoom 0.2
    "I must."
    "I want the world to see what abilities I have."
    "I must prove that I can finish something. Prove that I am not a failure."
    "Botany is my passion, but I am so bad at biology."
    "I study literature but..."
    "I ain’t good for that either."
    "Must finish something."
    "Must be good at something."
    "Must not be a failure."
    "What am I good at?"
    "Am I too much of a coward to fail? To finish anything."
    "It is already 2:15 AM."
    "Am I getting distracted again?"
    "I am at exam season. I have to study but I don’t want to."
    "It is my fault. Isn’t it? To wander mentally so much."
    "There are so many things I want to do."
    "Learn python, drawing, RPG maker, pixel art, botany, mycology, data science, linguistics, Indology..."
    "How the fuck will I combine this together???"
    show hortensia at center:
        xzoom 0.2 yzoom 0.2
    "Must focus on uni."
    "Must focus on important things."
    "MUST. FINISH. SOMETHING."
    "A seedling."
    "An idea."
    "Going back to botany again."
    show umbel at center:
        xzoom 0.2 yzoom 0.2
    "What really makes me happy?"
    "The simpler things of life."
    "Nature."
    show flowers at center:
        xzoom 0.2 yzoom 0.2
    "Chaos is my default state."
    "Nature is order in chaos."
    "A fractal reality."
    "Order that looks like chaos up closely."
    "Seeing the bigger picture, it turns into patterns."
    "Patterns are the only thing I see."
    "Everything is connected, just separated by human criteria."
    "Must I feel bad for not seeing the difference?"
    "Just like a language tree, the branches of this plant are distinct but part of the same system."
    "How will I combine botany with literature?"

    #II
    "I looked back at my notebook."
    "I had some decent drawings there."
    "Is that... a completed project?"
    "A foraging guide for my city."
    "There isnt any available."
    "Did I create something new?"
    "It doesnt have any value, you copied the information from different sources."
    "Isnt that a value in itself?"
    "YOU MADE SOMETHING THAT DIDNT EXIST BEFORE."
    "Look, more drawings."
    "I remember these. I followed a botanical art book. Tried to polish my techniques."
    "I learn that I must try, even though the drawing isnt scientifically acurate."
    "Must fail first."
    "But to fail is to win. "
    "Failing is conquering the fear to do something."
    "I conquered my fear."
    "I must keep drawing."
    "I must keep creating."
    "One page at a time."
    "One level at a time."

    #III
    "I wanted to show the world what I do. Even though Im afraid."
    "Im so afraid."
    "Will a botanist see my drawings? maybe an artist?"
    "Will they notice that I did opposite leaves when I shouldnt have?"
    "That I always round leaves."
    "My lines are too thick."
    show arbol at center:
        xzoom 0.2 yzoom 0.2
    "Even if you copy a plant, you bring something new to this world."
    "I am not afraid anymore."
    "I accept being an amateur."
    "This is my art."
    show lamiaceae at center:
        xzoom 0.2 yzoom 0.2
    "This is my game."
    show lamiaceae at center:
        xzoom 0.2 yzoom 0.2
    # This ends the game.

    return
