class form_top_dict:

    def __init__(self):

        self.sns_form_tops = {}
        self.sns_create_dict()

    def sns_create_dict(self):

        self.sns_form_tops['Seabed'] = ['','','','', 'Seabed', '']

        self.sns_form_tops['North Sea Group'] = ['Tertiary','Eocene','','North Sea Group','', '']

        self.sns_form_tops['Chalk'] = ['Cretaceous','Upper Cretaceous','','Chalk Group','', '']
        self.sns_form_tops['Plenus Marl'] = ['Cretaceous','Upper Cretaceous','','Chalk Group','Plenus Marl', '']
        self.sns_form_tops['Cromer Knoll Group'] = ['Cretaceous','Lower Cretaceous','','Cromer Knoll Group','', '']
        self.sns_form_tops['Red Chalk'] = ['Cretaceous','Lower Cretaceous','','Cromer Knoll Group','Red Chalk', '']
        self.sns_form_tops['Hidra'] = ['Cretaceous','Lower Cretaceous','','Cromer Knoll Group','Hidra', '']

        self.sns_form_tops['Speeton Clay'] = ['Cretaceous','Lower Cretaceous','','Cromer Knoll Group','Speeton Clay', '']
        self.sns_form_tops['Spilsby Sandstone'] = ['Cretaceous','Lower Cretaceous','','Cromer Knoll Group','Spilsby Sandstone', '']

        self.sns_form_tops['Humber'] = ['Jurassic','Upper Jurassic','','Humber Group','', '']
        self.sns_form_tops['Kimmeridge Clay Formation'] = ['Jurassic','Upper Jurassic','','Humber Group','Kimmeridge Clay Formation', '']
        #self.sns_form_tops['Middle Volgian'] = ['Jurassic','Upper Jurassic','Humber Group','Middle Volgian', '']
        #self.sns_form_tops['Lower Volgian'] = ['Jurassic','Upper Jurassic','Humber Group','Lower Volgian', '']
        self.sns_form_tops['Upper Kimmeridgian'] = ['Jurassic','Upper Jurassic','','Humber Group','Upper Kimmeridgian', '']
        self.sns_form_tops['Oxfordian'] = ['Jurassic','Upper Jurassic','','Humber Group','Oxfordian','']
        self.sns_form_tops['Oxford Clay'] = ['Jurassic','Upper Jurassic','','Humber Group','Oxford Clay', '']
        self.sns_form_tops['Corallian Limestone'] = ['Jurassic','Upper Jurassic','','Humber Group','', 'Corallian Limestone']

        self.sns_form_tops['West Sole'] = ['Jurassic','Middle Jurassic','','West Sole Group', '','']
        #self.sns_form_tops['Middle Bajocian'] = ['Jurassic','Middle Jurassic','West Sole Group', 'Middle Bajocian','']
        #self.sns_form_tops['West Sole'] = ['Jurassic','Middle Jurassic','West Sole Group', '','']

        self.sns_form_tops['Lias'] = ['Jurassic','Lower Jurassic','','Lias Group', '','']
        
        self.sns_form_tops['Winterton'] = ['Triassic','Upper Triassic','','Penarth Group', 'Winterton','']
        self.sns_form_tops['Top Rhaetic Sandstone'] = ['Triassic','Upper Triassic','','Penarth Group', 'Winterton','Top Rhaetic Sandstone']
        self.sns_form_tops['Base Rhaetic Sandstone'] = ['Triassic','Upper Triassic','','Penarth Group', 'Winterton','Base Rhaetic Sandstone']
        self.sns_form_tops['Triton'] = ['Triassic','Upper Triassic','','Haisborough Group', 'Triton','']
        self.sns_form_tops['Upper Keuper Claystone'] = ['Triassic','Upper Triassic','','Haisborough Group', 'Triton','Upper Keuper Claystone']
        self.sns_form_tops['Keuper Dolomite'] =['Triassic','Upper Triassic','','Haisborough Group', 'Triton','Keuper Dolomite']
        self.sns_form_tops['Keuper Red Claystone'] =['Triassic','Upper Triassic','','Haisborough Group', 'Triton','Keuper Red Claystone']
        self.sns_form_tops['Keuper Anhydrite'] =['Triassic','Upper Triassic','','Haisborough Group', 'Triton','Keuper Anhydrite']
        self.sns_form_tops['Middle Keuper Claystone'] =['Triassic','Upper Triassic','','Haisborough Group', 'Triton','Middle Keuper Claystone']
        self.sns_form_tops['Dudgeon'] =['Triassic','Upper Triassic','','Haisborough Group', 'Dudgeon','']
        self.sns_form_tops['Top Keuper Halite'] =['Triassic','Upper Triassic','','Haisborough Group', 'Dudgeon','Top Keuper Halite']
        self.sns_form_tops['Base Keuper Halite'] =['Triassic','Middle Triassic','','Haisborough Group', 'Dudgeon','Base Keuper Halite']
        self.sns_form_tops['Lower Keuper Claystone'] =['Triassic','Middle Triassic','','Haisborough Group', 'Dudgeon','Lower Keuper Claystone']
        self.sns_form_tops['Dowsing Dolomite'] =['Triassic','Middle Triassic','','Haisborough Group', 'Dowsing Dolomite','']
        self.sns_form_tops['Top Muschelkalk Halite'] =['Triassic','Middle Triassic','','Haisborough Group', 'Dowsing Dolomite','Top Muschelkalk Halite']
        self.sns_form_tops['Base Muschelkalk Halite'] =['Triassic','Middle Triassic','','Haisborough Group', 'Dowsing Dolomite','Base Muschelkalk Halite']
        self.sns_form_tops['Lower Muschelkalk Claystone'] =['Triassic','Middle Triassic','','Haisborough Group', 'Dowsing Dolomite','Lower Muschelkalk Claystone']
        self.sns_form_tops['Top Rot Halite'] =['Triassic','Middle Triassic','','Haisborough Group', 'Dowsing Dolomite','Top Rot Halite']
        self.sns_form_tops['Base Rot Halite'] =['Triassic','Lower Triassic','','Haisborough Group', 'Dowsing Dolomite','Base Rot Halite']
        self.sns_form_tops['Lower Rot Claystone'] =['Triassic','Lower Triassic','','Haisborough Group', 'Dowsing Dolomite','Lower Rot Claystone']
        self.sns_form_tops['Bunter Sandstone'] =['Triassic','Lower Triassic','','Bacton Group', 'Bunter Sandstone','']
        self.sns_form_tops['Bunter Shale'] =['Triassic','Lower Triassic','','Bacton Group', 'Bunter Shale','Rogenstein']
        self.sns_form_tops['Lower Bunter Claystone'] =['Triassic','Lower Triassic','','Bacton Group', 'Bunter Shale','Lower Bunter Claystone']
        self.sns_form_tops['Brockelschiefer'] =['Triassic','Lower Triassic','','Bacton Group', 'Bunter Shale','Brockelschiefer']

        self.sns_form_tops['Grenzanhydrit'] =['Permian','Upper Permian','Zechstein','Z4', 'Grenzanhydrit','']
        self.sns_form_tops['Aller Halite'] =['Permian','Upper Permian','Zechstein','Z4', 'Aller Halite','']
        self.sns_form_tops['Pegmatitanhydrite'] =['Permian','Upper Permian','Zechstein','Z4', 'Pegmatitanhydrite','']
        self.sns_form_tops['Roter Salzton'] =['Permian','Upper Permian','Zechstein','Z4', 'Roter Salzton','']
        self.sns_form_tops['Leine Halite'] =['Permian','Upper Permian','Zechstein','Z3', 'Leine Halite','']
        self.sns_form_tops['Hauptanhydrite'] =['Permian','Upper Permian','Zechstein','Z3', 'Hauptanhydrite','']
        self.sns_form_tops['Plattendolomit'] =['Permian','Upper Permian','Zechstein','Z3', 'Plattendolomit','']
        self.sns_form_tops['Grauer Salzton'] =['Permian','Upper Permian','Zechstein','Z3', 'Grauer Salzton','']
        self.sns_form_tops['Deckanhydrit'] =['Permian','Upper Permian','Zechstein','Z2', 'Deckanhydrit','']
        self.sns_form_tops['Stassfurt Halite'] =['Permian','Upper Permian','Zechstein','Z2', 'Stassfurt Halite','']
        self.sns_form_tops['Basalanhydrit'] =['Permian','Upper Permian','Zechstein','Z2', 'Basalanhydrit','']
        self.sns_form_tops['Hauptdolomit'] =['Permian','Upper Permian','Zechstein','Z2', 'Hauptdolomit','']
        self.sns_form_tops['Werranhydrit'] =['Permian','Upper Permian','Zechstein','Z1', 'Werranhydrit','']
        self.sns_form_tops['ZechsteinKalk'] =['Permian','Upper Permian','Zechstein','Z1', 'Zechsteinkalk','']
        self.sns_form_tops['Kupferschiefer'] =['Permian','Upper Permian','Zechstein','Z1', 'Kupferschiefer','']


        self.sns_form_tops['Silverpit'] =['Permian','Lower Permian','','Rotliegend', 'Silverpit','']
        self.sns_form_tops['Top Silverpit Halite'] =['Permian','Lower Permian','','Rotliegend', 'Silverpit','Top Silverpit Halite']
        self.sns_form_tops['Base Silverpit Halite'] =['Permian','Lower Permian','','Rotliegend', 'Silverpit','Base Silverpit Halite']
        self.sns_form_tops['Leman Sandstone'] =['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone','']
        self.sns_form_tops['Leman A'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Leman A']
        self.sns_form_tops['Leman B'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Leman B']
        self.sns_form_tops['Leman C'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Leman C']
        self.sns_form_tops['Zone 5b'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 5b']
        self.sns_form_tops['Zone 5a'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 5a']
        self.sns_form_tops['Zone 4b'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 4b']
        self.sns_form_tops['Zone 4a'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 4a']
        self.sns_form_tops['Zone 3b'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 3b']
        self.sns_form_tops['Zone 3a'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 3a']
        self.sns_form_tops['Zone 2b'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 2b']
        self.sns_form_tops['Zone 2a'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 2a']
        self.sns_form_tops['Zone 1b'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 1b']
        self.sns_form_tops['Zone 1a'] = ['Permian','Lower Permian','','Rotliegend', 'Leman Sandstone', 'Zone 1a']

        self.sns_form_tops['Base Zechstein'] =['','','','', '','']
        self.sns_form_tops['Carboniferous'] =['Carboniferous','','','', '','']
        self.sns_form_tops['Stephanian'] =['Carboniferous','Upper Carboniferous','Stephanian','','','']
        self.sns_form_tops['Westphalian'] =['Carboniferous','Upper Carboniferous','Westphalian','', '','']
        self.sns_form_tops['Namurian'] =['Carboniferous','Upper Carboniferous','Naumrian','', '','']
        self.sns_form_tops['Visean'] =['Carboniferous','Upper Carboniferous','Visean','', '','']
        self.sns_form_tops['Tournasian'] =['Carboniferous','Upper Carboniferous','Tournasian','', '','']
        self.sns_form_tops['Dinantian'] =['Carboniferous','Upper Carboniferous','Dinantian','', '','']
        self.sns_form_tops['Ketch'] =['Carboniferous','Upper Carboniferous','Westphalian','', '','Ketch']
        self.sns_form_tops['Lower Schooner'] =['Carboniferous','Upper Carboniferous','Westphalian','', '','Lower Schooner']
        self.sns_form_tops['Westhoe Coal'] =['Carboniferous','Upper Carboniferous','Westphalian','', 'Westhoe Coal','']
        self.sns_form_tops['Murdoch Sandstone'] =['Carboniferous','Upper Carboniferous','Westphalian','', '','Murdoch Sandstone']
        self.sns_form_tops['Caister Coal'] =['Carboniferous','Upper Carboniferous','Westphalian','', 'Caister Coal','']
        self.sns_form_tops['Bowland Shale'] =['Carboniferous','Upper Carboniferous','Namurian','Whitehurst', 'Bowland Shale','']
        self.sns_form_tops['Millstone Grit'] =['Carboniferous','Upper Carboniferous','Namurian','Whitehurst', 'Millstone Grit','']
        self.sns_form_tops['Upper Limestone'] =['Carboniferous','Lower Carboniferous','Namurian','Yoredale', 'Upper Limestone','']
        #self.sns_form_tops['Great Limestone'] =['Carboniferous','Lower Carboniferous','Yoredale', 'Upper Limestone','Great Limestone']
        self.sns_form_tops['Middle Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','']
        self.sns_form_tops['Top Quad Peaks Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Top Quad Peaks Limestone']
        self.sns_form_tops['Base Quad Peaks Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Base Quad Peaks Limestone']    
        self.sns_form_tops['Top 1B Sheet'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Top 1B Sheet']
        self.sns_form_tops['Base 1B Sheet'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Base 1B Sheet']  
        self.sns_form_tops['Top 1B Channel'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Top 1B Channel']
        self.sns_form_tops['Base 1B Channel'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Base 1B Channel']
        self.sns_form_tops['Top Eelwell Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Top Eelwell Limestone']
        self.sns_form_tops['Base Eelwell Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Base Eelwell Limestone'] 
        self.sns_form_tops['Top 1A Upper Channel'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Top 1A Upper Channel']
        self.sns_form_tops['Base 1A Upper Channel'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Base 1A Upper Channel']  
        self.sns_form_tops['Top 1A Sheet'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Top 1A Sheet']
        self.sns_form_tops['Base 1A Sheet'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Base 1A Sheet']       
        self.sns_form_tops['Top Oxford Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Middle Limestone','Top Oxford Limestone'] #zone 2
        self.sns_form_tops['Base Oxford Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Lower Limestone','Base Oxford Limestone'] 
        self.sns_form_tops['Lower Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Lower Limestone','']
        self.sns_form_tops['Top Twin Peaks Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Lower Limestone','Top Twin Peaks Limestone'] 
        self.sns_form_tops['Base Twin Peaks Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Lower Limestone','Base Twin Peaks Limestone'] #zone 3
        self.sns_form_tops['Top Watchlaw Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Lower Limestone','Top Watchlaw Limestone'] 
        self.sns_form_tops['Base Watchlaw Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Lower Limestone','Base Watchlaw Limestone'] #zone 4
        self.sns_form_tops['Dun Limestone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Lower Limestone','Dun Limestone']
        self.sns_form_tops['Whitby Sandstone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', '','Whitby Sandstone']
        self.sns_form_tops['Scremerston'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Scremerston','']
        self.sns_form_tops['Fell Sandstone'] =['Carboniferous','Lower Carboniferous','Visean','Yoredale', 'Fell Sandstone','']
        self.sns_form_tops['Cementstone'] =['Carboniferous','Lower Carboniferous','Tourvasian','Yoredale', 'Cementstone','']
        self.sns_form_tops['Tayport'] =['Carboniferous','Lower Carboniferous','Tourvasian','Upper Old Red', 'Tayport','']

        self.sns_form_tops['Devonian'] =['Devonian','','','', '','']
        self.sns_form_tops['Upper Old Red Sandstone'] =['Devonian','','','', 'Upper Old Red Sandstone','']

        self.sns_form_tops['TD'] = ['','','','', 'TD', '']

        #print(self.sns_form_tops)
        return self.sns_form_tops

if __name__ == "__main__":

    form_top_list = form_top_dict()
    test = form_top_list.sns_create_dict()
    #print(form_top_list.sns_create_dict() )

    #print(test['Oxford Clay'][0])
    #print(test['Oxford Clay'][1])
    #print(test['Oxford Clay'][2])
    #print(test['Oxford Clay'][3])
    #print(test['Oxford Clay'][4])
    #print(test['Oxford Clay'][5])
