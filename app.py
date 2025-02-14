import streamlit as st
from google.cloud import storage
from datetime import timedelta
from google.oauth2 import service_account
from backend import user_input_menu, multi_user_input_menu, process_locid, process_mlocid

secrets = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(secrets)
def generate_signed_url(blob_name):
    """Generates a signed URL to access a file in GCS."""
    try:
        bucket_name = "chickpea-transcriptome"  # Replace with your bucket name
        client = storage.Client(credentials=credentials)
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        # Check if the blob exists
        if not blob.exists():
            print(f"File {blob_name} does not exist in bucket {bucket_name}")  # Debugging
            return None
        # Generate a signed URL that expires in 1 hour
        url = blob.generate_signed_url(expiration=timedelta(hours=1), method='GET')
        print(f"Generated signed URL for {blob_name}: {url}")  # Debugging
        return url
    except Exception as e:
        print(f"Error generating signed URL for {blob_name}: {e}")  # Debugging
        return None

# --- Page Configurations ---
st.logo(generate_signed_url("pvz.gif"),size="large")
st.set_page_config(page_title="MultiClassClassificationInput App", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
pages = ["Home", "Start Task","Meta Data", "Glossary","Demonstration", "About"]
selected_page = st.sidebar.selectbox("Select Page :", pages)

# --- Home Page ---
if selected_page == "Home":
    st.title("Welcome to the Multi Class Classification App")
    st.write("**Home Page**")

    st.write("...")
    st.write("...")
    st.write("...")

# --- Start Task Page ---
elif selected_page == "Start Task":
    st.title("Start Task")
    st.write("**Begin the task by interacting with the backend process.**")
    col1,col2 = st.columns(2)

    with col1:
        tid = st.text_input("Enter the Gene ID: ", placeholder="e.g., Ca_00001", key="Tid_input1").strip()
        mtid = st.text_input("Enter multiple Gene IDs: ", placeholder="e.g., Ca_00001, Ca_00002", key="mTid_input2").strip()
        if mtid:
            mtid_list = [item.strip() for item in mtid.replace(",", " ").split()]
            mtid_list = list(set(mtid_list))
            mtid = ",".join(mtid_list)

    with col2:
        locid = st.text_input("Enter the NCBI ID: ", placeholder="e.g., LOC101511858", key="Locid_input1").strip()
        mlocid = st.text_input("Enter multiple NCBI IDs: ", placeholder="e.g., LOC101511858, LOC101496413", key="mLocid_input2").strip()
        if mlocid:
            mlocid_list = [item.strip() for item in mlocid.replace(",", " ").split()]
            mlocid_list = list(set(mlocid_list))
            mlocid = ",".join(mlocid_list)

    if st.button("Start"):
        if tid:
            result = user_input_menu(tid)
            st.write(result)
            st.toast("Task completed successfully.")
        elif mtid:
            result =multi_user_input_menu(mtid)
            st.write(result)
            st.toast("Task completed successfully.")
        elif locid:
            tid=process_locid(locid)
            result = user_input_menu(tid)
            st.write(result)
            st.toast("Task completed successfully.")
        elif mlocid:
            mtid=process_mlocid(mlocid)
            result = multi_user_input_menu(mtid)
            st.write(result)
            st.toast("Task completed successfully.")
        else:
            st.warning("Need either a Gene ID or NCBI ID to proceed.")
    elif tid == "":
        st.warning("Need Gene ID/ NCBI ID to proceed.")
    else:
        st.write("Press the 'Start' button to begin the task.")
        st.write("Follow the instructions or check out demonstrations")

# --- Meta Data Page ---
elif selected_page == "Meta Data":
    st.title("Meta Data")
    st.write("**Key Insights and Analytics from the Application Backend**")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(generate_signed_url("Images/1.png"), caption="Expression Data Heatmap", use_container_width=True)
        st.write("")

        st.image(generate_signed_url("Images/2.png"), caption="SVM Kernel Performance", use_container_width=True)
        st.write("")

        st.image(generate_signed_url("Images/7.png"), caption="Tissue Specific Distribution Plots", use_container_width=True)
        st.write("")

    with col2:
        st.image(generate_signed_url("Images/4.png"), caption="Functional Annotation [Root Tissues]", use_container_width=True)
        st.write("")

    col3, col4 = st.columns(2)
    with col3:
        st.image(generate_signed_url("Images/11.png"), caption="Functional Annotation [Seed Tissues]", use_container_width=True)
        st.write("")

    with col4:
        st.image(generate_signed_url("Images/5.png"), caption="WGCNA Heatmaps", use_container_width=True)
        st.write("")

    st.image(generate_signed_url("Images/3.png"), caption="Performance Charts for All Files", use_container_width=True)

    col5, col6 = st.columns(2)
    with col5:
        st.image(generate_signed_url("Images/8.png"), caption="Functional Annotation [Flower Development Stages]", use_container_width=True)
        st.write("")

        st.image(generate_signed_url("Images/9.png"), caption="Functional Annotation [Flower Parts]", use_container_width=True)
        st.write("")

    with col6:
        st.image(generate_signed_url("Images/10.png"), caption="Functional Annotation [Green Tissues]", use_container_width=True)
        st.write("")

        st.image(generate_signed_url("Images/6.png"), caption="Comparison of lncRNAs, TF, and Non-TF", use_container_width=True)
        st.write("")
        
# --- Glossary Page ---
elif selected_page == "Glossary":
    st.title("Glossary")
    st.write("**Key Terms and Definitions**")
    glossary_entries = {
    'GO - Gene Ontology': '- a framework for the model of biology that describes gene functions in a species-independent manner.',
    'KEGG - Kyoto Encyclopedia of Genes and Genomes': '- a database resource for understanding high-level functions and utilities of biological systems.',
    'FPKM - Fragments Per Kilobase of transcript per Million mapped reads': '- a normalized method for counting RNA-seq reads.',
    'miRNA - MicroRNA': '- small non-coding RNA molecules that regulate gene expression by binding to complementary sequences on target mRNA.',
    'lncRNA - Long Non-Coding RNA': '- a type of RNA molecule that is greater than 200 nucleotides in length but does not encode proteins.',
    'ST - Seed Tissue': '- the tissue in seeds that supports the development of the embryo and storage of nutrients.',
    'FDS - Flower Development Stages': '- the various phases of growth and development that a flower undergoes from bud to bloom.',
    'FP - Flower Parts': '- the various components that make up a flower, including petals, sepals, stamens, and carpels.',
    'GT - Green Tissues': ' - plant tissues that are photosynthetic, primarily found in leaves and stems.',
    'RT - Root Tissues': '- the tissues found in the root system of a plant, involved in nutrient absorption and anchorage.',
    'TF - Transcription Factor': '- a protein that controls the rate of transcription of genetic information from DNA to messenger RNA.',
    'Non-TF - Non-Transcription Factors': '- proteins or molecules that do not directly bind to DNA to initiate or regulate transcription, but still influence gene expression through other mechanisms.',
    'WGCNA - Weighted Gene Co-expression Network Analysis': '- a method for finding clusters (modules) of highly correlated genes and studying their relationships to clinical traits.',
    'PPI - Protein-Protein Interaction': '- physical contacts between two or more proteins that occur in a living organism and are essential for various biological functions, including signal transduction and gene regulation.',
    'SNP CALLING - Single Nucleotide Polymorphism': 'The process of identifying single nucleotide polymorphisms (SNPs) in a genome from sequencing data. SNPs are variations at a single position in the DNA sequence, and SNP calling is crucial for genetic studies and disease association analyses.',
    'PEPTIDE SEQUENCE': 'A sequence of amino acids that make up a peptide, which is a short chain of amino acids linked by peptide bonds.',
    'CDS SEQUENCE - Coding Sequence': '- the portion of a gene\'s DNA or RNA that codes for a protein.',
    'TRANSCRIPT SEQUENCE': 'The RNA sequence transcribed from a gene, which may be translated into a protein or may function as non-coding RNA.',
    'GENOMIC SEQUENCE': 'The complete sequence of nucleotides (DNA or RNA) that make up the entire genome of an organism.'}

    for term, definition in glossary_entries.items():
        with st.expander(term):
            st.write(definition)
    
# --- Demonstration Page ---
elif selected_page == "Demonstration":
    st.title("Demonstration Page")
    st.write("**Learn how to use this interface**")

    # Add help content here
    st.write("This page helps you understand how to use the app through video turotials. Follow the steps below:")
    
    st.subheader("Navigation Tutorial")
    video_url = generate_signed_url("Videos/navigation.mp4")
    if video_url:
        st.video(video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")

    st.subheader("Single Task Tutorial")
    video_url = generate_signed_url("Videos/start_task1.mp4")
    if video_url:
        st.video(video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")
    st.markdown("""
    1. Navigate to the **Start Task** page.
    2. Enter the 8-character code when prompted.
    3. Click the **Start** button to begin the task.
    4. Wait for the task to complete and view the results.""")

    st.subheader("Multi Task Tutorial")
    video_url = generate_signed_url("Videos/start_task2.mp4")
    if video_url:
        st.video(video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")
    st.markdown("""
    1. Navigate to the **Start Task** page.
    2. Enter the 8-character code when prompted.
    3. Click the **Start** button to begin the task.
    4. Wait for the task to complete and view the results.""")

    st.subheader("Glossary Tutorial")
    video_url = generate_signed_url("Videos/glossary.mp4")
    if video_url:
        st.video(video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")

    st.subheader("About Tutorial")
    video_url = generate_signed_url("Videos/contact us.mp4")
    if video_url:
        st.video(video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")
    
# --- About Page ---
elif selected_page == "About":
    st.title("About")
    st.write("**Learn more about the application and its developers.**")

    import urllib.parse
    with st.popover('Contact Us'):
        email_to = "gopalkalwan56@gmaill.com"
        subject = "MultiClassClassificationInput App Inquiry"
        body = "I am writing to inquire about..."
        subject_encoded = urllib.parse.quote(subject)
        body_encoded = urllib.parse.quote(body)
        # Create the mailto link
        mailto_link = f"mailto:{email_to}?subject={subject_encoded}&body={body_encoded}"
        st.markdown(f"[Tap the link to open E-mail](mailto:{email_to}?subject={subject_encoded}&body={body_encoded})")
