from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Leidos Pool',
           'description': '''Pooling Leidos''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    plate_1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 2)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 15

    source=tube_rack_1.wells(0,1,2)
    source_vol=[350, 350, 330]
    amounts=[310]
    
    for i in range(len(source)):
      p300.pick_up_tip()
      destination=tube_rack_1.wells(3)
      remain_vol=source_vol[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source[i], destination, new_tip = 'never')
      p300.air_gap(30)
      p300.blow_out(source[i])
      p300.drop_tip()
      
    
      
      
    
    
