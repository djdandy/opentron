from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'CDC P643926 Pool',
           'description': '''Aliquoting 100 vials of 46µL peptide pool from a single source''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    plate_1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 2)
    plate_2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 3)
    plate_3 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 5)
    plate_4 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 6)
    plate_5 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 7)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 15

    source=tube_rack_1.wells()[0]
    source_vol=5000 ##CHANGE ME EVERY TIME TO MATCH STARTING VOLUME
    remain_vol=source_vol
    amounts=[46]
    
    p300.pick_up_tip()

    for i in range(24):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
          
    for i in range(24):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
          
    for i in range(24):
      destination=plate_3.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
   
    for i in range(24):
      destination=plate_4.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
   
    for i in range(4):
      destination=plate_5.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
