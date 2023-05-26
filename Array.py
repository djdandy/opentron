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
      source=tube_rack_2.wells()[i+15]
      destination=plate_1.wells()[i+15]
      p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      destination=plate_2.wells()[i+15]
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      p300.drop_tip()
      
    for i in range(15):
      p300.pick_up_tip()
      source=tube_rack_3.wells()[i+15+15]
      destination=plate_1.wells()[i+15+15]
      p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      destination=plate_2.wells()[i+15+15]
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      p300.drop_tip()
      
      for i in range(15):
        p300.pick_up_tip()
        source=tube_rack_4.wells()[i+15+15+15]
        destination=plate_1.wells()[i+15+15+15]
        p300.well_bottom_clearance.aspirate = 1.5
        p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        destination=plate_2.wells()[i+15+15+15]
        p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        p300.drop_tip()
      
      for i in range(15):
        p300.pick_up_tip()
        source=tube_rack_5.wells()[i+15+15+15+15]
        destination=plate_1.wells()[i+15+15+15+15]
        p300.well_bottom_clearance.aspirate = 1.5
        p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        destination=plate_2.wells()[i+15+15+15+15]
        p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        p300.drop_tip()
      
      for i in range(6):
        p300.pick_up_tip()
        source=tube_rack_6.wells()[i+15+15+15+15+15]
        destination=plate_1.wells()[i+15+15+15+15+15]
        p300.well_bottom_clearance.aspirate = 1.5
        p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        destination=plate_2.wells()[i+15+15+15+15+15]
        p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        p300.drop_tip()
