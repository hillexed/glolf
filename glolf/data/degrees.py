import random

degree_types = ("ST","NS","XQ","A","IN","OSW","DRC","AAAAA","AAS","AB", 
    "BS","BA", "PhD", "MA", "MS")

#From Corpora
#https://github.com/dariusk/corpora/blob/59d201bb30786b84f581057d54e3f88f07fb2091/data/books/academic_subjects.json
course_types = {

  "description": "Academic subjects",
  "source": "Classification of Instructional Programs (CIP 2000) https://nces.ed.gov/pubs2002/cip2000/",
  "subjects": [
    "Accounting",
    "Advertising",
    "African Studies",
    "Afro-American Studies",
    "Agricultural Economics",
    "Agricultural Engineering",
    "Agronomy & Crop Science",
    "Native American Studies",
    "American Studies",
    "Analytical Chemistry",
    "Anatomy",
    "Anthropology",
    "Arabic Language & Literature",
    "Archeology",
    "Architectural Environmental Design",
    "Architectural Urban Design & Planning",
    "Architecture",
    "Art Teacher Education",
    "Asian Studies",
    "Astronomy",
    "Astrophysics",
    "Atmospheric Sciences & Meteorology",
    "Automotive Mechanics",
    "Aviation Systems & Avionics Maintenance",
    "Banking & Financial Support Services",
    "Biblical & Theological Languages",
    "Biochemistry",
    "Bioengineering & Biomedical Engineering",
    "Biological & Physical Sciences",
    "Biometrics",
    "Biophysics",
    "Business Statistics",
    "Business Teacher Education",
    "Business Economics",
    "Cardiovascular Technology",
    "Cell Biology",
    "Ceramic Sciences & Engineering",
    "Chemical & Molecular Physics",
    "Chemical Engineering",
    "Chemical Technology",
    "Chinese Language & Literature",
    "Civil Engineering",
    "Classics",
    "Classical Languages & Literatures",
    "Clinical Psychology",
    "Clothing & Textile Studies",
    "Comparative Literature",
    "Computer Science",
    "Computer Systems Analysis",
    "Construction Technology",
    "Consumer Economics & Science",
    "Counseling Psychology",
    "Student Counseling & Guidance Services",
    "Criminal Justice",
    "Criminology",
    "Dairy Science",
    "Dance",
    "Data Processing Technology",
    "Demography & Population Studies",
    "Dental Hygiene",
    "Developmental & Child Psychology",
    "Diesel Engine Repair",
    "Driver & Safety Teacher Education",
    "Earth & Planetary Sciences",
    "East Asian Studies",
    "Eastern European Area Studies",
    "Ecology",
    "Education of the Blind & Visually Handicapped",
    "Education of the Deaf & Hearing Impaired",
    "Education of the Emotionally Handicapped",
    "Education of the Gifted & Talented",
    "Education of the Mentally Handicapped",
    "Education of the Multiply Handicapped",
    "Education of the Physically Handicapped",
    "Education of the Speech Impaired",
    "Educational Psychology",
    "Educational Statistics & Research Methods",
    "Educational Supervision",
    "Electromechanical Technology",
    "Elementary Teacher Education",
    "Engineering Mechanics",
    "Engineering Physics",
    "English Creative Writing",
    "English Literature",
    "Entomology",
    "Environmental & Pollution Control Technology",
    "Environmental Health Engineering",
    "European Studies",
    "Experimental Psychology",
    "Film-Video Making",
    "Cinematography & Production",
    "Fine Arts",
    "Studio Arts",
    "Fire Protection & Safety Technology",
    "Food Sciences & Technology",
    "French Language & Literature",
    "General Marketing Operations",
    "Geochemistry",
    "Geography",
    "Geological Engineering",
    "Geology",
    "Geophysical Engineering",
    "Geophysics & Seismology",
    "German Language & Literature",
    "Greek Language & Literature",
    "Health Teacher Education",
    "Health Unit Coordination",
    "Hebrew Language & Literature",
    "Higher Education Administration",
    "Hispanic-American Studies",
    "Horticulture Science",
    "Hospital Administration",
    "Hotel & Restaurant Management",
    "Human Resources Management",
    "Humanities",
    "Humanistic Studies",
    "Industrial & Organizational Psychology",
    "Industrial Engineering",
    "Manufacturing Technology",
    "Information Processing",
    "Information Sciences & Systems",
    "Inorganic Chemistry",
    "Institutional Food Services Administration",
    "Instrumentation Technology",
    "Insurance & Risk Management",
    "Interior Architecture",
    "International Business",
    "International Relations & Affairs",
    "Investments & Securities",
    "Islamic Studies",
    "Italian Language & Literature",
    "Japanese Language & Literature",
    "Journalism",
    "School Teacher Education",
    "Labor Relations & Studies",
    "Landscape Architecture",
    "Latin American Studies",
    "Latin Language & Literature",
    "Law Enforcement",
    "Police Science",
    "Liberal Arts & Sciences",
    "Liberal Studies",
    "Library Science",
    "Librarianship",
    "Linguistics",
    "Marine Biology",
    "Aquatic Biology",
    "Materials Engineering",
    "Mathematical Statistics",
    "Mathematics",
    "Mathematics Teacher Education",
    "Mechanical Drafting",
    "Mechanical Engineering",
    "Mechanical Technology",
    "Medical Assistant",
    "Medical Illustrating",
    "Medical Laboratory Technology",
    "Medical Radiologic Technology",
    "Medical Records Administration",
    "Medical Records Technology",
    "Medical Technology",
    "Medicinal Chemistry",
    "Pharmaceutical Chemistry",
    "Medicine",
    "Metallurgical Engineering",
    "Metallurgy",
    "Microbiology",
    "Bacteriology",
    "Middle Eastern Studies",
    "Mining & Mineral Engineering",
    "Molecular Biology",
    "Music History & Literature",
    "Music Teacher Education",
    "Naval Architecture & Marine Engineering",
    "Neuroscience",
    "Nuclear Engineering",
    "Nuclear Physics",
    "Nuclear Power Technology",
    "Nursing",
    "Nutritional Sciences",
    "Occupational Therapy",
    "Ocean Engineering",
    "Oceanography",
    "Operations Research",
    "Optometry",
    "Organic Chemistry",
    "Ornamental Horticulture Operations & Management",
    "Osteopathic Medicine",
    "Pacific Area Studies",
    "Paleontology",
    "Petroleum Engineering",
    "Philosophy",
    "Photographic Technology",
    "Photography",
    "Physical & Theoretical Chemistry",
    "Physical Education Teaching & Coaching",
    "Physical Therapy",
    "Physiological Psychology",
    "Psychobiology",
    "Plant Pathology",
    "Plant Physiology",
    "Poultry Science",
    "Practical Nursing",
    "Early Childhood Education",
    "Kindergarten Teacher Education",
    "Psychiatry",
    "Public Administration",
    "Radiation Biology",
    "Radiobiology",
    "Radio & Television Broadcasting",
    "Range Science & Management",
    "Reading Teacher Education",
    "Real Estate",
    "Religious Studies",
    "Religious Education",
    "Religious Music",
    "Respiratory Therapy",
    "Russian & Slavic Area Studies",
    "Russian Language & Literature",
    "Scandinavian Languages & Literatures",
    "Secondary Teacher Education",
    "Slavic Languages & Literatures",
    "Social & Philosophical Foundations of Education",
    "Social Psychology",
    "Social Work",
    "Sociology",
    "Soil Sciences",
    "South Asian Languages & Literatures",
    "South Asian Studies",
    "Southeast Asian Studies",
    "Spanish Language & Literature",
    "Speech & Rhetorical Studies",
    "Speech Pathology & Audiology",
    "Teaching English as a Foreign Language",
    "Teaching English as a Second Language",
    "Textile Sciences & Engineering",
    "Theology",
    "Theological Studies",
    "Toxicology",
    "Urban Studies",
    "Urban Affairs",
    "Veterinary Medicine",
    "Visual & Performing Arts",
    "Welding Technology",
    "Western European Studies",
    "Wildlife & Wildlands Management"
  ]
}

def generate_degree():
    degree_type = random.choice(degree_types)
    degree_field = random.choice(course_types["subjects"])
    return f"{degree_type} in {degree_field}"

def generate_degree_based_on_name(seed):

    rng = random.Random(seed)
    degree_type = rng.choice(degree_types)
    degree_field = rng.choice(course_types["subjects"])
    return f"{degree_type} in {degree_field}"
    
