# MIAPPE v1.2: Request For Comments

A new revision of the MIAPPE standard is proposed with some minor improvements and clarifications and we would like to have your review before publishing it. It is available on the [MIAPPE github](https://github.com/MIAPPE/MIAPPE/tree/v1.2). The details are on the ["v1.2" milestone](https://github.com/MIAPPE/MIAPPE/milestone/5) and summarized below.

Feedback and contributions from anyone with interest in the field are very welcomed using the following:
  - Preferably directly on GitHub by voting or commenting on the issues referenced in the present RFC or on our public [issue tracker](https://github.com/MIAPPE/MIAPPE/issues). See detailed instruction [here](#issues-management). If need be, ie if your remark isn't covered by an existing [issue ](https://github.com/MIAPPE/MIAPPE/issues), feel free to create a new issue.
  - By writing to miappe at elixir-europe.org or one of the steering committee members. We will take care of transferring your feedback into GitHub issues. 

All feedback will be traced as GitHub issues. The reviews will be reorganised and merged when relevant. Feel free to comment on the results. 

We would like to encourage feedback by __30 MAR 2024__. We will prepare afterward a revised proposal in accordance with the comments. Those modifications will be discussed on the [issue tracker](https://github.com/MIAPPE/MIAPPE/issues).

Please share this request with anyone who you know who might be interested in contributing. All contributions will be discussed by the MIAPPE team, and responded to in writing, and contributors will be credited on www.miappe.org. All contributors will also be invited to participate in the writing of a paper to publicise the next standard version. If you have suggestions or ideas regarding such a MIAPPE success stories paper, feel free to add comment to the following [document](https://docs.google.com/document/d/1yVQCPLI8U8heYE0FEPQcJKYjGnf3CAvS0dpaVTvaM3g/edit?usp=sharing).

Development of MIAPPE is an open process, so if you would like to do more than just comment, and to participate in these meetings, please let us know via miappe at elixir-europe.org.

## Proposed modifications to the data model

### Investigation
No change in this version.

### Study

- https://github.com/MIAPPE/MIAPPE/issues/81 : The Crop Research Ontology link has been changed to point to AgroPortal where [CO_715](https://agroportal.lirmm.fr/ontologies/CO_715) is available. Te Crop research ontology should eventually be replaced by the agro ontology ([see](https://github.com/MIAPPE/MIAPPE/issues/106))

- https://github.com/MIAPPE/MIAPPE/issues/104 : Better description of the study title.

### Person
No change in this version.

### Data file

 - https://github.com/MIAPPE/MIAPPE/issues/88 : The datafile version number is now recommended but not mandatory


### Biological Material

Material source (accession) identification updates
 -  https://github.com/MIAPPE/MIAPPE/issues/61 : Material source ID description updated to make clear that genotypes can be given in the material ID fields.
 -  https://github.com/MIAPPE/MIAPPE/issues/82 : Add Material Source Institute code and Material Source Accession number to have an explicit accession identification triplet
 -  https://github.com/MIAPPE/MIAPPE/issues/67 : Improve documentation for Biological Material explicit accession and lot number (needed for MIAPPE/BrAPI mapping)
 -  https://github.com/MIAPPE/MIAPPE/issues/64 : Add placeholders for biological material external synonym IDs. 
 -  https://github.com/MIAPPE/MIAPPE/issues/84 : Add cv. for cultivar / infraspecific name : Use key-value pairs for the infraspecific name, or MCPD-compliant format. Exemples: "subspecies:vinifera, cultivar:Pinot noir", "subsp.:aestivum, cv.:Weneda, Group:winter", "subsp. vinifera cv. Pinot Noir". Free text is not allowed anymore.
 - https://github.com/MIAPPE/MIAPPE/issues/45 : Biological material Donor AccessionNumber is not mandatory anymore.
 - https://github.com/MIAPPE/MIAPPE/issues/62 : Fixed inconsistency between excel and tsv versions.

### Environment
No change in this version.

### Experimental factor
No change in this version.

### Event
No change in this version.

### Observation unit
No change in this version.

### Sample
No change in this version.

### Observed Variables

 - https://github.com/MIAPPE/MIAPPE/issues/66 : Add columns to allow documenting the trait using explicit entity and attribute
 - https://github.com/MIAPPE/MIAPPE/issues/73 : Add variable description and variable ID naming recommendations

## GDPR compliance
 - https://github.com/MIAPPE/MIAPPE/issues/96 : GPS locations can identify people. A notice will be displayed in the Readme to warn about this and recommend that fuzziness can be applied to comply with GDPR.

## Inclusion of the mappings in the release
The mappings are now part of the MIAPPE releases.

## Modifications to the file templates
 - https://github.com/MIAPPE/MIAPPE/issues/86 : Creation of a minimalist excel template with only the required sheets.
 - https://github.com/MIAPPE/MIAPPE/issues/85 : Creation of camelCase codenames.
 - https://github.com/MIAPPE/MIAPPE/issues/100 : Removal of the "line #" column in the data model TSV
 - https://github.com/MIAPPE/MIAPPE/issues/79 : The excel template has been updated. It has more visible definitions of mandatory columns (with a color code), and a README sheet. It is also tidier (investigation sheet transposed) and easier to parse (no more mixing of examples and data). 



## DOIs for MIAPPE releases
- https://github.com/MIAPPE/MIAPPE/issues/95 : MIAPPE releases will be published on Zenodo and have DOIs issued.

## Updated repository management

 - https://github.com/MIAPPE/MIAPPE/issues/80 : Older versions are not kept on the main branch, in order to comply with Git best practices. They are available as git tags.
 - https://github.com/MIAPPE/MIAPPE/issues/90 : Version numbers are not included in file and folder names anymore, in order to comply with Git best practices.
 - https://github.com/MIAPPE/MIAPPE/issues/97 : The licence text has been re-formatted in order to match the official text of the CC-BY-SA 4.0, to facilitate automatic classification of the repository.


# Issues management
1. You need to have a github account to contribute to the issues. To do so simply register [here](https://github.com/signup).
1. To contribute to an issue : First select and click on the modification you would like to comment in the present document (for instance [#81](https://github.com/MIAPPE/MIAPPE/issues/81)). Simply add comment at the bottom of the discussion thread. You can comment closed issues.
2. To create an issue, simply go the the [issue tracker](https://github.com/MIAPPE/MIAPPE/issues) and click on new issue.

