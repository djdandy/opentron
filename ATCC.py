from opentrons import protocol_api

metadata = {'apiLevel': '2.12'}

def run(protocol: protocol_api.ProtocolContext):
    plate_1 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    plate_2 = protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
    plate_3 = protocol.load_labware('corning_96_wellplate_360ul_flat', 3)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1])

    source=tube_rack.wells()[0]

    p300.pick_up_tip()
    for i in range(96):
        destination=plate_1.wells()[i]
        p300.distribute(200, source, destination, new_tip='never', blow_out=True, blowout_location='source well')
        print("Plate 1", i)
    for i in range(96):
        destination=plate_2.wells()[i]
        p300.distribute(200, source, destination, new_tip='never', blow_out=True, blowout_location='source well')
        print("Plate 2", i)
    for i in range(8):
        destination=plate_3.wells()[i]
        p300.distribute(200, source, destination, new_tip='never', blow_out=True, blowout_location='source well')
        print("Plate 3", i)
