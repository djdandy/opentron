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

    p300.move_to(plate_1['A1'].top())
    
    p300.move_to(plate_1['C3'].top())
           
    p300.move_to(plate_1['B5'].top())

    p300.move_to(plate_1['E6'].top())
         
    p300.move_to(plate_1['A8'].top())
           
    p300.move_to(plate_1['F9'].top())
