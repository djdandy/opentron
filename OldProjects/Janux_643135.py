from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Janux Aliquoting',
           'description': '''Aliquoting 300 vials of solution from a single source''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    plate_1 = protocol.load_labware('agilent_54_tuberack_2000ul', 2)
    plate_2 = protocol.load_labware('agilent_54_tuberack_2000ul', 3)
    plate_3 = protocol.load_labware('agilent_54_tuberack_2000ul', 5)
    plate_4 = protocol.load_labware('agilent_54_tuberack_2000ul', 6)
    plate_5 = protocol.load_labware('agilent_54_tuberack_2000ul', 7)
    plate_6 = protocol.load_labware('agilent_54_tuberack_2000ul', 8)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 15

    source=tube_rack_1.wells()[0]
    source_vol=10500
    remain_vol=source_vol
    amounts=[40]
    
    p300.pick_up_tip()

    for i in range(54):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
    
    for i in range(54):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      
    for i in range(54):
      destination=plate_3.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      
    for i in range(54):
      destination=plate_4.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      
    for i in range(54):
      destination=plate_5.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      
    for i in range(30):
      destination=plate_6.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
