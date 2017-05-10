plover_dict_converter
=====================

Utility scripts to convert between RTF/CRE and Plover JSON dictionary files, and to merge multiple Plover JSON dictionaries into one.

**Note: Plover already supports reading RTF natively, so you no longer need this script unless for some reason you want to convert your RTF dictionaries to JSON, for example the easier readability.**

This script relies on [PLY](http://www.dabeaz.com/ply/) → `pip install ply`

## Converting RTF/CRE to JSON

The script is invoked as:

`python convert_rtfcre_to_json_dict.py input.rtf > output_dict.json 2> report.txt`

Make sure to read the report.

## Merging multiple JSON dictionaries

To merge multiple plover dictionaries into one, use the merge script. This will produce a dictionary where the later dictionaries override the earlier ones.

It is invoked as follows:

`python merge_dicts.py dict1.json dict2.json ... > merged_dict.json 2> report.txt`

You may want to see the report (or not).

## Converting JSON to RTF/CRE

There is also a script to convert from a plover json dictionary to an RTF/CRE dictionary that, in theory, could be imported by any other CAT program.

Make sure the command line is correct because the output file will be overwritten without warning:

`python convert_json_to_rtfcre_dict.py input.json output.rtf`
