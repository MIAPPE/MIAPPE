# Release notes
## MIAPPE v1.2

This new version of the MIAPPE standard proposed some additions as well as minor improvements and clarifications. It remains fully compatible with MIAPPE v1.1.

### New fields and properties

#### Biological Material Identification

There are several improvements to make the identification of Biological Material Sources more convenient.
 
1. The identification of *"Biological Material"* source was improved. In addition to the "_Material Source ID_", which is composed of the concatenation of Holding Institute plus Accession Number, explicite fields have been added to unambiguously identify the _Material Source_. Furthermore the opportunity to use also external IDs other IDs e.g. project or BioSamples IDs was added. For details see [issue #67](https://github.com/MIAPPE/MIAPPE/issues/67), [issue #82](https://github.com/MIAPPE/MIAPPE/issues/82), [issue #64](https://github.com/MIAPPE/MIAPPE/issues/64). 

	 - Material source accession number
	 - Material source accession name
	 - Material source institute code
	 - Material source institute name
	 - Material source other identifiers


1. The Definition for the *"Infraspecific name"* was extended. In addition to MCPD-compliant key-value pairs it now supports _cv._ for _cultivar_, _e.g. "subspecies:vinifera, cultivar:Pinot noir"_. For details see  [issue #84](https://github.com/MIAPPE/MIAPPE/issues/84)
1.  The description of the *"Material Source ID"* was updated to make clear that genotypes can be given in the material ID fields, even if e.g. no accession number can be delivered. It is also allowed to provide material derived from crossing of known accessions, e.g.  "mother_accession X father_accession". For details see  [issue #61](https://github.com/MIAPPE/MIAPPE/issues/61)

#### Observed Variables
 

The *"Trait"* description was extended and decomposed with four additional fields to improve compatibility with Crop Ontology and some EMPHASIS information systems. For details see  [issue #66](https://github.com/MIAPPE/MIAPPE/issues/66).

	 - Trait Entity
	 - Trait Entity Accession Number
	 - Trait Characteristic
	 - Trait Characteristic Accession Number




### General Improvements

1. Removed numbering of the MIAPPE specifications. Add  camelCase *"Codename"* to standardize field naming in MIAPPE implementations. This is similar to the BrAPI approach. See details at [issue #85](https://github.com/MIAPPE/MIAPPE/issues/85),[issue #100](https://github.com/MIAPPE/MIAPPE/issues/100)
2. The Excel template "[MIAPPE_Spreadsheet_Template.xlsx](https://github.com/MIAPPE/MIAPPE/blob/v1.2/Templates/MIAPPE_Spreadsheet_Template.xlsx)" was updated to make it tidier and to make the definitions of mandatory columns more visible by using a colorcode. Furthermore an additional reduced Excel template sheet [MIAPPE_Minimal_Spreadsheet_Template.xlsx](https://github.com/MIAPPE/MIAPPE/blob/v1.2/Templates/MIAPPE_Minimal_Spreadsheet_Template.xlsx) with only required sheets and fields was created.
