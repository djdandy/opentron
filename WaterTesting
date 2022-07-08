from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'Test Aliquot',
           'description': '''Aliquoting x vials of Water from a single source''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    plate_1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 1)
    plate_2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 2)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 4)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1])

#Setting a singular source
    source=tube_rack.wells()[0]

#Getting the singular tip to use for the entire aliquot
    p300.pick_up_tip()
    for i in range(6):
#Setting a new destination for every iteration, this avoids using a a list within the function (though a list could be used)
        destination = plate_1.wells()[i]
        p300.distribute(100, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
#Calling a print as a check for success
        print("Plate 1", i)
    for i in range(3):
        destination = plate_2.wells()[i]
        p300.distribute(100, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        print("Plate 2", i)
