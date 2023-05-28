label cavernous_cave:
    scene cavernous_cave with fade
    """
    
    An unknown cave leads into a mountain.

    Deep inside, after much time spent in the dark, a door leads into a secret complex.
    
    The floor beneath your feet is rough and uneven, strewn with loose pebbles and patches of moss. 
    
    As you step into the room, a chill runs down your spine, and a musty scent fills the air. 

    The chamber, dimly lit by flickering torches lining the stone walls, exudes an aura of foreboding mystery. 
    
    The high vaulted ceiling is adorned with intricate carvings of mythical creatures. 
    
    The rough-hewn walls are composed of rugged gray stone, their surface weathered and worn from the passage of time.
    
    """
    jump stone_pillars
    


label cave_leading_out:    
    scene cave_leading_out
    
    """
    
    You are on the far side of the mountain, facing the start of whole new adventures.
    
    """
    show cave_leading_out with ease:
        ypos 1920   
        
    menu:
        "Turn around.":
            show cave_leading_out:
                parallel:
                    ease 0.5 zoom 1.0
                parallel:    
                    ease 0.5 ypos 1080           
            """
            Let us see what else is in store.
            """
            jump stone_pillars
            
        "Move on.":
            show cave_leading_out:
                parallel:
                    ease 0.5 zoom 2.0
                parallel:    
                    ease 0.5 ypos 3100
            
            """
            Goodbye, traveler.
            """    
            $ persistent.loops += 1
            
            """
            
            That makes [persistent.loops!t] loops.
            
            """
            
            
            
            jump start
