def petrel_tops_header_file(feet = False):
    '''
    ()->(list of strings)
    Subroutine to create a list containing required header lines for Petrel well tops import file
    PRECONDITION: Specified format below is valid - created for v2019.3
    K JAGGS DEC 2020
    '''
    
    #create list to host header
    text_header = []
    
    #append required lines to header
    text_header.append('# Petrel well tops')
    text_header.append('# Unit in X and Y direction:')
    if feet == True:
        text_header.append('# Unit in depth: ft')
    elif feet == False:
        text_header.append('# Unit in depth: m')
    text_header.append('VERSION 2')
    text_header.append('BEGIN HEADER')
    #text_header.append('X')
    #text_header.append('Y')
    #text_header.append('Z')
    #text_header.append('TWT picked')
    #text_header.append('TWT auto')
    #text_header.append('Geological age')
    text_header.append('MD')
    #text_header.append('PVD auto')
    #text_header.append('Type')
    text_header.append('Surface')
    text_header.append('Well')
    text_header.append('Interpreter')
    #text_header.append('Confidence factor')
    #text_header.append('Dip angle')
    #text_header.append('Dip azimuth')
    #text_header.append('Missing')
    #text_header.append('TVT')
    #text_header.append('TST')
    #text_header.append('TVT zone')
    #text_header.append('TST zone')
    #text_header.append('Observation number')
    #text_header.append('Used by dep.conv.')
    #text_header.append('Used by geo mod')
    #text_header.append('Zone log')
    #text_header.append('Edited by user')
    #text_header.append('Symbol')
    #text_header.append('Locked to fault')
    text_header.append('END HEADER')

    #print(text_header)

    return text_header