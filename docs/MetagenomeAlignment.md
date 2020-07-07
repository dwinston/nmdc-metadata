
# Type: metagenome alignment




URI: [nmdc:MetagenomeAlignment](https://microbiomedata/meta/MetagenomeAlignment)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Agent]<was%20associated%20with(i)%200..1-++[MetagenomeAlignment&#124;num_aligned_reads:string%20%3F;execution_resource(i):string%20%3F;git_url(i):string%20%3F;has_input(i):string%20*;activity_id(i):string;started_at_time(i):string%20%3F;ended_at_time(i):string%20%3F;used(i):string%20%3F],%20[Activity]<was%20informed%20by(i)%200..1-%20[MetagenomeAlignment],%20[WorkflowExecutionActivity]^-[MetagenomeAlignment])

## Parents

 *  is_a: [WorkflowExecutionActivity](WorkflowExecutionActivity.md) - Represents an instance of an execution of a particular workflow

## Attributes


### Own

 * [num_aligned_reads](num_aligned_reads.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from activity:

 * [activity id](activity_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
    * inherited from: None
 * [started at time](started_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: None
 * [ended at time](ended_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: None
 * [was associated with](was_associated_with.md)  <sub>OPT</sub>
    * range: [Agent](Agent.md)
    * inherited from: None
 * [used](used.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: [Activity](Activity.md)

### Inherited from agent:

 * [acted on behalf of](acted_on_behalf_of.md)  <sub>OPT</sub>
    * range: [Agent](Agent.md)
    * inherited from: None
 * [was informed by](was_informed_by.md)  <sub>OPT</sub>
    * range: [Activity](Activity.md)
    * inherited from: None

### Inherited from biosample processing:

 * [biosample processing➞has input](biosample_processing_has_input.md)  <sub>0..*</sub>
    * range: [Biosample](Biosample.md)
    * inherited from: [BiosampleProcessing](BiosampleProcessing.md)

### Inherited from workflow execution activity:

 * [execution resource](execution_resource.md)  <sub>OPT</sub>
    * Description: Example: NERSC-Cori
    * range: [String](types/String.md)
    * inherited from: None
 * [git url](git_url.md)  <sub>OPT</sub>
    * Description: Example: https://github.com/microbiomedata/mg_annotation/releases/tag/0.1
    * range: [String](types/String.md)
    * inherited from: None
