# fingerprint-comparator
Create fingerprint for strings and compare them

## Parameters
```
$ ./fingerprint-comparator.py -h
usage: fingerprint-comparator.py [-h] --input inputFile
                                 [--remove-words word1 word2 ... [word1 word2 ... ...]]
                                 [--output-type {text,json}]

create fingerprint for strings and compare them

optional arguments:
  -h, --help            show this help message and exit
  --input inputFile     input file which contains strings, each line for one
                        string
  --remove-words word1 word2 ... [word1 word2 ... ...]
                        remove these words and then create fingerprints

```

##Usage

###Example1
Input file:
```
ABC TEKNOLOJİ SANAYİ VE DIŞ TİC.LTD. ŞTİ. 
ABC TEKNOLOJİ SANAYİ VE DIŞ TİC. LTD.ŞTİ
XYZ KİMYA SAN. TİC LTD. ŞTİ.
XYZ KİMYA SAN.VE TİC.LTD.ŞTİ.
123 INSAAT
```
run fingerprint-comparator and print output
```
$ ./fingerprint-comparator.py --input file --output-type text.
+abcteknoloj.sanay.vedi.t.cltd.t.
--ABC TEKNOLOJİ SANAYİ VE DIŞ TİC.LTD. ŞTİ. 
--ABC TEKNOLOJİ SANAYİ VE DIŞ TİC. LTD.ŞTİ
```
run fingerprint-comparator and print output as json.
```
$ ./fingerprint-comparator.py --input file --output-type json
{
    "abcteknoloj.sanay.vedi.t.cltd.t.": [
        "ABC TEKNOLOJİ SANAYİ VE DIŞ TİC.LTD. ŞTİ. ", 
        "ABC TEKNOLOJİ SANAYİ VE DIŞ TİC. LTD.ŞTİ"
    ]
}
```

###Example2
Input file:
```
ABC TEKNOLOJİ SANAYİ VE DIŞ TİC.LTD. ŞTİ. 
ABC TEKNOLOJİ SANAYİ VE DIŞ TİC. LTD.ŞTİ
XYZ KİMYA SAN. TİC LTD. ŞTİ.
XYZ KİMYA SAN.VE TİC.LTD.ŞTİ.
123 INSAAT
```
run fingerprint-comparator by using --remove-words, this will force fingerprint-comparator to create fingerprints after removing words.
```
$ ./fingerprint-comparator.py --input file --remove-words "ve " " ve" --output-type text
+abcteknoloj.sanay.di.t.cltd.t.
--ABC TEKNOLOJİ SANAYİ VE DIŞ TİC.LTD. ŞTİ. 
--ABC TEKNOLOJİ SANAYİ VE DIŞ TİC. LTD.ŞTİ
+xyzk.myasant.cltd.t.
--XYZ KİMYA SAN. TİC LTD. ŞTİ.
--XYZ KİMYA SAN.VE TİC.LTD.ŞTİ.
```