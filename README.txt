opentrons Notes
Dylan Dandy <tohtoridandy@outlook.com>
Modified: 6.20.22

Tutorial? https://docs.opentrons.com/v2/tutorial.html

Complex Common Commands? https://docs.opentrons.com/v2/new_complex_commands.html

Protocol library? https://docs.opentrons.com/v2/new_protocol_api.html#protocol-api-reference

Default labware? https://labware.opentrons.com/

Need to create labware? https://labware.opentrons.com/create/

Default hardware? https://docs.opentrons.com/v2/new_modules.html

Examples? https://docs.opentrons.com/v2/new_examples.html

!!! IMPORTANT !!!
Simulation with python (without Jupyter or the Robot) seems to only work with Python <v3.10 as v3.10 removed loop.
Also need pip (need to setup an environment PATH) installed with opentrons installed as well.

Preference is to simulate through python by:
  python -m opentrons.simulate /path/to/protocol
  
If needed, I can work on this stuff on Replit
