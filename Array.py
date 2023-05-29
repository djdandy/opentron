from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Matchpoint Aliquotting',
           'description': '''Aliquoting Array plates from multiple sources''',
           'author': 'Dylan D + Kristo'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    tube_rack_1 = protocol.load_labware('opentrons_15_tuberack_nest_15ml_conical', 1)
    tube_rack_2 = protocol.load_labware('opentrons_15_tuberack_nest_15ml_conical', 4)
    tube_rack_3 = protocol.load_labware('opentrons_15_tuberack_nest_15ml_conical', 7)
    tube_rack_4 = protocol.load_labware('opentrons_15_tuberack_nest_15ml_conical', 10)
    tube_rack_5 = protocol.load_labware('opentrons_15_tuberack_nest_15ml_conical', 11)
    tube_rack_6 = protocol.load_labware('opentrons_15_tuberack_nest_15ml_conical', 8)
    plate_1 = protocol.load_labware('nest_96_wellplate_2ml_deep', 6)
    plate_2 = protocol.load_labware('nest_96_wellplate_2ml_deep', 3)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 15
    
    amounts=[50]

    for i in range(15):
      p300.pick_up_tip()
      source=tube_rack_1.wells()[i]
      destination=plate_1.wells()[i]
      p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      destination=plate_2.wells()[i]
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      p300.drop_tip()
      
    for i in range(15):
      p300.pick_up_tip()
      source=tube_rack_2.wells()[i]
      destination=plate_1.wells()[i+15]
      p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      destination=plate_2.wells()[i+15]
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      p300.drop_tip()
      
    for i in range(15):
      p300.pick_up_tip()
      source=tube_rack_3.wells()[i]
      destination=plate_1.wells()[i+15+15]
      p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      destination=plate_2.wells()[i+15+15]
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      p300.drop_tip()
      
    for i in range(15):
      p300.pick_up_tip()
      source=tube_rack_4.wells()[i]
      destination=plate_1.wells()[i+15+15+15]
      p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      destination=plate_2.wells()[i+15+15+15]
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      p300.drop_tip()
      
    for i in range(15):
      p300.pick_up_tip()
      source=tube_rack_5.wells()[i]
      destination=plate_1.wells()[i+15+15+15+15]
      p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      destination=plate_2.wells()[i+15+15+15+15]
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      p300.drop_tip()
      
    for i in range(6):
      p300.pick_up_tip()
      source=tube_rack_6.wells()[i]
      destination=plate_1.wells()[i+15+15+15+15+15]
      p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      destination=plate_2.wells()[i+15+15+15+15+15]
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      p300.drop_tip()
