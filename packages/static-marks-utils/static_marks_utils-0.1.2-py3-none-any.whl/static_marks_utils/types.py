SectionName = str
StaticMarksEntryValue = str
StaticMarksEntryDisplayName = str
StaticMarksCardDisplayName = str
StaticMarksEntry = dict[StaticMarksEntryDisplayName, list[StaticMarksEntryValue]]
StaticMarksCard = dict[StaticMarksCardDisplayName, list[StaticMarksEntry]]
StaticMarksSectionBody = list[StaticMarksCard]
StaticMarksYAML = dict[SectionName, StaticMarksSectionBody]
