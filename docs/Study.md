
# Type: study


A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying projects.

URI: [nmdc:Study](https://microbiomedata/meta/Study)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AttributeValue]<doi%200..1-++[Study&#124;id:string;name:string%20%3F;alternate_identifiers:string%20*;description(i):string%20%3F],%20[PersonValue]<principal%20investigator%200..1-++[Study],%20[AttributeValue]<specific_ecosystem%200..1-++[Study],%20[AttributeValue]<ecosystem_subtype%200..1-++[Study],%20[AttributeValue]<ecosystem_type%200..1-++[Study],%20[AttributeValue]<ecosystem_category%200..1-++[Study],%20[AttributeValue]<ecosystem%200..1-++[Study],%20[OmicsProcessing]-%20part%20of%200..*>[Study],%20[Database]++-%20study%20set%200..*>[Study],%20[NamedThing]^-[Study])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[OmicsProcessing](OmicsProcessing.md)** *[omics processing➞part of](omics_processing_part_of.md)*  <sub>0..*</sub>  **[Study](Study.md)**
 *  **[Database](Database.md)** *[study set](study_set.md)*  <sub>0..*</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [doi](doi.md)  <sub>OPT</sub>
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem](ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem_category](ecosystem_category.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem_subtype](ecosystem_subtype.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem_type](ecosystem_type.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [principal investigator](principal_investigator.md)  <sub>OPT</sub>
    * Description: represents the PI
    * range: [PersonValue](PersonValue.md)
 * [specific_ecosystem](specific_ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [study➞alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [study➞id](study_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [study➞name](study_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * inherited from: None
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)
    * inherited from: None
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
    * inherited from: None
 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)
    * inherited from: None

### Domain for slot:

 * [study➞alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [study➞id](study_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [study➞name](study_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | proposal |
|  | | research proposal |
|  | | research study |
|  | | investigation |

