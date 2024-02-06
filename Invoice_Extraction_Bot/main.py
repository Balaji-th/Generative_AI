from dotenv import load_dotenv
import streamlit as st
from utils import *

load_dotenv()
def main():
    st.set_page_config(page_title="Invoice Extraction App",page_icon="🤖")
    st.title("Invoice Extraction Bot....!🤖")
    st.subheader("Can I help you in invoice data extraction?")

    pdf = st.file_uploader("Upload invoice here in PDF format",type=["pdf"],accept_multiple_files=True)
    submit = st.button("Extract invoice info")

    if submit:
        with st.spinner("wait for it..."):
            df = create_docs(pdf)
            st.write(df.head())

            data_as_csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download data as CSV",
                data_as_csv,
                "benchmark-tools.csv",
                "text/csv",
                key="download-tools-csv",
            )

        st.success("I hope that i have saved time..😉")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

