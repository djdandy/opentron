from opentrons import protocol_api

metadata = {'apiLevel': '2.12',
           'protocolName': 'ATCC Aliquot',
           'description': '''Aliquoting 200 vials of ATCC with a premade source''',
           'author': 'Dylan D'}

def run(protocol: protocol_api.ProtocolContext):
    plate_1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 1)
    plate_2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 2)
    plate_3 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 3)
    plate_4 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 4)
    plate_5 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 5)
    plate_6 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 6)
    plate_7 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 7)
    plate_8 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 8)
    plate_9 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_screwcap', 9)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 10)
    tube_rack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 11)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])

#Setting a singular source
    source=tube_rack.wells()[0]

#Getting the singular tip to use for the entire aliquot
    p300.pick_up_tip()
    for i in range(24):
#Setting a new destination for every iteration, this avoids using a a list within the function (though a list could be used)
        destination = plate_1.wells()[i]
        p300.distribute(200, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
#Calling a print as a check for success
        print("Plate 1", i)
    for i in range(24):
        destination = plate_2.wells()[i]
        p300.distribute(200, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        print("Plate 2", i)
    for i in range(24):
        destination = plate_3.wells()[i]
        p300.distribute(200, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        print("Plate 3", i)
    for i in range(24):
        destination = plate_4.wells()[i]
        p300.distribute(200, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        print("Plate 4", i)
    for i in range(24):
        destination = plate_5.wells()[i]
        p300.distribute(200, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        print("Plate 5", i)
    for i in range(24):
        destination = plate_6.wells()[i]
        p300.distribute(200, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        print("Plate 6", i)
    for i in range(24):
        destination = plate_7.wells()[i]
        p300.distribute(200, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        print("Plate 7", i)
    for i in range(24):
        destination = plate_8.wells()[i]
        p300.distribute(200, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        print("Plate 8", i)
    for i in range(8):
        destination = plate_9.wells()[i]
        p300.distribute(200, source, destination, new_tip = 'never', blow_out = True, blowout_location = 'source well')
        print("Plate 9", i)
