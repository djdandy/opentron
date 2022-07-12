from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Seqirus Pool',
           'description': '''Creating the Seqirus pool via Matrix''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    tube_rack_1 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    tube_rack_2 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
    tube_rack_3 = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 3)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1])

#Setting a singular Destination
    destination=tube_rack_3.wells()[3]

#Getting the singular tip to use for the entire aliquot
    p300.transfer([1,2,3,4], tube_rack_1.wells()[0,1,2,3],destination, new_tip = 'always')
    p300.transfer([1,2,3,4], tube_rack_2.wells()[0,1,2,3],destination, new_tip = 'always')
    p300.transfer([1,2,3,4], tube_rack_3.wells()[0,1,2,3],destination, new_tip = 'always')
