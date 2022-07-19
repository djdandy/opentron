opentrons Notes
Dylan Dandy <tohtoridandy@outlook.com>
Modified: 7.18.22

CURRENT CONICAL HEIGHT EQUATIONS:
For a 15mL conical above 1.5mL, height[mm]=(0.006[mm/µL]*(remaining_volume[µL])-8.7638[mm])+23[mm]
For a 50mL conical above 3.3mL, height[mm]=(0.002[mm/µL]*(remaining_volume[µL])-6.2216[mm])+17[mm]

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
  OR
  py -m opentrons.simulate /path/to/protocol
  
If needed, I can work on this stuff on Replit
