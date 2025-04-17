from NLP_MiniProject.rules import verb_suffixes

def get_tags(verb_form):
    # Create a list of all possible suffix matches with their tags
    all_suffixes = []
   
    for lakara, voices in verb_suffixes.items():
        for voice, persons in voices.items():
            for purusha, numbers in persons.items():
                for vachana, suffix in numbers.items():
                    all_suffixes.append((suffix, {
                        "Lakāra (Tense/Mood)": lakara,
                        "Voice (Pāda)": voice,
                        "Purusha (Person)": purusha,
                        "Vachana (Number)": vachana,
                        "Matched Suffix": suffix
                    }))
   
    # Sort all suffixes by length in descending order
    all_suffixes.sort(key=lambda x: len(x[0]), reverse=True)

    for suffix, tag_info in all_suffixes:
        if verb_form.endswith(suffix):
            return [tag_info]  # Return only the first (longest, most specific) match

    return []  # No match found