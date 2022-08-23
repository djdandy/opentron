from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Height Adjustment Based on 50mL conicals',
           'description': '''Testing Height Adjustment Based on Volumes''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    tube_rack_2 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])
    
    #Setting a default dispense height, this is 15mm from the bottom
    p300.well_bottom_clearance.dispense = 15

    #Setting the:
    #Source tube & location
    #Source tube volume
    #Remaining source's volume for calculations
    #Amounts to be aliquoted for a SINGLE tube rack
    source=tube_rack_1.wells()[0]
    source_vol=4000
    remain_vol=source_vol
    amounts=[20, 30, 30, 40, 50, 60]
    
    #Picking up the tip
    p300.pick_up_tip()

    #Reading the amount of aliquots needed to be done for a single tube rack
    for i in range(len(amounts)):
      #Setting the destination(s) for the tube rack
      destination=tube_rack_2.wells()[i]
      #Using the previous (or set) remaining volume, subtract the amount needed for an aliquot and overwrite remaining volume
      remain_vol=remain_vol-amounts[i]
      #Because we are taking extras AND returning our source solution, we need a temp. remaining volume that includes a little extra
      temp_remain_vol=(remain_vol)-3000
      #Using the temp. remaining volume because that is the height/depth we need to actually have breathing room,
      #we check if it's above the 1.5mL mark to avoid the cone
      if temp_remain_vol>=3300:
        #If the we are above the bottom cone, use the temp. remaining volume to calulate for a desired height/depth
        #and ADDING the height of 3.3mL (the cone - 1.7cm tall)
        p300.well_bottom_clearance.aspirate = (0.002*(temp_remain_vol)-6.2216)+17
      else:
        #If we don't meet the requirements for avoiding the cone, just go relatively deep to get enough liquid
        p300.well_bottom_clearance.aspirate = 1.5
      #Finally the transfer can be done, using the amount, source, destination; we set the height/depth while doing calculations
      p300.distribute(amounts[i], source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
      #For the sake of my sanity, this prints remaining volume AFTER aliquoting, remaining volume before aliquoting,
      #temp. remaining volume which height is decided from, and the height of aspiration
      print("After " +str(remain_vol) +"µL ||", "Before " +str(remain_vol+amounts[i]) +"µL ||", "Temp " +str(temp_remain_vol) +"µL ||", "Height " +str(p300.well_bottom_clearance.aspirate) +"mm")
