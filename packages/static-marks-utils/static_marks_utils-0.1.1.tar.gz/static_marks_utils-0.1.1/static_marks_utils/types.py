SectionName = str
StaticMarksEntryValue = str
StaticMarksEntryDisplayName = str
StaticMarksCardDisplayName = str
StaticMarksEntry = dict[StaticMarksEntryDisplayName, list[StaticMarksEntryValue]]
StaticMarksCard = dict[StaticMarksCardDisplayName, list[StaticMarksEntry]]
SectionBody = list[StaticMarksCard]
StaticMarksYAML = dict[SectionName, SectionBody]
