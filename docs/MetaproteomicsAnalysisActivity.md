
# Type: metaproteomics analysis activity




URI: [nmdc:MetaproteomicsAnalysisActivity](https://microbiomedata/meta/MetaproteomicsAnalysisActivity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowExecutionActivity],[WorkflowExecutionActivity]^-[MetaproteomicsAnalysisActivity&#124;execution_resource(i):string%20%3F;git_url(i):string%20%3F;has_input(i):string%20*;has_output(i):string%20*;activity_id(i):string;started_at_time(i):string%20%3F;ended_at_time(i):string%20%3F;used(i):string%20%3F],[Agent],[Activity])

## Parents

 *  is_a: [WorkflowExecutionActivity](WorkflowExecutionActivity.md) - Represents an instance of an execution of a particular workflow

## Attributes


### Inherited from workflow execution activity:

 * [activity id](activity_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [ended at time](ended_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [execution resource](execution_resource.md)  <sub>OPT</sub>
    * Description: Example: NERSC-Cori
    * range: [String](types/String.md)
 * [git url](git_url.md)  <sub>OPT</sub>
    * Description: Example: https://github.com/microbiomedata/mg_annotation/releases/tag/0.1
    * range: [String](types/String.md)
 * [has input](has_input.md)  <sub>0..*</sub>
    * Description: An input to a process.
    * range: [String](types/String.md)
 * [has output](has_output.md)  <sub>0..*</sub>
    * Description: An output biosample to a processing step
    * range: [String](types/String.md)
 * [started at time](started_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [used](used.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [was associated with](was_associated_with.md)  <sub>OPT</sub>
    * range: [Agent](Agent.md)
 * [was informed by](was_informed_by.md)  <sub>OPT</sub>
    * range: [Activity](Activity.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | workflow subset |

