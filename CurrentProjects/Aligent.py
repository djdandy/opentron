from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Aligenting',
           'description': '''NA''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
    plate_1 = protocol.load_labware('agilent_54_tuberack_2000ul', 5)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])

    
    p300.pick_up_tip()

    for i in [0,14,25,34,42,53]:
      destination=plate_1.wells()[i]
      p300.move_to(destination)
