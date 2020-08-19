---
parent: Classes
title: nmdc:OntologyClass
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: OntologyClass




URI: [nmdc:OntologyClass](https://microbiomedata/meta/OntologyClass)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ControlledTermValue]++-%20term%200..1%3E[OntologyClass%7Cid(i):string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20%2A],[OntologyClass]%5E-[EnvironmentalMaterialTerm],[NamedThing]%5E-[OntologyClass],[NamedThing],[EnvironmentalMaterialTerm],[ControlledTermValue])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [EnvironmentalMaterialTerm](EnvironmentalMaterialTerm.md)

## Referenced by class

 *  **[ControlledTermValue](ControlledTermValue.md)** *[term](term.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)
