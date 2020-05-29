
# Type: named thing


a databased entity or concept/class

URI: [nmdc:NamedThing](https://microbiomedata/meta/NamedThing)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing&#124;id:string%20%3F;name:string%20%3F;description:string%20%3F;alternate_identifiers:string%20*]^-\[Study],%20\[NamedThing]^-\[Person],%20\[NamedThing]^-\[OntologyClass],%20\[NamedThing]^-\[DataObject],%20\[NamedThing]^-\[BiosampleProcessing],%20\[NamedThing]^-\[Biosample])

## Children

 * [Biosample](Biosample.md) - A material sample. It may be environmental (encompassing many organisms) or isolate or tissue.   An environmental sample containing genetic material from multiple individuals is commonly referred to as a biosample.  
 * [BiosampleProcessing](BiosampleProcessing.md) - A process that takes one or more biosamples as inputs and generates one or as outputs. Examples of outputs include samples cultivated from another sample or data objects created by instruments runs.
 * [DataObject](DataObject.md) - An object that primarily consists of symbols that represent information.   Files, records, and omics data are examples of data objects. 
 * [OntologyClass](OntologyClass.md)
 * [Person](Person.md) - represents a person, such as a researcher
 * [Study](Study.md) - A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying projects.  

## Referenced by class


## Attributes


### Own

 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
 * [id](id.md)  <sub>OPT</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)

### Domain for slot:

 * [16s_recover](16s_recover.md)  <sub>OPT</sub>
    * Description: Can a 16S gene be recovered from the submitted SAG or MAG?
    * range: [TextValue](TextValue.md)
 * [16s_recover_software](16s_recover_software.md)  <sub>OPT</sub>
    * Description: Tools used for 16S rRNA gene extraction
    * range: [TextValue](TextValue.md)
 * [adapters](adapters.md)  <sub>OPT</sub>
    * Description: Adapters provide priming sequences for both amplification and sequencing of the sample-library fragments. Both adapters should be reported; in uppercase letters
    * range: [TextValue](TextValue.md)
 * [alt](alt.md)  <sub>OPT</sub>
    * Description: "Altitude is a term used to identify heights of objects such as airplanes, space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric layers and clouds. It is used to measure the height of an object which is above the earthbs surface. In this context, the altitude measurement is the vertical distance between the earth's surface above sea level and the sampled position in the air"
    * range: [QuantityValue](QuantityValue.md)
 * [annot](annot.md)  <sub>OPT</sub>
    * Description: "Tool used for annotation, or for cases where annotation was provided by a community jamboree or model organism database rather than by a specific submitter"
    * range: [TextValue](TextValue.md)
 * [assembly_name](assembly_name.md)  <sub>OPT</sub>
    * Description: Name/version of the assembly provided by the submitter that is used in the genome browsers and in the community
    * range: [TextValue](TextValue.md)
 * [assembly_qual](assembly_qual.md)  <sub>OPT</sub>
    * Description: "The assembly quality category is based on sets of criteria outlined for each assembly quality category. For MISAG/MIMAG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities with a consensus error rate equivalent to Q50 or better. High Quality Draft:Multiple fragments where gaps span repetitive regions. Presence of the 23S, 16S and 5S rRNA genes and at least 18 tRNAs. Medium Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Low Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Assembly statistics include, but are not limited to total assembly size, number of contigs, contig N50/L50, and maximum contig length. For MIUVIG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities, with extensive manual review and editing to annotate putative gene functions and transcriptional units. High-quality draft genome: One or multiple fragments, totaling 3 90% of the expected genome or replicon sequence or predicted complete. Genome fragment(s): One or multiple fragments, totalling < 90% of the expected genome or replicon sequence, or for which no genome size could be estimated"
    * range: [TextValue](TextValue.md)
 * [assembly_software](assembly_software.md)  <sub>OPT</sub>
    * Description: "Tool(s) used for assembly, including version number and parameters"
    * range: [TextValue](TextValue.md)
 * [attribute](attribute.md)  <sub>OPT</sub>
    * Description: A attribute of a biosample. Examples: depth, habitat, material. For NMDC, attributes SHOULD be mapped to terms within a MIxS template
    * range: [String](types/String.md)
 * [bin_param](bin_param.md)  <sub>OPT</sub>
    * Description: The parameters that have been applied during the extraction of genomes from metagenomic datasets
    * range: [TextValue](TextValue.md)
 * [bin_software](bin_software.md)  <sub>OPT</sub>
    * Description: Tool(s) used for the extraction of genomes from metagenomic datasets
    * range: [TextValue](TextValue.md)
 * [biotic_relationship](biotic_relationship.md)  <sub>OPT</sub>
    * Description: "Description of relationship(s) between the subject organism and other organism(s) it is associated with. E.g., parasite on species X; mutualist with species Y. The target organism is the subject of the relationship, and the other organism(s) is the object"
    * range: [TextValue](TextValue.md)
 * [chimera_check](chimera_check.md)  <sub>OPT</sub>
    * Description: "A chimeric sequence, or chimera for short, is a sequence comprised of two or more phylogenetically distinct parent sequences. Chimeras are usually PCR artifacts thought to occur when a prematurely terminated amplicon reanneals to a foreign DNA strand and is copied to completion in the following PCR cycles. The point at which the chimeric sequence changes from one parent to the next is called the breakpoint or conversion point "
    * range: [TextValue](TextValue.md)
 * [collection_date](collection_date.md)  <sub>OPT</sub>
    * Description: "The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant"
    * range: [TimestampValue](TimestampValue.md)
 * [compl_appr](compl_appr.md)  <sub>OPT</sub>
    * Description: "The approach used to determine the completeness of a given SAG or MAG, which would typically make use of a set of conserved marker genes or a closely related reference genome. For UViG completeness, include reference genome or group used, and contig feature suggesting a complete genome"
    * range: [TextValue](TextValue.md)
 * [compl_score](compl_score.md)  <sub>OPT</sub>
    * Description: "Completeness score is typically based on either the fraction of markers found as compared to a database or the percent of a genome found as compared to a closely related reference genome. High Quality Draft: >90%, Medium Quality Draft: >50%, and Low Quality Draft: < 50% should have the indicated completeness scores"
    * range: [TextValue](TextValue.md)
 * [compl_software](compl_software.md)  <sub>OPT</sub>
    * Description: "Tools used for completion estimate, i.e. checkm, anvi'o, busco"
    * range: [TextValue](TextValue.md)
 * [contam_score](contam_score.md)  <sub>OPT</sub>
    * Description: "The contamination score is based on the fraction of single-copy genes that are observed more than once in a query genome. The following scores are acceptable for; High Quality Draft: < 5%, Medium Quality Draft: < 10%, Low Quality Draft: < 10%. Contamination must be below 5% for a SAG or MAG to be deposited into any of the public databases"
    * range: [TextValue](TextValue.md)
 * [contam_screen_input](contam_screen_input.md)  <sub>OPT</sub>
    * Description: The type of sequence data used as input
    * range: [TextValue](TextValue.md)
 * [contam_screen_param](contam_screen_param.md)  <sub>OPT</sub>
    * Description: "Specific parameters used in the decontamination sofware, such as reference database, coverage, and kmers. Combinations of these parameters may also be used, i.e. kmer and coverage, or reference database and kmer"
    * range: [TextValue](TextValue.md)
 * [decontam_software](decontam_software.md)  <sub>OPT</sub>
    * Description: Tool(s) used in contamination screening
    * range: [TextValue](TextValue.md)
 * [depth](depth.md)  <sub>OPT</sub>
    * Description: Please refer to the definitions of depth in the environmental packages
    * range: [TextValue](TextValue.md)
 * [detec_type](detec_type.md)  <sub>OPT</sub>
    * Description: Type of UViG detection
    * range: [TextValue](TextValue.md)
 * [ecosystem](ecosystem.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [ecosystem_category](ecosystem_category.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [ecosystem_subtype](ecosystem_subtype.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [ecosystem_type](ecosystem_type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [elev](elev.md)  <sub>OPT</sub>
    * Description: "Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface, while altitude is used for points above the surface, such as an aircraft in flight or a spacecraft in orbit"
    * range: [QuantityValue](QuantityValue.md)
 * [encoded_traits](encoded_traits.md)  <sub>OPT</sub>
    * Description: "Should include key traits like antibiotic resistance or xenobiotic degradation phenotypes for plasmids, converting genes for phage"
    * range: [TextValue](TextValue.md)
 * [env_broad_scale](env_broad_scale.md)  <sub>OPT</sub>
    * Description: "In this field, report which major environmental system your sample or specimen came from. The systems identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. were you in the desert or a rainforest?). We recommend using subclasses of ENVOUs biome class: http://purl.obolibrary.org/obo/ENVO_00000428. Format (one term): termLabel [termID], Format (multiple terms): termLabel [termID]|termLabel [termID]|termLabel [termID]. Example: Annotating a water sample from the photic zone in middle of the Atlantic Ocean, consider: oceanic epipelagic zone biome [ENVO:01000033]. Example: Annotating a sample from the Amazon rainforest consider: tropical moist broadleaf forest biome [ENVO:01000228]. If needed, request new terms on the ENVO tracker, identified here: http://www.obofoundry.org/ontology/envo.html"
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [env_local_scale](env_local_scale.md)  <sub>OPT</sub>
    * Description: "In this field, report the entity or entities which are in your sample or specimenUs local vicinity and which you believe have significant causal influences on your sample or specimen. Please use terms that are present in ENVO and which are of smaller spatial grain than your entry for env_broad_scale. Format (one term): termLabel [termID]; Format (multiple terms): termLabel [termID]|termLabel [termID]|termLabel [termID]. Example: Annotating a pooled sample taken from various vegetation layers in a forest consider: canopy [ENVO:00000047]|herb and fern layer [ENVO:01000337]|litter layer [ENVO:01000338]|understory [01000335]|shrub layer [ENVO:01000336]. If needed, request new terms on the ENVO tracker, identified here: http://www.obofoundry.org/ontology/envo.html"
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [env_medium](env_medium.md)  <sub>OPT</sub>
    * Description: "In this field, report which environmental material or materials (pipe separated) immediately surrounded your sample or specimen prior to sampling, using one or more subclasses of ENVOUs environmental material class: http://purl.obolibrary.org/obo/ENVO_00010483. Format (one term): termLabel [termID]; Format (multiple terms): termLabel [termID]|termLabel [termID]|termLabel [termID]. Example: Annotating a fish swimming in the upper 100 m of the Atlantic Ocean, consider: ocean water [ENVO:00002151]. Example: Annotating a duck on a pond consider: pond water [ENVO:00002228]|air ENVO_00002005. If needed, request new terms on the ENVO tracker, identified here: http://www.obofoundry.org/ontology/envo.html"
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [env_package](env_package.md)  <sub>OPT</sub>
    * Description: "MIxS extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported"
    * range: [TextValue](TextValue.md)
 * [estimated_size](estimated_size.md)  <sub>OPT</sub>
    * Description: The estimated size of the genome prior to sequencing. Of particular importance in the sequencing of (eukaryotic) genome which could remain in draft form for a long or unspecified period.
    * range: [TextValue](TextValue.md)
 * [experimental_factor](experimental_factor.md)  <sub>OPT</sub>
    * Description: "Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO; for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI"
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [extrachrom_elements](extrachrom_elements.md)  <sub>OPT</sub>
    * Description: Do plasmids exist of significant phenotypic consequence (e.g. ones that determine virulence or antibiotic resistance). Megaplasmids? Other plasmids (borrelia has 15+ plasmids)
    * range: [TextValue](TextValue.md)
 * [feat_pred](feat_pred.md)  <sub>OPT</sub>
    * Description: "Method used to predict UViGs features such as ORFs, integration site, etc."
    * range: [TextValue](TextValue.md)
 * [file_size](file_size.md)  <sub>OPT</sub>
    * Description: units should be bytes.. may be overkill to allow different units
    * range: [String](types/String.md)
 * [geo_loc_name](geo_loc_name.md)  <sub>OPT</sub>
    * Description: "The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (v 1.512) (http://purl.bioontology.org/ontology/GAZ)"
    * range: [TextValue](TextValue.md)
 * [gold_path_field](gold_path_field.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [has input](has_input.md)  <sub>0..*</sub>
    * Description: An input to a process.
    * range: [String](types/String.md)
 * [health_disease_stat](health_disease_stat.md)  <sub>OPT</sub>
    * Description: Health or disease status of specific host at time of collection
    * range: [TextValue](TextValue.md)
 * [host_pred_appr](host_pred_appr.md)  <sub>OPT</sub>
    * Description: Tool or approach used for host prediction
    * range: [TextValue](TextValue.md)
 * [host_pred_est_acc](host_pred_est_acc.md)  <sub>OPT</sub>
    * Description: "For each tool or approach used for host prediction, estimated false discovery rates should be included, either computed de novo or from the literature"
    * range: [TextValue](TextValue.md)
 * [host_spec_range](host_spec_range.md)  <sub>OPT</sub>
    * Description: The NCBI taxonomy identifier of the specific host if it is known
    * range: [TextValue](TextValue.md)
 * [investigation_type](investigation_type.md)  <sub>OPT</sub>
    * Description: "Nucleic Acid Sequence Report is the root element of all MIGS/MIMS compliant reports as standardized by Genomic Standards Consortium. This field is either eukaryote,bacteria,virus,plasmid,organelle, metagenome,mimarks-survey, mimarks-specimen, metatranscriptome, single amplified genome, metagenome-assembled genome, or uncultivated viral genome"
    * range: [TextValue](TextValue.md)
 * [isol_growth_condt](isol_growth_condt.md)  <sub>OPT</sub>
    * Description: "Publication reference in the form of pubmed ID (pmid), digital object identifier (doi) or url for isolation and growth condition specifications of the organism/material"
    * range: [TextValue](TextValue.md)
 * [lat_lon](lat_lon.md)  <sub>OPT</sub>
    * Description: The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in WGS84 system
    * range: [GeolocationValue](GeolocationValue.md)
 * [lib_layout](lib_layout.md)  <sub>OPT</sub>
    * Description: "Specify whether to expect single, paired, or other configuration of reads"
    * range: [TextValue](TextValue.md)
 * [lib_reads_seqd](lib_reads_seqd.md)  <sub>OPT</sub>
    * Description: Total number of clones sequenced from the library
    * range: [TextValue](TextValue.md)
 * [lib_screen](lib_screen.md)  <sub>OPT</sub>
    * Description: Specific enrichment or screening methods applied before and/or after creating libraries
    * range: [TextValue](TextValue.md)
 * [lib_size](lib_size.md)  <sub>OPT</sub>
    * Description: Total number of clones in the library prepared for the project
    * range: [TextValue](TextValue.md)
 * [lib_vector](lib_vector.md)  <sub>OPT</sub>
    * Description: Cloning vector type(s) used in construction of libraries
    * range: [TextValue](TextValue.md)
 * [mag_cov_software](mag_cov_software.md)  <sub>OPT</sub>
    * Description: Tool(s) used to determine the genome coverage if coverage is used as a binning parameter in the extraction of genomes from metagenomic datasets
    * range: [TextValue](TextValue.md)
 * [mid](mid.md)  <sub>OPT</sub>
    * Description: "Molecular barcodes, called Multiplex Identifiers (MIDs), that are used to specifically tag unique samples in a sequencing run. Sequence should be reported in uppercase letters"
    * range: [TextValue](TextValue.md)
 * [nucl_acid_amp](nucl_acid_amp.md)  <sub>OPT</sub>
    * Description: "A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the enzymatic amplification (PCR, TMA, NASBA) of specific nucleic acids"
    * range: [TextValue](TextValue.md)
 * [nucl_acid_ext](nucl_acid_ext.md)  <sub>OPT</sub>
    * Description: "A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the material separation to recover the nucleic acid fraction from a sample"
    * range: [TextValue](TextValue.md)
 * [num_replicons](num_replicons.md)  <sub>OPT</sub>
    * Description: "Reports the number of replicons in a nuclear genome of eukaryotes, in the genome of a bacterium or archaea or the number of segments in a segmented virus. Always applied to the haploid chromosome count of a eukaryote"
    * range: [TextValue](TextValue.md)
 * [number_contig](number_contig.md)  <sub>OPT</sub>
    * Description: "Total number of contigs in the cleaned/submitted assembly that makes up a given genome, SAG, MAG, or UViG"
    * range: [TextValue](TextValue.md)
 * [part of](part_of.md)  <sub>0..*</sub>
    * Description: Links a resource to another resource that either logically or physically includes it.
    * range: [String](types/String.md)
 * [pathogenicity](pathogenicity.md)  <sub>OPT</sub>
    * Description: To what is the entity pathogenic
    * range: [TextValue](TextValue.md)
 * [pcr_cond](pcr_cond.md)  <sub>OPT</sub>
    * Description: Description of reaction conditions and components of PCR in the form of  'initial denaturation:94degC_1.5min; annealing=...'
    * range: [TextValue](TextValue.md)
 * [pcr_primers](pcr_primers.md)  <sub>OPT</sub>
    * Description: "PCR primers that were used to amplify the sequence of the targeted gene, locus or subfragment. This field should contain all the primers used for a single PCR reaction if multiple forward or reverse primers are present in a single PCR reaction. The primer sequence should be reported in uppercase letters"
    * range: [TextValue](TextValue.md)
 * [ploidy](ploidy.md)  <sub>OPT</sub>
    * Description: "The ploidy level of the genome (e.g. allopolyploid, haploid, diploid, triploid, tetraploid). It has implications for the downstream study of duplicated gene and regions of the genomes (and perhaps for difficulties in assembly). For terms, please select terms listed under class ploidy (PATO:001374) of Phenotypic Quality Ontology (PATO), and for a browser of PATO (v 2018-03-27) please refer to http://purl.bioontology.org/ontology/PATO"
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [pred_genome_struc](pred_genome_struc.md)  <sub>OPT</sub>
    * Description: Expected structure of the viral genome
    * range: [TextValue](TextValue.md)
 * [pred_genome_type](pred_genome_type.md)  <sub>OPT</sub>
    * Description: Type of genome predicted for the UViG
    * range: [TextValue](TextValue.md)
 * [project_name](project_name.md)  <sub>OPT</sub>
    * Description: Name of the project within which the sequencing was organized
    * range: [TextValue](TextValue.md)
 * [propagation](propagation.md)  <sub>OPT</sub>
    * Description: "This field is specific to different taxa. For phages: lytic/lysogenic, for plasmids: incompatibility group, for eukaryotes: sexual/asexual (Note: there is the strong opinion to name phage propagation obligately lytic or temperate, therefore we also give this choice"
    * range: [TextValue](TextValue.md)
 * [reassembly_bin](reassembly_bin.md)  <sub>OPT</sub>
    * Description: Has an assembly been performed on a genome bin extracted from a metagenomic assembly?
    * range: [TextValue](TextValue.md)
 * [ref_biomaterial](ref_biomaterial.md)  <sub>OPT</sub>
    * Description: "Primary publication if isolated before genome publication; otherwise, primary genome report"
    * range: [TextValue](TextValue.md)
 * [ref_db](ref_db.md)  <sub>OPT</sub>
    * Description: "List of database(s) used for ORF annotation, along with version number and reference to website or publication"
    * range: [TextValue](TextValue.md)
 * [rel_to_oxygen](rel_to_oxygen.md)  <sub>OPT</sub>
    * Description: "Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic are valid descriptors for microbial environments"
    * range: [TextValue](TextValue.md)
 * [samp_collect_device](samp_collect_device.md)  <sub>OPT</sub>
    * Description: The method or device employed for collecting the sample
    * range: [TextValue](TextValue.md)
 * [samp_mat_process](samp_mat_process.md)  <sub>OPT</sub>
    * Description: "Any processing applied to the sample during or after retrieving the sample from environment. This field accepts OBI, for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI"
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [samp_size](samp_size.md)  <sub>OPT</sub>
    * Description: "Amount or size of sample (volume, mass or area) that was collected"
    * range: [QuantityValue](QuantityValue.md)
 * [seq_meth](seq_meth.md)  <sub>OPT</sub>
    * Description: "Sequencing method used; e.g. Sanger, pyrosequencing, ABI-solid"
    * range: [TextValue](TextValue.md)
 * [seq_quality_check](seq_quality_check.md)  <sub>OPT</sub>
    * Description: "Indicate if the sequence has been called by automatic systems (none) or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms). Applied only for sequences that are not submitted to SRA,ENA or DRA"
    * range: [TextValue](TextValue.md)
 * [sim_search_meth](sim_search_meth.md)  <sub>OPT</sub>
    * Description: "Tool used to compare ORFs with database, along with version and cutoffs used"
    * range: [TextValue](TextValue.md)
 * [single_cell_lysis_appr](single_cell_lysis_appr.md)  <sub>OPT</sub>
    * Description: Method used to free DNA from interior of the cell(s) or particle(s)
    * range: [TextValue](TextValue.md)
 * [single_cell_lysis_prot](single_cell_lysis_prot.md)  <sub>OPT</sub>
    * Description: Name of the kit or standard protocol used for cell(s) or particle(s) lysis
    * range: [TextValue](TextValue.md)
 * [size_frac](size_frac.md)  <sub>OPT</sub>
    * Description: Filtering pore size used in sample preparation
    * range: [QuantityValue](QuantityValue.md)
 * [sop](sop.md)  <sub>OPT</sub>
    * Description: "Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences"
    * range: [TextValue](TextValue.md)
 * [sort_tech](sort_tech.md)  <sub>OPT</sub>
    * Description: Method used to sort/isolate cells or particles of interest
    * range: [TextValue](TextValue.md)
 * [source_mat_id](source_mat_id.md)  <sub>OPT</sub>
    * Description: "A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2)."
    * range: [TextValue](TextValue.md)
 * [source_uvig](source_uvig.md)  <sub>OPT</sub>
    * Description: Type of dataset from which the UViG was obtained
    * range: [TextValue](TextValue.md)
 * [specific_ecosystem](specific_ecosystem.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [specific_host](specific_host.md)  <sub>OPT</sub>
    * Description: "If there is a host involved, please provide its taxid (or environmental if not actually isolated from the dead or alive host - i.e. a pathogen could be isolated from a swipe of a bench etc) and report whether it is a laboratory or natural host)"
    * range: [TextValue](TextValue.md)
 * [submitted_to_insdc](submitted_to_insdc.md)  <sub>OPT</sub>
    * Description: "Depending on the study (large-scale e.g. done with next generation sequencing technology, or small-scale) sequences have to be submitted to SRA (Sequence Read Archive), DRA (DDBJ Read Archive) or via the classical Webin/Sequin systems to Genbank, ENA and DDBJ. Although this field is mandatory, it is meant as a self-test field, therefore it is not necessary to include this field in contextual data submitted to databases"
    * range: [TextValue](TextValue.md)
 * [subspecf_gen_lin](subspecf_gen_lin.md)  <sub>OPT</sub>
    * Description: "This should provide further information about the genetic distinctness of the sequenced organism by recording additional information e.g. serovar, serotype, biotype, ecotype, or any relevant genetic typing schemes like Group I plasmid. It can also contain alternative taxonomic information. It should contain both the lineage name, and the lineage rank, i.e. biovar:abc123"
    * range: [TextValue](TextValue.md)
 * [target_gene](target_gene.md)  <sub>OPT</sub>
    * Description: Targeted gene or locus name for marker gene studies
    * range: [TextValue](TextValue.md)
 * [target_subfragment](target_subfragment.md)  <sub>OPT</sub>
    * Description: Name of subfragment of a gene or locus. Important to e.g. identify special regions on marker genes like V6 on 16S rRNA
    * range: [TextValue](TextValue.md)
 * [tax_class](tax_class.md)  <sub>OPT</sub>
    * Description: "Method used for taxonomic classification, along with reference database used, classification rank, and thresholds used to classify new genomes"
    * range: [TextValue](TextValue.md)
 * [tax_ident](tax_ident.md)  <sub>OPT</sub>
    * Description: The phylogenetic marker(s) used to assign an organism name to the SAG or MAG
    * range: [TextValue](TextValue.md)
 * [trna_ext_software](trna_ext_software.md)  <sub>OPT</sub>
    * Description: Tools used for tRNA identification
    * range: [TextValue](TextValue.md)
 * [trnas](trnas.md)  <sub>OPT</sub>
    * Description: The total number of tRNAs identified from the SAG or MAG
    * range: [TextValue](TextValue.md)
 * [trophic_level](trophic_level.md)  <sub>OPT</sub>
    * Description: Trophic levels are the feeding position in a food chain. Microbes can be a range of producers (e.g. chemolithotroph)
    * range: [TextValue](TextValue.md)
 * [url](url.md)  <sub>OPT</sub>
    * range: [TextValue](TextValue.md)
 * [vir_ident_software](vir_ident_software.md)  <sub>OPT</sub>
    * Description: "Tool(s) used for the identification of UViG as a viral genome, software or protocol name  including version number, parameters, and cutoffs used"
    * range: [TextValue](TextValue.md)
 * [virus_enrich_appr](virus_enrich_appr.md)  <sub>OPT</sub>
    * Description: "List of approaches used to enrich the sample for viruses, if any"
    * range: [TextValue](TextValue.md)
 * [votu_class_appr](votu_class_appr.md)  <sub>OPT</sub>
    * Description: "Cutoffs and approach used when clustering new UViGs in Rspecies-levelS vOTUs. Note that results from standard 95% ANI / 85% AF clustering should be provided alongside vOTUS defined from another set of thresholds, even if the latter are the ones primarily used during the analysis"
    * range: [TextValue](TextValue.md)
 * [votu_db](votu_db.md)  <sub>OPT</sub>
    * Description: "Reference database (i.e. sequences not generated as part of the current study) used to cluster new genomes in ""species-level"" vOTUs, if any"
    * range: [TextValue](TextValue.md)
 * [votu_seq_comp_appr](votu_seq_comp_appr.md)  <sub>OPT</sub>
    * Description: "Tool and thresholds used to compare sequences when computing ""species-level"" vOTUs"
    * range: [TextValue](TextValue.md)
 * [wga_amp_appr](wga_amp_appr.md)  <sub>OPT</sub>
    * Description: Method used to amplify genomic DNA in preparation for sequencing
    * range: [TextValue](TextValue.md)
 * [wga_amp_kit](wga_amp_kit.md)  <sub>OPT</sub>
    * Description: Kit used to amplify genomic DNA in preparation for sequencing
    * range: [TextValue](TextValue.md)