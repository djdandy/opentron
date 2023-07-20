from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Leidos Aliquoting - Part 2',
           'description': '''Dispensing petide for one 0.5mg NET, then for ten 0.05mg NET on top of ACN solvent - Make sure to edit all starting values as indictaed!!!''',
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
    
    p300.well_bottom_clearance.dispense = 35 #Avoiding any touching of liquids in the vial with the pipette tip.

### Peptide Dispensing ###

    ### Peptide 1 ###
    
    source=tube_rack_1.wells()[0]
    source_vol=2400 ### CHANGE ME TO MATCH PEPTIDE 1 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[548.6] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 1 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(11,12):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[54.9] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 1 IS NEEDED for 0.05mg NET 

    for i in range(0,10):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 2 ###
    
    source=tube_rack_1.wells()[1]
    source_vol=2200 ### CHANGE ME TO MATCH PEPTIDE 2 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[628.4] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 2 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(12,13):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[62.8] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 2 IS NEEDED for 0.05mg NET 

    for i in range(14,24):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 3 ###
    
    source=tube_rack_1.wells()[2]
    source_vol=2000 ### CHANGE ME TO MATCH PEPTIDE 3 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[547.5] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 3 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(11,12):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[54.8] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 3 IS NEEDED for 0.05mg NET 

    for i in range(0,10):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 4 ###
    
    source=tube_rack_1.wells()[3]
    source_vol=2000 ### CHANGE ME TO MATCH PEPTIDE 4 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[635.2] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 4 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(12,13):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[63.5] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 4 IS NEEDED for 0.05mg NET 

    for i in range(14,24):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 5 ###
    
    source=tube_rack_1.wells()[4]
    source_vol=1500 ### CHANGE ME TO MATCH PEPTIDE 5 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[555.6] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 5 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(11,12):
      destination=plate_3.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[55.6] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 5 IS NEEDED for 0.05mg NET 

    for i in range(0,10):
      destination=plate_3.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 6 ###
    
    source=tube_rack_1.wells()[5]
    source_vol=2200 ### CHANGE ME TO MATCH PEPTIDE 6 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[689.7] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 6 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(12,13):
      destination=plate_3.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[69.0] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 6 IS NEEDED for 0.05mg NET 

    for i in range(14,24):
      destination=plate_3.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 7 ###
    
    source=tube_rack_1.wells()[6]
    source_vol=2300 ### CHANGE ME TO MATCH PEPTIDE 7 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[892.4] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 7 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(11,12):
      destination=plate_4.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[89.2] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 7 IS NEEDED for 0.05mg NET 

    for i in range(0,10):
      destination=plate_4.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 8 ###
    
    source=tube_rack_1.wells()[7]
    source_vol=2400 ### CHANGE ME TO MATCH PEPTIDE 8 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[708.8] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 8 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(12,13):
      destination=plate_4.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[70.9] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 8 IS NEEDED for 0.05mg NET 

    for i in range(14,24):
      destination=plate_4.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 9 ###
    
    source=tube_rack_1.wells()[8]
    source_vol=1700 ### CHANGE ME TO MATCH PEPTIDE 9 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[617.2] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 9 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(11,12):
      destination=plate_5.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[61.7] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 9 IS NEEDED for 0.05mg NET 

    for i in range(0,10):
      destination=plate_5.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 10 ###
    
    source=tube_rack_1.wells()[9]
    source_vol=2400 ### CHANGE ME TO MATCH PEPTIDE 10 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[477.3] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 10 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(12,13):
      destination=plate_5.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[47.7] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 10 IS NEEDED for 0.05mg NET 

    for i in range(14,24):
      destination=plate_5.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 11 ###
    
    source=tube_rack_1.wells()[10]
    source_vol=2500 ### CHANGE ME TO MATCH PEPTIDE 11 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[628.8] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 11 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(11,12):
      destination=plate_6.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[62.9] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 11 IS NEEDED for 0.05mg NET 

    for i in range(0,10):
      destination=plate_6.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 12 ###
    
    source=tube_rack_1.wells()[11]
    source_vol=2000 ### CHANGE ME TO MATCH PEPTIDE 12 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[561.1] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 12 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(12,13):
      destination=plate_6.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[56.1] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 12 IS NEEDED for 0.05mg NET 

    for i in range(14,24):
      destination=plate_6.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 13 ###
    
    source=tube_rack_1.wells()[12]
    source_vol=2400 ### CHANGE ME TO MATCH PEPTIDE 13 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[693.6] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 13 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(11,12):
      destination=plate_7.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[69.4] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 13 IS NEEDED for 0.05mg NET 

    for i in range(0,10):
      destination=plate_7.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 14 ###
    
    source=tube_rack_1.wells()[13]
    source_vol=2300 ### CHANGE ME TO MATCH PEPTIDE 14 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[559.8] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 14 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(12,13):
      destination=plate_7.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[56.0] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 14 IS NEEDED for 0.05mg NET 

    for i in range(14,24):
      destination=plate_7.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 15 ###
    
    source=tube_rack_1.wells()[14]
    source_vol=2300 ### CHANGE ME TO MATCH PEPTIDE 15 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[791.9] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 15 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(11,12):
      destination=plate_8.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[79.2] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 15 IS NEEDED for 0.05mg NET 

    for i in range(0,10):
      destination=plate_8.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()

    ### Peptide 16 ###
    
    source=tube_rack_2.wells()[0]
    source_vol=1900 ### CHANGE ME TO MATCH PEPTIDE 16 STARTING AMOUNT
    remain_vol=source_vol

    amounts=[615.1] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 16 IS NEEDED for 0.5mg NET 
    p300.pick_up_tip()

    for i in range(12,13):
      destination=plate_8.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    
    amounts=[61.5] #CHANGE ME TO MATCH HOW MUCH PEPTIDE 16 IS NEEDED for 0.05mg NET 

    for i in range(14,24):
      destination=plate_8.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never', blow_out = False, blowout_location = 'source well')
    p300.drop_tip()
