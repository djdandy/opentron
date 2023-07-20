from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Leidos ACN - Part 1',
           'description': '''Dispensing solvent for 10 vials - Make sure to edit all starting values as indictaed!!!''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tube_rack_1 = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 1)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    plate_1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 3)
    tube_rack_2 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 4)
    plate_2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 5)
    plate_3 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 6)
    plate_4 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 7)
    plate_5 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 8)
    plate_6 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 9)
    plate_7 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 10)
    plate_8 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 11)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 30 #Avoiding any touching of liquids in the vial with the pipette tip.

### ACN Dispensing ###
    source=tube_rack_2.wells()[6]
    source_vol=22000 ### CHANGE ME TO MATCH ACN STARTING AMOUNT
    remain_vol=source_vol

    ### Peptide 1 ACN ###

    amounts=[149.4] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 1 
    p300.pick_up_tip()

    for i in range(0,10):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 2 ACN ###

    amounts=[79.8] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 2

    for i in range(14,24):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 3 ACN ###

    amounts=[96.7] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 3

    for i in range(0,10):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 4 ACN ###

    amounts=[89.4] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 4

    for i in range(14,24):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 5 ACN ###

    amounts=[66.5] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 5

    for i in range(0,10):
      destination=plate_3.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 6 ACN ###

    amounts=[92.2] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 6

    for i in range(14,24):
      destination=plate_3.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 7 ACN ###

    amounts=[75.3] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 7

    for i in range(0,10):
      destination=plate_4.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 8 ACN ###

    amounts=[60.7] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 8

    for i in range(14,24):
      destination=plate_4.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 9 ACN ###

    amounts=[82.9] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 9

    for i in range(0,10):
      destination=plate_5.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 10 ACN ###

    amounts=[93.2] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 10

    for i in range(14,24):
      destination=plate_5.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 11 ACN ###

    amounts=[149.4] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 11

    for i in range(0,10):
      destination=plate_6.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 12 ACN ###

    amounts=[121.9] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 12

    for i in range(14,24):
      destination=plate_6.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 13 ACN ###

    amounts=[95.5] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 13

    for i in range(0,10):
      destination=plate_7.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 14 ACN ###

    amounts=[99.5] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 14

    for i in range(14,24):
      destination=plate_7.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 15 ACN ###

    amounts=[36.4] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 15

    for i in range(0,10):
      destination=plate_8.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')

    ### Peptide 16 ACN ###

    amounts=[54.7] #CHANGE ME TO MATCH HOW MUCH ACN IS NEEDED FOR PEPTIDE 16

    for i in range(14,24):
      destination=plate_8.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
