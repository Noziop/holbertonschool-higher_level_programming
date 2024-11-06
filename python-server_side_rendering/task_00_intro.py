#!/usr/bin/python3
"""Module for generating invitations from a template."""


def generate_invitations(template: str, attendees: list) -> None:
    """
    Generate invitation files from a template for each attendee.
    
    Args:
        template (str): The invitation template with placeholders
        attendees (list): List of dictionaries containing attendee information
    """
    # Type checking
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    if not all(isinstance(a, dict) for a in attendees):
        print("Error: All attendees must be dictionaries")
        return

    # Empty input checking
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Generate invitations
    for index, attendee in enumerate(attendees, 1):
        # Create a copy of the template
        invitation = template
        
        # Replace placeholders
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A')
            if value is None:  # Handle None values
                value = 'N/A'
            invitation = invitation.replace(f"{{{key}}}", str(value))
        
        # Write to output file
        output_file = f"output_{index}.txt"
        try:
            with open(output_file, 'w') as f:
                f.write(invitation)
        except IOError as e:
            print(f"Error writing to file {output_file}: {e}")