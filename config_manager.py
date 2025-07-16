import os, json, platform

def get_config_directory():
    """Get the configuration directory based on the operating system."""
    if platform.system() == "Windows":
        base_dir = os.getenv('APPDATA') or os.path.expanduser('~\\AppData\\Roaming')
    else:  # Linux / macOS systems
        base_dir = os.path.expanduser('~/.config')
    
    config_dir = os.path.join(base_dir, 'doctors_diary')
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, 'config.json')
    
config_path = get_config_directory()

def load_config():
    """Load configuration from the JSON file."""
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {config_path}. Using default configuration.")
    return {}

def save_config(config_data: dict):
    """Save configuration to the JSON file."""
    if  not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
    try:
        with open(config_path, 'w') as file:
            json.dump(config_data, file, indent=4)
        print(f"Configuration saved to {config_path}")
        return True
    except IOError as e:
        print(f"Error saving configuration: {e}")
        return False

def update_config(key, value):
    """Update a specific section (like 'labels') in the config without overwriting others."""
    config_data = load_config()

    if key in config_data and isinstance(config_data.get(key), dict) and isinstance(value, dict):
        # Update only the sub-keys (like specific labels)
        config_data[key].update(value)
    else:
        # Set the key if it doesn't exist or isn't a dict
        config_data[key] = value

    return save_config(config_data)

DEFAULT_CONFIG = {
    "theme": "system",
    "labels": {
        "institudeEN_name": "MASNUN HOMEO MEDICARE",
        "owner_name": "\u09a1\u09be. \u09b6\u09c7\u0996 \u09b0\u09bf\u099c\u0993\u09df\u09be\u09a8\u09c1\u09b0 \u09b0\u09b9\u09ae\u09be\u09a8",
        "position_label": "\u09b9\u09cb\u09ae\u09bf\u0993\u09aa\u09cd\u09af\u09be\u09a5\u09bf\u0995 \u09ae\u09c7\u09a1\u09bf\u09b8\u09bf\u09a8 \u098f\u09a8\u09cd\u09a1 \u09a8\u09bf\u0989\u099f\u09cd\u09b0\u09bf\u09b6\u09a8 \u0995\u09a8\u09b8\u09be\u09b2\u099f\u09c7\u09a8\u09cd\u099f",
        "contact_num": "Mobile:  01328-976677",
        "certificate_info": "\u09b0\u09c7\u099c\u09bf\u0983 \u099a\u09bf\u0995\u09bf\u09ce\u09b8\u0995 \u09b8\u09cd\u09ac\u09be\u09b8\u09cd\u09a5\u09cd\u09af \u0985\u09a7\u09bf\u09a6\u09aa\u09cd\u09a4\u09b0, \u09a8\u0982- H 1098",
        "instituteBN_name": "\u09ae\u09be\u09b8\u09a8\u09c1\u09a8 \u09b9\u09cb\u09ae\u09bf\u0993 \u09ae\u09c7\u09a1\u09bf\u0995\u09c7\u09df\u09be\u09b0 ",
        "owner_occupation": "\u09aa\u09cd\u09b0\u09ad\u09be\u09b7\u0995, \u09ac\u09c7\u0997\u09ae \u09ab\u09bf\u09b0\u09cb\u099c\u09be \u0986\u09ae\u09bf\u09b0 \u09b9\u09cb\u09ae\u09bf\u0993\u09aa\u09cd\u09af\u09be\u09a5\u09bf\u0995 \u09ae\u09c7\u09a1\u09bf\u0995\u09c7\u09b2 \u0995\u09b2\u09c7\u099c \u0993 \u09b9\u09be\u09b8\u09aa\u09be\u09a4\u09be\u09b2",
        "header_label": "GENERAL INFORMATION",
        "id_label": "Patient ID:",
        "name_label": "Patient Name:",
        "date_label": "Date:",
        "sex_label": "Gender:",
        "age_label": "Age:",
        "job_label": "Occupation:",
        "marriage_label": "Marital Status:",
        "Religion_label": "Religion:",
        "Address_label": "Address:",
        "contact_label": "Contact No:",
        "illness_label": "Patient's Complain (Detailed history of the present illness):",
        "history_label": "History of past illness (with treatment):",
        "header_label2": "PHYSICAL SYMPTOMS",
        "thermal_label": "Thermal Reaction:",
        "thirst_label": "Thirst:",
        "tongue_label": "Tongue:",
        "appetite_label": "Appetite:",
        "craving_label": "Cravings or Liking of (Food & Drinks):",
        "dislike_label": "Aversion or Disliking (Food & Drinks):",
        "intolerance_label": "Food Allergies/ Intolarance/ Aggravation (Food & Drinks):",
        "hunger_label": "Hunger:",
        "bathing_label": "Bathing",
        "sweat_label": "Sweat/ Perspiration:",
        "aleep_label": "Sleep:",
        "dreams_label": "Dreams:",
        "salivation_label": "Salivation:",
        "urine_label": "Urine:",
        "stool_label": "Stool:",
        "rectum_label": "Rectum:",
        "skin_label": "Skin:",
        "aliments_label": "Aliments from:",
        "generalModalities_label": "General Modalities:",
        "nailAnalysis_label": "Nail Analysis:",
        "others_label_2": "Others Symptoms:",
        "femaleOnly_label": "For Female Only ",
        "label_23": "(Is sex desire Absent or Excessive or Others problem )",
        "pregnancy_label": "H/O Pregnancy:",
        "obstetric_label": "Obstetric History:",
        "marriedFor_label": "Married for",
        "gravida_label": "Gravida",
        "abortion_label": "Abortion",
        "header_label3": "MENTAL SYMPTOMS",
        "will_label": "Will:",
        "will2_label": "(It refers to that faculty of mind by which a person decides what to do)",
        "A_label": "A. Loves, hates & emotions:",
        "B_label": "B. Lasciviousness, revulsion to sex, sexual perversons:",
        "C_label": "C. Fears:",
        "D_label": "D. Temperament:",
        "E_label": "E. Nature & habits:",
        "effectCompany_label": "Effect of Company:",
        "effectConsolation_label": "Effect of Consolation:",
        "daSex_label": "D/A of sex:",
        "daSpecialsense_label": "D/A of special senses:",
        "grief_label": "Grief:",
        "gesturesPostures_label": "Various gestures & postures:",
        "anxiety_label": "Anxiety states:",
        "intellect_label": "Intellect/ Understanding:",
        "memory_label": "Memory:",
        "anger_label": "Anger:",
        "avarice_label": "Avarice:",
        "religiouos_label": "Religious:",
        "dominating_label": "Dominating:",
        "laughing_label": "Laughing:",
        "selfConfidence_label": "Self-confidence:",
        "sentimental_label": "Sentimental:",
        "sharing_label": "Sharing (His/her problem to others):",
        "shock_label": "Shock:",
        "sympathetic_label": "Sympathetic:",
        "weeping_label": "Weeping:",
        "work_label": "Work:",
        "aggravation_label": "Aggravation/ Amelioration:",
        "pastHistory_label": "Past History:",
        "familyHistory_label": "Family History:",
        "fatherSide_label": "Father Side:",
        "motherSide_label": "Mother Side:",
        "others_label": "Others Symptoms:",
        "physicalExamination_label": "Physical Examination:",
        "laboratoryInvestigation_label": "Laboratory Investigations:",
        "label": "Prescription"
    }
}

