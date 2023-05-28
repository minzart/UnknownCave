label stone_pillars:    
    scene stone_pillars
    
    """

    A row of stone pillars, intricately carved with runes and symbols of unknown origin, stand like silent sentinels. 
    
    Who built this place, and why? Where lead the many passages burrowing into the mountains?
    
    Their purpose eludes you, yet their presence adds an air of mysticism to the chamber.

    """
    
    menu:
        "Enter the left passage.":
            jump left_start
        "Go straight through.":
            jump cave_leading_out
        "Enter the right passage.":
            jump right_start