# MIAPPE v1.2: Request for Comments

A revision to the previously published MIAPPE standard is being developed. Its progress can be tracked on the ["v1.2" milestone](https://github.com/MIAPPE/MIAPPE/milestone/5).

Comments are very welcome:
  - by email to **miappe-sc@elixir-europe.org** (or miappe@elixir-europe.org ?) 
  - directly on GitHub by voting, commenting or creating issues on our public [issue tracker](https://github.com/MIAPPE/MIAPPE/issues).

All feedback will be traced as Github issues. The reviews will be reorganised and merged when relevant. Feel free to comment on the results. 

We would like to encourage feedback by the end of __November 2023__, so that we can prepare a revised proposal in accordance with the comments (and take further feedback prior to eventual ratification by the MIAPPE steering committee).

Please share this request with anyone who you know who might be interested in contributing. All contributions will be discussed by the MIAPPE team, and responded to in writing, and contributors will be credited on www.miappe.org. All contributors will also be invited to participate in the writing of a paper to publicise the next standard version.

Development of MIAPPE is an open process, so if you would like to do more than just comment, and to participate in these meetings, please let us know via miappe-feedback@ebi.ac.uk.

## Proposed modifications for v1.2

### Biological Material
### Observed Variables
https://github.com/MIAPPE/MIAPPE/issues/61 : Material source ID description updated to make clear that genotypes can be given in the material ID fields.

https://github.com/MIAPPE/MIAPPE/issues/62 : Fixed inconsistency between excel and tsv versions.

https://github.com/MIAPPE/MIAPPE/issues/84 : Use key-value pairs for the infraspecific name, or MCPD-compliant format. Exemples: "subspecies:vinifera, cultivar:Pinot noir", "subsp.:aestivum, cv.:Weneda, Group:winter", "subsp. vinifera cv. Pinot Noir". Free text is not allowed anymore.

https://github.com/MIAPPE/MIAPPE/issues/88 : Make the datafile version number recommended but not mandatory

### GDPR compliance
https://github.com/MIAPPE/MIAPPE/issues/96 : GPS locations can identify people. A notice will be diplayed in the Readme to warn about this and recommend that fuzziness can be applied to comply with GDPR.

### Inclusion of the mappings in the release
The mappings are now part of the MIAPPE releases.

### Modifications to the file templates
https://github.com/MIAPPE/MIAPPE/issues/79 : The excel template has been updated. It has more visible definitions of mandatory columns (with a color code), and a README sheet. It is also tidier (investigation sheet transposed) and easier to parse (no more mixing of examples and data). 

## DOIs for MIAPPE releases
https://github.com/MIAPPE/MIAPPE/issues/95 : MIAPPE releases will be published on Zenodo and have DOIs issued.

## Updated repository management

https://github.com/MIAPPE/MIAPPE/issues/94 : Only use standard and git-friendly file formats are used for development, to facilitate git diffs and track modifications easily. For diffusion, any file format can still be used of course.  

https://github.com/MIAPPE/MIAPPE/issues/80 : Older versions are not kept on the main branch, in order to comply with Git best practices. They are available as git tags. 

https://github.com/MIAPPE/MIAPPE/issues/90 :  Version numbers are not included in file and folder names anymore, in order to comply with Git best practices. 

https://github.com/MIAPPE/MIAPPE/issues/97 : The licence text has been re-formatted in order to match the official text of the CC-BY-SA 4.0, to facilitate automatic classification of the repository.




