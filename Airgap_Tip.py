from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Airgap/Tip Testing',
           'description': '''Checking if an airgap can be done after a dispense and what does it look like? Also,
           checking tip commands''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    plate_1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 2)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 15

    source=tube_rack_1.wells()[0]
    source_vol=2500
    remain_vol=source_vol
    amounts=[100]
    
    p300.pick_up_tip()

    for i in range(2):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-400
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.aspirate(amounts[0], source)
      p300.dispense(amounts[0], destination)
      p300.air_gap(30)
      p300.blow_out(source)
      
    p300.drop_tip()
    p300.pick_up_tip()
    p300.return_tip()
    
      
      
    
    
