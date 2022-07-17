from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Height Adjustment',
           'description': '''Testing Height Adjustment Based on Volumes''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    tube_rack_2 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1])
    
    pipette.well_bottom_clearance.dispense = 15

    source=tube_rack_1.wells()[0]
    source_vol=1500
    remain_vol=source_vol
    amounts=[20, 30, 30, 40]
    
    p300.pick_up_tip()

    for i in range(len(amounts)):
      destination=tube_rack_2.wells()[i]
      if remain_vol>=1500:
        pipette.well_bottom_clearance.aspirate = !!!!!HEIGHT FROM VOL CALC!!!!!
        remain_vol=remain_vol-amounts[i]
      else:
        pipette.well_bottom_clearance.aspirate = 5
      p300.distribute(amounts[i], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      print(remain_vol, pipette.well_bottom_clearance.aspirate)
