
# Type: omics processing


The methods and processes used to generate omics data from a biosample or organism.

URI: [nmdc:OmicsProcessing](https://microbiomedata/meta/OmicsProcessing)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Study],[ControlledTermValue]<omics%20type%200..1-++[OmicsProcessing&#124;id:string;name:string%20%3F;alternate_identifiers:string%20*;description(i):string%20%3F],[DataObject]<has%20output%200..*-%20[OmicsProcessing],[Study]<part%20of%200..*-%20[OmicsProcessing],[Database]++-%20omics%20processing%20set%200..*>[OmicsProcessing],[BiosampleProcessing]^-[OmicsProcessing],[Database],[DataObject],[ControlledTermValue],[BiosampleProcessing],[Biosample])

## Parents

 *  is_a: [BiosampleProcessing](BiosampleProcessing.md) - A process that takes one or more biosamples as inputs and generates one or as outputs. Examples of outputs include samples cultivated from another sample or data objects created by instruments runs.

## Referenced by class

 *  **[Database](Database.md)** *[omics processing set](omics_processing_set.md)*  <sub>0..*</sub>  **[OmicsProcessing](OmicsProcessing.md)**

## Attributes


### Own

 * [omics processing➞alternate identifiers](omics_processing_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [omics processing➞has output](omics_processing_has_output.md)  <sub>0..*</sub>
    * range: [DataObject](DataObject.md)
 * [omics processing➞id](omics_processing_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [omics processing➞name](omics_processing_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [omics processing➞part of](omics_processing_part_of.md)  <sub>0..*</sub>
    * range: [Study](Study.md)
 * [omics type](omics_type.md)  <sub>OPT</sub>
    * Description: The type of omics data
    * range: [ControlledTermValue](ControlledTermValue.md)
    * Example: metatranscriptome None
    * Example: metagenome None

### Inherited from biosample processing:

 * [biosample processing➞has input](biosample_processing_has_input.md)  <sub>0..*</sub>
    * range: [Biosample](Biosample.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | The IDs for objects coming from GOLD will have prefixes gold:GpNNNN |

