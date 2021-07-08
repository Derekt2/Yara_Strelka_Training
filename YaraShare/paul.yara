rule Sample_Exercise5 {
    meta:
        author = "asdfjklas;vnklas;vsav"
        description = "Matches all words in test file"
        date = "06/22/2021"
        version = "1.0"
        license = "N/A"
        family="N/A"
        sha256_hashes= "N/A"
        weight= 0
        scope ="['testing', 'asdfmkoasdfjknosadfn']"
        intel ="['N/A']"
    strings:
        $string1 = "hello"
        $string2 = "exercise"
        $string3 = "five"
	
    condition:
        all of them 
}
