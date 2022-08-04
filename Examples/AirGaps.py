from opentrons import protocol_api

metadata = {'apiLevel': '2.12'}

def run(protocol: protocol_api.ProtocolContext):
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', 4)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])

    p300.pick_up_tip()

    for well in reservoir.wells()[:4]:
        p300.aspirate(35, well)
        p300.air_gap(10)

    p300.dispense(225, plate['A1'])

    p300.return_tip()
