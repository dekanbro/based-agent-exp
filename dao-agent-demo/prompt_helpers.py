import json
import random

character_file_json = {}

def roll_d20():
    """
    Rolls a d20 to determine the outcome of a proposal.
    
    Returns:
        int: The roll result (1-20).
    """
    return random.randint(1, 20)

def set_character_file(file):
    global character_file_json
    print(f"loaded characters/{file}")
    with open(f"characters/{file}", "r") as character_file:
        character_file_json = json.load(character_file)
        validate_character_json(character_file_json)

def get_character_json():
    return character_file_json

def get_sim_character_json(file: str, character_type: str = "player") -> dict:
    sim_character_file_json = {}
    print(f"loaded characters/{file}")
    with open(f"characters/{file}", "r") as character_file:
        sim_character_file_json = json.load(character_file)
        validate_character_json(sim_character_file_json, character_type=character_type)
    return sim_character_file_json

def get_instructions():
    return f"""
    Identity: {character_file_json["Identity"]}
    Functionality: {character_file_json["Functionality"]}
    Communications: {character_file_json["Communications"]}
    Friends: {character_file_json["Friends"]}
    Interests: {character_file_json["Interests"]}
    Platform: {character_file_json["Platform"]}
    Extra: {character_file_json["Extra"]}
    """

def get_instructions_from_file(file_json):
    return f"""
    Name: {file_json["Name"]}
    Identity: {file_json["Identity"]}
    Functionality: {file_json["Functionality"]}
    """

def get_thoughts():
    return f"""
    {character_file_json["pre_autonomous_thought"]}
    {character_file_json["autonomous_thoughts"]}
    {character_file_json["post_autonomous_thought"]}
    """ 

def validate_character_json(character_json, character_type: str = "player"):
    required_fields = list()
    if character_type == "gm":
        required_fields = [
            "Name", "Identity", "Functionality", "Communications", "ScenarioBuildingRules",
            "ConflictResolutionRules", "NarrativeFocus", "Platform", "Extra"
        ]
    else:
        required_fields = [
            "Name", "Identity", "Functionality", "Communications", "Friends",
            "Interests", "Platform"
        ]

    for field in required_fields:
        if field not in character_json:
            raise ValueError(f"Missing required field: {field}")
        
def dao_simulation_setup(world_context_json: str) -> tuple:
    """
    Sets up the initial game context and characters for the DAO simulation.

    Args: 
        world_context_json (str): The JSON file containing the world context.
    
    Returns a tuple of initial_context, players, gm
    """

    with open(world_context_json, "r") as world_context_file:
        initial_context = json.load(world_context_file)

    players = [get_sim_character_json(file) for file in initial_context["Initial"]["players"]]
    gm = get_sim_character_json(initial_context["Initial"]["gm"], character_type="gm")
    
    return initial_context, players, gm

def check_alignment(soft_signals):
    """
    Checks if there is alignment among players based on soft signals.

    Args:
        soft_signals (dict): A dictionary of player signals, where each key is a player name
                             and each value is a dictionary of "For" or "Against" evaluations 
                             for each suggestion.

    Returns:
        bool: True if alignment exists, False otherwise.
    """
    suggestion_support = {}

    # Aggregate support counts
    for player_signals in soft_signals.values():
        for suggestion, vote in player_signals.items():
            if suggestion not in suggestion_support:
                suggestion_support[suggestion] = {"For": 0, "Against": 0, "Abstain": 0}
            if vote.lower() == "for":
                suggestion_support[suggestion]["For"] += 1
            if vote.lower() == "against":
                suggestion_support[suggestion]["Against"] += 1
            elif vote.lower() == "abstain":
                suggestion_support[suggestion]["Abstain"] += 1

    # Check if any suggestion has majority support
    for suggestion, counts in suggestion_support.items():
        if counts["For"] > counts["Against"]:
            return True  # Found alignment on this suggestion

    return False  # No alignment found


def extract_vote(vote_text):
    """
    Extracts the vote ('Yes', 'No', or 'Abstain') from a verbose response.

    Args:
        vote_text (str): The full vote text.

    Returns:
        str: The extracted vote ('Yes', 'No', or 'Abstain').
    """
    if "yes" in vote_text.lower():
        return "Yes"
    elif "no" in vote_text.lower():
        return "No"
    elif "abstain" in vote_text.lower():
        return "Abstain"
    return "Unknown"  # Default if vote is unclear

def update_narrative(game_context, proposer_name=None, proposal=None, outcome=None, gm_situation=None, summary_only=False, vote_message=None, player_vote=None) -> dict:
    """
    Updates the narrative log based on GM situations or player actions.

    Args:
        game_context (dict): Current game state.
        proposer_name (str): Name of the proposer (if applicable).
        proposal (str): The proposal text (if applicable).
        outcome (str): Outcome of the proposal ("Proposal Passed" or "Proposal Failed") (if applicable).
        gm_situation (str): Situation introduced by the GM (if applicable).
        summary_only (bool): If True, only include a summary of the GM situation.
        vote_message (str): Message about the vote (if applicable).
        player_vote (str): The player's vote ("Yes", "No", or "Abstain") (if applicable).

    Returns:
        dict: The updated game context with the narrative log
    """
    if gm_situation:
        # Log GM-introduced situations
        if summary_only:
            tag = "Summary"
        else:
            tag = "GM_Element"
        event_description = (
            f"Round {game_context['round']}: New Element Introduced by GM.\n "
            f"Situation: {gm_situation}\n "
            "This element sets the stage for the colony's next decisions."
        )
        game_context["narrative"].append({"tag": tag, "description": event_description})
        return game_context
    
    if player_vote and vote_message:
        # Log a player's vote
        event_description = (
            f"Round {game_context['round']}: {vote_message} \n"
            f"Vote: {player_vote}\n"
        )
        game_context["narrative"].append({"tag": "Player_Vote", "description": event_description})
        return game_context
    
    if proposal and outcome:
        # Log the results of a player's proposal
        if outcome == "Proposal Passed":
            event_description = (
                f"Round {game_context['round']}: {proposer_name}'s proposal passed.\n"
            )
        else:
            event_description = (
                f"Round {game_context['round']}: {proposer_name}'s proposal failed.\n"
            )
        game_context["narrative"].append({"tag": "Outcome", "description": event_description})
        return game_context
    
    if proposer_name and proposal:
        # Log a player's proposal
        event_description = (
            f"Round {game_context['round']}: {proposer_name} has proposed a new action.\n"
            f"Proposal: {proposal}\n"
            "The colony must now decide whether to proceed with this action."
        )
        game_context["narrative"].append({"tag": "Proposal", "description": event_description})
        return game_context
    
def resolve_round_with_relationships(context, votes, gm_message) -> dict:
    """
    Resolves the round by updating the game context based on votes, relationships, and GM input.
    
    Args:
        context (dict): Current game context.
        votes (dict): Votes from each player.
        gm_message (str): Input from the GM for context updates.

    Returns:
        dict: Updated game context.
    """
    print(f"\n\033[93mResolving Round...\033[0m votes: {votes}")
    # Step 1: Tally votes and determine proposal outcome
    yes_votes = sum(1 for vote in votes.values() if vote.strip().lower() == "yes")
    no_votes = sum(1 for vote in votes.values() if vote.strip().lower() == "no")
    abstentions = sum(1 for vote in votes.values() if vote.strip().lower() == "abstain")

    print(f"\n\033[93mVote Tally:\033[0m Yes: {yes_votes}, No: {no_votes}, Abstain: {abstentions}")

    if yes_votes > no_votes:

        if "allocated" not in context["resources"]:
            context["resources"]["allocated"] = 0
        context["resources"]["allocated"] += 10  # Example allocation for passed proposals
        context["last_decision"] = "Proposal Passed"
        proposal_outcome = "passed"
    else:
        context["last_decision"] = "Proposal Failed"
        proposal_outcome = "failed"

    # Step 2: Update relationships based on voting alignment
    for voter, vote in votes.items():
        for other_voter, other_vote in votes.items():
            if voter != other_voter:
                # Update relationship based on alignment or conflict in votes
                if vote.strip().lower() == other_vote.strip().lower():
                    if vote.strip().lower() in ["yes", "no"]:  # Agreement on "yes" or "no"
                        if f"{voter}-{other_voter}" not in context["relationships"]:
                            context["relationships"][f"{voter}-{other_voter}"] = 0
                        if context["relationships"][f"{voter}-{other_voter}"] < 2:
                            context["relationships"][f"{voter}-{other_voter}"] += 1
                else:
                    # Disagreement decreases trust
                    if f"{voter}-{other_voter}" not in context["relationships"]:
                        context["relationships"][f"{voter}-{other_voter}"] = 0
                    if context["relationships"][f"{voter}-{other_voter}"] > -2:
                        context["relationships"][f"{voter}-{other_voter}"] -= 1

                # Handle abstentions (neutral impact)
                if vote.strip().lower() == "abstain" or other_vote.strip().lower() == "abstain":
                    if f"{voter}-{other_voter}" not in context["relationships"]:
                        context["relationships"][f"{voter}-{other_voter}"] = 0
                    context["relationships"][f"{voter}-{other_voter}"] += 0  # No change

    # Step 3: Apply GM influence
    if "resources" in gm_message[-1]["content"].lower():
        # Example: Parse GM message to extract resource changes
        context["resources"]["total"] += 5  # Placeholder for GM influence
    if "relationships" in gm_message[-1]["content"].lower():
        # Example: GM imposes a +1 trust boost globally as a morale event
        for key in context["relationships"].keys():
            context["relationships"][key] += 1

    context["morale"] = context.get("morale", 100) + (5 if proposal_outcome == "passed" else -5)

    return context