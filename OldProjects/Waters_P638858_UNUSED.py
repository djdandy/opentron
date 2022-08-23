from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Waters Pool',
           'description': '''Creating the Waters pool and aliquoting''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    tube_rack_2 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 3)
    plate_1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 4)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])

    p300.well_bottom_clearance.dispense = 15
    
#Setting a singular Destination
    destination=tube_rack_2.wells()[0]

    for i in range(6):
      source=tube_rack_1.wells()[i]
      source_vol=[100, 200, 300, 400, 500, 600]
      remain_vol=source_vol[i]
      amounts=[10, 20, 30, 40, 50, 60]
      remain_vol=remain_vol-amounts[i]
      temp_remain_vol=(remain_vol)-170
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 7.5
      p300.transfer(amounts[i], source, destination, new_tip = 'always' blow_out = True, blowout_location = 'source well')
    
    source=tube_rack_2.wells()[0]
    source_vol=2100
    remain_vol=source_vol
    amounts=[20, 30, 30, 40, 50, 60]
    
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
