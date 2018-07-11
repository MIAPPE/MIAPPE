



### Request for comments on MIAPPE_Checklist-Data-Model-v1.1

All feedback on the current work in progress version are welcomed. You can find more information in [README-Request-for-comments](README-Request-for-comments.md).


# Overview

This document describes the MIAPPE Checklist and Data Model v1.1, a proposed revision and extension to the MIAPPE minimal information standard published by Krajewski et al. (doi:10.1093/jxb/erv271). The revision has been proposed by the plant research community within ELIXIR, a pan-European federation of life science resources, and has four primary goals:

1. The extension of MIAPPE’s scope to accommodate woody plants as an additional use-case.
1. The specification of a data model for MIAPPE, to facilitate its implementation in various formats and enable its automatic validation.
1. Compatibility of the MIAPPE logical standard with common frameworks for representing these data types, namely ISA-Tools and the Plant Breeding API (BrAPI).
1. The enrichment of MIAPPE, with the provision of clear definitions and examples for all fields.

In this document, we review the MIAPPE data model and explain the changes motivated by the first three goals (those motivated by the last goal are self-explanatory). The overall objective is to enhance the accessibility and usability of MIAPPE, leading to its adoption by a wider community.

# Organisation

- [MIAPPE_Checklist-Data-Model-v1.1.xlsx](MIAPPE_Checklist-Data-Model-v1.1.xlsx) and [MIAPPE_Checklist-Data-Model-v1.1.pdf](MIAPPE_Checklist-Data-Model-v1.1.pdf) : This is the reference document describing the Data Model and the Apendix wchich contain the checklist.
- MIAPPE_Checklist-Data-Model-v1.1.``*``.tsv : text version of the xlsx for versionning tracability

## __*IMPORTANT*__ : Versioning and commiting
All changes must be made in : MIAPPE_Checklist-Data-Model-v1.1.**xlsx**. Each time you commit save the two csv files from the xlsx.

# MIAPPE Data Model

**Figure 1** – Schematic representation of the MIAPPE data model.
![MIAPPE-data-model](MIAPPE_Checklist-Data-Model-v1.1.png?raw=true "MIAPPE-data-model")

The MIAPPE data model, illustrated in Figure 1, is heavily influenced by
the generic ISA (Implemenetation-Study-Assay) data model, as
interoperability with the tools from the ISA framework
(https://isa-tools.org) was one of our main goals. Of its four central
objects (represented in orange in the schema), three have a direct
correspondence with ISA objects: *Investigation* and *Study* are
homonymous in both models, and *Observed Variable* corresponds to the
ISA concept *Assay*. The fourth object type, *Observation Unit*, is a
central object in the data model of the Plant Breeding API (BrAPI), and
together with *Observed Variable*, is important to enable MIAPPE
compliant data to be served via BrAPI.

The objects *Investigation* and *Study* merit further attention as they
were not explicitly defined in MIAPPE 1.0, and the generic ISA
definitions are broad and flexible. A section devoted to general
metadata was included in the original checklist, but no formal
separation between these two objects was described, in spite of
references to ISA. If ISA-Tab is to be used as a format for data
exchange or database submission, then *Investigation* and *Study* must
be explicit objects in the MIAPPE specification, leading to their
inconsistent use. The practice we propose here is that publication and
submission metadata be listed at the *Investigation* level only, and
that links to data files, timing and location data be listed at the
*Study* level only, with the additional restriction that a *Study* must
have a single location.


# Explanation of Proposed Changes

The changes made in the proposed version of MIAPPE can be roughly divided into four categories: terminological changes, organisational changes, scope extensions, and modelling simplifications.

## Terminological Changes

These changes were aimed at making field labels less ambiguous and/or promoting interoperability with external resources. They were the following: 

1.  Renaming of *Biosource* to *Biological Material* which was deemed
    more intuitive

2.  Renaming of *Treatment* to *Factor*\
    This matches the terminology of ISA, which uses *Factor* rather than
    *Treatment* to refer to this concept. The Breeding API uses
    *Treatment* to refer to the same generic concept, but each
    *Treatment* is described by a *Factor* and a *Modality*, which now
    correspond to MIAPPE *Factor* *Type* and *Factor Value*
    respectively. Thus, this change promotes interoperability with both
    ISA and the Breeding API. Furthermore, it avoids the ambiguity of
    the name "treatment", which may be used in a broader sense to refer
    to any cultivation practices. A *Factor* is expected to be a
    controlled variable, the effect of which is the object of the study.

## Organisational Changes

These changes were motivated by the need to convey the data model intuitively, even implicitly in the checklist of required fields. For this to be possible, each section in the MIAPPE checklist should correspond to an object (or pair of objects, in the case of paired objects like *Environment Parameter* and *Parameter Value*) in the MIAPPE data model. Conversely, where multiple attributes of a single data object appear on the checklist, for clarity these should be listed in their own section. The changes falling under this category were the following:

3.  Creation of new sections: *Investigation*, *Study*, and *Observation
    Unit*

4.  Abolition of sections with no representation in the data model, and
    redistribution of their metadata fields into the new sections:

    a.  *General Metadata* -- fields split between *Investigation* and
        *Study*; some duplicated in both (e.g., *Title* and
        *Description*)

    b.  *Timing and Location* -- fields moved to *Study* section

    c.  *Experimental Design* -- fields split between *Study* and
        *Observation Unit*

5.  Grouping unique and mandatory *Environment* fields under the
    *Study*, namely: *Type of growth facility* and *Cultural practices*

## Scope Extensions

These changes were motivated by the need to accommodate the woody plant use-case or capture additional types of information. They were the following: 

6.  Addition of a *License* field under *Investigation* for FAIR
    compliance

7.  Addition of *Person* section to describe parties involved in the
    investigation or any of its studies, including information about
    their roles and affiliations.

8.  Addition of fields for listing *Data Files* and providing their
    version at the *Study* level\
    Data files were not listed in MIAPPE 1.0 and the version is
    necessary for FAIR compliance.

9.  Extension of the *Biological Material* section to accommodate woody
    plants:

    a.  Addition of geographical coordinates as a means of uniquely
        identifying woody plants in the field, as an alternative to
        accession numbers

    b.  Renaming of *Seed Source* to *Material Source* due to the fact
        that woody plants (and other types of plants also) may not be
        necessarily propagated by means of seeds.

    c.  Replacement of the fields *Pretreatments* and *Conservation
        conditions*, which pertained to *Seed preparation*, by the more
        generic field *Biological material preprocessing* which englobes
        both aspects. *Preprocessing* has been chosen instead of
        *pretreatment* to avoid the ambiguity of the name "treatment",
        as discussed above.

10. Addition of *Event* section to describe discrete occurrences that
    happened during the experiment, and that must be associated with a
    date. These can be natural or artificial interventions, can
    encompass elements of planning (e.g. planting) including parts of
    *Factors* (e.g. watering), or sporadic events (e.g. rain). They may
    apply globally, to the whole study, or locally, to specific
    observation units.

11. Generalisation of the description of *Observation Unit*.\
    Since the layout of experiments may vary greatly, users should be
    able to define their layout instead of having to provide specific
    levels. This has beenenabled by introducing the paired fields
    *Spatial distribution: type* and *Spatial distribution: value*,
    where users can provide specific coordinates as key-value pairs
    (e.g. block: 5; plot: 1; latitude: +2.341). In combination with the
    *Observation Unit levels* field under *Study*, this enables the
    description of hierarchies.

## Modelling Simplifications

These changes were aimed at simplifying the checklist by avoiding exhaustive lists of categories for aspects such as *Factors* or *Environment* parameters. Given the broad scope of MIAPPE, the categories that make sense in one experimental setting may not make sense in another, so it is impossible to enforce mandatory fields of these types. Furthermore, it would be virtually impossible to be fully exhaustive, and thus it is best to give the users some flexibility. As such, we opted for a streamlined common representation under which any category from an exhaustive list can be provided by the users when appropriate in their particular experiments. The aspects for which this type of simplification was made were:

12. *Factor*, which is described using three fields: *Factor type* (or
    name), a *Factor description* (elaborating on the specific
    applications and details in free text), and *Factor values* (a list
    of all different modalities for this specific factor). The list of
    possible factor types is to be supplied as an appendix to the MIAPPE
    checklist.

13. *Environment*, which is described using two fields: *Environment
    parameter name* and *Environment parameter value*. This section
    supports the description of environmental conditions that were
    constant throughout the *Study*. Environment parameters that were
    actively measured during the experiment should be recorded as
    *Observed variables*. As in the case of *Factors*, a list of
    possible *Environment parameters* is to be supplied as an appendix
    to the MIAPPE checklist in order to guide users.

14. *Samples*, in which a number of fields describing sample
    conservation conditions (e.g. salinity, oxygenation, storage
    temperature) have been condensed into a single, free-text field,
    *Sample description*.
