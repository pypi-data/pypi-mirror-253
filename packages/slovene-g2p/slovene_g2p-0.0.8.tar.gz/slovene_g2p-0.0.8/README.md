# slovene_g2p
A converter that converts Slovene words to their IPA and/or SAMPA transcriptions.



## usage

```
from slovene_g2p.SloveneG2P import SloveneG2P
g2p = SloveneG2P("ipa_symbol", "cjvt_ipa_detailed_representation", "phoneme_string")
g2p.convert_to_phonetic_transcription(word="govoriti", msd_sl="Ggdd-em", morphological_pattern_code="G1.2.d")
```

phoneme_option can be either "ipa_symbol" or "sampa_symbol" and representation option can be either "cjvt_ipa_detailed_representation", "cjvt_ipa_robust_representation", "cjvt_sampa_detailed_representation", "cjvt_sampa_robust_representation"

both msd_sl and morphological_pattern_code are available in sloleks 3.0 and provided by classla python package