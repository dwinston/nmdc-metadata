
# Type: attribute value


The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and the structured value

URI: [nmdc:AttributeValue](https://microbiomedata/meta/AttributeValue)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AttributeValue&#124;has_raw_value:string%20%3F]^-\[UrlValue],%20\[AttributeValue]^-\[TimestampValue],%20\[AttributeValue]^-\[TextValue],%20\[AttributeValue]^-\[QuantityValue],%20\[AttributeValue]^-\[IntegerValue],%20\[AttributeValue]^-\[GeolocationValue],%20\[AttributeValue]^-\[ControlledTermValue],%20\[AttributeValue]^-\[BooleanValue])

## Children

 * [BooleanValue](BooleanValue.md) - A value that is a boolean
 * [ControlledTermValue](ControlledTermValue.md) - A controlled term or class from an ontology
 * [GeolocationValue](GeolocationValue.md) - A normalized value for a location on the earth's surface
 * [IntegerValue](IntegerValue.md) - A value that is an integer
 * [QuantityValue](QuantityValue.md) - A simple quantity, e.g. 2cm
 * [TextValue](TextValue.md) - A basic string value
 * [TimestampValue](TimestampValue.md) - A value that is a timestamp. The range should be ISO-8601
 * [UrlValue](UrlValue.md) - A value that is a string that conforms to URL syntax

## Referenced by class


## Attributes


### Own

 * [has raw value](has_raw_value.md)  <sub>OPT</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)

### Domain for slot:

 * [has raw value](has_raw_value.md)  <sub>OPT</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)