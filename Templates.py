from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Height Adjustment Based on 15mL conicals',
           'description': '''Testing Height Adjustment Based on Volumes''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    #
    #
    #One to many
    #
    #
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    tube_rack_2 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    tube_rack_3= protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 3)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 15

    source=tube_rack_1.wells()[0]
    source_vol=1800
    remain_vol=source_vol
    amounts=[20, 30, 30, 40, 50, 60]
    
    p300.pick_up_tip()

    for i in range(len(amounts)):
      destination=tube_rack_2.wells()[i]
      remain_vol=remain_vol-amounts[i]
      temp_remain_vol=(remain_vol)-170
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 7.5
      p300.distribute(amounts[i], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      print("After " +str(remain_vol) +"µL ||", "Before " +str(remain_vol+amounts[i]) +"µL ||", "Temp " +str(temp_remain_vol) +"µL ||", "Height " +str(p300.well_bottom_clearance.aspirate) +"mm")
    
    remain_vol=remain_vol
    amounts=[20, 30, 30, 40, 50, 60]
    
    for i in range(len(amounts)):
      destination=tube_rack_3.wells()[i]
      remain_vol=remain_vol-amounts[i]
      temp_remain_vol=(remain_vol)-170
      if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 7.5
      p300.distribute(amounts[i], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      print("After " +str(remain_vol) +"µL ||", "Before " +str(remain_vol+amounts[i]) +"µL ||", "Temp " +str(temp_remain_vol) +"µL ||", "Height " +str(p300.well_bottom_clearance.aspirate) +"mm")   
   
    #
    #
    #Many to one
    #
    #
    
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    tube_rack_2 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    tube_rack_3 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 3)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1])
    
    p300.well_bottom_clearance.dispense = 15

    destination=tube_rack_3.wells()[4]

    for i in range(4):
      source=tube_rack_1.wells()[i]
      source_vol=[100, 200, 300, 400]
      remain_vol=source_vol[i]
      amounts=[20, 30, 30, 40]
      remain_vol=remain_vol-amounts[i]
      temp_remain_vol=(remain_vol)-170
        if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 7.5
      p300.transfer(amounts[i], source, destination, new_tip = 'always')
      print("After " +str(remain_vol) +"µL ||", "Before " +str(remain_vol+amounts[i]) +"µL ||", "Temp " +str(temp_remain_vol) +"µL ||", "Height " +str(p300.well_bottom_clearance.aspirate) +"mm")

      
    for i in range(4):
      source=tube_rack_2.wells()[i]
      source_vol=[300, 400, 500, 600]
      remain_vol=source_vol[i]
      amounts=[30, 40, 50, 60]
      remain_vol=remain_vol-amounts[i]
      temp_remain_vol=(remain_vol)-170
        if temp_remain_vol>=1500:
        p300.well_bottom_clearance.aspirate = (0.006*(temp_remain_vol)-8.7638)+23
      else:
        p300.well_bottom_clearance.aspirate = 7.5
      p300.transfer(amounts[i], source, destination, new_tip = 'always')
      print("After " +str(remain_vol) +"µL ||", "Before " +str(remain_vol+amounts[i]) +"µL ||", "Temp " +str(temp_remain_vol) +"µL ||", "Height " +str(p300.well_bottom_clearance.aspirate) +"mm")
