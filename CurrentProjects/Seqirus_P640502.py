from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Seqirus Aliquoting',
           'description': '''Pooling 2 peptides, then Aliquoting 40 vials of 1nmol/peptide (30µL) pool solution from a single source''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    plate_1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 2)
    plate_2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 3)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 50

    source=tube_rack_1.wells()[3]
    source_vol=5000
    remain_vol=source_vol
    amounts=[1173.9862]
    
    p300.pick_up_tip()

    destination=tube_rack_1.wells()[4]
    remain_vol=remain_vol-amounts[0]
    temp_remain_vol=(remain_vol)-500
    if temp_remain_vol>=1500:
      p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
    else:
      p300.well_bottom_clearance.aspirate = 1.5
    p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
    
    p300.drop_tip()
    
    source=tube_rack_1.wells()[0]
    source_vol=5500
    remain_vol=source_vol
    amounts=[89.6414343]
    
    p300.pick_up_tip()

    destination=tube_rack_1.wells()[4]
    remain_vol=remain_vol-amounts[0]
    temp_remain_vol=(remain_vol)-500
    if temp_remain_vol>=1500:
      p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
    else:
      p300.well_bottom_clearance.aspirate = 1.5
    p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
    
    p300.drop_tip()
    
    source=tube_rack_1.wells()[1]
    source_vol=2000
    remain_vol=source_vol
    amounts=[86.3723608]
    
    p300.pick_up_tip()

    destination=tube_rack_1.wells()[4]
    remain_vol=remain_vol-amounts[0]
    temp_remain_vol=(remain_vol)-500
    if temp_remain_vol>=1500:
      p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
    else:
      p300.well_bottom_clearance.aspirate = 1.5
    p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
    
    p300.drop_tip()
    
    source=tube_rack_1.wells()[4]
    source_vol=1350
    remain_vol=source_vol
    amounts=[30]
    
    p300.pick_up_tip()
    p300.mix(3, 250, source)
           
    p300.well_bottom_clearance.dispense = 15

    for i in range(24):
      destination=plate_1.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-500
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
    
    remain_vol=remain_vol
    amounts=[30]
    
    for i in range(16):
      destination=plate_2.wells()[i]
      remain_vol=remain_vol-amounts[0]
      temp_remain_vol=(remain_vol)-500
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 1.5
      p300.distribute(amounts[0], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
