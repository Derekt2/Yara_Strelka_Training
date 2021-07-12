rule Sample_Exercise5_Margarita {
    meta:
        author = "Derek Thomas & Paul Hutelmyer"
        description = "Matches keyword in VBS file"
        date = "06/22/2021"
        version = "1.0"
        license = "N/A"
        family="N/A"
        sha256_hashes= "N/A"
        weight= 0
        scope ="['testing', 'hunting']"
        intel ="['N/A']"
    strings:
        $string1 = "margaritasexy
	
    condition:
        all of them 
}