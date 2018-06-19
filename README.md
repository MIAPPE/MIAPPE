# MIAPPE v1.1: Request for Comments

A revision to the previously published MIAPPE standard has been proposed. It extends [MIAPPE v1.0](https://github.com/MIAPPE/MIAPPE-checklist) and contains some specific recommendations as to how the MIAPPE principles should be applied to various types of experiments/material. The document is split into

- [MIAPPE_Checklist-v1.1](MIAPPE_Checklist-v1.1.tsv)
- [MIAPPE_Checklist-Appendix_I-Environment-v1.1](MIAPPE_Checklist-Appendix_I-Environment-v1.1.tsv)
- [MIAPPE_Checklist-Appendix_II-Treatment-v1.1](MIAPPE_Checklist-Appendix_II-Treatment-v1.1.tsv)

and now open for consultation, and we welcome contributions from anyone with interest in the field. 

Feedback can be provided in a number of ways:

- Comment directly on the proposal in [Google docs](https://docs.google.com/document/d/1071CknesZEh8xeGyA1gK1HP3LFPaZ5gpsEW0v8KqzPk/edit#heading=h.gjdgxs).  We will try to leave comments up for as long as possible to facilitate discussion, but will harvest comments from the document if necessary to prevent it from becoming unwieldy.
- Read the document (as [PDF](https://github.com/langeipk/MIAPPE-checklist/blob/v1.1-rfc/MIAPPE_v1.1_rfc1_proposal.pdf), or in Google docs), and email to miappe-feedback@ebi.ac.uk
- Read the document, and raise an issue on our public [GitHub tracker](https://github.com/MIAPPE/MIAPPE-checklist/issues)
- Provide chances as [pull request](https://help.github.com/articles/about-pull-requests/).

We would like to encourage feedback by the end of August 2018, in order that we can prepare a revised proposal in accordance with the comments (and take further feedback prior to eventual ratification by the MIAPPE steering committee). 
Please share this request with anyone who you know who might be interested in contributing. We request that individuals do not comment anonymously. All contributions will be discussed by the development team, and responded to in writing, and contributors will be credited on www.miappe.org.  All contributors will also be invited to participate in the writing of a paper to publicise the final standard.
Responses to comments will be prepared by the development team via remote discussion (email and meetings). Development of MIAPPE is an open process, so if you would like to do more than just comment, and to participate in these meetings, please let us know via miappe-feedback@ebi.ac.uk.

# Overview to revision 1.1

The present revision of MIAPPE, carried out by ELIXIR's plant use case, aimed at achieving four main goals:
 
1. The extension of MIAPPE’s scope, namely to accommodate woody plants as an additional use-case.
2. The specification of a data model for MIAPPE, to facilitate its implementation in various formats and enable its automatic validation.
3. The interoperability between MIAPPE and related external resources, namely ISA-Tools and the Breeding API.
4. The enrichment of MIAPPE with clear definitions and examples for all fields, to improve its accessibility to users.

In this document, we review MIAPPE’s data model specification and explain the changes motivated by the first three goals (those motivated by the last goal are self-explanatory).
Overall, we believe that this MIAPPE revision will enhance its accessibility and usability, leading to its adoption by a wider community.

# MIAPPE v1.1 proposal for assessment
An extended set of recommendations for metadata and phenotypic data annotation was developed by the EXCELERATE work
package 7 team based on the publicly available version of MIAPPE (Ćwiek-Kupczyńska et al. 2016; DOI: 10.1186/s13007-016-0144-
4), as presented below. Some attributes have been edited and new ones added. The main lines of these proposed changes are
summarized below:
- Study metadata section : Attributes, definitions and mandatory status aligned on DOI metadata instead on “Default ISA-Tab
list for terms and mandatory fields”
- Biosource section: here we aligned further to MCPD, while being non-redundant with details that would be stored in
genebanks catalogs. We also aimed at being more generic and include some forest trees specificities for the identification of
the plant material.
- Environment sections: most attributes are not mandatory anymore to keep generic across different types of experiments
- Experimental design section: the section has been revised in depth to take into account when relevant ISA-tab vocabulary but
also Important description elements for field experiments of crops and forest trees, and for greenhouse experiments
- Sample collection section: samples attributes have all been grouped here and aligned with BioSample specifications that also
have been revised in parallel. The objective is to improve the interoperability between phenotyping and genomic/genotyping
experiment made on the same accessions/varieties.
- Observed Variables section: this section has been completely revised to be aligned with the Crop Ontology’s specifications.
More details of the changes he details can be seen in [column H of the working document from which ths proposal was prepared](https://docs.google.com/spreadsheets/d/1SiUVvauhdNSpAfHgds-vQpjAXYs34lFD8wSOZdkyCgY/edit#gid=98983789)

Definition for Attributes in each of the 10 sections (Study metadata, Timing and location of study, Biosource, Environment-growth facility, Environment-rooting conditions, Environment-nutrients, Treatments, Experimental design, Sample collection, processing and management, Observed variables) were included, as well as examples and ontologies/data types that should be used to describe the attributes. Some general guidelines are also provided below for a consistent use of the standard.

**Conventions for the Sample MIAPPE metadata**

1. If there is a "Derived Material" attribute, it should be unique in each sample of the investigation
2. If there is not unique value or non-existent values for "Derived Material", then the "Material Source" should be unique per sample
in the investigation UNLESS in the investigation there are time series
3. For trees: if there is value for either latitude or longitude there should be value for both.
4. For trees: if there is value for altitude there should be value for all three: latitude, longitude and altitude.
5. for the definition of the ontologies, the FULL URL of the term is expected
6. "Material Source" and "Derived Material" cannot have the same value in 1 sample
7. The "Environment: XXX" sections should describe the environmental parameters that are measured but are not modified as an
experimental factor
8. The “Treatment” section should describe a plant experimental condition (EO:0007359) or set of conditions describing the
application of an abiotic (EO:0007191) or biotic plant treatment (EO:0007357) or the combinatorial application thereof. The treatment (or Factor) is declared and described at the study level (e.g. Experimental field X) and varies in the different assays of the study (e.g. different plots or plants in the experimental field).

# MIAPPE Data Model

**Figure 1** – Schematic representation of MIAPPE’s data model specification.
![MIAPPE-data-model](MIAPPE-data-model.png?raw=true "MIAPPE-data-model")

MIAPPE’s data model specification, illustrated in Figure 1, was heavily influenced by the ISA data model, as interoperability with the ISA-Tools was one of our main goals. Of its four central objects (represented in orange in the schema), three have a direct correspondence with ISA: Investigation and Study are homonymous in both models, and Observed Variable corresponds to ISA Assay. The fourth, Observation Unit, is a central object in the data model of the Breeding API, and together with Observed Variable, is key to enable interoperability with the latter.

The objects Investigation and Study merit further attention as they were not explicitly defined in MIAPPE 1.0. Only a section devoted to general metadata was included therein, with a reference to ISA-Tab, but with no formal separation between these two objects. If we want to support ISA-Tab as a submission format, then Investigation and Study must be explicit objects in the MIAPPE specification or we risk users not understanding the separation between them and/or leaving one of them unfilled. The proposed data model is that publication and submission metadata be listed at the Investigation level only, and that links to data files, timing and location data be listed at the Study level only, with the restriction that a Study must have a single location.

# Explanation of Proposed Changes

The changes made in the proposed version of MIAPPE can be roughly divided into four categories: terminological changes, organisational changes, scope extensions, and modelling simplifications.
Terminological Changes
These changes were aimed at making field labels less ambiguous and/or promoting interoperability with external resources. They were the following: 

1.	Renaming of Biosource to Biological Material which was deemed more intuitive 
2.	Renaming of Treatment to Factor
This matches ISA, which uses Factor rather than Treatment to refer to this concept. The Breeding API uses Treatment to refer to the same generic concept, but each Treatment is described by a Factor and a Modality, which now correspond to MIAPPE Factor Type and Factor Value respectively. Thus, this change promotes interoperability with both ISA and the Breeding API. Furthermore, it avoids the ambiguity of the name “treatment”, which may be used in a broader sense to refer to any cultivation practices. A Factor is expected to be a controlled variable, the effect of which is the object of the study.

**Organisational Changes**

These changes were motivated by the need to convey the data model intuitively, even at the checklist level. For this to be possible, each section in the MIAPPE checklist should correspond to data model object or pair of objects (in the case of paired objects like Environment Parameter and Parameter Value). Conversely, each data model object for which we need to list multiple attributes should have its own section in the MIAPPE checklist.  The changes falling under this category were the following:

3. Creation of new sections: Investigation, Study, and Observation Unit
4. Abolishment of old sections with no representation in the data model, and redistribution of their metadata fields into the new sections:
    1. General Metadata: fields split between Investigation and Study; some duplicated in both (e.g., Title and Description)
    2. Timing and Location: fields moved to Study section
    3. Experimental Design: fields split between Study and Observation Unit
5. Grouping unique and mandatory Environment fields under the Study, namely: Type of growth facility and Cultural practices

**Scope Extensions**

These changes were motivated by the need to accommodate the woody plant use-case or capture more types of information. They were the following: 

6.	Addition of a License field under Investigation for FAIR compliance**
7.	Addition of Person section to describe parties involved in the investigation or any of its studies, including information about their roles and affiliations.**
8.	Addition of fields for listing Data Files and providing their version at the Study level**
Data files were not listed in MIAPPE 1.0 and the version is necessary for FAIR compliance.
9.	Extension of the Biological Material section to accommodate woody plants:**
  1.	Addition of geographical coordinates as a means of uniquely identifying woody plants in the field, instead of accession.
  2.	Renaming of Seed Source to Material Source due to the fact that woody plants (and not only) may not be necessarily propagated by means of seeds.
  3.	Replacement of the fields Pretreatments and Conservation conditions, which pertained to Seed preparation, by the more generic field Biological material preprocessing which englobes both aspects (preprocessing was chosen instead of pretreatment to avoid the ambiguity of the name “treatment”).
10.	Addition of Event section to describe discrete occurrences that happened during the experiment, and that must be associated with a date. These can be natural or artificial interventions, can encompass elements of planning (e.g. planting) including parts of Factors (e.g. watering), or sporadic events (e.g. rain). They may apply globally, to the whole study, or locally, to specific observation units.
11. Generalisation of the Observation Unit description
Since the layout of experiments may vary greatly, users should be able to define their layout instead of having to provide specific levels. This was enabled by the paired fields Spatial distribution: type and Spatial distribution: value, where users can provide specific coordinates under the logic of key-value pairs (e.g. block: 5; plot: 1; latitude: +2.341). In combination with the Observation unit levels field under Study, this enables the description of hierarchies.

**Modelling Simplifications**

These changes were aimed at simplifying the checklist by avoiding exhaustive lists of categories for aspects such as Factors or Environment parameters. Given the broad scope of MIAPPE, the categories that make sense in one experimental setting may not make sense in another, so it is impossible to enforce mandatory fields of these types. Furthermore, it would be virtually impossible to be fully exhaustive, and thus it is best to give the users some flexibility. As such, we opted for a streamlined common representation under which any category from an exhaustive list can be provided by the users when adequate in their particular experiments. The aspects for which this type of simplification was made were:

12.	Factor, which is described using three fields: Factor type (or name), a Factor description (elaborating on the specific applications and details in free text), and Factor values (a list of all different modalities for this specific factor). The list of possible factor types is to be supplied as an appendix to the MIAPPE checklist.
