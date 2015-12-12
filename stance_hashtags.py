# Nicolas Hahn
# keep track of hashtags that are good indicators of tweets 
# that have stance for or against these topics

abortion = {
    'topic': 'abortion',
    'fullname': 'Legalization of Abortion',
    'topic_id': 3,
    'FAVOR':[
        '#ProChoice',
        '#StandWithPP',
        '#IStandWithPP',
        '#RightToChoose',
    ],
    'AGAINST':[
        '#ProLife',
        '#DefundPP',
        '#PrayToEndAbortion',
        '#UnbornLivesMatter',
    ],
    'extra_query':[],
}
atheism = {
    'topic': 'atheism',
    'fullname': 'Atheism',
    'topic_id': 28,
    'FAVOR':[
        '#SacrilegeSunday',
        '#NotAfraidOfBurningInHell',
        '#AtheistVoter',
        # '#Awesome', # run a check after to make sure #atheism is also in there
        '#DogmaFree',
        '#AntiReligion',
        '#AntiGod',
        '#FreeThinker',
        '#ReligionDoesHarm',
        '#FreedomFromReligion',
        '#ReligiousFreedom',
        '#AntiTheist',
        '#AtheistBecause',
        '#YayTheism',
        '#GodFree',
        '#Agnostic',
        '#ReligionKills',
        '#NoGod',
        '#NoGods',
        '#ProudAtheist',
        '#GoodWithoutGod',
        '#Atheist',
    ],
    'AGAINST':[
        '#AntiAtheism',
        '#FuckAtheism',
        '#HolyBible',
        '#Islam',
        '#Spirituality',
        '#God',
        '#PrayerWorks',
        '#PrayerChangesThings',
        '#TeamJesus',
        '#PraiseTheLord',
        '#JesusIsLord',
    ],
    'extra_query':[
        '#Awesome',
    ],
}
hillary_clinton = {
    'topic': 'hillary',
    'fullname': 'Hillary Clinton',
    'topic_id': 31,
    'FAVOR':[
        '#HillYes',
        '#ImWithHer',
        '#ITrustHillary',
        '#TeamHillary',
    ],
    'AGAINST':[
        '#NoHillary',
        '#NoHillary2016',
        '#StopHillary',
        '#StopHillary2016',
        '#HillaryForPrison',
        '#HillaryForPrison2016',
        '#OhHillNo',
        '#NoHillNo',
        '#HillNo',
        '#NotWithHer',
        '#Shillary',
        '#Hilliar',
        '#WhyImNotVotingForHillary',
        '#Benghazi',
        '#NoMoreClintons',
    ],
    'extra_query':[],
}
feminism = {
    'topic': 'feminism',
    'fullname': 'Feminist Movement',
    'topic_id': 30,
    'FAVOR':[
        '#FeminismIsForEveryone',
        '#PatriarchyIsUgly',
        '#FeministsAreBeautiful',
        '#YesAllWomen',
        '#YayFeminism',
    ],
    'AGAINST':[
        '#AntiFeminism',
        '#AntiFeminist',
        '#FeminismIsAwful',
        '#WomenAgainstFeminism',
        '#FeminismIsCruelty',
        '#SpankAFeminist',
        '#IDontNeedFeminism',
        '#Feminazi',
    ],
    'extra_query':[],
}
climate_change = {
    'topic': 'climate',
    'fullname': 'Climate Change is a Real Concern',
    'topic_id': 29,
    'FAVOR':[
        '#DemandClimateAction',
        '#ClimateAction',
        '#SaveOurPlanet',
        '#SaveThePlanet',
        '#GlobalWarmingIsReal',
        '#ActOnClimate',
        '#ClimateReporting2015',
        '#CambioClimatico',
        '#KeepItInTheGround',
        '#RisingSeaLevels',
        '#SaveTheEarth',
        '#Deforestation',
        '#CitizensClimateLobby2015',
        '#CarbonTaxScam',
        '#Playin4Climate',
    ],
    'AGAINST':[
        '#Lies',
        '#Hoax',
        '#Scam',
        '#Fraud',
        '#GlobalWarmingIsALie',
        '#ClimateChangeIsALie',
        '#GlobalWarmingIsAHoax',
        '#ClimateChangeIsAHoax',
    ],
    'extra_query':[
        '#Lies',
        '#Hoax',
        '#Scam',
        '#Fraud',
    ],
}

gun_control = {
    'topic': 'gun control',
    'fullname': 'Gun Control',
    # 'topic_id': not added to iac yet,
    'FAVOR':[
        '#GunControl',
        '#AntiGun',
    ],
    'AGAINST':[
        '#ProGun',
        '#2A',
        '#2ndAmendment',
        '#2ndAmmendment',
        '#SecondAmendment',
        '#SecondAmmendment',
        '#RightToBearArms',
    ],
}


all_topics = [
    abortion, 
    atheism, 
    hillary_clinton, 
    feminism, 
    climate_change
    # gun_control
]
