---
parent: Classes
title: nmdc:WorkflowExecutionActivity
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: WorkflowExecutionActivity


Represents an instance of an execution of a particular workflow

URI: [nmdc:WorkflowExecutionActivity](https://microbiomedata/meta/WorkflowExecutionActivity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DataObject]++-%20was%20generated%20by%200..1%3E[WorkflowExecutionActivity%7Cexecution_resource:string%20%3F;git_url:string%20%3F;has_input:string%20%2A;has_output:string%20%2A;activity_id(i):string;started_at_time(i):string%20%3F;ended_at_time(i):string%20%3F;used(i):string%20%3F],[WorkflowExecutionActivity]%5E-[ReadQCAnalysisActivity],[WorkflowExecutionActivity]%5E-[MetaproteomicsAnalysisActivity],[WorkflowExecutionActivity]%5E-[MetagenomeAssembly],[WorkflowExecutionActivity]%5E-[MetagenomeAnnotationActivity],[WorkflowExecutionActivity]%5E-[MetabolomicsAnalysisActivity],[Activity]%5E-[WorkflowExecutionActivity],[ReadQCAnalysisActivity],[MetaproteomicsAnalysisActivity],[MetagenomeAssembly],[MetagenomeAnnotationActivity],[MetabolomicsAnalysisActivity],[DataObject],[Agent],[Activity])

---


## Parents

 *  is_a: [Activity](Activity.md) - a provence-generating activity

## Children

 * [MetabolomicsAnalysisActivity](MetabolomicsAnalysisActivity.md)
 * [MetagenomeAnnotationActivity](MetagenomeAnnotationActivity.md)
 * [MetagenomeAssembly](MetagenomeAssembly.md)
 * [MetaproteomicsAnalysisActivity](MetaproteomicsAnalysisActivity.md)
 * [ReadQCAnalysisActivity](ReadQCAnalysisActivity.md)

## Referenced by class

 *  **[DataObject](DataObject.md)** *[data object➞was generated by](data_object_was_generated_by.md)*  <sub>OPT</sub>  **[WorkflowExecutionActivity](WorkflowExecutionActivity.md)**

## Attributes


### Own

 * [execution resource](execution_resource.md)  <sub>OPT</sub>
    * Description: Example: NERSC-Cori
    * range: [String](types/String.md)
 * [git url](git_url.md)  <sub>OPT</sub>
    * Description: Example: https://github.com/microbiomedata/mg_annotation/releases/tag/0.1
    * range: [String](types/String.md)

### Inherited from activity:

 * [activity id](activity_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [started at time](started_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [ended at time](ended_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [was associated with](was_associated_with.md)  <sub>OPT</sub>
    * range: [Agent](Agent.md)
 * [used](used.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from agent:

 * [acted on behalf of](acted_on_behalf_of.md)  <sub>OPT</sub>
    * range: [Agent](Agent.md)
 * [was informed by](was_informed_by.md)  <sub>OPT</sub>
    * range: [Activity](Activity.md)

### Inherited from biosample processing:

 * [biosample processing➞has input](biosample_processing_has_input.md)  <sub>0..*</sub>
    * range: [Biosample](Biosample.md)

### Inherited from omics processing:

 * [omics processing➞part of](omics_processing_part_of.md)  <sub>0..*</sub>
    * range: [Study](Study.md)
 * [omics processing➞has output](omics_processing_has_output.md)  <sub>0..*</sub>
    * range: [DataObject](DataObject.md)
 * [omics type](omics_type.md)  <sub>OPT</sub>
    * Description: The type of omics data
    * range: [ControlledTermValue](ControlledTermValue.md)
    * Example: metatranscriptome None
    * Example: metagenome None
 * [omics processing➞id](omics_processing_id.md)  <sub>REQ</sub>
    * Description: The primary identifier for the omics processing. E.g. GOLD:GpNNNN
    * range: [String](types/String.md)
 * [omics processing➞name](omics_processing_name.md)  <sub>OPT</sub>
    * Description: A human readable name or description of the omics processing.
    * range: [String](types/String.md)
 * [omics processing➞alternate identifiers](omics_processing_alternate_identifiers.md)  <sub>0..*</sub>
    * Description: The same omics processing may have distinct identifiers in different databases (e.g. GOLD and EMSL, as well as NCBI)
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | workflow subset |
