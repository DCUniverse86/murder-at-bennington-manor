#Donald Carpenter Jr.                                Python                                             11/15/2025

import random

# List of all clues the player has discovered
clues_found = []
# Set of suspects the player has questioned
interrogated = set() 

# Define all suspects with their information
suspects = {
    'Lilith Bennington': {
        'relationship': 'wife',
        'reason': 'According to the other suspects, Charles III was leaving her for another woman',
        'alibi': 'According to Lilith, she was getting changed in the bedroom',
        'special_clues': {  
            "Dining Room": "a lipstick-stained napkin beside the victim's seat",
            "Bedroom": "a hidden bottle of sleeping pills in her vanity",
            "Library": "a torn love letter from Charles to another woman"
        }
    },
    'Charles Bennington IV': {
        'relationship': 'son',
        'reason': 'According to the other suspects, he was being cut out of the will',
        'alibi': 'According to Charles IV, he was using the bathroom',
        'special_clues': {
            "Study": "a torn piece of the will in the fireplace",
            "Library": "an unsigned letter demanding inheritance",
            "Garden": "muddy footprints matching his shoes"
        }
    },
    'William Jeeves': {
        'relationship': 'butler',
        'reason': 'According to the other suspects, Charles III treated him like garbage',
        'alibi': 'According to William, he was doing work around the house',
        'special_clues': {
            "Kitchen": "a servant's glove with dried blood",
            "Dining Room": "a silver tray smeared with blood",
            "Study": "a crumpled note reading 'I can't take it anymore, sir!'"
        }
    },
    'Joseph Mills': {
        'relationship': 'business partner',
        'reason': 'According to other suspects, he was being forced out of the business',
        'alibi': 'According to Joseph, he was arguing with Charles III at the dinner table',
        'special_clues': {
            "Dining Room": "a wine glass with traces of poison",
            "Study": "a business contract with blood stains",
            "Library": "a threatening letter signed 'J.M.'"
        }
    }
}

# Red herrings are misleading clues that can appear regardless of who the killer is
red_herrings = {
    "Dining Room": [
        "two wine glasses with different fingerprints",
        "a turned over chair from the scuffle"
    ],
    "Library": [
        "a woman's earring on the carpet",
        "a servant's glove tucked into a book"
    ],
    "Study": [
        "a half-burned note saying 'Meet me after dinner'",
        "muddy shoeprints not matching anyone's footwear"
    ],
    "Kitchen": [
        "a shattered plate near the counter",
        "a knife missing from the block"
    ],
    "Garden": [
        "freshly disturbed soil near the hedge",
        "a muddy trail leading back to the house"
    ],
    "Bedroom": [
        "a strand of blonde hair on the pillow",
        "a perfume bottle knocked over"
    ]
}

# Generic clues appear in every game regardless of the killer
generic_clues = {
    "Dining Room": ["a chair knocked over during the struggle"],
    "Library": ["a candle burned halfway down"],
    "Study": ["a clock stopped at 9:12 PM"],
    "Kitchen": ["a faint smell of smoke"],
    "Garden": ["a wet footprint by the door"],
    "Bedroom": ["the window slightly ajar despite the storm"]
}

# Initialize game variables
areas = list(generic_clues.keys()) 
searched_areas = set()

# Randomly select the killer at the start of the game
killer = random.choice(list(suspects.keys()))

# Displays introduction to game
def start_game():
    print("\n" + "="*50)
    print("       MURDER AT BENNINGTON MANOR")
    print("="*50 + "\n")
    print("It was a dark and stormy night at Bennington Manor.")
    print("Sir Charles Bennington III was found dead after the")
    print("lights went out during dinner.")
    print("\nYou, the detective, must explore the manor, collect")
    print("clues, and find the killer. Each room holds secrets")
    print("and each suspect may lie.")
    print("\n  Be careful - once you accuse someone, the game is over!\n")
    input("Press Enter to begin your investigation...")
    crime_scene()

# Main hub where the player chooses their next action
def crime_scene():
    # Check if all areas have been searched
    if len(searched_areas) == len(areas):
        print("\n" + "="*50)
        print("You've searched every area of the house.")
        print("Time to make your accusation!")
        print("="*50)
        return accuse()
    
    # Display current progress and menu
    print("\n" + "-"*50)
    print(" MAIN HALL")
    print("-"*50)
    print(f"Areas searched: {len(searched_areas)}/{len(areas)}")
    print(f"Suspects interrogated: {len(interrogated)}/{len(suspects)}")
    print(f"Clues collected: {len(clues_found)}")
    print("\nWhat would you like to do?")
    print("  1. Investigate an area")
    print("  2. Interrogate a suspect")
    print("  3. Review clues found")
    print("  4. Analyze connections")
    print("  5. Make an accusation")
    
    # Get player's choice and route to appropriate function
    choice = input("\nEnter choice (1-5): ").strip()
    if choice == "1":
        choose_area()
    elif choice == "2":
        choose_suspect()
    elif choice == "3":
        review_clues()
    elif choice == "4":
        analyze_clues()
    elif choice == "5":
        accuse()
    else:
        print("\n Invalid choice. Please enter a number between 1 and 5.")
        input("Press Enter to continue...")
        crime_scene()

# Display available areas and let the player choose one to investigate
def choose_area():
    # Filter out areas that have already been searched
    available = [a for a in areas if a not in searched_areas]
    if not available:
        print("\n You've searched every place already!")
        input("Press Enter to continue...")
        return crime_scene()
    
    # Display menu of available areas
    print("\n" + "-"*50)
    print(" AVAILABLE AREAS TO SEARCH:")
    print("-"*50)
    for i, area in enumerate(available, 1):
        print(f"  {i}. {area}")
    print(f"  {len(available) + 1}. Return to main hall")
    
    # Get player's choice and validate
    choice = input("\nChoose an area number: ").strip()
    try:
        idx = int(choice) - 1
        if idx == len(available):
            return crime_scene()
        elif 0 <= idx < len(available):
            investigate(available[idx])
        else:
            print("\n Invalid selection")
            input("Press Enter to try again...")
            choose_area()
    except ValueError:
        print("\n Please enter a valid number.")
        input("Press Enter to try again...")
        choose_area()

#Search a specific area and collect clues
def investigate(area):
    print(f"\n{'='*50}")
    print(f" Searching the {area.upper()}...")
    print("="*50)
    # Mark this area as searched
    searched_areas.add(area)
    
    # Collect all clues found in this area
    found_here = []
    
    # Add generic clues (always present)
    found_here += generic_clues.get(area, [])
    
    # Add killer-specific clues if this area has them
    if area in suspects[killer]['special_clues']:
        found_here.append(suspects[killer]['special_clues'][area])
    
    # Add 1-2 random red herrings from this area
    available_herrings = red_herrings.get(area, [])
    if available_herrings:
        herrings = random.sample(available_herrings, k=min(2, len(available_herrings)))
        found_here += herrings
    
    # Display all clues found and add them to the player's collection
    print("\n You discover:")
    for clue in found_here:
        print(f"   - {clue}")
        clues_found.append(clue)
    
    print("\n You carefully note everything and return to the hall.")
    input("Press Enter to continue...")
    crime_scene()

# Display suspects and let the player choose one to interrogate
def choose_suspect():
    # Filter out suspects who have already been questioned
    available = [name for name in suspects.keys() if name not in interrogated]
    if not available:
        print("\n You've interrogated everyone already!")
        input("Press Enter to continue...")
        return crime_scene()
    
    # Display menu of all suspects (marking questioned ones)
    print("\n" + "-"*50)
    print(" SUSPECTS:")
    print("-"*50)
    for i, name in enumerate(suspects.keys(), 1):
        status = "  (already questioned)" if name in interrogated else ""
        print(f"  {i}. {name}{status}")
    print(f"  {len(suspects) + 1}. Return to main hall")
    
    # Get player's choice and validate
    choice = input("\nChoose a suspect number: ").strip()
    try:
        idx = int(choice) - 1
        if idx == len(suspects):
            return crime_scene()
        elif 0 <= idx < len(suspects):
            suspect_name = list(suspects.keys())[idx]
            interrogate(suspect_name)
        else:
            print("\n Invalid selection")
            input("Press Enter to try again...")
            choose_suspect()
    except ValueError:
        print("\n Please enter a valid number.")
        input("Press Enter to try again...")
        choose_suspect()

# Question a suspect and learn their motive, alibi, and relationship
def interrogate(suspect_name):
    info = suspects[suspect_name]
    # Mark this suspect as questioned
    interrogated.add(suspect_name)  
    
    # Display all information about the suspect
    print(f"\n{'='*50}")
    print(f"️  INTERROGATING: {suspect_name.upper()}")
    print("="*50)
    print(f"\n Relationship: {info['relationship'].title()}")
    print(f" Motive: {info['reason']}")
    print(f" Alibi: {info['alibi']}")
    
    print("\n" + "-"*50)
    input("Press Enter to return to the main hall...")
    crime_scene()
    
# Display all clues the player has collected
def review_clues():
    print("\n" + "="*50)
    print(" CLUES COLLECTED")
    print("="*50)
    if clues_found:
        for i, clue in enumerate(clues_found, 1):
            print(f"  {i}. {clue}")
    else:
        print("  No clues found yet. Start investigating!")
    print("="*50)
    input("\nPress Enter to return to the main hall...")
    crime_scene()

# Provide hints about how to interpret the clues
def analyze_clues():
    print("\n" + "="*50)
    print(" CLUE ANALYSIS")
    print("="*50)
    
    if not clues_found:
        print("\n  You haven't collected any clues yet!")
        print("  Investigate areas to gather evidence.")
    else:
        # Give general hints about interpreting evidence
        print("\n Look for patterns in the evidence:")
        print("   - Blood evidence suggests violence")
        print("   - Poison suggests premeditation")
        print("   - Personal items link to specific suspects")
        print("   - Location of clues may reveal the killer's movements")
        print(f"\n  You have {len(clues_found)} clues so far.")
        
        # Suggest further investigation if incomplete
        if len(searched_areas) < len(areas):
            print(f"  Consider searching the remaining {len(areas) - len(searched_areas)} areas.")
        
        if len(interrogated) < len(suspects):
            print("  You haven't questioned all suspects yet.")
    
    print("="*50)
    input("\nPress Enter to return to the main hall...")
    crime_scene()

# Let the player make their final accusation and end the game
def accuse():
    print("\n" + "="*50)
    print("  FINAL ACCUSATION")
    print("="*50)
    print("\nWho do you accuse of murdering Charles Bennington III?")
    print()
    for i, name in enumerate(suspects.keys(), 1):
        print(f"  {i}. {name}")
    
    choice = input("\nType the suspect's number or full name: ").strip()
    
    # Allow player to input either a number or the suspect's name
    accused = None
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(suspects):
            accused = list(suspects.keys())[idx]
    except ValueError:
        for name in suspects.keys():
            if choice.lower() == name.lower():
                accused = name
                break
    
    # Handle invalid input
    if not accused:
        print("\n That person isn't even a suspect! Case dismissed.")
        print("The killer remains free...")
        exit()
    
    # Dramatic reveal
    print(f"\n{'='*50}")
    print(f"You point at {accused} and declare:")
    print("'YOU are the murderer of Charles Bennington III!'")
    print("="*50)
    input("\nPress Enter to reveal the truth...")
    
    # Check if the player guessed correctly
    if accused == killer:
        print("\n" + "*"*25)
        print("\n   YOU'RE CORRECT!")
        print(f"\n  {accused} breaks down under the pressure of your")
        print("\n  evidence and confesses to the murder!")
        print("\n   CASE CLOSED - EXCELLENT DETECTIVE WORK! ")
        print("\n" + "*"*25)
    else:
        print("\n" + "*"*25)
        print(f"\n  {accused} proves their innocence with irrefutable evidence!")
        print(f"\n  The real killer was {killer}.")
        print("\n They smile coldly as you realize your mistake.")
        print("\n   GAME OVER - THE KILLER GOES FREE ")
        print("\n" + "*"*25)
        
    

# Start the game 
start_game()