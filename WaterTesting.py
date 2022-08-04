from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Test Aliquot',
           'description': '''Aliquoting x vials of Water from a single source''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    plate_1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 2)
    plate_2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 3)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 15

    source=tube_rack_1.wells()[0]
    source_vol=2500
    remain_vol=source_vol
    amounts=[100, 50, 75, 150]
    
    p300.pick_up_tip()

    for i in range(len(amounts)):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[i]
      temp_remain_vol=(remain_vol)-170
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 7.5
      p300.distribute(amounts[i], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      print("After " +str(remain_vol) +"µL ||", "Before " +str(remain_vol+amounts[i]) +"µL ||", "Temp " +str(temp_remain_vol) +"µL ||", "Height " +str(p300.well_bottom_clearance.aspirate) +"mm")
    
    remain_vol=remain_vol
    amounts=[30, 200, 500]
    
    for i in range(len(amounts)):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[i]
      temp_remain_vol=(remain_vol)-170
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 7.5
      p300.distribute(amounts[i], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      print("After " +str(remain_vol) +"µL ||", "Before " +str(remain_vol+amounts[i]) +"µL ||", "Temp " +str(temp_remain_vol) +"µL ||", "Height " +str(p300.well_bottom_clearance.aspirate) +"mm")   
