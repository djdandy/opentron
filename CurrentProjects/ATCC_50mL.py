from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'ATCC Aliquoting',
           'description': '''Aliquoting 100 vials of solution from a single source''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    plate_1 = protocol.load_labware('agilent_54_tuberack_2000ul', 2)
    plate_2 = protocol.load_labware('agilent_54_tuberack_2000ul', 3)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 15

    source=tube_rack_1.wells()[6]
    source_vol=10500
    remain_vol=source_vol
    amounts=[100]
    
    p300.pick_up_tip()

    for i in range(54):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never')
      p300.air_gap(30)
      p300.blow_out(source)
    
    remain_vol=remain_vol
    amounts=[100]
    
    for i in range(46):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-3000
      if temp_remain_vol>=3300:
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.transfer(amounts[0], source, destination, new_tip = 'never')
      p300.air_gap(30)
      p300.blow_out(source)
