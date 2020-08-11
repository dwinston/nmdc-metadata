
# Type: person


represents a person, such as a researcher

URI: [nmdc:Person](https://microbiomedata/meta/Person)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing]^-[Person&#124;id:string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20*],[NamedThing])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class


## Attributes


### Own

 * [person➞id](person_id.md)  <sub>REQ</sub>
    * Description: Should be an ORCID. Specify in CURIE format. E.g ORCID:0000-1111-...
    * range: [String](types/String.md)

### Inherited from named thing:

 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | not yet in use |

