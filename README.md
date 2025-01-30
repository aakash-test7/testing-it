# Multi-Class Classification App Architecture

## Files
- **app.py**
  - Main Streamlit application file.
  - Handles UI, navigation, and user interactions.
- **backend.py**
  - Contains backend logic for data processing, API calls, and interactions with Google Cloud Storage (GCS).
- **config.toml**
  - Configuration file for Streamlit theme settings.
- **requirements.txt**
  - Lists all Python dependencies required for the project.

## Functions in app.py
- **generate_signed_url(blob_name)**
  - Generates a signed URL to access a file in Google Cloud Storage (GCS).
- **Main Application Logic**
  - Handles page navigation and user input.
  - Pages:
    - Home
    - Start Task
    - Meta Data
    - Glossary
    - Demonstration
    - About

## Functions in backend.py
- **read_excel_from_gcs(bucket_name, blob_name, header=0)**
  - Reads an Excel file from Google Cloud Storage (GCS).
- **normalize_data(data)**
  - Normalizes data using log2 transformation.
- **format_sequence(seq)**
  - Formats a sequence for display.
- **get_string_network_link(protein_transcript)**
  - Fetches a network link from the STRING DB API.
- **filter_orthologs(tid)**
  - Filters orthologs data for a given transcript ID.
- **filter_paralogs(tid)**
  - Filters paralogs data for a given transcript ID.
- **web_driver()**
  - Initializes a Selenium web driver for web scraping.
- **automate_Cultivated_task(tid)**
  - Automates SNP calling for cultivated varieties.
- **automate_Wild_task(tid)**
  - Automates SNP calling for wild varieties.
- **transcriptid_info(tid)**
  - Displays information for a given transcript ID.
- **user_input_menu(tid)**
  - Handles user input for a single transcript ID.
- **multi_user_input_menu(mtid)**
  - Handles user input for multiple transcript IDs.
- **multi_transcriptid_info(mtid)**
  - Displays information for multiple transcript IDs.
- **process_locid(locid)**
  - Maps given NCBI ID with Gene ID  
- **process_mlocid(mlocid)**    
  - Maps multiple NCBI IDs with Gene IDs
    
## Requirements (requirements.txt)
- **pandas**
- **numpy**
- **matplotlib**
- **seaborn**
- **openpyxl**
- **selenium**
- **beautifulsoup4**
- **requests**
- **streamlit**
- **google-cloud-storage**
- **google-auth**

## Data Files in Google Cloud Storage (GCS)
- **FPKM_Matrix(Ca).xlsx**
  - Contains FPKM matrix data.
- **8.xlsx**
  - Contains miRNA data.
- **9.xlsx**
  - Contains protein data.
- **7.xlsx**
  - Contains combined data.
- **10.xlsx**
  - Contains GO and KEGG data.
- **13.xlsx**
  - Contains cellular localization data.
- **14.txt**
  - Contains orthologs data.
- **15.txt**
  - Contains paralogs data.

## Pages in the App
- **Home**
  - Welcome page with basic information.
- **Start Task**
  - Allows users to input transcript IDs and start tasks.
- **Meta Data**
  - Displays key insights and analytics from the backend.
- **Glossary**
  - Provides definitions for key terms.
- **Demonstration**
  - Includes video tutorials for using the app.
- **About**
  - Provides information about the app and developers.

## External APIs
- **STRING DB**
  - Provides protein-protein interaction networks.
- **Other APIs**
  - Used for SNP calling and other tasks.

## Google Cloud Storage (GCS)
- **Bucket Name**: `chickpea-transcriptome`
- **Data Files Stored**:
  - FPKM_Matrix(Ca).xlsx
  - miRNA data (8.xlsx)
  - Protein data (9.xlsx)
  - Combined data (7.xlsx)
  - GO and KEGG data (10.xlsx)
  - Cellular localization data (13.xlsx)
  - Orthologs data (14.txt)
  - Paralogs data (15.txt)
- **Icons SVG Stored**
- **Images Stored**
- **Video Tutorials Stored**
   
